import argparse
import sys

import settings
from adapters import get_bigquery_client


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-p",
        "--project-id",
        default=settings.PROJECT_ID,
        help="GCP project to run against (default: %(default)s)",
    )
    parser.add_argument(
        "-d",
        "--analytics-dataset",
        default=settings.ANALYTICS_DATASET_NAME,
        help="analytics dataset to check (default: %(default)s)",
    )
    args = parser.parse_args(argv[1:])

    client = get_bigquery_client(args.project_id)

    print("checking analytics dataset availability")
    dataset = client.get_dataset(args.analytics_dataset)
    print(f"dataset: {dataset}")

    query = f"""
    SELECT pseudo_user_id, ARRAY_LENGTH(ARRAY_AGG(
    DISTINCT device.operating_system || device.category || device.mobile_brand_name
    )) AS device_count
    FROM `{args.project_id}.{args.analytics_dataset}.pseudonymous_users_*`
    GROUP BY pseudo_user_id
    HAVING device_count > 1
    """
    query_job = client.query(query)

    print("user_id\t\t\tdevice_count")
    for row in query_job:
        print(f"{row[0]}\t{row[1]}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
