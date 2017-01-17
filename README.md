# Endpoint Freshener

This project provides an AWS Lambda that freshens the given API endpoint when new data is added to the S3.
The function should be invoked from another Lambda like so:
```
url_payload = { "freshen_url": "https://api.trade.gov/v1/endpoint_goes_here/freshen.json?api_key="}
lambda_client.invoke(FunctionName="endpoint_freshen", InvocationType='Event', Payload=json.dumps(url_payload))
```

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python
* Pip
* Virtualenv
* Virtualenvwrapper
* AWS credentials

Then make sure you have your [Trade.gov API Admin Key](https://api.trade.gov) handy. Your need to be authorized as an admin in order to freshen the data.

## Getting Started

  git clone git@github.com:GovWizely/lambda-endpoint-freshen.git
  cd lambda-endpoint-freshen
  mkvirtualenv -r requirements.txt lambda-endpoint-freshen

## Configuration

* Edit `service.py` and change the `API_KEY` to use your key
* Define AWS credentials in either `config.yaml` or in the [default] section of ~/.aws/credentials.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the API key or AWS credentials to version control

## Invocation

  lambda invoke -v
 
## Deploy

  lambda deploy
