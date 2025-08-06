# Git-Narrate User Guide 📖

Welcome to Git-Narrate! This guide will help you get started with turning your project's history into an exciting story.

## What is Git-Narrate?

Imagine your project is like a movie, and every change you make is a scene. Git-Narrate is like a movie director that watches all these scenes and creates a story about how your project was made. It looks at your project's `git` history (the log of all your changes) and writes a narrative about it.

## Getting Started

### 1. Installation

To use Git-Narrate, you first need to install it on your computer. Open your terminal or command prompt and type the following command:

```bash
pip install git-narrate
```

This will download and install Git-Narrate so you can use it from anywhere on your computer.

### 2. Running Git-Narrate

Once installed, you can run Git-Narrate on any of your projects that use `git`.

1.  **Navigate to your project folder:**
    Open your terminal and go to the folder of the project you want to analyze. For example:
    ```bash
    cd /path/to/your/project
    ```

2.  **Run the command:**
    Now, simply run the `git-narrate` command, telling it to look at the current folder (`.`):
    ```bash
    git-narrate .
    ```

This will create a new file in your project folder called `git_story.md`. This file contains the story of your project's development!

## Fun Things You Can Do

### Create an HTML Story

If you want a story that looks like a webpage, you can tell Git-Narrate to create an HTML file.

```bash
git-narrate . --output=my_story.html --format=html
```

This will create a file named `my_story.html` that you can open in your web browser.

### Create Visualizations

Git-Narrate can also create cool charts to show you who has contributed to your project and when most of the work was done.

```bash
git-narrate . --visualize
```

This will create two image files:
*   `timeline.png`: A chart showing how many changes were made over time.
*   `contributors.png`: A chart showing who made the most changes.

## AI-Powered Storytelling (Now Default!)

Git-Narrate now uses Artificial Intelligence by default to create detailed and engaging stories about your project's journey. To make this work, you'll need to set up an API key:

1.  **Get an API Key:**
    This feature uses the Z.ai platform. You'll need to get an API key from them.

2.  **Set up your API Key:**
    *   Create a file named `.env` in your project folder.
    *   Inside this file, add the following line, replacing `"your_api_key_here"` with your actual key:
        ```
        OPENAI_API_KEY="your_api_key_here"
        ```

Now, Git-Narrate will automatically use AI to write a more creative story about your project's journey.

## For Developers: A Quick Look Under the Hood

If you're a developer and want to contribute to Git-Narrate, here's a quick overview of how it works:

*   **`analyzer.py`**: This is the heart of the tool. It uses `GitPython` to read the `.git` folder and extract all the data about commits, branches, tags, and contributors.
*   **`narrator.py`**: This module takes the data from the analyzer and turns it into a story. It has different functions to create Markdown, HTML, or plain text stories.
*   **`ai_narrator.py`**: This module sends the project data to the Z.ai API and gets back a more detailed story.
*   **`visualizer.py`**: This module uses `matplotlib` to create the timeline and contributor charts.
*   **`cli.py`**: This file defines the command-line interface using `click`, so you can run `git-narrate` with different options.

### Contributing

We welcome contributions! If you want to help make Git-Narrate even better, please check out our [Contributing Guide](https://github.com/000xs/Git-Narrate/blob/main/CONTRIBUTING.md).

### License

Git-Narrate is licensed under the MIT License. You can find more details in the [LICENSE](https://github.com/000xs/Git-Narrate/blob/main/LICENSE) file.
