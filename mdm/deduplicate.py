import pandas as pd
import psycopg2
from splink.duckdb.duckdb_linker import DuckDBLinker
from splink_settings import settings

def run_deduplication():
    conn = psycopg2.connect(
        host="postgres",
        dbname="mdm",
        user="mdm",
        password="mdm"
    )

    df = pd.read_sql("SELECT * FROM ecommerce_customer_staging", conn)

    # use DuckDB backend for Splink
    linker = DuckDBLinker(df, settings)

    # estimate u & parameters
    linker.estimate_u_using_random_sampling(max_pairs=1e6)
    linker.estimate_parameters_using_expectation_maximisation()

    # cluster at threshold e.g., 0.85
    clusters = linker.cluster_pairwise_predictions_at_threshold(0.85)

    # write to master
    master_df = clusters.as_pandas_dataframe()
    master_df.to_sql("ecommerce_customer_master", conn, if_exists="append", index=False)
