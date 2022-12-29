#!/usr/bin/python3
"""Ascripr that takes a letter and
sends a POST request with the letter as a parameter."""

if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = ''
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data={'q': query})

    try:
        result = res.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
