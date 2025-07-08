# Pre-Commit Hooks

## Definition

    Script that run automatically before "git commit"

### Purpose

    Enforce code style (Flake8)
    Run tests (pytest)
    Prevent bad commits

### Working Setup

    create a yaml or yml file
        - pre-commit-config.yml (root dir)
        - pytest.ini (with pythonpath)
