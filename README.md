# Create State - Cursor Plugin

**Persistent memory for AI coding assistants**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cursor Plugin](https://img.shields.io/badge/Cursor-Plugin-purple.svg)](https://cursor.com/docs/plugins)

Create State transforms AI coding assistants from forgetful tools into persistent companions. Every insight, decision, and code pattern is captured in a knowledge graph that grows smarter with every interaction.

## Why Create State?

Without persistent memory, every AI conversation starts from scratch. You explain the same context, re-describe architectural decisions, and watch your AI make the same mistakes it made yesterday.

**Create State solves this:**

- **Persistent Memory** - Decisions, code patterns, and debugging insights survive across sessions
- **Session Handoff** - Save AI "thinking state" and restore it later, even with a different AI assistant
- **Knowledge Graph** - Automatically captures and visualizes relationships in your codebase
- **Proactive Insights** - Background analysis surfaces issues and improvements you might have missed

## Quick Start

### 1. Install the Plugin

**From Cursor Marketplace** (Coming Soon):
Search for "Create State" in Cursor's plugin marketplace.

**From Source** (Available Now):
```bash
git clone https://github.com/Create-State/cursor-plugin.git
```
Then install from local path in Cursor (see [Cursor's plugin documentation](https://cursor.com/docs/plugins) for details).

### 2. Authenticate

**Are you using Remote SSH?** (developing on a remote server via SSH or WSL)

| Your Setup | Authentication | What to Do |
|------------|----------------|------------|
| Local Cursor | OAuth (default) | Nothing - just connect and sign in when prompted |
| Remote SSH/WSL | API Key | [Configure API key](#api-key-setup-for-remote-ssh) |

**OAuth (Local Users):** The plugin works out of the box. On first connection, Cursor will prompt you to sign in via your browser. Create an account at [createstate.ai](https://createstate.ai/web/signup) if you don't have one.

**API Key (Remote SSH Users):** See [API Key Setup](#api-key-setup-for-remote-ssh) below.

### 3. Verify Installation

Check that `create-state` appears in your MCP servers list (Settings > MCP), then just ask your AI:

> "Check if we have any recent session handoffs"

If connected, your AI will respond with session information.

## Using Create State

The plugin works through natural conversation. Just talk to your AI like you normally would.

### Setting Up a New Project

When starting work on a new project, ask your AI to create a world model for it:

> "Create a world model for this project called 'my-awesome-app'"

> "Set up Create State for this codebase"

Your AI will create a world model - a dedicated knowledge container for this project's decisions, patterns, and context.

### Managing Your World Models

To see all your projects:

> "What world models do I have?"

> "List my projects"

To switch to a different project:

> "Load the world model for my-awesome-app"

> "Switch to the billing-service project"

Your AI will load that project's context, so it knows the history and decisions specific to that codebase.

### Starting Your Day

When you begin a coding session, simply ask:

> "Can you restore our last session?"

or

> "What were we working on yesterday?"

Your AI will check for recent handoffs and restore the context, so you can pick up right where you left off.

### During Development

Create State captures knowledge automatically as you work. The plugin's rules guide your AI to preserve important context after commits and significant changes.

You can also ask your AI to remember things explicitly:

> "This was a tricky bug - please capture what we learned about the caching issue"

> "Save our discussion about the authentication architecture"

> "Remember that we decided to use Redis for sessions instead of JWT"

### Finding Past Knowledge

When you need to recall previous decisions or context:

> "Why did we choose PostgreSQL over MongoDB?"

> "What do we know about the payment processing module?"

> "Have we dealt with rate limiting issues before?"

Your AI searches your knowledge graph and brings back relevant context.

### Getting Insights

Ask for analysis and suggestions:

> "What issues should I be aware of in this codebase?"

> "Are there any patterns or improvements you'd suggest?"

> "Give me a summary of this project's architecture"

### Ending Your Session

Before closing Cursor, let your AI save the session state:

> "Let's wrap up - save our session for next time"

> "Create a handoff so I can continue tomorrow"

This preserves your AI's "thinking state" - the context, hypotheses, and understanding built during your session.

## What Happens Automatically

The plugin includes rules that guide your AI to:

- **Restore context** at the start of each session
- **Capture knowledge** after significant code changes
- **Preserve session state** when you're done working

You don't need to remember commands or tool names. Just work naturally, and the important stuff gets captured.

## Example Workflow

```
You: "Morning! What were we working on?"

AI: [Restores from last session handoff]
    "Yesterday we were debugging the user authentication flow. 
     We identified an issue with token refresh and decided to 
     implement a retry mechanism. Want me to continue from there?"

You: "Yes, let's finish that. Here's the error I'm seeing..."

[... you work together on the fix ...]

You: "Great, that's working now. Let's commit."

AI: [Commits and automatically captures the context]
    "Committed. I've saved our debugging insights about the 
     token refresh issue to the knowledge graph."

You: "Perfect. I need to switch to the billing feature now."

AI: "Before we switch, should I create a handoff for the auth 
    work in case you want to return to it?"

You: "Good idea, yes."

AI: [Creates session handoff]
    "Done. The auth session is saved. Now, what do we know 
     about the billing feature from previous work?"
    [Searches knowledge graph]
    "Last month we discussed using Stripe for payments and 
     decided on a usage-based model. Here's what we captured..."
```

## Dashboard

Visualize your knowledge graph at [createstate.ai/web/dashboard](https://createstate.ai/web/dashboard):

- Interactive knowledge graph visualization
- Session timelines and chat history
- Project insights and recommendations
- Code version history

## API Key Setup for Remote SSH

If you use Cursor's Remote SSH feature to develop on a remote server, OAuth tokens won't sync to the remote host. You must use API key authentication instead.

### Step 1: Get Your API Key

1. Create an account at [createstate.ai/web/signup](https://createstate.ai/web/signup) (or sign in)
2. Go to [createstate.ai/web/api-keys](https://createstate.ai/web/api-keys)
3. Click "Generate New Key" and copy it (starts with `cs_`)

### Step 2: Configure mcp.json

Find the plugin's `mcp.json` file and replace its contents:

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

### Step 3: Restart Cursor

Restart Cursor to apply the changes.

**Important:**
- Use `/api/mcp/` (not `/mcp/`) for API key authentication
- You must hardcode the API key - Cursor does not support `${env:VAR}` syntax for remote servers

## Pricing

A free tier is available to try out the platform. Enhanced options are available for teams and power users.

Visit [createstate.ai/web/#pricing](https://www.createstate.ai/web/#pricing) for details.

## Resources

- **Website**: [createstate.ai](https://createstate.ai)
- **Documentation**: [createstate.ai/web/documentation](https://createstate.ai/web/documentation)
- **API Reference**: [createstate.ai/web/api](https://createstate.ai/web/api)
- **API Keys**: [createstate.ai/web/api-keys](https://createstate.ai/web/api-keys)

## Support

- **Email**: support@createstate.ai
- **GitHub Issues**: [Create an issue](https://github.com/Create-State/cursor-plugin/issues)

## Security & Privacy

Your code and context are encrypted in transit and at rest. We never train on your data.

- [Privacy Policy](https://createstate.ai/web/privacy)
- [Security Policy](https://createstate.ai/web/security-policy)
- [Terms of Service](https://createstate.ai/web/terms)

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**Built with care by the Create State team**

[Website](https://createstate.ai) | [Documentation](https://createstate.ai/web/documentation) | [Support](mailto:support@createstate.ai)
