# Import the config file
import yaml
with open('./config.yml') as f:
    config = yaml.safe_load(f)

# Import external libs
from payload import Payload
import json
import requests


# Instantiate the payload.
payload = Payload (
    text = "I love this product",
    external_id = "my_external_id"
)

# Preparate the header request.
headers = dict()
headers['content-type'] = config['content-type']
headers['x-rapidapi-host'] = config['x-rapidapi-host']
headers['x-rapidapi-key'] = config['x-rapidapi-key']

# Invoke the endpoint and print the response.
response = requests.request("POST", config['url'], data=json.dumps(payload.__dict__), headers=headers)
print(response.json())