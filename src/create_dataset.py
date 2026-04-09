import sys

from google.cloud import bigquery


def main(argv: list[str]) -> int:
    client = bigquery.Client()

    # set dataset_id to the ID of the dataset to create
    dataset_id = "peerless-text-365915.Demo_dataset_python"

    # construct a full Dataset object to send to the API
    dataset = bigquery.Dataset(dataset_id)

    # create dataset
    dataset = client.create_dataset(dataset, timeout=30)
    print("created dataset {client.project}.{dataset.dataset_id}")


if __name__ == "__main__":
    sys.exit(main(sys.argv))

