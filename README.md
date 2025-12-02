# Markdown Combiner

A simple, drop-in Python script that automatically combines multiple
Markdown (`.md`) files into a single `combined.md` file.\
Just place the script in any folder containing Markdown files and
**double-click it on Windows** --- no command line required.

## Features

-   Automatically scans the script's folder for all `.md` files\
-   Uses each file's **name** as a `# Heading` in the combined output\
-   Sorts files alphabetically before combining\
-   Skips the output file if it already exists\
-   Safe to run repeatedly\
-   Works by simply **double-clicking** on Windows\
-   No arguments or terminal needed

## How It Works

1.  Copy `combine_md.py` into any folder with your Markdown files.
2.  Double-click `combine_md.py`.
3.  The script:
    -   Finds every `*.md` file in the same folder\
    -   Creates `combined.md`\
    -   Inserts each file's contents under a section titled with the
        file name\
    -   Prints a summary and waits for Enter so the window does not
        close immediately

Example structure:

    folder/
    │
    ├── notes.md
    ├── chapter1.md
    ├── summary.md
    └── combine_md.py

Running the script produces:

    folder/
    │
    ├── notes.md
    ├── chapter1.md
    ├── summary.md
    ├── combine_md.py
    └── combined.md   <-- generated output

## Combined Output Format

Each file becomes a section:

``` markdown
# notes
<contents of notes.md>

# chapter1
<contents of chapter1.md>

# summary
<contents of summary.md>
```
