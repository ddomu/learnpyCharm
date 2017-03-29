import requests
import json

"""
Modify these please
"""
url='http://10.10.20.58/ins'
switchuser='admin'
switchpassword='cisco123'


myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show vrf",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword))

print type(response)

if response.ok :
    print response.json()
    output = response.json()['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']
    print output

    for o in output:
        print o['vrf_id'] , " ", o['vrf_name']

else:
    print response.text



#for key, value in response.iteritems():
#    print value

