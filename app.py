import sqlite3
import os
import requests
import sys

# 🚨 Hardcoded Secret (Should be detected by Secret Scanning)
API_KEY = "sk_live_1234567890abcdef"

# 🚨 Insecure SQL Query (More explicit taint tracking for CodeQL)
def get_user_data():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    username = input("Enter username: ")  # Untrusted user input
    
    # **More obvious SQL Injection vulnerability**
    query = "SELECT * FROM users WHERE username = '" + username + "'"  
    cursor.execute(query)  # 🚨 Unsanitized SQL query
    result = cursor.fetchall()

    conn.close()
    return result

# 🚨 Insecure HTTP request (No SSL verification)
def fetch_data():
    url = input("Enter URL to fetch: ")  # Untrusted user input
    response = requests.get(url, verify=False)  # 🚨 Missing SSL verification
    return response.text

# 🚨 Insecure use of environment variables
def load_env_variable():
    secret = os.getenv("DATABASE_PASSWORD")  # Sensitive data exposure
    print(f"Loaded secret: {secret}")  # 🚨 Potential exposure of secrets

if __name__ == "__main__":
    print(get_user_data())
    print(fetch_data())
    load_env_variable()
