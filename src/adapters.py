import google.auth
from google.cloud import bigquery

import settings


def get_bigquery_client() -> bigquery.Client:
    credentials, _ = google.auth.default(quota_project_id=settings.PROJECT_ID)
    return bigquery.Client(project=settings.PROJECT_ID, credentials=credentials)
