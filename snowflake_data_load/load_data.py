# This script uses dlt (https://dlthub.com/) to move data since its fairly lightweight and straightforward to use.
# Other potential options are Meltano and Airbyte , both of which have readymade connectors to use (https://hub.meltano.com/extractors/tap-spacex-api / https://airbyte.com/connectors/spacex-api)
# The downside is they're both significantly heavier and their readymade connectors use v4 of the API.

import dlt
from dlt.sources.rest_api import rest_api_source

source = rest_api_source({
    "client": {
        "base_url": "https://api.spacexdata.com/v5/",
        "paginator": {
            "type": "json_link",
            "next_url_path": "paging.next",
        },
    },
    "resources": 
        ["launches"],
})

pipeline = dlt.pipeline(
    pipeline_name="spacex_data_load",
    destination="snowflake",
    dataset_name="public",
)

load_info = pipeline.run(source)
print((load_info))