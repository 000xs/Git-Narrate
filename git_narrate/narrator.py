from typing import Dict, Any, List
from datetime import datetime
import re
from .ai_narrator import AINarrator

class RepoNarrator:
    def __init__(self, repo_data: Dict[str, Any], use_ai: bool = False):
        self.repo_data = repo_data
        self.use_ai = use_ai
        if not use_ai:
            self.milestones = self._detect_milestones()
            self.phases = self._group_into_phases()
    
    def generate_story(self, output_format: str = "markdown") -> str:
        """Generate the repository story in the specified format."""
        if self.use_ai:
            ai_narrator = AINarrator(self.repo_data)
            story = ai_narrator.generate_story()
            return self._format_ai_story(story, output_format)
        else:
            if output_format.lower() == "html":
                return self._generate_html()
            elif output_format.lower() == "text":
                return self._generate_text()
            return self._generate_markdown()
    
    def _format_ai_story(self, story: str, output_format: str) -> str:
        """Format the AI-generated story for output."""
        if output_format.lower() == "html":
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>The Story of {self.repo_data['repo_name']}</title>
                <style>
                    body {{ font-family: Georgia, serif; line-height: 1.8; max-width: 800px; margin: 0 auto; padding: 40px; }}
                    h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                    .story {{ text-align: justify; }}
                </style>
            </head>
            <body>
                <h1>The Story of {self.repo_data['repo_name']}</h1>
                <div class="story">
                    {story.replace('\n', '<br>')}
                </div>
            </body>
            </html>
            """
        elif output_format.lower() == "text":
            return f"THE STORY OF {self.repo_data['repo_name'].upper()}\n\n{story}"
        else:
            return f"# The Story of {self.repo_data['repo_name']}\n\n{story}"
    
    def _detect_milestones(self) -> List[Dict[str, Any]]:
        """Identify key milestones in repository history."""
        milestones = []
        
        # Initial commit
        if self.repo_data["commits"]:
            first_commit = min(self.repo_data["commits"], key=lambda c: c["date"])
            milestones.append({
                "type": "initial",
                "date": first_commit["date"],
                "description": "Project inception",
                "commit": first_commit["sha"],
                "author": first_commit["author"]
            })
        
        # Tags/releases
        for tag in self.repo_data["tags"]:
            if tag["date"]:
                milestones.append({
                    "type": "release",
                    "date": tag["date"],
                    "description": f"Release {tag['name']}",
                    "commit": tag["commit"]
                })
        
        # Major merges (simplified detection)
        for commit in self.repo_data["commits"]:
            if commit["is_merge"] and "merge" in commit["message"].lower():
                milestones.append({
                    "type": "merge",
                    "date": commit["date"],
                    "description": f"Major merge: {commit['message'].splitlines()[0]}",
                    "commit": commit["sha"],
                    "author": commit["author"]
                })
        
        # Sort milestones by date
        return sorted(milestones, key=lambda m: m["date"])
    
    def _group_into_phases(self) -> List[Dict[str, Any]]:
        """Group commits into development phases."""
        if not self.repo_data["commits"]:
            return []
        
        # Simple time-based grouping (monthly)
        phases = []
        current_month = None
        current_phase = None
        
        for commit in sorted(self.repo_data["commits"], key=lambda c: c["date"]):
            commit_month = commit["date"].strftime("%Y-%m")
            
            if commit_month != current_month:
                if current_phase:
                    phases.append(current_phase)
                
                current_month = commit_month
                current_phase = {
                    "month": commit_month,
                    "commits": [],
                    "contributors": set(),
                    "start_date": commit["date"],
                    "end_date": commit["date"]
                }
            
            current_phase["commits"].append(commit)
            current_phase["contributors"].add(commit["author"])
            current_phase["end_date"] = commit["date"]
        
        if current_phase:
            phases.append(current_phase)
        
        return phases
    
    def _generate_markdown(self) -> str:
        """Generate story in Markdown format."""
        story = f"# The Story of {self.repo_data['repo_name']}\n\n"
        
        # Overview
        story += "## Overview\n\n"
        story += f"- **Total Commits**: {len(self.repo_data['commits'])}\n"
        story += f"- **Contributors**: {len(self.repo_data['contributors'])}\n"
        story += f"- **Branches**: {len(self.repo_data['branches'])}\n"
        story += f"- **Releases**: {len(self.repo_data['tags'])}\n\n"
        
        # Milestones
        story += "## Key Milestones\n\n"
        for milestone in self.milestones:
            icon = {"initial": "🚀", "release": "🎉", "merge": "🔀"}.get(milestone["type"], "📌")
            story += f"- {icon} **{milestone['date'].strftime('%Y-%m-%d')}**: {milestone['description']}\n"
        story += "\n"
        
        # Development phases
        story += "## Development Phases\n\n"
        for phase in self.phases:
            month_name = datetime.strptime(phase["month"], "%Y-%m").strftime("%B %Y")
            story += f"### {month_name}\n\n"
            story += f"- **Commits**: {len(phase['commits'])}\n"
            story += f"- **Contributors**: {', '.join(phase['contributors'])}\n"
            story += f"- **Period**: {phase['start_date'].strftime('%Y-%m-%d')} to {phase['end_date'].strftime('%Y-%m-%d')}\n\n"
            
            # Highlight significant commits
            significant = [c for c in phase["commits"] if self._is_significant(c)]
            if significant:
                story += "**Notable Changes**:\n"
                for commit in significant[:3]:  # Top 3 per month
                    story += f"- {commit['message'].splitlines()[0]} ({commit['author']})\n"
                story += "\n"
        
        # Contributors section
        story += "## Contributors\n\n"
        for author, stats in sorted(self.repo_data["contributors"].items(), 
                                   key=lambda x: x[1]["commits"], reverse=True):
            story += f"### {author}\n\n"
            story += f"- **Commits**: {stats['commits']}\n"
            story += f"- **Lines Added**: {stats['insertions']}\n"
            story += f"- **Lines Removed**: {stats['deletions']}\n"
            story += f"- **Active Period**: {stats['first_commit'].strftime('%Y-%m-%d')} to {stats['last_commit'].strftime('%Y-%m-%d')}\n\n"
        
        return story
    
    def _generate_html(self) -> str:
        """Generate story in HTML format."""
        md_story = self._generate_markdown()
        html_story = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>The Story of {self.repo_data['repo_name']}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                h2 {{ color: #34495e; margin-top: 30px; }}
                h3 {{ color: #7f8c8d; }}
                ul {{ padding-left: 20px; }}
                li {{ margin-bottom: 8px; }}
            </style>
        </head>
        <body>
            {self._markdown_to_html(md_story)}
        </body>
        </html>
        """
        return html_story
    
    def _generate_text(self) -> str:
        """Generate story in plain text format."""
        md_story = self._generate_markdown()
        text_story = re.sub(r'#+\s*', '', md_story)  # Remove headers
        text_story = re.sub(r'\*\*(.*?)\*\*', r'\1', text_story)  # Remove bold
        text_story = re.sub(r'-\s*', '• ', text_story)  # Replace list markers
        return text_story
    
    def _markdown_to_html(self, md_text: str) -> str:
        """Simplified Markdown to HTML conversion."""
        html = md_text.replace("\n\n", "</p><p>")
        html = html.replace("\n", "<br>")
        html = f"<p>{html}</p>"
        return html
    
    def _is_significant(self, commit: Dict[str, Any]) -> bool:
        """Determine if a commit is significant."""
        msg = commit["message"].lower()
        keywords = ["initial", "release", "major", "refactor", "rewrite", "feat:", "fix:", "break"]
        return any(keyword in msg for keyword in keywords) or commit["files_changed"] > 10
