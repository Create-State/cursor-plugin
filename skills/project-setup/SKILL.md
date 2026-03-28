---
name: project-setup
description: Initialize a new project with Create State monitoring and world model. Use when starting work on a new project, onboarding to an existing codebase, or when the user wants to set up knowledge tracking.
---

# Project Setup Skill

Initialize a new project with Create State for knowledge tracking, AI monitoring, and session continuity.

## When to Use

- Starting work on a new project
- Onboarding to an existing codebase
- User says "set up Create State for this project"
- User wants to start tracking decisions and code
- No existing world model for current project

## Step-by-Step Process

### Step 1: Check for Existing World Model

First, check if a world model already exists:

```
Tool: listUserWorldModels
Arguments: {}
```

Look for a model matching the current project. If one exists, use it instead of creating a new one.

### Step 2: Create World Model

If no existing model, create one:

```
Tool: createWorldModel
Arguments:
  project_name: "My Project Name"
  language: "python"  # or javascript, typescript, auto
  description: "Brief description of the project"
```

**Parameters:**
- `project_name` (required): A descriptive name for the project
- `language` (required): Primary programming language (or "auto" for mixed)
- `description`: Brief project description

The created model becomes your active model automatically.

### Step 3: Start Project Monitoring

Enable autonomous AI monitoring:

```
Tool: startProjectMonitoring
Arguments:
  project_path: "."
  project_name: "My Project Name"
  goals: ["Build authentication system", "Improve test coverage"]
```

**Parameters:**
- `project_path` (required): Path to project directory (usually ".")
- `project_name`: Custom name (defaults to directory name)
- `goals`: Array of project goals/objectives

Monitoring enables:
- Background codebase analysis
- Proactive insight generation
- Pattern detection
- Continuous context building

### Step 4: Initial Context Capture

Capture initial project context to seed the knowledge graph:

```
Tool: captureConversationContext
Arguments:
  context: "## Project Initialization

### Project Overview
[Brief description of what this project does]

### Technology Stack
- Language: Python 3.11
- Framework: FastAPI
- Database: PostgreSQL
- Cache: Redis

### Key Directories
- src/ - Main source code
- tests/ - Test suite
- docs/ - Documentation

### Current Priorities
1. [Priority 1]
2. [Priority 2]

### Known Issues
- [Any known issues or tech debt]"
```

### Step 5: Verify Setup

Confirm everything is working:

```
Tool: getProjectWorldModel
Arguments:
  project_path: "."
  include_insights: true
```

This should return the newly created model with initial context.

## Complete Example

**User:** "Set up Create State for this React project"

**Assistant:**

1. Check existing models:
```
listUserWorldModels: {}
# Result: No matching model found
```

2. Create world model:
```
createWorldModel:
  project_name: "React Dashboard"
  language: "typescript"
  description: "Admin dashboard with charts and user management"
```

3. Start monitoring:
```
startProjectMonitoring:
  project_path: "."
  project_name: "React Dashboard"
  goals: ["Implement user management", "Add real-time charts"]
```

4. Capture initial context:
```
captureConversationContext:
  context: "## React Dashboard - Project Setup

### Overview
Admin dashboard for managing users and viewing analytics.

### Tech Stack
- React 18 with TypeScript
- Vite for build
- TailwindCSS for styling
- React Query for data fetching
- Recharts for visualizations

### Structure
- src/components/ - Reusable UI components
- src/pages/ - Route pages
- src/hooks/ - Custom React hooks
- src/api/ - API client functions"
```

5. Confirm to user:
"I've set up Create State for your React Dashboard project. The knowledge graph is ready to track your decisions and code. I'll capture important context as we work, and you can restore this session anytime with a handoff."

## What Happens After Setup

Once set up:
- **Automatic capture targeting**: All captures go to this model
- **Background analysis**: AI monitors and generates insights
- **Session continuity**: Create handoffs to preserve state
- **Knowledge accumulation**: Decisions and code build over time

## Recommended Next Steps

After initial setup, suggest:

1. **Explore the codebase**: Ask questions to understand the project
2. **Capture existing knowledge**: Document known patterns and decisions
3. **Set up session workflow**: Create handoffs at session end
4. **Check insights**: Use `getProactiveInsights` to see AI observations

## Troubleshooting

### Model creation fails
- Check API key is valid
- Ensure project_name is unique
- Verify account has available model quota

### Monitoring doesn't start
- Check project_path exists
- Verify directory has code files
- Try with explicit project_path instead of "."

### No insights generated
- Monitoring takes time to analyze
- Check back after a few minutes
- Ensure codebase has sufficient content
