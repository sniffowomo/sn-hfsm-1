from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


def save_to_markdown(
    content: Union[str, List, Dict, Any],
    prefix: str = "output",
    directory: str = ".",
    header_level: int = 1,
    include_time_in_filename: bool = True,
    metadata: Optional[Dict[str, str]] = None
) -> Path:
    """
    Saves content to a markdown file with date/time in filename and header.

    Args:
        content: Content to save (str, list, dict, or any object with __str__)
        prefix: Filename prefix before the date
        directory: Output directory
        header_level: Markdown header level (1-6)
        include_time_in_filename: Whether to include time in filename
        metadata: Optional dict of additional info to show at top (e.g., company name, address, phone)

    Returns:
        Path to the created markdown file

    Example Use:
        metadata = {
        "Company": "TechFusion Inc.",
        "Address": "123 Innovation Drive, Silicon Valley, CA 94043",
        "Phone": "+1 (555) 123-4567",
        "Email": "contact@techfusion.com",
        "Project": "Internal Security Audit",
    }

    save_to_markdown(
        ["Finding 1: XSS Vulnerability", "Finding 2: Weak Password Policy"],
        prefix="security_report",
        metadata=metadata
)
    """
    # Create directory if needed
    Path(directory).mkdir(parents=True, exist_ok=True)

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    datetime_str = f"{date_str} {time_str}"

    markdown_content = _convert_to_markdown(content, header_level)

    # Build metadata section
    header_section = ""
    if metadata:
        header_section = "\n".join(
            [f"- ##{key}: {value}" for key, value in metadata.items()])

    # Final content with header and metadata
    content_with_header = f"# Generated on {datetime_str}\n"
    if header_section:
        content_with_header += f"\n{header_section}\n"
    content_with_header += f"\n{markdown_content}"

    # Generate filename
    if include_time_in_filename:
        filename = f"{prefix}_{date_str}_{time_str.replace(':', '-')}.md"
    else:
        filename = f"{prefix}_{date_str}.md"

    filepath = Path(directory) / filename

    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content_with_header)

    return filepath


def _convert_to_markdown(content: Any, header_level: int = 1) -> str:
    """Helper function to convert different types to Markdown"""
    if isinstance(content, str):
        return content
    elif isinstance(content, (list, tuple, set)):
        return "\n".join(f"- {item}" for item in content)
    elif isinstance(content, dict):
        return "\n".join(f"- **{k}**: {v}" for k, v in content.items())
    else:
        header = "#" * header_level
        return f"{header} Content\n\n{str(content)}"
