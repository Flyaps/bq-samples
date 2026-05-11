# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

BigQuery sample scripts. Each file in `src/` is a standalone example that exercises one piece of the `google-cloud-bigquery` client (e.g. `create_dataset.py` creates a dataset). Scripts are not wired together into a CLI or library — they're intended to be read and run individually.

## Environment

- Dependencies are managed with Poetry (`pyproject.toml`, `poetry.lock`). Requires Python >= 3.10.
- Install: `poetry install`
- Run a sample: `poetry run python src/create_dataset.py`
- The BigQuery client picks up credentials from Application Default Credentials. Authenticate locally with `gcloud auth application-default login` before running.
- The target GCP project is currently hardcoded inside each script (e.g. `peerless-text-365915` in `create_dataset.py`). When adapting a sample, edit the literal at the top of `main()` rather than introducing config plumbing.

## Conventions for new samples

- Mirror the shape of `src/create_dataset.py`: a `main(argv: list[str]) -> int` entry point, `sys.exit(main(sys.argv))` guard, and inline comments calling out the BigQuery API steps. Keep each script self-contained and readable top-to-bottom — these are teaching examples, not production code.
- Sample data lives in `data/` (e.g. `data/industry.csv`) and is loaded by relative path from the repo root.
