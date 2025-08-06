import click
from pathlib import Path
from .analyzer import RepoAnalyzer
from .narrator import RepoNarrator
from .visualizer import RepoVisualizer

@click.command()
@click.argument("repo_path", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option("--output", "-o", type=click.Path(), default=None, help="Output file path")
@click.option("--format", "-f", "output_format", 
              type=click.Choice(["markdown", "html", "text"], case_sensitive=False),
              default="markdown", help="Output format")
@click.option("--visualize", "-v", is_flag=True, help="Generate visualization charts")
@click.option("--no-narrative", is_flag=True, help="Skip narrative generation (visualize only)")
@click.option("--use-ai", is_flag=True, help="Use AI model for story generation (requires OPENAI_API_KEY)")
@click.option("--ai-model", default="gpt-4-turbo", help="AI model to use (default: gpt-4-turbo)")
def main(repo_path, output, output_format, visualize, no_narrative, use_ai, ai_model):
    """Generate a human-readable story of a git repository's development."""
    repo_path = Path(repo_path)
    
    if output:
        output_path = Path(output)
    else:
        output_path = repo_path / f"git_story.{output_format}"
    
    # Analyze repository
    click.echo(f"Analyzing repository at {repo_path}...")
    analyzer = RepoAnalyzer(repo_path)
    repo_data = analyzer.analyze()
    
    # Generate narrative
    if not no_narrative:
        if use_ai:
            click.echo("Generating AI-powered narrative...")
            click.echo(f"Using model: {ai_model}")
        else:
            click.echo("Generating narrative...")
        
        narrator = RepoNarrator(repo_data, use_ai=use_ai)
        story = narrator.generate_story(output_format)
        
        # Save narrative
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(story)
        click.echo(f"Narrative saved to {output_path}")
    
    # Generate visualization
    if visualize:
        click.echo("Generating visualizations...")
        visualizer = RepoVisualizer(repo_data)
        timeline_path = repo_path / "timeline.png"
        contributors_path = repo_path / "contributors.png"
        
        visualizer.plot_timeline(timeline_path)
        visualizer.plot_contributors(contributors_path)
        
        click.echo(f"Timeline saved to {timeline_path}")
        click.echo(f"Contributors chart saved to {contributors_path}")

if __name__ == "__main__":
    main()