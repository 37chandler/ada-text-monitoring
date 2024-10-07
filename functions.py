from google.cloud import bigquery

def count_log_entries(client):
    """
    Returns the count of rows in the log table.
    """
    query = """
        SELECT COUNT(*)
        FROM `umt-msba.carbitrage.log_20241007`
    """
    query_job = client.query(query, location="US")
    rows = query_job.result()
    for row in rows:
        return row[0]

def count_raw_listing_pages(client):
    """
    Returns the count of rows in the raw listing pages table.
    """
    query = """
        SELECT COUNT(*)
        FROM `umt-msba.carbitrage.raw_listing_pages_20241007`
    """
    query_job = client.query(query, location="US")
    rows = query_job.result()
    for row in rows:
        return row[0]

def count_links_need_harvesting(client):
    """
    Returns the count of rows in the links_need_harvesting table.
    """
    query = """
        SELECT COUNT(*)
        FROM `umt-msba.carbitrage.links_need_harvesting_20241007`
    """
    query_job = client.query(query, location="US")
    rows = query_job.result()
    for row in rows:
        return row[0]


def get_raw_listing_pages_on_date(client, date):
    """
    Returns the count of raw listing pages pulled on a given date.
    """
    query = f"""
        SELECT COUNT(*)
        FROM `umt-msba.carbitrage.raw_listing_pages_20241007`
        WHERE DATE(datetime_pulled) = '{date}'
    """
    query_job = client.query(query, location="US")
    rows = query_job.result()
    for row in rows:
        return row[0]