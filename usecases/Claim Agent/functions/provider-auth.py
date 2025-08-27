import os
import json

DEBUG = True

def print_debug(text, data=None):
    if DEBUG:
        print(f'----------- {text} -----------')
        if data is not None:
            print(json.dumps(data, indent=4))

def main(message):
    request = message
    
    print_debug ("Message object:", message)
    
    response = {"authorized": True}
    
    return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": response
    }
