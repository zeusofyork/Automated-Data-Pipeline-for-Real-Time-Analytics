import pandas as pd
from sqlalchemy import create_engine

# Database configuration with redundancy (using multiple hosts)
DB_PRIMARY = "localhost"  # Primary host
DB_REPLICA = "localhost"  # Replica host (example placeholder)
DB_PORT = '5432'
DB_NAME = 'analytics_dev_db'
DB_USER = 'userAdmin'
DB_PASSWORD = 'userAdmin'

# Database connection strings
DATABASE_URIS = [
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_PRIMARY}:{DB_PORT}/{DB_NAME}",
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_REPLICA}:{DB_PORT}/{DB_NAME}"
]

def get_database_engine():
    """Attempt to connect to available database hosts."""
    for uri in DATABASE_URIS:
        try:
            engine = create_engine(uri)
            # Test the connection
            with engine.connect() as connection:
                print(f"Connected to database: {uri}")
                return engine
        except Exception as e:
            print(f"Failed to connect to {uri}: {e}")
    raise ConnectionError("Unable to connect to any database host.")

def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def transform_data(df):
    """Perform data cleaning and transformation."""
    df = df.dropna()  # Remove missing values
    df['processed_at'] = pd.Timestamp.now()  # Add a timestamp column
    return df

def save_to_db(df, table_name, engine):
    """Save the transformed data to a PostgreSQL table."""
    with engine.connect() as connection:
        df.to_sql(table_name, con=connection, if_exists='replace', index=False)
        print(f"Data saved to table: {table_name}")

if __name__ == "__main__":
    try:
        # Step 1: Get a database engine with failover
        db_engine = get_database_engine()

        # Step 2: Load raw data
        raw_data = load_data("data/raw_data.csv")

        # Step 3: Transform the data
        transformed_data = transform_data(raw_data)

        # Step 4: Save the data to PostgreSQL
        save_to_db(transformed_data, "processed_data", db_engine)

        print("Data pipeline executed successfully!")
    except Exception as error:
        print(f"Pipeline failed: {error}")
