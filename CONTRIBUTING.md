# Contributing to Create State Cursor Plugin

Thank you for your interest in contributing to the Create State Cursor Plugin! This document provides guidelines for contributing.

## Ways to Contribute

### Reporting Issues

If you find a bug or have a feature request:

1. Check existing [issues](https://github.com/Create-State/cursor-plugin/issues) to avoid duplicates
2. Create a new issue with a clear title and description
3. Include steps to reproduce (for bugs) or use cases (for features)
4. Add relevant labels if possible

### Suggesting Improvements

We welcome suggestions for:

- New skills or rules
- Documentation improvements
- Workflow enhancements
- Integration ideas

### Pull Requests

For code contributions:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Test thoroughly in Cursor
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

## Development Setup

### Prerequisites

- Cursor IDE
- Create State account with API key
- Git

### Local Testing

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/cursor-plugin.git
   ```

2. Copy to Cursor's local plugins directory:
   ```bash
   mkdir -p ~/.cursor/plugins/local
   cp -r cursor-plugin ~/.cursor/plugins/local/create-state
   ```

3. Restart Cursor and verify the plugin loads

4. Test your changes in a real Cursor session

### Running Tests

```bash
cd cursor-plugin
pytest tests/ -v
```

## Code Guidelines

### Rules (.mdc files)

- Use clear, concise descriptions
- Include practical examples
- Test with multiple AI models

### Skills (SKILL.md files)

- Follow the established skill format
- Include step-by-step instructions
- Reference appropriate MCP tools

### General

- Keep changes focused and minimal
- Update documentation as needed
- Follow existing code style

## Questions?

- Open a [discussion](https://github.com/Create-State/cursor-plugin/discussions)
- Email us at support@createstate.ai

## Code of Conduct

Be respectful, inclusive, and constructive. We're all here to build something useful together.

---

Thank you for contributing to Create State!
