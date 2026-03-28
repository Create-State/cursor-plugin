---
name: setup
description: Set up Create State - configure authentication for local or remote development
---

# Create State Setup

Create State supports two authentication methods. Choose based on your setup:

| Setup | Recommended Auth | Why |
|-------|------------------|-----|
| Local Cursor | OAuth (default) | Just works, no configuration needed |
| Remote SSH/WSL | API Key | OAuth tokens don't sync to remote hosts |

## Option 1: OAuth (Local Development)

**This is the default.** If you're using Cursor locally, Create State should work automatically:

1. The plugin uses the `/mcp/` endpoint with OAuth
2. On first use, Cursor will prompt you to authorize with Create State
3. Sign in at https://createstate.ai and authorize the connection

**That's it!** No API key needed for local development.

## Option 2: API Key (Remote SSH/WSL)

If you develop on a remote server via SSH or WSL, you must use API key authentication:

### Step 1: Get Your API Key

1. Visit https://createstate.ai/web/signup to create a free account (or log in)
2. Go to https://createstate.ai/web/api-keys
3. Click "Generate New Key"
4. Copy the key (starts with `cs_`)

### Step 2: Configure the Plugin

Find the plugin's `mcp.json` file and replace its contents with:

```json
{
  "mcpServers": {
    "create-state": {
      "url": "https://createstate.ai/api/mcp/",
      "headers": {
        "Authorization": "Bearer cs_your_api_key_here"
      }
    }
  }
}
```

Replace `cs_your_api_key_here` with your actual API key.

**Important:**
- Use `/api/mcp/` (not `/mcp/`) for API key authentication
- You must hardcode the API key directly - Cursor does not support `${env:VAR}` syntax for remote servers
- Restart Cursor after making changes

### Step 3: Verify Connection

Ask me to run `listHandoffPackages` - if it returns results (or an empty list), you're connected!

## Troubleshooting

**"Authentication required" error:**
- For OAuth: Try signing out and back in at createstate.ai, then restart Cursor
- For API key: Verify the key is correct and uses the `/api/mcp/` endpoint

**"OAuth tokens not accepted" error:**
- You're using the `/api/mcp/` endpoint but haven't configured an API key
- Either switch to `/mcp/` for OAuth, or add your API key to the headers

**MCP server not appearing:**
- Ensure the plugin is installed correctly
- Check Cursor's MCP settings for the create-state entry
- Restart Cursor

**Need help?**
- Email: support@createstate.ai
- Docs: https://createstate.ai/docs
