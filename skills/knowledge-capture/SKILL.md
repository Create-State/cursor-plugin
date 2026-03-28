---
name: knowledge-capture
description: Capture decisions, code, and context to the knowledge graph. Use after making code changes, architectural decisions, commits, or when the user wants to preserve important information.
---

# Knowledge Capture Skill

Capture important knowledge to the Create State knowledge graph for future reference and AI continuity.

## When to Use

- After writing or modifying significant code
- After making architectural decisions
- After git commits
- When user says "remember this" or "save this decision"
- When discussing trade-offs or design choices
- After debugging sessions with important findings

## Two Types of Capture

### 1. captureCode - For Code Changes

Use when you've written or modified code that should be preserved.

```
Tool: captureCode
Arguments:
  code: "<the actual code content>"
  language: "python"  # or javascript, typescript, etc.
  file_path: "src/auth/auth_service.py"
  description: "JWT authentication service"
  change_type: "new"  # or update, fix, refactor
  ai_model: "Claude Opus 4"
```

**Parameters:**
- `code` (required): The actual code content
- `language` (required): Programming language
- `file_path` (required): Full path relative to repo root
- `description`: Brief description of what it does
- `change_type`: new | update | fix | refactor
- `ai_model`: Your AI model identifier

### 2. captureConversationContext - For Decisions and Context

Use for architectural decisions, debugging findings, and important context.

```
Tool: captureConversationContext
Arguments:
  context: "<rich context - see guidelines below>"
  ai_model: "Claude Opus 4"
```

**Parameters:**
- `context` (required): Rich context (see format below)
- `ai_model`: Your AI model identifier

## Rich Context Format

Don't capture brief summaries - they lose valuable knowledge. Include:

### Problem/Task Statement
- What was the original problem or request?
- What symptoms or errors were observed?

### Investigation Process
- What did you explore to understand the issue?
- What files/components did you examine?
- What hypotheses did you form and test?

### Root Cause Analysis
- What was the actual cause?
- What chain of events led to the problem?
- Why wasn't this obvious initially?

### Design Decision Rationale
- What solution did you choose?
- What alternatives were considered?
- Why was this approach chosen?
- What trade-offs were made?

### Key Insights for Future
- What should future developers/AI know?
- What gotchas exist?
- What related areas might need attention?

## Example: Poor vs Rich Capture

### Poor (don't do this)
```
"Fixed the auth bug. Commit abc123."
```

### Rich (do this)
```
## Authentication Token Refresh Bug - Analysis

### Problem Statement
Users were being logged out unexpectedly after ~1 hour.

### Investigation
1. Checked JWT expiry settings - set to 1 hour
2. Examined refresh token flow in auth_service.py
3. Found refresh endpoint wasn't being called

### Root Cause
Frontend was checking token expiry but not triggering refresh.
The isExpired() check used >= instead of >, causing refresh
to trigger AFTER expiry, not before.

### Solution
Changed expiry check to trigger refresh 5 minutes before expiry.
Added buffer to prevent race conditions.

### Key Insight
Token refresh should happen BEFORE expiry with a buffer,
not at the moment of expiry.
```

## Post-Commit Workflow

After EVERY commit, capture BOTH:

1. **Context** - What changed and why
2. **Code** - The actual code for each significant file

```
# After: git commit -m "feat: add rate limiting"

# Step 1: Capture context
captureConversationContext:
  context: "Commit def456: feat: add rate limiting
  
  Added Redis-based rate limiting to API endpoints.
  - 100 requests/minute for authenticated users
  - 20 requests/minute for anonymous users
  
  Files: src/middleware/rate_limit.py, src/web/routes.py
  
  Decision: Used sliding window algorithm for smoother limits."

# Step 2: Capture code
captureCode:
  code: [rate_limit.py content]
  language: python
  file_path: src/middleware/rate_limit.py
  change_type: new
```

## When to Synthesize

After capturing, consider calling `synthesizeProjectContext` to consolidate knowledge:

- After completing a major feature
- Before switching work areas
- After 3-4 rapid captures
- Before creating a session handoff

## Automatic Features

- **Auto-targeting**: Captures go to your active model automatically
- **Auto-synthesis**: After every 5 captures, knowledge is synthesized
- **Version history**: Code captures maintain version history
- **Relationships**: The graph tracks relationships between captures
