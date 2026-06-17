# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

BigQuery sample scripts. Each sample in `src/` exercises one piece of the `google-cloud-bigquery` client (e.g. `create_dataset.py` creates a dataset) and is meant to be read and run on its own — they're not wired together into a CLI or library. Two small shared modules back the samples:

- `src/settings.py` — the target `PROJECT_ID` and `DATASET_NAME` in one place.
- `src/adapters.py` — `get_bigquery_client()`, which constructs a `bigquery.Client` for the configured project.

Samples import these by bare module name (`import settings`, `from adapters import get_bigquery_client`), which works because running `python src/<sample>.py` puts `src/` on `sys.path`.

## Environment

- Dependencies are managed with uv (`pyproject.toml`, `uv.lock`). Requires Python >= 3.10.
- Install: `uv sync`
- Run a sample: `uv run python src/create_dataset.py`
- The BigQuery client picks up credentials from Application Default Credentials. Authenticate locally with `gcloud auth application-default login` before running.
- The target GCP project and dataset live in `src/settings.py` (`PROJECT_ID = "bq-demo-beef"`, `DATASET_NAME = "demoset"`). Point a sample at your own project by editing those literals rather than per-script values.

## Conventions for new samples

- Mirror the shape of `src/create_dataset.py`: a `main(argv: list[str]) -> int` entry point, a `sys.exit(main(sys.argv))` guard, and inline comments calling out the BigQuery API steps. Get the client via `get_bigquery_client()` from `adapters` and read config from `settings` rather than re-hardcoding the project. Keep each sample readable top-to-bottom — these are teaching examples, not production code.
- Sample data lives in `data/` (e.g. `data/industry.csv`) and is loaded by relative path from the repo root, so run samples from the repo root.
