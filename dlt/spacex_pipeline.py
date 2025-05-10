"""
SpaceX Data Pipeline

This script handles the extraction and loading of SpaceX launch data from The Space Devs API
into a MotherDuck database using DLT.
"""

import os
import dlt
from dlt.sources.rest_api import rest_api_source

# Environment Variables
API_BASE_URL = os.getenv('SPACEDEVS_API_URL', 'https://lldev.thespacedevs.com/2.3.0/')
PIPELINE_NAME = 'spacex_data_load'
DESTINATION = 'motherduck'
DATASET_NAME = 'bronze'

def create_source():
    """
    Create and configure the REST API source for SpaceX launch data.
    """
    source_config = {
        "client": {
            "base_url": API_BASE_URL,
            "paginator": {
                "type": "auto",
                "next_url_path": "next",
            },
        },
        "resource_defaults": {
            "write_disposition": "replace",  # Use replace as cohort is small
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
    }
    
    return rest_api_source(source_config)


def create_pipeline():
    """
    Create and configure the DLT pipeline.
    """
    return dlt.pipeline(
        pipeline_name=PIPELINE_NAME,
        destination=DESTINATION,
        dataset_name=DATASET_NAME,
    )


def run_pipeline(pipeline, source):
    """
    Execute the pipeline with the given source.
    """
    try:
        load_info = pipeline.run(source)
        return load_info
    except Exception as e:
        print(f"Pipeline execution failed: {str(e)}")
        raise


def main():
    """
    Main function to orchestrate the data pipeline execution.
    """
    try:
        source = create_source()
        pipeline = create_pipeline()
        load_info = run_pipeline(pipeline, source)
        print(load_info)
    except Exception as e:
        print(f"Pipeline failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
