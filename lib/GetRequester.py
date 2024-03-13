import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = requests.get(self.url)
        return json.loads(response.content)

# # test
# url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
# test = GetRequester(url)

# test.get_response_body()