
import pandas as pd
import os
from google.cloud import storage

# --- Configuration ---
BUCKET_NAME = "vishaldatcom" 

def convert_csv_to_parquet_and_upload():
    """
    Reads the large CSV, converts it to Parquet format, and uploads
    it to Google Cloud Storage.
    """
    print("Starting conversion and upload process...")

    # Define file paths
    local_csv_file = 'index/output/CDC_StandardizedPrecipitationIndex_output.csv'
    local_parquet_file = 'spi_data.parquet' # Will be created temporarily
    destination_blob_name = 'spi_data.parquet' # The name of the file in GCS

    # --- Step 1: Read the large CSV ---
    print(f"Reading data from {local_csv_file}...")
    df = pd.read_csv(local_csv_file)
    
    # Ensure 'countyfips' is a string for consistent filtering
    df['countyfips'] = df['countyfips'].astype(str).str.zfill(5)

    # --- Step 2: Convert to Parquet ---
    print(f"Converting data to Parquet format and saving to {local_parquet_file}...")
    df.to_parquet(local_parquet_file, engine='pyarrow')

    # --- Step 3: Upload the Parquet file to GCS ---
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(destination_blob_name)

        print(f"Uploading {local_parquet_file} to GCS bucket gs://{BUCKET_NAME}...")
        blob.upload_from_filename(local_parquet_file)

        print("Upload complete.")
        public_url = blob.public_url
        print(f"Your Parquet file is now available at: {public_url}")

    except Exception as e:
        print(f"An error occurred during the GCS upload: {e}")
        print("Please ensure you have authenticated with 'gcloud auth application-default login'")
        print(f"and that the bucket '{BUCKET_NAME}' exists and you have permissions.")

    finally:
        # --- Step 4: Clean up the temporary local file ---
        if os.path.exists(local_parquet_file):
            os.remove(local_parquet_file)
            print(f"Cleaned up temporary file: {local_parquet_file}")

if __name__ == "__main__":
    convert_csv_to_parquet_and_upload()
