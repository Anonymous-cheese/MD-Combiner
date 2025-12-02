#!/usr/bin/env python3
import sys
from pathlib import Path

def main():
    # Folder where this script is located
    script_path = Path(__file__).resolve()
    folder = script_path.parent

    output_file = folder / "combined.md"

    # Find all .md files in this folder (non-recursive)
    md_files = sorted(folder.glob("*.md"))

    # Exclude the output file if it already exists
    md_files = [f for f in md_files if f.name != output_file.name]

    if not md_files:
        print("No markdown (*.md) files found in this folder.")
        print("Folder:", folder)
        input("\nPress Enter to exit...")
        return

    print("Combining the following files:\n")
    for f in md_files:
        print(" -", f.name)

    with output_file.open("w", encoding="utf-8") as out:
        for i, md_file in enumerate(md_files, start=1):
            title = md_file.stem  # file name without extension

            # Write section header
            out.write(f"# {title}\n\n")

            # Write content
            content = md_file.read_text(encoding="utf-8")
            out.write(content.rstrip() + "\n")

            # Blank line between sections (except after last)
            if i != len(md_files):
                out.write("\n\n")

    print("\nDone.")
    print(f"Created: {output_file.name}")
    print(f"Location: {folder}")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
