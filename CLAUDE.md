# CLAUDE.md

## Project Overview

This is a **Git training repository** used for learning and practicing basic Git commands and workflows. The content is written in Japanese. There is no application code, build system, or runtime — only text files documenting Git learning progress.

## Repository Structure

```
intro_git/
├── CLAUDE.md          # This file — guidance for AI assistants
├── first.txt.txt      # Main learning notes (Git commands reference)
└── second.txt         # Additional file used for multi-file commit practice
```

## File Details

- **first.txt.txt** — Contains a list of Git commands being learned (`git add`, `git commit`, `git rm`, `git status`, `git diff`), written in Japanese.
- **second.txt** — A simple file ("追加したファイル" / "Added file") created to practice multi-file commits.

## Languages and Tools

- **Language:** Plain text (Japanese / UTF-8)
- **No programming languages, frameworks, or libraries**
- **No package manager or dependency files**
- **No build system**

## Development Workflow

There is no build, lint, or test workflow. Changes are made directly to text files and committed with Git.

### Common Git operations practiced in this repo

```bash
git add <file>
git commit -m "message"
git rm <file>
git status
git diff
```

## Testing

No tests exist. There is no test framework or test runner.

## Linting / Formatting

No linting or formatting tools are configured.

## CI/CD

No CI/CD pipelines are configured.

## Conventions

- **Commit messages** are written in Japanese, describing the change concisely (e.g., "git diffを追記", "複数ファイルのコミット").
- **File naming** is simple and descriptive.
- **Branch strategy:** Primary branch is `master`.

## Key Context for AI Assistants

- This is an educational/learning repo, not a production project.
- Content is in Japanese — preserve the language when editing existing files.
- Keep changes minimal and aligned with the repo's purpose of demonstrating Git basics.
- There is no `.gitignore` — be mindful not to introduce generated or sensitive files.
