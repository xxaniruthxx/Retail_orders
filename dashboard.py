import streamlit as st
import mysql.connector
import pandas as pd
import os
import socket

# ✅ Get local IP address for network access
def get_network_url():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return f"http://{local_ip}:8501"

# ✅ Connect to MySQL (XAMPP Server)
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="retail_orders"
    )

# ✅ Fetch all table names
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = [table[0] for table in cursor.fetchall()]
cursor.close()
conn.close()

# ✅ Streamlit UI
st.title("📊 Retail Orders Database Viewer")

# ✅ Select table from dropdown
selected_table = st.selectbox("Select a table to view:", tables)

# ✅ Fetch and display selected table
if selected_table:
    conn = get_connection()
    query = f"SELECT * FROM {selected_table}"
    df = pd.read_sql(query, conn)
    st.write(f"### 📂 {selected_table} Table")
    st.dataframe(df)
    conn.close()

# ✅ Print Local & Network URLs
local_url = "http://localhost:8501"
network_url = get_network_url()

print("\n🔗 **Copy and paste a link into your browser:**")
print(f"👉 Localhost: {local_url}")
print(f"🌐 Network: {network_url}")

# ✅ Auto-run Streamlit (Runs once, No Loop)
if __name__ == "__main__":
    os.system("streamlit run dashboard.py")
