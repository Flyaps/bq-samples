import sys
from pathlib import Path

from google.cloud import bigquery

import settings
from adapters import get_bigquery_client


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: upload_table.py <path_to_csv>")
        return 1

    client = get_bigquery_client()

    dataset = bigquery.DatasetReference(client.project, settings.DATASET_NAME)
    table_ref = dataset.table(Path(argv[1]).stem)

    # configure the load: CSV input, skip the header row, infer the schema
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    # load_table_from_file reads a binary file object and starts a load job
    with open(argv[1], "rb") as fd:
        job = client.load_table_from_file(fd, table_ref, job_config=job_config)

    # block until the load job finishes (raises if it failed)
    job.result()

    # report how many rows the table holds now
    table = client.get_table(table_ref)
    print(f"loaded {table.num_rows} rows into {table.full_table_id}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
