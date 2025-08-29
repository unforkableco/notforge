import re
from pathlib import Path


def clean_outside_codeblocks(content: str) -> str:
    """Clean non-Markdown notations outside fenced code blocks.

    - Remove HTML comments and tags
    - Normalize non-breaking spaces
    - Unescape common LaTeX escapes (e.g., \!Forge, \&, \%)
    - Convert LaTeX inline math \( ... \) to inline code
    - Convert LaTeX display math \[ ... \] to fenced code blocks
    """
    # Remove HTML comments
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    # Remove HTML tags
    content = re.sub(r"<[^>]+>", "", content)
    # Normalize non-breaking spaces
    content = content.replace("\u00A0", " ")
    # Unescape specific sequences
    content = content.replace("\\!Forge", "!Forge")
    # Unescape common LaTeX escapes for punctuation
    content = re.sub(r"\\([&%_#$])", r"\1", content)
    # Inline math: \( ... \) -> `...`
    content = re.sub(r"\\\((.+?)\\\)", r"`\1`", content, flags=re.DOTALL)
    # Display math: \[ ... \] -> fenced code block
    content = re.sub(r"\\\[(.+?)\\\]", lambda m: "```\n" + m.group(1) + "\n```", content, flags=re.DOTALL)
    # Trim trailing spaces on each line
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    return content


def normalize_markdown_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Split on fenced code blocks to avoid altering their contents
    parts = re.split(r"(```[\s\S]*?```)", text)
    for i in range(0, len(parts), 2):
        if i < len(parts):
            parts[i] = clean_outside_codeblocks(parts[i])
    normalized = "".join(parts)
    path.write_text(normalized, encoding="utf-8")


def main() -> None:
    book_dir = Path(__file__).resolve().parents[1] / "book"
    for md_file in sorted(book_dir.glob("*.md")):
        normalize_markdown_file(md_file)


if __name__ == "__main__":
    main()


