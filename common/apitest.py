import requests
import json

class api_get:

    def get_test1(self, URL, label1):

        label_cnt = 0
        label_str = []

        # sending get request and saving the response as response object
        r = requests.get(url=URL)
        d = r.content

        # extracting data in json format
        data = json.loads(d)

        for listcount in range((len(data["planListing"]["plans"]))):
            label_str.append((data["planListing"]["plans"][listcount][label1]))
            label_cnt = label_cnt + 1

        return label_str, label_cnt