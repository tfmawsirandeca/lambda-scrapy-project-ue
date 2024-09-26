# Web Scraping Project with AWS Lambda and SAM

This project demonstrates how to create a web scraping application using Scrapy and deploy it as an AWS Lambda function using AWS SAM (Serverless Application Model). The application uses Scrapy to scrape data from a website and AWS Lambda to run the Scrapy spider in a serverless environment.

## Project Structure
- `handler.py`: Contains the Lambda handler function that runs the Scrapy spider.
- `requirements.txt`: Lists the required Python packages.
- `template.yaml`: SAM template defining the Lambda function and API Gateway.


## Build the SAM application
sam build

## Testing Locally
sam local start-api --port 3000

## Deploy solution 
sam deploy --guided

## delete recources deployed
sam delete

