# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 01:17:16 2021

@author: sagar kumar
"""

import requests
import json
ip_address = "3.21.75.112"
port = "5000"
data = [[5.1, 3.5, 1.5, 0.4]]

url = 'http://{0}:{1}/predict/'.format(ip_address, port)

json_data = json.dumps(data)
header = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
response = requests.post(url, data = json_data, headers = header)
print(response, response.text)