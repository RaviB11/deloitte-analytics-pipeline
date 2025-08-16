# etl_pipeline.py
import pandas as pd
import os

def run_etl_pipeline():
    """
    This function runs the complete ETL pipeline:
    1. Extract: Loads the raw data from a CSV file.
    2. Transform: Cleans the data, renames columns, and creates new features.
    3. Load: Saves the processed data to a new CSV file ready for analysis.
    """
    
    # --- 1. EXTRACT ---
    raw_data_path = 'predictive_maintenance.csv'
    print(f"EXTRACT: Loading raw data from '{raw_data_path}'...")
    
    if not os.path.exists(raw_data_path):
        print(f"Error: Raw data file not found at '{raw_data_path}'.")
        return

    df = pd.read_csv(raw_data_path)
    print("EXTRACT: Data loaded successfully.")

    # --- 2. TRANSFORM ---
    print("TRANSFORM: Starting data cleaning and transformation...")

    df.rename(columns={'Type': 'Product_Quality_Grade', 'Target': 'Failure_Status'}, inplace=True)
    df['Defect_Status'] = df['Failure_Status'].apply(lambda x: 'Defect' if x == 1 else 'No Defect')
    df['Air_temperature_C'] = round(df['Air temperature [K]'] - 273.15, 2)
    df['Process_temperature_C'] = round(df['Process temperature [K]'] - 273.15, 2)
    df.drop(columns=['Air temperature [K]', 'Process temperature [K]'], inplace=True)
    
    print("TRANSFORM: Data transformation complete.")

    # --- 3. LOAD ---
    processed_data_path = 'processed_manufacturing_data.csv'
    print(f"LOAD: Saving processed data to '{processed_data_path}'...")
    df.to_csv(processed_data_path, index=False)
    print(f"LOAD: Processed data saved successfully. ETL Pipeline finished.")

if __name__ == "__main__":
    run_etl_pipeline()
