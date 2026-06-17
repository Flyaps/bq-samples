# bq-samples

A small collection of standalone Python scripts that exercise the
[`google-cloud-bigquery`](https://cloud.google.com/python/docs/reference/bigquery/latest)
client. Each sample in `src/` demonstrates one piece of the BigQuery API
(creating a dataset, loading a table, running a query, etc.) — they're
intended to be read and run individually, not wired together into a CLI or
library. A couple of small shared modules (`settings.py`, `adapters.py`) hold
the project config and client setup the samples reuse.

## Requirements

- Python ≥ 3.10
- [uv](https://docs.astral.sh/uv/) for dependency management
- A Google Cloud project with the BigQuery API enabled
- `gcloud` CLI, authenticated

## Setup

```bash
uv sync
```

### Authenticate

The BigQuery client picks up credentials from Application Default Credentials
(ADC). Pick one of:

**Option A — your user account (simplest):**

```bash
gcloud auth application-default login
```

**Option B — impersonate a service account (recommended for shared resources):**

```bash
SA=bq-full@<your-project>.iam.gserviceaccount.com

# one-time: grant your user permission to mint tokens for the SA
gcloud iam service-accounts add-iam-policy-binding $SA \
  --member="user:you@example.com" \
  --role="roles/iam.serviceAccountTokenCreator"

# then point ADC at the SA
gcloud auth application-default login --impersonate-service-account=$SA
```

No long-lived JSON key sits on disk this way — tokens are short-lived and
revoking access is a one-line IAM change.

### Revoking SA access

To take back impersonation rights from a user (e.g. when someone leaves the
project), remove the IAM binding you granted earlier:

```bash
gcloud iam service-accounts remove-iam-policy-binding $SA \
  --member="user:you@example.com" \
  --role="roles/iam.serviceAccountTokenCreator"
```

That alone stops any *new* tokens from being minted. Already-issued access
tokens stay valid until they expire (≤ 1 hour); there is no per-token revoke
on GCP's side. If you need every outstanding token gone *now*, disable the
service account itself — every existing token instantly stops working:

```bash
gcloud iam service-accounts disable $SA       # reversible with `enable`
```

On the local machine, also clear the ADC file so the impersonation config
doesn't linger:

```bash
gcloud auth application-default revoke
# or just delete ~/.config/gcloud/application_default_credentials.json
```

To audit who currently has impersonation rights on the SA:

```bash
gcloud iam service-accounts get-iam-policy $SA
```

## Running a sample

```bash
uv run python src/create_dataset.py
```

The target GCP project and dataset live in `src/settings.py`
(`PROJECT_ID`, `DATASET_NAME`) — edit those literals to point the samples at
your own project. Run samples from the repo root so the `data/` fixtures
resolve by relative path.

## Layout

```
src/                 samples — one BigQuery concept per file
  create_dataset.py    create a new dataset
  settings.py          PROJECT_ID / DATASET_NAME for all samples
  adapters.py          get_bigquery_client() — builds the BigQuery client
data/                small CSV fixtures loaded by some of the samples
  industry.csv
```

## Adding a new sample

Mirror the shape of `src/create_dataset.py`:

- a `main(argv: list[str]) -> int` entry point
- a `sys.exit(main(sys.argv))` guard at the bottom
- inline comments calling out the BigQuery API steps
- the client from `get_bigquery_client()` (in `adapters`) and config from `settings`

Keep each sample readable top-to-bottom — these are teaching examples, not
production code. Put any sample data in `data/` and load it by relative path
from the repo root.

## License

MIT — see [LICENSE](LICENSE).
