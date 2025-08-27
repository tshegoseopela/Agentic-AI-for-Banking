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
    
    response = {}
    if ('member_id' in request and request['member_id'] == '12345678'):
        claims_list = [
            {
                'claim_title': "Claim 1",
                'claim_number':'3311',
                'date_of_service': 'June 9th, 2024',
                'status': 'declined',
                'claim_description': "Office visit for discussion of general wellness and anti aging strategies, including recommendations for nutritional supplements and stress management techniques, not related to the diagnosis or treatment of a specific medical condition."
            },
            {
                'claim_title': "Claim 2",
                'claim_number':'1622',
                'date_of_service': 'January 10, 2024',
                'status': 'approved',
                'claim_description': "Office visit with a physician for evaluation and treatment, including examination via x-ray to assess and diagnose bone or joint condition."
            }
        ]
        
        response['member_id'] = 12345678
        response['first_name'] = "Jim"
        response['last_name'] = "Briggs"
        response['phone_number'] = '+13672366712'
        response['email'] = 'jim_briggs@hotmail.com'
        response['address'] = {}
        response['address']['street'] = '162 2nd St'
        response['address']['city'] = 'Lousiville'
        response['address']['state'] = 'KY'
        response['address']['zip_code'] = '43421'
        response['claims_list'] = claims_list        
    else:
        claims_list = [
            {
                'claim_title': "Claim 1",
                'claim_number':'2299',
                'date_of_service': 'July 28th, 2024',
                'status': 'approved',
                'claim_description': "Medical services rendered for a cesarean section delivery, including pre-operative care, surgical delivery, and post-operative recovery, resulting in the birth of a newborn girl."
            },
            {
                'claim_title': "Claim 2",
                'claim_number':'2746',
                'date_of_service': 'August 10, 2024',
                'status': 'pending, in process of adjudication',
                'claim_description': "Postpartum follow-up visit to monitor recovery and address any concerns or complications following recent childbirth."
            }
        ]
        
        response['member_id'] = request['member_id']
        response['first_name'] = "Jane"
        response['last_name'] = "Smith"
        response['phone_number'] = '+14215551234'
        response['email'] = 'janesmith@gmail.com'
        response['address'] = {}
        response['address']['street'] = '123 Elm St'
        response['address']['city'] = 'Springfield'
        response['address']['state'] = 'IL'
        response['address']['zip_code'] = '62701'
        response['claims_list'] = claims_list        

    
    print(f'----------- Test -----------')
    print_debug ("Response object:", response)

    return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": response
    }
