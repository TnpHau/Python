import json
from .services.service_a import get_service_a_response
from .services.service_b import post_service_b_data

def service_a_handler(event, context):
    response = get_service_a_response()
    return {
        'statusCode': 200,
        'body': json.dumps(response)  # Chuyển response thành chuỗi JSON
    }

def service_b_handler(event, context):
    data = event.get('body', {})
    
    if isinstance(data, str):
        data = json.loads(data)  # Chuyển chuỗi thành dictionary

    response = post_service_b_data(data)
    return {
        'statusCode': 200,
        'body': json.dumps(response)  # Chuyển response thành chuỗi JSON
    }
