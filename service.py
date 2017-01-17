# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
import json

API_KEY = 'YOUR_API_TRADE_GOV_ADMIN_KEY_HERE'

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    try:
        response = requests.get(event['freshen_url'] + API_KEY)
        print(response.text)
        return response.text
    except Exception as e:
        print(e)
        raise e