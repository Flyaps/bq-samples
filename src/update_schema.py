import sys

from google.cloud import bigquery

import settings
from adapters import get_bigquery_client


def main(argv: list[str]) -> int:
    client = get_bigquery_client()

    dataset_ref = bigquery.DatasetReference(client.project, settings.DATASET_NAME)
    table_ref = dataset_ref.table("industry")

    table = client.get_table(table_ref)
    # table.schema returns a fresh copy each access, so mutating it in place is a no-op.
    # Build the new schema list and assign it back through the setter.
    table.schema = table.schema + [
        bigquery.SchemaField("description", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("is_active", "BOOLEAN", mode="NULLABLE"),
    ]
    table = client.update_table(table, ["schema"])

    print(f"Schema has been updated for {table.full_table_id}")
    print("Current schema:")
    for field in table.schema:
        print(f"  {field.name} {field.field_type} ({field.mode})")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
