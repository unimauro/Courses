from google.cloud import bigquery
client = bigquery.Client()
sql = """
SELECT *
FROM
`bigquery-public-data.samples.natality`
limit 10
"""

natalityDF = client.query(sql).to_dataframe()
natalityDF.head()


