#!/bin/bash

# Exit on error
set -e

# Meltano setup
meltano install extractor "$EXTRACTOR"
meltano install loader "$LOADER"
meltano install transform "$EXTRACTOR"
meltano install transformer dbt

# Install dbt dependencies files
meltano invoke dbt deps

# Try to drop the users_stream table to allow dbt snapshot to capture hard deleted users from source
meltano invoke dbt run-operation googleads_drop_google_ads_stream_tables || true

# Run the elt, and dbt commands and tests
meltano elt "$EXTRACTOR" "$LOADER" --transform=skip
meltano invoke dbt run -m tap_googleads