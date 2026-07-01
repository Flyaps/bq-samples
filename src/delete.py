"""Delete table and dataset sample"""

import sys

from adapters import get_bigquery_client


def main(argv: list[str]) -> int:
    client = get_bigquery_client()

    tempo = "tmp"

    dataset_ref = client.create_dataset(tempo, exists_ok=True)
    table_ref = client.create_table(dataset_ref.table(tempo), exists_ok=True)

    client.delete_table(table_ref)
    client.delete_dataset(dataset_ref, delete_contents=True)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
