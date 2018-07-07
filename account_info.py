import requests
import json
url = "http://api1.eosnairobi.io:8898/v1/chain/get_block"

# response = requests.request("POST", url)
r = response.post(url, data=json.dumps({'block_num_or_id':4613648}))
# print(response.text)
print(r.text)
