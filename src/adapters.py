from google.cloud import bigquery

import settings


def get_bigquery_client() -> bigquery.Client:
    return bigquery.Client(project=settings.PROJECT_ID)
