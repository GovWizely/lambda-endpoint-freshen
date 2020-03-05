[![CircleCI](https://circleci.com/gh/GovWizely/lambda-endpoint-freshen.svg?style=svg)](https://circleci.com/gh/GovWizely/lambda-endpoint-freshen)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=GovWizely/lambda-endpoint-freshen)](https://dependabot.com)
[![Maintainability](https://api.codeclimate.com/v1/badges/313039270d5cc676239f/maintainability)](https://codeclimate.com/github/GovWizely/lambda-endpoint-freshen/maintainability)

# Endpoint Freshener

This project provides an AWS Lambda that freshens the given API endpoint when new data is added to the S3 bucket.
The function should be invoked from another Lambda like so:
```
url_payload = { "freshen_url": "https://api.trade.gov/v1/endpoint_goes_here/freshen.json?api_key="}
lambda_client.invoke(FunctionName="endpoint_freshen", InvocationType='Event', Payload=json.dumps(url_payload))
```

## Prerequisites

- This project is tested against Python 3.7+ in [CircleCI](https://app.circleci.com/github/GovWizely/lambda-endpoint-freshen/pipelines).
- Make sure you have your [Trade.gov API Admin Key](https://api.trade.gov) handy. Your need to be authorized as an admin in order to freshen the data.

## Getting Started

	git clone git@github.com:GovWizely/lambda-endpoint-freshen.git
	cd lambda-endpoint-freshen
	mkvirtualenv -p /usr/local/bin/python3.8 -r requirements-test.txt lambda-endpoint-freshen

If you are using PyCharm, make sure you enable code compatibility inspections for Python 3.7/3.8.

### Tests

```bash
python -m pytest
```

## Configuration

* Define the [Trade.gov API Admin Key](https://api.trade.gov) as an environment variable `export API_KEY=your_key`. This will allow you to run the Lambda locally.
* Define AWS credentials in either `config.yaml` or in the [default] section of `~/.aws/credentials`. To use another profile, you can do something like `export AWS_DEFAULT_PROFILE=govwizely`.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.

## Invocation

	lambda invoke -v
 
## Deploy
    
In the AWS Lambda console, set up the `API_KEY` environment variable. Then you are ready to deploy:

	lambda deploy --requirements requirements.txt
