def lambda_handler(event, context):
    name = event.get("name", "Guest")
    return {
        'statusCode': 200,
        'body': f'Hello, {name}! Welcome to Dom\'s AWS project.'
    }
