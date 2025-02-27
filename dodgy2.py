import sqlite3
import os
import requests

# Hardcoded secret (will trigger a secret scanning alert)
API_KEY = "sk_live_1234567890abcdef"

# Insecure use of input (SQL Injection)
def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 🚨 SQL Injection vulnerability (unsanitized user input)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)  
    result = cursor.fetchall()
    
    conn.close()
    return result

# Insecure HTTP request (missing certificate verification)
def fetch_data(url):
    # 🚨 Missing SSL verification (MITM vulnerability)
    response = requests.get(url, verify=False)
    return response.text

if __name__ == "__main__":
    user_input = input("Enter username: ")
    print(get_user_data(user_input))

    url = input("Enter URL to fetch: ")
    print(fetch_data(url))
