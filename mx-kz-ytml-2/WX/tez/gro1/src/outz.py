import io
import re
import textwrap
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from rich import inspect as rich_inspect
from rich.console import Console
from rich.pretty import pretty_repr
from rich.traceback import install

# Enable rich tracebacks for debugging
install()
console = Console()


def strip_ansi_sequences(text):
    """Remove ANSI escape sequences from the text."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def save_output_to_markdown(output, directory="rez", label="output"):
    """
    Saves 'output' as a nicely formatted Markdown file in 'directory',
    using 'label' and a detailed timestamp in the filename.
    """
    try:
        dir_path = Path(directory)
        dir_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
        file_path = dir_path / f"{label}_{timestamp}.md"

        # Attempt pretty formatting; fallback to raw repr
        try:
            content = pretty_repr(output)
        except Exception:
            content = repr(output)

        md = (
            f"# {label}\n\n"
            f"**Timestamp:** {timestamp}\n\n"
            "```\n"
            f"{content}\n"
            "```\n"
        )

        with file_path.open("w", encoding="utf-8") as f:
            f.write(md)

        console.print(f"[bold green]✅ Saved to {file_path.resolve()}[/]")

    except Exception:
        console.print_exception(show_locals=True)


def inspect_and_save_to_image(var, label="inspected_object", directory="rez"):
    """
    Uses rich.inspect() to introspect 'var', captures the output,
    and saves it to an image file.
    """
    try:
        buf = io.StringIO()
        temp_console = Console(file=buf, force_terminal=True, width=120)

        rich_inspect(var, console=temp_console, methods=True, all=True)
        output_str = buf.getvalue()

        # Strip ANSI escape sequences
        plain_text_output = strip_ansi_sequences(output_str)

        # Create an image from the text
        font = ImageFont.load_default()
        max_width = 800  # Maximum width of the image
        line_height = 15  # Height of each line in the image
        # Approximate character width
        lines = textwrap.wrap(plain_text_output, width=max_width // 10)

        # Calculate the size of the image
        image_height = len(lines) * line_height
        image = Image.new('RGB', (max_width, image_height),
                          color=(255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Draw each line of text
        for i, line in enumerate(lines):
            draw.text((10, i * line_height), line, font=font, fill=(0, 0, 0))

        # Save the image
        dir_path = Path(directory)
        dir_path.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
        file_path = dir_path / f"{label}_{timestamp}.png"
        image.save(file_path)

        console.print(f"[bold green]✅ Saved to {file_path.resolve()}[/]")

    except Exception:
        console.print_exception(show_locals=True)
