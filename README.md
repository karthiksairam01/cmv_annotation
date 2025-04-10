# CMV Annotation Tool

This tool helps annotate relationships between comments in Reddit's Change My View (CMV) subreddit discussions.

## Directory Structure

```
annotation-project/
├── data/
│   ├── raw/                  # Original data
│   │   └── cmv_usable.jsonl
│   └── processed/            # Output and intermediate files
│       └── annotations/      # Folder for different annotators
├── scripts/
│   └── annotate.py           # The main annotation script
└── README.md                 # This documentation
```
## Downloading the data

Link: https://o365coloradoedu-my.sharepoint.com/:u:/g/personal/kasa6776_colorado_edu/ERk-W6rM8UVLndCp6UePizIBMmgdbq_j2EcUG7C6v53j3w?e=eB665a

## Getting Started

1. Clone this repository
2. Place your CMV data file at `data/raw/cmv_usable.jsonl` (or specify a different location with the `--input` flag)
3. Run the annotation script as described below

## Running the Annotation Tool

The basic usage is:

```bash
python scripts/annotate.py --annotator YOUR_NAME
```

This will start an annotation session with the default settings (5 annotations per session).

### Command Line Arguments

- `--annotator`, `-a`: (Required) Name of the annotator (used in output filename)
- `--max`, `-m`: Maximum number of annotations in this session (default: 5)
- `--input`, `-i`: Input data file path (default: data/raw/cmv_usable.jsonl)
- `--output-dir`, `-o`: Output directory for annotations (default: data/processed/annotations)
- `--middleware`, `-w`: Middleware data file path (default: data/processed/middleware_data.json)

### Example Usage

```bash
# Basic usage with required annotator name
python scripts/annotate.py --annotator john

# Set maximum annotations to 10
python scripts/annotate.py --annotator sarah --max 10

# Specify custom input and output locations
python scripts/annotate.py --annotator david --input my_data.json --output-dir my_annotations
```

## Annotation Guide

When annotating, you'll be shown a comment and its parent comment. You need to choose the relationship between them:

- `a` - The comment agrees with the parent comment
- `s` - The comment disagrees with the parent comment
- `n` - The comment has a neutral or other relation to the parent comment
- `exit` - Save your progress and quit the session

## Output Format

The annotations are saved in a JSON file named `cmv_relations_YOUR_NAME.json` in the output directory.

