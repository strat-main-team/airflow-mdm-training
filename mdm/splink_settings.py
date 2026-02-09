from splink.duckdb.duckdb_linker import DuckDBLinker

settings = {
    "link_type": "dedupe_only",
    # block on unique id match OR city match
    "blocking_rules_to_generate_predictions": [
        "l.customer_unique_id = r.customer_unique_id",
        "l.city = r.city"
    ],
    "comparisons": [
        {
            "col_name": "customer_unique_id",
            "comparison_levels": [
                {"sql_condition": "l.customer_unique_id = r.customer_unique_id"},
                {"sql_condition": "ELSE"}
            ]
        },
        {
            "col_name": "city",
            "comparison_levels": [
                {"sql_condition": "l.city = r.city"},
                {"sql_condition": "ELSE"}
            ]
        },
        {
            "col_name": "state",
            "comparison_levels": [
                {"sql_condition": "l.state = r.state"},
                {"sql_condition": "ELSE"}
            ]
        }
    ]
}
