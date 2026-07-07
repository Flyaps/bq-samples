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
    args = parser.parse_args(argv[1:])

    client = get_bigquery_client(args.project_id)

    print("checking analytics dataset availability")
    dataset = client.get_dataset("analytics_360350030")
    print(f"dataset: {dataset}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
