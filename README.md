# Automated Data Pipeline for Real-Time Analytics

This project demonstrates the implementation of an automated data pipeline capable of collecting, processing, and analyzing real-time business metrics.

## Features
- **Data Ingestion:** Simulated with CSV files.
- **Data Transformation:** Data cleaning and structuring using Pandas.
- **Data Storage:** Processed data stored in PostgreSQL.
- **Data Visualization:** Prepared data for integration with dashboards.

## Requirements
- Python 3.8+
- Docker (for PostgreSQL)

## Setup Instructions
1. Start PostgreSQL using Docker:
   ```bash
   docker run --name postgres -e POSTGRES_USER=userAdmin -e POSTGRES_PASSWORD=userAdmin -e POSTGRES_DB=anaytics_dev_db -p 5432:5432 -d postgres
