import sqlite3
import os

def unsafe_query(user_input):
    """SQL Injection vulnerability"""
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # Vulnerable: direct string concatenation
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    cursor.execute(query)
    return cursor.fetchall()

def command_injection(filename):
    """Command injection vulnerability"""
    # Vulnerable: unsanitized input in os.system
    os.system("cat " + filename)

def hardcoded_secret():
    """Hardcoded secret"""
    api_key = "AKIAIOSFODNN7EXAMPLE"
    secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    return api_key, secret
