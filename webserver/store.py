import requests

def get_categories():
    r = requests.get('https://www.thestatsdontlie.com/football/europe/italy/serie-a/over-1-5-goals/')
    print(r.status_code)
    print(r.text)
    
    categories = r.json()
    
    for category in categories:
        print(category['name'])