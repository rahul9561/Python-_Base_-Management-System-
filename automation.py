import pandas as pd
from db import get_connection

def export_to_csv(filename="employees_backup.csv"):
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM employees", conn)
    conn.close()
    df.to_csv(filename, index=False)
    print(f"✅ Data exported to {filename}")
