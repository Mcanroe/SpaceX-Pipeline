# This script uses dlt (https://dlthub.com/) to move data since its fairly lightweight and straightforward to use.
# Other potential options are Meltano and Airbyte , both of which have readymade connectors to use (https://hub.meltano.com/extractors/tap-spacex-api / https://airbyte.com/connectors/spacex-api)
# The downside is they're both significantly heavier compared to dlt.

import dlt
from dlt.sources.rest_api import rest_api_source

source = rest_api_source(
    {
        "client": {
            "base_url": "https://api.spacexdata.com/v4/",
            "paginator": {
                "type": "json_link",
                "next_url_path": "paging.next",
            },
        },
        "resource_defaults": {
            "write_disposition": "replace",
        },
        "resources": [
            "launches",
            "crew",
            "landpads",
            "launchpads",
            "rockets",
        ],
    }
)

pipeline = dlt.pipeline(
    pipeline_name="spacex_data_load",
    destination="snowflake",  # Snowflake is used purely for practice , in reality a DLT pipeline of this scale could be pulled into duckdb and transformed with a tool like dbt/sqlmesh
)

load_info = pipeline.run(source)
print((load_info))
