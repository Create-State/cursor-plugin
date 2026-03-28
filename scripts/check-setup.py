#!/usr/bin/env python3
"""
Create State - Session Start Hook
Checks authentication configuration and provides guidance if needed.
Cross-platform: works on Windows, macOS, and Linux.

Supports two auth methods:
- OAuth (default for /mcp/): No config needed, authenticates via browser
- API Key (for /api/mcp/): Requires hardcoded key in mcp.json headers

Note: Cursor does not support ${env:VAR} syntax for remote MCP server headers.
API keys must be configured directly in mcp.json.
"""

import json
import os
from pathlib import Path


def get_mcp_config() -> dict:
    """Load and return mcp.json config."""
    script_dir = Path(__file__).parent
    plugin_dir = script_dir.parent
    mcp_json = plugin_dir / "mcp.json"

    if not mcp_json.exists():
        return {}

    try:
        with open(mcp_json) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def check_auth_config() -> tuple[str, list[str]]:
    """
    Check authentication configuration.
    
    Returns:
        tuple: (auth_type, list of issues)
        auth_type: 'oauth', 'api_key', or 'unknown'
    """
    config = get_mcp_config()
    issues = []

    servers = config.get("mcpServers", {})
    create_state = servers.get("create-state", {})

    if not create_state:
        return "unknown", ["No 'create-state' server found in mcp.json"]

    url = create_state.get("url", "")
    auth = create_state.get("auth", {})
    headers = create_state.get("headers", {})

    # Check URL basics
    if not url:
        issues.append(
            "No URL configured for create-state server.\n"
            "   Add: \"url\": \"https://createstate.ai/mcp/\""
        )
        return "unknown", issues

    # Check for HTTP (should be HTTPS)
    if url.startswith("http://") and "localhost" not in url:
        issues.append(
            "URL uses HTTP instead of HTTPS.\n"
            "   For security, use: https://createstate.ai/..."
        )

    # Check domain
    valid_domains = ["createstate.ai", "dev.createstate.ai", "beta.createstate.ai", "localhost"]
    is_valid_domain = any(domain in url for domain in valid_domains)
    
    if not is_valid_domain:
        issues.append(
            f"Unexpected domain in URL: {url}\n"
            "   Expected: https://createstate.ai/mcp/ (OAuth)\n"
            "          or https://createstate.ai/api/mcp/ (API key)"
        )

    # Check endpoint path
    valid_paths = ["/mcp/", "/mcp", "/api/mcp/", "/api/mcp"]
    has_valid_path = any(path in url for path in valid_paths)
    
    if is_valid_domain and not has_valid_path:
        issues.append(
            f"Unexpected endpoint path in URL: {url}\n"
            "   Valid endpoints:\n"
            "   - /mcp/ for OAuth authentication\n"
            "   - /api/mcp/ for API key authentication"
        )

    # Determine auth type based on config
    if auth.get("type") == "oauth":
        # OAuth config - check URL is correct for OAuth
        if "/api/mcp" in url:
            issues.append(
                "OAuth auth configured but URL uses /api/mcp/ endpoint.\n"
                "   The /api/mcp/ endpoint does not support OAuth.\n"
                "   Change URL to: https://createstate.ai/mcp/"
            )
        return "oauth", issues

    # Check for API key in headers
    auth_header = headers.get("Authorization", "")
    
    if not auth_header:
        # No auth configured
        if "/api/mcp" in url:
            issues.append(
                "Using /api/mcp/ endpoint but no Authorization header.\n"
                "   Add: \"Authorization\": \"Bearer cs_your_api_key\""
            )
        return "unknown", issues

    # API key auth - check for common issues
    if "${env:" in auth_header:
        issues.append(
            "Environment variable syntax detected in Authorization header.\n"
            "   Cursor does NOT support ${env:VAR} for remote MCP servers.\n"
            "   Replace with your actual API key:\n"
            "   \"Authorization\": \"Bearer cs_your_actual_key_here\""
        )

    if "/mcp/" in url and "/api/mcp" not in url:
        issues.append(
            "API key auth configured but URL uses /mcp/ endpoint.\n"
            "   The /mcp/ endpoint uses OAuth, not API keys.\n"
            "   Change URL to: https://createstate.ai/api/mcp/"
        )

    return "api_key", issues


def main():
    auth_type, issues = check_auth_config()

    # OAuth users without issues - nothing to do
    if auth_type == "oauth" and not issues:
        return

    # API key users without issues - nothing to do
    if auth_type == "api_key" and not issues:
        return

    # Show issues if any
    if issues:
        print()
        print("=" * 62)
        print("  Create State: Configuration Issue Detected")
        print("=" * 62)
        print()
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
            print()
        print("For setup instructions, see:")
        print("  https://createstate.ai/web/documentation")
        print()
        print("Or check the plugin README.")
        print("=" * 62)
        print()


if __name__ == "__main__":
    main()
