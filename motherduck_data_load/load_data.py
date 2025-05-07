import dlt
from dlt.sources.rest_api import rest_api_source
import os

source = rest_api_source(
    {
        "client": {
            "base_url": "https://lldev.thespacedevs.com/2.3.0/",
            "paginator": {
                "type": "auto",
                "next_url_path": "next",
            },
        },
        "resource_defaults": {
            "write_disposition": "append", 
        },
        "resources": [
            {
                "name": "launches",
                "endpoint": {
                    "path": "launches",
                    "params": {
                        "limit": 100,
                        "lsp__name": "SpaceX",
                    },
                },
            },
            ],
    },
)

pipeline = dlt.pipeline(
    pipeline_name="spacex_data_load",
    destination="motherduck",
    dataset_name="bronze",
)

load_info = pipeline.run(source)
print((load_info))
