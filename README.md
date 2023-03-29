# Weather Stats API
These are the respective API endpoints :
        
        /api/weather - retrieves weather data
        /api/weather/stats - provides statistics about the data
        /docs - provides documentation using openapi

## Prerequisites

The following prerequisites are required to use this API:

    Python (3.7 or higher)
    Virtualenv
    SQLite
    AWS account (if deploying to AWS)

## Installation and Usage

### To install the required dependencies, create and activate a virtual environment with the following commands:

    python -m virtual_env virtual_env

### To activate the virtual environment:

    virtual_env\Scripts\activate (in Windows)
    source virtual_env/bin/activate (in Linux and Mac)

### Then, install the required dependencies:

    pip install -r requirements.txt

### Move to src dir:
    
    cd src

### To ingest the data:

    python ingest_file.py

### To run the server:

    uvicorn app:app --reload

### To access the API endpoints:
    http://127.0.0.1:8000/api/weather/ -- for weather records
    http://127.0.0.1:8000/api/weather/stats -- for weather stats
    http://127.0.0.1:8000/docs -- ui specification of api

    
## To run tests:
    
    cd src
    pytest

# AWS Deployment

Here are the steps to follow for deploying the API to AWS:

    - Create a Python project that contains the FastAPI application code in an app.py file.
    - Create a new AWS Lambda function and configure its runtime to use Python 3.8 or later.
    - Package your Python code and any dependencies as a ZIP file and upload it to AWS Lambda.
    - Set the handler function in your Lambda function to the name of your FastAPI application function.
    - Create an API Gateway, either a REST API or HTTP API, that integrates with your Lambda function.
    - Deploy the API to a publicly accessible endpoint.
    - You can use RDS to store the ingested data.

## Conclusion
    - FastAPI is a powerful and efficient framework for building weather APIs. This approach demonstrates the potential for leveraging FastAPI to create scalable and secure APIs that can handle large volumes of data. In addition, deploying the APIs on AWS provides the flexibility to configure and manage scalability and security features to ensure optimal performance and protection against potential threats. By leveraging the robust capabilities of AWS, weather APIs can be efficiently managed and optimized for enhanced functionality and user experience.