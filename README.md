 
# Git-Narrate: The Repository Storyteller 📖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Git-Narrate is a Python tool that transforms git repository metadata into a human-readable narrative. It analyzes commit history, branches, tags, and contributor activity to generate a chronological story of a project's development, highlighting key events, milestones, and evolution patterns.

## Features

- **Repository Analysis**: Extracts commit history, branches, tags, and contributor statistics
- **Narrative Generation**: Creates human-readable stories in multiple formats (Markdown, HTML, plain text)
- **Visualization**: Generates timeline and contributor activity charts
- **CLI Interface**: Easy-to-use command-line interface
- **Customizable Output**: Flexible output options for different use cases

## Installation

### From PyPI (recommended)

```bash
pip install git-narrate
```

### From Source

```bash
git clone https://github.com/git-narrate/git-narrate.git
cd git-narrate
pip install .
```

For development installation:

```bash
pip install -e .[dev]
```

## Quick Start

Generate a narrative for a git repository:

```bash
git-narrate /path/to/your/repository
```

This will create a Markdown file named `git_story.md` in the repository directory.

## Usage

### Basic Usage

```bash
git-narrate /path/to/repo
```

### Specify Output Format and Location

```bash
git-narrate /path/to/repo --output=story.html --format=html
```

### Generate Visualizations

```bash
git-narrate /path/to/repo --visualize
```

This will generate two PNG files:
- `timeline.png`: Shows commit activity over time
- `contributors.png`: Shows contributor activity

### Generate Only Visualizations (no narrative)

```bash
git-narrate /path/to/repo --visualize --no-narrative
```

### Command Line Options

```
Usage: git-narrate [OPTIONS] REPO_PATH

  Generate a human-readable story of a git repository's development.

Options:
  -o, --output PATH           Output file path
  -f, --format [markdown|html|text]
                              Output format
  -v, --visualize             Generate visualization charts
  --no-narrative              Skip narrative generation (visualize only)
  --use-ai                    Use AI model for story generation (requires OPENAI_API_KEY)
  --ai-model TEXT             AI model to use (default: glm-4.5-flash)
  --help                      Show this message and exit.
```

## AI-Powered Narrative Generation

Git-Narrate can leverage AI models to generate more sophisticated and engaging narratives. This feature requires an API key for the Z.ai platform (using the `glm-4.5-flash` model by default).

### Setup for AI Generation

1.  **Get an API Key**: Obtain an API key from Z.ai.
2.  **Set Environment Variable**: Set your API key as an environment variable named `OPENAI_API_KEY`.
    *   On Linux/macOS: `export OPENAI_API_KEY="your_api_key_here"`
    *   On Windows (Command Prompt): `set OPENAI_API_KEY="your_api_key_here"`
    *   On Windows (PowerShell): `$env:OPENAI_API_KEY="your_api_key_here"`
    *   Alternatively, create a `.env` file in the root of your project and add `OPENAI_API_KEY="your_api_key_here"` to it.

### Usage with AI

```bash
git-narrate /path/to/repo --use-ai
```

This will generate an AI-powered narrative. You can also specify a different AI model if needed (e.g., `--ai-model glm-4.5`).

### Data Privacy and AI Generation

When using the `--use-ai` flag, Git-Narrate sends processed repository metadata (including project name, timeline events, contributor information, and the content of your `README.md` file) to the Z.ai API.

**Important Considerations:**
*   **Sensitive Data in README.md**: Ensure that your `README.md` file does not contain any sensitive or proprietary information that you do not wish to share with the AI service.
*   **Commit Messages**: While Git-Narrate extracts high-level plot points from commit messages, be mindful that detailed or sensitive information in commit messages could be part of the data sent to the AI.
*   **API Key Security**: Your `OPENAI_API_KEY` is used for authentication with the Z.ai API and should be kept secure. It is recommended to use environment variables or a `.env` file for this purpose.

Git-Narrate aims to provide an accurate and engaging story based on your repository's history while respecting data privacy.

## Examples

### Example 1: Basic Markdown Story

```bash
git-narrate ~/projects/my-awesome-app
```

Creates a Markdown file with the story of `my-awesome-app` development.

### Example 2: HTML Story with Visualizations

```bash
git-narrate ~/projects/my-awesome-app --output=history.html --format=html --visualize
```

Creates an HTML file with the story and PNG files with visualizations.

### Example 3: Only Visualizations

```bash
git-narrate ~/projects/my-awesome-app --visualize --no-narrative
```

Generates only the visualization charts without a narrative.

## Output Samples

### Narrative Sample (Markdown)

```markdown
# The Story of my-awesome-app

## Overview

- **Total Commits**: 120
- **Contributors**: 4
- **Branches**: 3
- **Releases**: 5

## Key Milestones

- 🚀 **2022-01-15**: Project inception
- 🎉 **2022-03-22**: Release v1.0
- 🔀 **2022-07-10**: Major merge: Merge feature/user-authentication

## Development Phases

### January 2022

- **Commits**: 15
- **Contributors**: Jane Doe
- **Period**: 2022-01-15 to 2022-01-31

**Notable Changes**:
- Initial project setup (Jane Doe)
- Add core modules (Jane Doe)

### February 2022

- **Commits**: 22
- **Contributors**: Jane Doe, John Smith
- **Period**: 2022-02-01 to 2022-02-28

**Notable Changes**:
- Implement user authentication (John Smith)
- Add database models (Jane Doe)

## Contributors

### Jane Doe

- **Commits**: 65
- **Lines Added**: 3,420
- **Lines Removed**: 1,210
- **Active Period**: 2022-01-15 to 2022-12-05

### John Smith

- **Commits**: 35
- **Lines Added**: 2,150
- **Lines Removed**: 890
- **Active Period**: 2022-02-10 to 2022-11-20
```

### Visualization Sample

Timeline visualization:
![Timeline](https://raw.githubusercontent.com/git-narrate/git-narrate/main/docs/sample-timeline.png)

Contributors visualization:
![Contributors](https://raw.githubusercontent.com/git-narrate/git-narrate/main/docs/sample-contributors.png)

## How It Works

1. **Repository Analysis**: Git-Narrate uses GitPython to analyze the git repository, extracting:
   - Commit history (author, date, message, files changed)
   - Branches and merge points
   - Tags and releases
   - Contributor activity statistics

2. **Milestone Detection**: The tool identifies key milestones in the repository history:
   - Initial commit
   - Releases (tags)
   - Major merges

3. **Phase Grouping**: Commits are grouped into development phases (monthly by default) to show the evolution of the project over time.

4. **Narrative Generation**: The structured data is transformed into a human-readable story using natural language generation techniques.

5. **Visualization**: Optional charts are generated to visualize repository activity and contributor statistics.

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please:
1. Check the [documentation](https://github.com/git-narrate/git-narrate/wiki)
2. Search existing [issues](https://github.com/git-narrate/git-narrate/issues)
3. Create a new issue if needed

## Roadmap

- [ ] Sentiment analysis of commit messages
- [ ] File evolution tracking
- [ ] Support for remote repositories (GitHub/GitLab)
- [ ] Custom story templates
- [ ] Multi-repository comparison
- [ ] Web interface

## Acknowledgments

- [GitPython](https://github.com/gitpython-developers/GitPython) for git repository access
- [Click](https://click.palletsprojects.com/) for the CLI interface
- [Matplotlib](https://matplotlib.org/) for visualization
- [Rich](https://github.com/Textualize/rich) for enhanced CLI output
```

### 2. CONTRIBUTING.md

```markdown
# Contributing to Git-Narrate

Thank you for your interest in contributing to Git-Narrate! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

This project follows a [Code of Conduct](CODE_OF_CONDUCT.md). Please read and follow it in all interactions with the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with the following information:

1. A clear and descriptive title
2. A detailed description of the problem
3. Steps to reproduce the issue
4. Expected behavior
5. Actual behavior
6. Environment information (OS, Python version, Git-Narrate version)
7. Any relevant error messages or screenshots

### Suggesting Features

We welcome feature suggestions! When suggesting a feature, please:

1. Check if the feature has already been requested
2. Provide a clear and descriptive title
3. Explain the feature in detail
4. Explain why the feature would be useful
5. Provide examples of how the feature would work

### Contributing Code

#### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/git-narrate.git
   cd git-narrate
   ```
3. Set up your development environment:
   ```bash
   pip install -e .[dev]
   pre-commit install
   ```

#### Making Changes

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature-name-or-issue-number
   ```
2. Make your changes
3. Ensure your code follows the project's style guidelines:
   ```bash
   black .
   flake8 .
   mypy git_narrate
   ```
4. Add tests for new functionality or bug fixes
5. Run the tests:
   ```bash
   pytest
   ```
6. Commit your changes with a clear commit message:
   ```bash
   git commit -m "Add feature: Description of the feature"
   ```
7. Push your changes to your fork:
   ```bash
   git push origin feature-name-or-issue-number
   ```
8. Create a pull request to the main repository

#### Pull Request Guidelines

- Ensure your PR has a clear title and description
- Link to any relevant issues
- Make sure all tests pass
- Update documentation if necessary
- Your PR should be focused on a single change or feature

### Documentation Contributions

We welcome documentation improvements! To contribute to the documentation:

1. Fork the repository
2. Make your changes to the documentation files
3. Submit a pull request

## Coding Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all public functions and classes
- Write tests for new functionality

## Getting Help

If you need help with contributing, you can:

1. Create an issue with the "question" label
2. Join our community discussions (link to be added)
3. Contact the maintainers directly

## Project Structure

```
git-narrate/
│
├── git_narrate/               # Main package
│   ├── __init__.py
│   ├── cli.py                 # Command-line interface
│   ├── analyzer.py            # Core repository analysis
│   ├── narrator.py            # Story generation logic
│   ├── visualizer.py          # Optional visualization
│   └── utils.py               # Helper functions
│
├── tests/                     # Unit tests
│   ├── __init__.py
│   ├── test_analyzer.py
│   ├── test_narrator.py
│   └── fixtures/              # Sample repos for testing
│       └── sample_repo.git/
│
├── docs/                      # Documentation
│   └── ...
│
├── requirements.txt           # Dependencies
├── setup.py                   # Package configuration
├── README.md                  # Main documentation
├── CONTRIBUTING.md            # Contribution guidelines
├── LICENSE                    # MIT License
└── CODE_OF_CONDUCT.md         # Code of Conduct
```

Thank you for contributing to Git-Narrate!
```

### 3. LICENSE

```markdown
MIT License

Copyright (c) 2023 Git-Narrate Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 4. CODE_OF_CONDUCT.md

```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
contact@git-narrate.dev.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.
```

### 5. docs/usage.md

```markdown
# Git-Narrate Usage Guide

This guide provides detailed information on how to use Git-Narrate to analyze git repositories and generate development narratives.

## Installation

Before using Git-Narrate, ensure you have Python 3.8 or higher installed. Then install Git-Narrate:

```bash
pip install git-narrate
```

For development installation, see the [Contributing Guide](../CONTRIBUTING.md).

## Basic Usage

The simplest way to use Git-Narrate is to provide a path to a git repository:

```bash
git-narrate /path/to/your/repository
```

This will analyze the repository and create a Markdown file named `git_story.md` in the repository directory.

## Command Line Options

Git-Narrate provides several command line options to customize its behavior:

### Output Options

- `--output`, `-o`: Specify the output file path
  ```bash
  git-narrate /path/to/repo --output=my_project_story.md
  ```

- `--format`, `-f`: Specify the output format (markdown, html, or text)
  ```bash
  git-narrate /path/to/repo --format=html
  ```

### Visualization Options

- `--visualize`, `-v`: Generate visualization charts
  ```bash
  git-narrate /path/to/repo --visualize
  ```

- `--no-narrative`: Skip narrative generation (only generate visualizations)
  ```bash
  git-narrate /path/to/repo --visualize --no-narrative
  ```

## Examples

### Example 1: Generate a Markdown Story

```bash
git-narrate ~/projects/my-awesome-app
```

This creates a Markdown file named `git_story.md` in the `~/projects/my-awesome-app` directory.

### Example 2: Generate an HTML Story with Custom Output Path

```bash
git-narrate ~/projects/my-awesome-app --output=~/docs/history.html --format=html
```

This creates an HTML file named `history.html` in the `~/docs` directory.

### Example 3: Generate Visualizations Only

```bash
git-narrate ~/projects/my-awesome-app --visualize --no-narrative
```

This generates two PNG files in the repository directory:
- `timeline.png`: Shows commit activity over time
- `contributors.png`: Shows contributor activity

### Example 4: Generate a Complete Report with Visualizations

```bash
git-narrate ~/projects/my-awesome-app --output=~/reports/report.html --format=html --visualize
```

This creates an HTML report with visualizations in the `~/reports` directory and PNG files in the repository directory.

## Understanding the Output

### Narrative Output

The narrative output is structured into several sections:

1. **Overview**: Provides summary statistics about the repository
2. **Key Milestones**: Highlights important events in the repository's history
3. **Development Phases**: Groups commits into time-based phases and summarizes activity
4. **Contributors**: Details about each contributor's activity

### Visualization Output

Git-Narrate generates two types of visualizations:

1. **Timeline Visualization**: A bar chart showing commit activity over time
   - X-axis: Time (months)
   - Y-axis: Number of commits
   - Each bar represents the number of commits in a month

2. **Contributors Visualization**: A horizontal bar chart showing contributor activity
   - Y-axis: Contributor names
   - X-axis: Number of commits
   - Each bar represents the number of commits by a contributor

## Advanced Usage

### Analyzing Remote Repositories

Currently, Git-Narrate works with local git repositories. To analyze a remote repository:

1. Clone the repository locally:
   ```bash
   git clone https://github.com/user/repo.git
   ```
2. Run Git-Narrate on the local clone:
   ```bash
   git-narrate repo
   ```

### Customizing the Narrative

The narrative generation is based on heuristics to identify important events and phases. You can influence the narrative by:

1. **Using clear commit messages**: Git-Narrate analyzes commit messages to identify significant changes
2. **Using tags**: Tags are treated as release milestones
3. **Using branch names**: Branch names are included in the analysis

### Large Repositories

For large repositories with many commits, Git-Narrate may take longer to analyze. You can:

1. Use the `--no-narrative` option to generate only visualizations
2. Consider analyzing specific branches or time periods (future feature)

## Troubleshooting

### Common Issues

1. **"Not a git repository" error**
   - Ensure the path you provide is a git repository (contains a `.git` directory)
   - Check if you have read permissions for the repository

2. **"No commits found" error**
   - The repository might be empty (no commits)
   - Check if you're in the correct branch

3. **Visualization files not generated**
   - Ensure you have the required visualization dependencies installed
   - Check if you have write permissions in the output directory

### Getting Help

If you encounter issues not covered here:

1. Check the [issues](https://github.com/git-narrate/git-narrate/issues) page
2. Create a new issue with details about your problem
3. Include the command you ran and any error messages
```

### 6. docs/api.md

```markdown
# Git-Narrate API Documentation

This document provides detailed information about Git-Narrate's internal API for developers who want to extend or integrate with the tool.

## Core Modules

### analyzer.py

The `analyzer.py` module contains the `RepoAnalyzer` class, which is responsible for extracting data from git repositories.

#### RepoAnalyzer

```python
class RepoAnalyzer:
    def __init__(self, repo_path: Path)
    def analyze(self) -> Dict[str, Any]
    def _get_commits(self) -> List[Dict[str, Any]]
    def _get_branches(self) -> List[Dict[str, Any]]
    def _get_tags(self) -> List[Dict[str, Any]]
    def _get_contributors(self) -> Dict[str, Dict[str, Any]]
```

**Methods:**

- `__init__(repo_path)`: Initialize the analyzer with a path to a git repository
- `analyze()`: Perform complete repository analysis and return structured data
- `_get_commits()`: Extract commit history
- `_get_branches()`: Get branch information
- `_get_tags()`: Get tag information
- `_get_contributors()`: Get contributor statistics

**Example Usage:**

```python
from git_narrate.analyzer import RepoAnalyzer
from pathlib import Path

analyzer = RepoAnalyzer(Path("/path/to/repo"))
repo_data = analyzer.analyze()
```

### narrator.py

The `narrator.py` module contains the `RepoNarrator` class, which is responsible for generating human-readable narratives from repository data.

#### RepoNarrator

```python
class RepoNarrator:
    def __init__(self, repo_data: Dict[str, Any])
    def generate_story(self, output_format: str = "markdown") -> str
    def _detect_milestones(self) -> List[Dict[str, Any]]
    def _group_into_phases(self) -> List[Dict[str, Any]]
    def _generate_markdown(self) -> str
    def _generate_html(self) -> str
    def _generate_text(self) -> str
    def _markdown_to_html(self, md_text: str) -> str
    def _is_significant(self, commit: Dict[str, Any]) -> bool
```

**Methods:**

- `__init__(repo_data)`: Initialize the narrator with repository data
- `generate_story(output_format)`: Generate a story in the specified format
- `_detect_milestones()`: Identify key milestones in repository history
- `_group_into_phases()`: Group commits into development phases
- `_generate_markdown()`: Generate story in Markdown format
- `_generate_html()`: Generate story in HTML format
- `_generate_text()`: Generate story in plain text format
- `_markdown_to_html()`: Convert Markdown to HTML
- `_is_significant()`: Determine if a commit is significant

**Example Usage:**

```python
from git_narrate.narrator import RepoNarrator

narrator = RepoNarrator(repo_data)
story = narrator.generate_story("markdown")
```

### visualizer.py

The `visualizer.py` module contains the `RepoVisualizer` class, which is responsible for generating visualizations from repository data.

#### RepoVisualizer

```python
class RepoVisualizer:
    def __init__(self, repo_data: Dict[str, Any])
    def plot_timeline(self, output_path: Path)
    def plot_contributors(self, output_path: Path)
```

**Methods:**

- `__init__(repo_data)`: Initialize the visualizer with repository data
- `plot_timeline(output_path)`: Generate a timeline visualization and save to file
- `plot_contributors(output_path)`: Generate a contributors visualization and save to file

**Example Usage:**

```python
from git_narrate.visualizer import RepoVisualizer
from pathlib import Path

visualizer = RepoVisualizer(repo_data)
visualizer.plot_timeline(Path("/path/to/timeline.png"))
visualizer.plot_contributors(Path("/path/to/contributors.png"))
```

### utils.py

The `utils.py` module contains utility functions used throughout the project.

#### Functions

```python
def format_date(date: datetime) -> str
def format_duration(start: datetime, end: datetime) -> str
def get_top_contributors(contributors: Dict[str, Dict[str, Any]], limit: int = 5) -> List[Dict[str, Any]]
def clean_commit_message(message: str) -> str
```

**Functions:**

- `format_date()`: Format a datetime object for display
- `format_duration()`: Calculate and format a duration between two dates
- `get_top_contributors()`: Get the top contributors by commit count
- `clean_commit_message()`: Clean up a commit message for display

## Data Structures

### Repository Data

The `analyze()` method of `RepoAnalyzer` returns a dictionary with the following structure:

```python
{
    "repo_name": str,                    # Name of the repository
    "commits": [                         # List of commits
        {
            "sha": str,                  # Commit SHA
            "author": str,               # Author name
            "email": str,                # Author email
            "date": datetime,            # Commit date
            "message": str,              # Commit message
            "files_changed": int,        # Number of files changed
            "insertions": int,           # Number of lines inserted
            "deletions": int,            # Number of lines deleted
            "is_merge": bool             # Whether the commit is a merge
        },
        ...
    ],
    "branches": [                        # List of branches
        {
            "name": str,                 # Branch name
            "commit": str,               # Branch commit SHA
            "is_remote": bool            # Whether the branch is remote
        },
        ...
    ],
    "tags": [                            # List of tags
        {
            "name": str,                 # Tag name
            "commit": str,               # Tag commit SHA
            "date": datetime             # Tag date (if available)
        },
        ...
    ],
    "contributors": {                    # Dictionary of contributors
        "author_name": {
            "commits": int,              # Number of commits
            "insertions": int,           # Number of lines inserted
            "deletions": int,            # Number of lines deleted
            "first_commit": datetime,    # First commit date
            "last_commit": datetime      # Last commit date
        },
        ...
    }
}
```

### Milestones

The `_detect_milestones()` method of `RepoNarrator` returns a list of milestones with the following structure:

```python
[
    {
        "type": str,                     # Milestone type ("initial", "release", "merge")
        "date": datetime,                # Milestone date
        "description": str,               # Milestone description
        "commit": str,                   # Commit SHA
        "author": str                    # Author name (if available)
    },
    ...
]
```

### Phases

The `_group_into_phases()` method of `RepoNarrator` returns a list of phases with the following structure:

```python
[
    {
        "month": str,                    # Month in "YYYY-MM" format
        "commits": [                     # List of commits in this phase
            {
                "sha": str,
                "author": str,
                "date": datetime,
                "message": str,
                "files_changed": int,
                "insertions": int,
                "deletions": int,
                "is_merge": bool
            },
            ...
        ],
        "contributors": set,             # Set of contributor names
        "start_date": datetime,          # First commit date in phase
        "end_date": datetime             # Last commit date in phase
    },
    ...
]
```

## Extending Git-Narrate

### Adding New Output Formats

To add a new output format:

1. Add a new method to the `RepoNarrator` class in `narrator.py`:
   ```python
   def _generate_new_format(self) -> str:
       # Implementation for the new format
       pass
   ```

2. Update the `generate_story()` method to handle the new format:
   ```python
   def generate_story(self, output_format: str = "markdown") -> str:
       if output_format.lower() == "new_format":
           return self._generate_new_format()
       # ... existing code ...
   ```

3. Update the CLI in `cli.py` to include the new format in the choices:
   ```python
   @click.option("--format", "-f", "output_format", 
                 type=click.Choice(["markdown", "html", "text", "new_format"], case_sensitive=False),
                 default="markdown", help="Output format")
   ```

### Adding New Visualizations

To add a new visualization:

1. Add a new method to the `RepoVisualizer` class in `visualizer.py`:
   ```python
   def plot_new_visualization(self, output_path: Path):
       # Implementation for the new visualization
       pass
   ```

2. Update the CLI in `cli.py` to include an option for the new visualization:
   ```python
   @click.option("--new-viz", is_flag=True, help="Generate new visualization")
   def main(repo_path, output, output_format, visualize, no_narrative, new_viz):
       # ...
       if new_viz:
           visualizer.plot_new_visualization(repo_path / "new_viz.png")
       # ...
   ```

### Adding New Analysis Features

To add a new analysis feature:

1. Add a new method to the `RepoAnalyzer` class in `analyzer.py`:
   ```python
   def _get_new_feature(self) -> SomeDataType:
       # Implementation for the new feature
       pass
   ```

2. Update the `analyze()` method to include the new feature:
   ```python
   def analyze(self) -> Dict[str, Any]:
       return {
           # ... existing data ...
           "new_feature": self._get_new_feature()
       }
   ```

3. Update the `RepoNarrator` class to use the new feature in the narrative generation if needed.
```

This comprehensive documentation provides everything users and contributors need to understand, use, and extend Git-Narrate. The documentation includes installation instructions, usage examples, API reference, and contribution guidelines.
#   G i t - N a r r a t e  
 