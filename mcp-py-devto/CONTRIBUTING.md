# Contributing to MCP Python Dev.to Integration

Thank you for your interest in contributing to this project! This document provides guidelines and steps for contributing.

## Code of Conduct

By participating in this project, you agree to follow our Code of Conduct:
- Be respectful and inclusive
- Use welcoming language
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/mcp-py-devto/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

### Suggesting Enhancements

1. Open a new issue describing:
   - The proposed feature
   - Why it would be useful
   - Possible implementation approaches

### Pull Request Process

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes following our coding standards
4. Write or update tests as needed
5. Update documentation if required
6. Run the test suite:
   ```bash
   pytest tests/
   ```
7. Commit your changes:
   ```bash
   git commit -m "Add: brief description of changes"
   ```
8. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
9. Open a Pull Request

## Development Setup

1. Follow the installation steps in the README.md
2. Install development dependencies:
   ```bash
   pip install .
   ```

## Coding Standards

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Write tests for new functionality

## Testing

- Write unit tests for new features
- Ensure all tests pass before submitting PR
- Maintain or improve code coverage

## Documentation

- Update README.md if adding new features
- Document new functions/classes with docstrings
- Update API documentation if endpoints change

## Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, maintainers will merge your PR

## Release Process

1. Version numbers follow [Semantic Versioning](https://semver.org/)
2. Changes are documented in CHANGELOG.md
3. Releases are tagged in git

## Additional Notes

- If you need help, create an issue or contact maintainers
- For security issues, please email security@example.com
- Join our community chat for discussions

Thank you for contributing to MCP Python Dev.to Integration!
