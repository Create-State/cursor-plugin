---
name: session-restore
description: Restore session continuity from a previous handoff. Use when starting a new conversation, resuming work, or when the user asks to continue from where they left off.
---

# Session Restore Skill

Restore your AI session context from a previous handoff to maintain continuity across conversations.

## When to Use

- At the start of any new conversation
- When user says "continue from where we left off"
- When user says "restore my session" or "pick up where we left off"
- When returning to a project after a break

## Step-by-Step Process

### Step 1: Check for Recent Handoffs

Call `listHandoffPackages` to see available session handoffs:

```
Tool: listHandoffPackages
Arguments: {}
```

This returns a list of handoff packages with:
- Handoff ID
- Creation timestamp
- Age (how long ago it was created)
- Associated projects/world models
- AI model that created it
- Status (active/expired)

### Step 2: Evaluate Handoffs

Look for handoffs from the last 24 hours. If found:
- Note the most recent handoff_id
- Check which world model(s) it includes
- Verify it matches the project the user wants to work on

If no recent handoffs exist, skip to Step 4.

### Step 3: Restore from Handoff

Call `restoreFromHandoff` with the most recent handoff_id:

```
Tool: restoreFromHandoff
Arguments:
  handoff_id: "<the handoff ID from step 1>"
  priority_restoration: true
```

This restores:
- AI thinking state and pending insights
- Active world model (set automatically)
- Session context and hypotheses
- Project priorities and focus areas

After restoration, all captures automatically target the restored model.

### Step 4: Alternative - Load World Model Directly

If no recent handoff exists, load the world model directly:

```
Tool: getProjectWorldModel
Arguments:
  project_path: "."
  include_insights: true
```

Or if the user has multiple models:

```
Tool: listUserWorldModels
Arguments: {}
```

Then load the specific model they want to work on.

## What Gets Restored

A handoff package preserves:

1. **Active World Model** - The project context you were working on
2. **AI Thinking State** - Pending thoughts, hypotheses, and focus areas
3. **Proactive Insights** - AI-generated suggestions and observations
4. **Session Continuity** - Where you left off and what's pending

## Key Concept: Active Model

When you restore from a handoff, the world model becomes your "active model":

- All `captureCode` calls automatically target it
- All `captureConversationContext` calls automatically target it
- No need to specify model_id or project_path

This makes captures simple and intuitive.

## Example Conversation Flow

**User:** "Let's continue working on the authentication feature"

**Assistant:**
1. Call `listHandoffPackages` - finds handoff from 2 hours ago
2. Call `restoreFromHandoff` with that handoff_id
3. Report: "I've restored your session. You were working on the MCP-Test-Model project. Last session, you were implementing JWT authentication. I have 3 pending insights about the auth flow. Ready to continue?"

## Troubleshooting

### No handoffs found
- User may be new or handoffs expired (7-day default)
- Ask which project they want to work on
- Use `createWorldModel` if they need a new project

### Multiple world models
- Use `listUserWorldModels` to show options
- Let user choose which project to work on
- Load with `getProjectWorldModel` using project_name

### Handoff restoration fails
- Check if handoff_id is valid
- Try loading world model directly instead
- Report the issue to the user
