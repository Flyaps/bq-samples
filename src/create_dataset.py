import sys

from google.cloud import bigquery

import settings
from adapters import get_bigquery_client


def main(argv: list[str]) -> int:
    client = get_bigquery_client()

    # set dataset_id to the ID of the dataset to create
    dataset_id = f"{settings.PROJECT_ID}.{settings.DATASET_NAME}"

    # construct a full Dataset object to send to the API
    dataset = bigquery.Dataset(dataset_id)

    # create dataset
    dataset = client.create_dataset(dataset, timeout=30)
    print(f"created dataset {dataset.project}.{dataset.dataset_id}")

    # create dataset - one-liner:
    dataset = client.create_dataset(settings.DATASET_NAME, exists_ok=True)
    print(f"created dataset {dataset.project}.{dataset.dataset_id}")


if __name__ == "__main__":
    sys.exit(main(sys.argv))

