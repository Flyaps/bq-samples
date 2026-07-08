import google.auth
from google.cloud import bigquery

import settings


def get_bigquery_client(project_id=settings.PROJECT_ID) -> bigquery.Client:
    credentials, _ = google.auth.default(quota_project_id=project_id)
    return bigquery.Client(project=project_id, credentials=credentials)
