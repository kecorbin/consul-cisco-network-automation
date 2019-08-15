#!/usr/bin/env python
import sys
import requests
import json
# Devnet sandbox uses self-signed certs - disable warnings
import urllib3
urllib3.disable_warnings()

# constants
BASE_URL = "https://sbx-nxos-mgmt.cisco.com/api"
auth_url = BASE_URL + "/aaaLogin.json"
ipv4_url = BASE_URL + "/mo/sys/acl/ipv4/oName-web_servers.json"

AUTH_PAYLOAD = {
    "aaaUser": {
        "attributes": {
          "name": "admin",
          "pwd": "Admin_1234!"
           }
    }
}

OBJECT_GROUP = {
    "ipv4aclAddrGroup": {
        "attributes": {
            "name": "web_servers",
            "persistentOnReload": "true",
            "status": ""
        },
        "children": []
    }
}


def object_group_member(addr, seq):
    member_dict = {
        "ipv4aclAddrMember": {
            "attributes": {
                "prefix": addr,
                "prefixLength": "32",
                "prefixMask": "0.0.0.0",
                "rn": "seq-{}".format(seq),
                "seqNum": "{}".format(seq),
                "status": ""
            }
        }
    }
    return member_dict

def update_switch():
    # login and get token
    r = requests.post(auth_url, json=AUTH_PAYLOAD, verify=False)
    r_json = r.json()

    token = r_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {'APIC-cookie':token}
    # delete object-group
    r = requests.delete(ipv4_url, cookies=cookie, verify=False)
    print(r.text)
    # recreate with updated members
    print(requests.put(ipv4_url, cookies=cookie, json=OBJECT_GROUP, verify=False).json())

if __name__ == "__main__":
    # JSON data is sent as std
    update = sys.stdin.read()
    data = json.loads(update)
    seq = 10
    for d in data:
        addr = d['Node']['TaggedAddresses']['lan']
        OBJECT_GROUP['ipv4aclAddrGroup']['children'].append(object_group_member(addr, seq))
        seq = seq + 10
    update_switch()
