# Contributing to AI Personalization Restoration Framework

Thank you for your interest in contributing! This document provides guidelines for contributions.

## How to Contribute

### Reporting Issues

If you encounter problems:
1. Check if the issue already exists in [GitHub Issues](https://github.com/yourusername/ai-personalization-framework/issues)
2. If not, create a new issue with:
   - Clear description of the problem
   - Model and version used
   - Stage where issue occurred
   - Expected vs. actual behavior
   - Steps to reproduce

### Suggesting Enhancements

For feature requests:
1. Open an issue tagged as "enhancement"
2. Describe the use case
3. Explain why existing functionality doesn't address it
4. Propose implementation approach if possible

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: brief description of what you added"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**

### Contributing Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add examples from real-world usage
- Translate to other languages
- Improve formatting or organization

### Contributing Examples

Real-world examples help others:
1. Use the template in `templates/`
2. Anonymize sensitive information
3. Include:
   - Role description
   - Complete configuration
   - Validation checkpoints
   - Lessons learned
4. Place in appropriate `examples/` subdirectory

## Code Standards

### Markdown Files
- Use ATX-style headers (`#` not underlines)
- Maximum line length: 120 characters for prose
- Use code fences with language identifiers
- Include table of contents for docs > 200 lines

### Python Scripts (if contributing tools)
- PEP 8 compliance
- Type hints for function parameters
- Docstrings for public functions
- Comprehensive error handling

### Prompt Text
- Preserve original structure and logic
- Add clarifications in separate sections
- Test changes across multiple models
- Document model-specific variations

## Pull Request Process

1. **Update documentation** if you change functionality
2. **Add tests** if you add tools/scripts
3. **Update CHANGELOG.md** with your changes
4. **Ensure all files** have appropriate headers/licenses
5. **Request review** from maintainers
6. **Address feedback** promptly

### PR Title Format
```
Type: Brief description

Types:
- Add: New feature or example
- Fix: Bug fix
- Docs: Documentation only
- Refactor: Code restructuring
- Test: Test additions/changes
```

### PR Description Template
```markdown
## Description
[What does this PR do?]

## Motivation
[Why is this change needed?]

## Changes
- [List key changes]

## Testing
[How was this tested?]

## Checklist
- [ ] Documentation updated
- [ ] Examples added (if applicable)
- [ ] Tested across multiple models (if applicable)
- [ ] No breaking changes (or documented if yes)
```

## Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment:
- **Be respectful** of differing viewpoints and experiences
- **Be collaborative** - we're building something together
- **Be constructive** in feedback
- **Be patient** with new contributors
- **Be clear** in communication

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or trolling
- Publishing others' private information
- Spam or excessive self-promotion
- Other conduct inappropriate in a professional setting

## Questions?

- **General questions:** Open a [GitHub Discussion](https://github.com/yourusername/ai-personalization-framework/discussions)
- **Bug reports:** Open an [Issue](https://github.com/yourusername/ai-personalization-framework/issues)
- **Security concerns:** Email [security contact]

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Thanked in project documentation

Significant contributors may be invited to become maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make AI personalization restoration accessible to everyone!
