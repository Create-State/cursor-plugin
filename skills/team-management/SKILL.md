---
name: team-management
description: Manage teams, members, and project sharing in Create State. Use when the user wants to set up teams, invite members, share projects, or manage working capacity.
---

# Team Management Skill

Manage teams, members, and project sharing for enterprise collaboration.

## When to Use

- When user wants to create or manage teams
- When user needs to invite or remove team members
- When user wants to share projects with teams
- When user asks about working capacity
- When user needs team activity or contributor info

## Step-by-Step: Creating a Team

### Step 1: Create the Team

```
Tool: createTeam
Arguments:
  name: "Backend Team"
  description: "API and services team"
```

### Step 2: Invite Members

```
Tool: inviteToTeam
Arguments:
  team_id: "<team ID from step 1>"
  email: "developer@example.com"
  role: "member"  # or "admin", "viewer"
```

Roles:
- **admin**: Full team management permissions
- **member**: Standard team member, can contribute
- **viewer**: Read-only access to team resources

### Step 3: Share Projects

```
Tool: shareProjectWithTeam
Arguments:
  team_id: "<team ID>"
  world_model_id: "<project ID>"
  permission: "write"  # or "read", "admin"
```

## Step-by-Step: Managing Working Capacity

Working capacity determines which team context you operate under for a project.

### Check Current Capacity

```
Tool: getWorkingCapacity
Arguments:
  world_model_id: "<project ID>"
```

This returns:
- Current team context (if any)
- Available team options
- AI policy restrictions

### Set Working Capacity

```
Tool: setWorkingCapacity
Arguments:
  world_model_id: "<project ID>"
  team_id: "<team ID>"  # or omit for personal capacity
```

## Step-by-Step: Team Intelligence

### Find Topic Experts

When user asks "Who knows about authentication?" or similar:

```
Tool: findTopicExpert
Arguments:
  topic: "authentication"
  team_id: "<optional - limit to specific team>"
```

### Get Team Pulse

For an overview of team activity:

```
Tool: getTeamPulse
Arguments:
  team_id: "<optional filter>"
  world_model_id: "<optional filter>"
```

### Check Colleague Activity

When user asks "What has Sarah been working on?":

```
Tool: getColleagueActivity
Arguments:
  colleague_email: "sarah@example.com"
  days: 7  # default lookback
```

### Get Contributor Stats

For detailed contribution metrics:

```
Tool: getContributorStats
Arguments:
  contributor_email: "developer@example.com"
  world_model_id: "<optional filter>"
```

## Listing Resources

### List Your Teams

```
Tool: listTeams
Arguments: {}
```

### List Team Members

```
Tool: listTeamMembers
Arguments:
  team_id: "<team ID>"
```

### List Team Projects

```
Tool: listTeamProjects
Arguments:
  team_id: "<team ID>"
```

### Get Team Details

```
Tool: getTeamDetails
Arguments:
  team_id: "<team ID>"
```

## Member Management

### Update Member Role

```
Tool: updateMemberRole
Arguments:
  team_id: "<team ID>"
  user_id: "<user ID>"
  role: "admin"  # or "member", "viewer"
```

### Remove Member

```
Tool: removeTeamMember
Arguments:
  team_id: "<team ID>"
  user_id: "<user ID>"
```

## Project Sharing

### Share Project

```
Tool: shareProjectWithTeam
Arguments:
  team_id: "<team ID>"
  world_model_id: "<project ID>"
  permission: "write"
```

### Unshare Project

```
Tool: unshareProjectFromTeam
Arguments:
  team_id: "<team ID>"
  world_model_id: "<project ID>"
```

## Example Conversations

### "Create a team for our backend developers"

1. Call `createTeam` with name "Backend Team"
2. Get the team_id from the response
3. Report success and ask if they want to invite members

### "Share this project with the Backend Team"

1. Get active model for project ID (from session)
2. Call `listTeams` to find Backend Team ID (or ask user)
3. Call `shareProjectWithTeam` with the IDs
4. Report sharing confirmation

### "Who on my team knows about billing?"

1. Call `findTopicExpert` with topic "billing"
2. Present the experts with their expertise scores
3. Suggest reaching out to the top expert

### "What's the team pulse?"

1. Call `getTeamPulse`
2. Summarize active members, recent activity, top contributors
3. Highlight any notable patterns or insights

## Troubleshooting

### "Feature requires Teams tier"
User needs to upgrade to Teams or Enterprise subscription.

### "Permission denied"
User may not have admin role on the team. Check their role with `getTeamDetails`.

### "Team not found"
Verify team ID. Use `listTeams` to get correct IDs.
