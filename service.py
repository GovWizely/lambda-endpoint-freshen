import json
import logging
import os

import requests


def handler(event, context):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise KeyError('API_KEY env var is empty')
    print("Received event: " + json.dumps(event, indent=2))
    response = True
    try:
        freshen_response = requests.get(event["freshen_url"] + api_key)
        print(freshen_response.text)
        if "error" in freshen_response.json():
            response = False
    except Exception as e:
        logging.error(e)
        response = False
    return response
