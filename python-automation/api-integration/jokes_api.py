#!/usr/bin/env python3
"""
Joke API Integration
Fetch random jokes from two different APIs based on user preference.

APIs Used:
    1. Official Joke API: http://official-joke-api.appspot.com/
    2. Dad Jokes API: https://api.api-ninjas.com/v1/dadjokes

Dependencies:
    pip install requests
"""

import requests

# API URLs
RANDOM_JOKES_URL = "http://official-joke-api.appspot.com/random_joke"
DAD_JOKES_URL = "https://api.api-ninjas.com/v1/dadjokes"

# API Key for Dad Jokes (replace with your own)
DAD_JOKES_API_KEY = "nRujjcLgnfxBSII8LOChrEfUY2WZk5tBrGvbd5mT"

def get_jokes(url_type, mood):
    """
    Fetch jokes from the specified API.
    
    Args:
        url_type (str): URL of the API to call
        mood (str): Type of joke - "1" for random, "2" for dad jokes
    
    Returns:
        str: Formatted joke string
    """
    try:
        if mood == "1":
            # Fetch random joke
            response = requests.get(url=url_type)
            data = response.json()
            final_joke = data["setup"] + "\n" + data["punchline"]
        else:
            # Fetch dad joke with API key
            headers = {
                "X-Api-Key": DAD_JOKES_API_KEY
            }
            response = requests.get(url=url_type, headers=headers)
            data = response.json()
            
            if isinstance(data, list) and len(data) > 0:
                final_joke = data[0]["joke"]
            else:
                final_joke = "Error getting dad joke"
        
        return final_joke
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"

def main():
    print("\n=== Joke API Fetcher ===")
    print("1. Random Joke")
    print("2. Dad Joke")
    
    mood = input("\nEnter choice (1 or 2): ")
    
    if mood == "1":
        url_type = RANDOM_JOKES_URL
    elif mood == "2":
        url_type = DAD_JOKES_URL
    else:
        print("Invalid choice!")
        return
    
    final_joke = get_jokes(url_type, mood)
    print("\n" + "="*40)
    print("Here is your joke:\n")
    print(final_joke)
    print("="*40 + "\n")

if __name__ == "__main__":
    main()
