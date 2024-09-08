# Web Scraping Project with AWS Lambda and SAM

This project demonstrates how to create a web scraping application using Scrapy and deploy it as an AWS Lambda function using AWS SAM (Serverless Application Model). The application uses Scrapy to scrape data from a website and AWS Lambda to run the Scrapy spider in a serverless environment.

## Project Structure
- `lambda_function.py`: Contains the Lambda handler function that runs the Scrapy spider.
- `requirements.txt`: Lists the required Python packages.
- `template.yaml`: SAM template defining the Lambda function and API Gateway.
- `event.json`: Sample event file for local testing.
- `web_scraping_project/`: The Scrapy project directory containing spiders and settings.


## Build the SAM application
sam build

## Testing Locally
sam local start-api --port 3000

## Run one file spider command
scrapy runspider scrapy_project/spiders/ajo_spider.py

## Deploy solution 
sam deploy --guided

