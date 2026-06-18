import sys

import settings
from adapters import get_bigquery_client


def main(argv: list[str]) -> int:
    client = get_bigquery_client()

    query_job = client.query(f"SELECT * FROM {settings.DATASET_NAME}.industry LIMIT 5")

    for row in query_job.result():
        print(row[0])

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
