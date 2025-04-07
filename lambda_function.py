import json
import datetime

def lambda_handler(event, context):
    name = event.get("name", "Guest")
    now = datetime.datetime.utcnow().isoformat()

    response = {
        "message": f"Hello, {name}! This is Dom's AWS Lambda project.",
        "timestamp": now,
        "status": "success"
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

# This part lets you run it locally
if __name__ == "__main__":
    event = {"name": "Dom"}
    result = lambda_handler(event, None)
    print(result)
