import json
import requests  # Make sure to add requests to your Lambda layer or include in deployment package
import boto3

def run_eventbridge(eventbridge, results):
    try:
        # Ensure results is JSON-serializable
        detail = json.dumps(results)
    except (TypeError, ValueError) as e:
        print(f"Failed to serialize results to JSON: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Failed to serialize results to JSON."})
        }
    print('mi detail format')
    print(detail)
    print('result')
    print(results)
    # Create the event
    response = eventbridge.put_events(
        Entries=[
            {
                'Source': 'custom.lambda1',
                'DetailType': 'Lambda1ToLambda2',
                'Detail': json.dumps({
                    'message': 'Hello from Lambda 1',
                    'data': results
                }),
                'EventBusName': 'default'
            }
        ]
    )
    
    # Log the EventBridge response
    print(f'Event sent: {response}')
    return response

def lambda_handler(event, context):
    eventbridge = boto3.client('events')
    
    # URL to scrape
    url = "https://wgt45uf3mc.us-east-1.awsapprunner.com/scrape"
    
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if request was successful
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Failed to fetch data from the scraping URL."})
        }
    
    # Parse the JSON response
    try:
        response_data = response.json()
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Failed to parse JSON response."})
        }
    
    # Extract the 'data' array
    results = response_data.get("data", [])
    print('data')
    print('results')
    # Check if 'results' is valid
    if not isinstance(results, list):
        print(f"Unexpected results format: {results}")
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Unexpected results format."})
        }
    
    # Send the event to EventBridge
    event_response = run_eventbridge(eventbridge, response_data)
    
    # Return the data array as the response
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
