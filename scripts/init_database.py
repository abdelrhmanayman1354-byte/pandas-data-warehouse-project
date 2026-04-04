from sqlalchemy import create_engine, text

# ===============================================================================
# Python Script: Initialize Database Schemas
# ===============================================================================
# Script Purpose:
#   This script establishes the initial connection to PostgreSQL and creates
#   the required schemas (bronze, silver, gold) if they do not exist.
# ===============================================================================

# Connection Details
USER = 'postgres'
PASSWORD = ***** # Replace with your actual password
HOST = 'localhost'
PORT = 5432
DB_NAME = 'datawarehouse'

def init_db():
    try:
        # 1. Create the Connection Engine
        engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
        
        # 2. Establish connection and create schemas
        with engine.connect() as conn:
            print("--- Initializing Database Schemas ---")
            
            # Executing SQL commands to create schemas
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS bronze;"))
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS silver;"))
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS gold;"))
            
            # Commit changes
            conn.commit()
            
        print("✅ Connection successful!")
        print("✅ Schemas (bronze, silver, gold) are ready.")
        
    except Exception as e:
        print(f"❌ Error during database initialization: {e}")

if __name__ == "__main__":
    init_db()
