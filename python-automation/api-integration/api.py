#!/usr/bin/env python3
"""
API Integration Example
Basic GET request to a public API and processing response data.

Dependencies:
    pip install requests
"""

import requests

# Using a fake API that returns sample todo item
url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    # Making a GET request to the API
    response = requests.get(url)
    
    # Print response object
    print(f"Response Object: {response}")
    
    # Print HTTP status code
    print(f"Status Code: {response.status_code}")
    
    # Print JSON content
    print(f"JSON Response: {response.json()}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: Failed to fetch data from API - {e}")
