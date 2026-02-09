import pandas as pd
import psycopg2
from splink.duckdb.duckdb_linker import DuckDBLinker
from splink_settings import settings


conn = psycopg2.connect(
host="postgres",
dbname="mdm",
user="mdm",
password="mdm"
)


df = pd.read_sql("SELECT * FROM customer_staging", conn)


linker = DuckDBLinker(df, settings)
linker.estimate_u_using_random_sampling(max_pairs=1e6)
linker.estimate_parameters_using_expectation_maximisation()


clusters = linker.cluster_pairwise_predictions_at_threshold(0.9)


clusters_df = clusters.as_pandas_dataframe()
clusters_df.to_sql("customer_master", conn, if_exists="append", index=False)