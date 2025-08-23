import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db import get_connection

def visualize_data():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM employees", conn)
    conn.close()

    if df.empty:
        print("⚠ No data to visualize.")
        return

    # Salary Distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df["salary"], bins=10, kde=True)
    plt.title("Salary Distribution")
    plt.show()

    # Department-wise Count
    plt.figure(figsize=(8,5))
    sns.countplot(x="department", data=df)
    plt.title("Employees per Department")
    plt.show()
