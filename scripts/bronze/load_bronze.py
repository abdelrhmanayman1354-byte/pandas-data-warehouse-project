import pandas as pd
import time
import os
from datetime import datetime
from sqlalchemy import create_engine, text

# ===============================================================================
# Python Script: Load Bronze Layer (Source -> Bronze)
# ===============================================================================
# Script Purpose:
#   This script loads data into the 'bronze' schema in PostgreSQL from external CSV files.
#   It performs the following actions:
#   - Establishes a connection to the PostgreSQL Database.
#   - Ensures the required schemas (bronze, silver, gold) exist.
#   - Reads CRM and ERP datasets using Pandas.
#   - Replaces (Truncates & Inserts) data into bronze tables.
#   - Logs the duration and status of each load operation.
# ===============================================================================

def load_bronze():
    """
    Main function to execute the Bronze Layer ETL process.
    Matches the logic of the SQL Stored Procedure: bronze.load_bronze
    """
    batch_start_time = time.time()
    
    print('================================================')
    print('Loading Bronze Layer')
    print('================================================')

    # Base path for datasets
    base_path = r'D:\course\SQL\sql-data-warehouse-project-121e1489758aa2149d248d61668f275309c06cbd\datasets'
    
    # Mapping table names to their relative file paths
    crm_tables = {
        'crm_cust_info': 'source_crm\\cust_info.csv',
        'crm_prd_info': 'source_crm\\prd_info.csv',
        'crm_sales_details': 'source_crm\\sales_details.csv'
    }
    
    erp_tables = {
        'erp_loc_a101': 'source_erp\\LOC_A101.csv',
        'erp_cust_az12': 'source_erp\\CUST_AZ12.csv',
        'erp_px_cat_g1v2': 'source_erp\\PX_CAT_G1V2.csv'
    }

    try:
        # ------------------------------------------------
        # Loading CRM Tables
        # ------------------------------------------------
        print('------------------------------------------------')
        print('Loading CRM Tables')
        print('------------------------------------------------')
        
        for table_name, rel_path in crm_tables.items():
            start_time = time.time()
            print(f'>> Truncating Table: bronze.{table_name}')
            print(f'>> Inserting Data Into: bronze.{table_name}')
            
            # Read CSV and load to SQL (if_exists='replace' handles Truncate + Bulk Insert)
            df = pd.read_csv(os.path.join(base_path, rel_path))
            df.to_sql(table_name, engine, schema='bronze', if_exists='replace', index=False)

            row_count = len(df)
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print(f'>> Row Loaded: {row_count}')
            print(f'>> Load Duration: {duration} seconds')
            print('>> -------------')

        # ------------------------------------------------
        # Loading ERP Tables
        # ------------------------------------------------
        print('------------------------------------------------')
        print('Loading ERP Tables')
        print('------------------------------------------------')
        
        for table_name, rel_path in erp_tables.items():
            start_time = time.time()
            print(f'>> Truncating Table: bronze.{table_name}')
            print(f'>> Inserting Data Into: bronze.{table_name}')
            
            df = pd.read_csv(os.path.join(base_path, rel_path))
            df.to_sql(table_name, engine, schema='bronze', if_exists='replace', index=False)
            
            row_count = len(df)
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print(f'>> Row Loaded: {row_count}')
            print(f'>> Load Duration: {duration} seconds')
            print('>> -------------')

        # Final Batch Logging
        batch_end_time = time.time()
        total_duration = round(batch_end_time - batch_start_time, 2)
        
        print('==========================================')
        print('Loading Bronze Layer is Completed')
        print(f'   - Total Load Duration: {total_duration} seconds')
        print('==========================================')

    except Exception as e:
        print('==========================================')
        print('ERROR OCCURED DURING LOADING BRONZE LAYER')
        print(f'Error Message: {str(e)}')
        print('==========================================')

# Execute the process
if __name__ == "__main__":
    load_bronze()
