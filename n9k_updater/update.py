#!/usr/bin/env python
import sys
import requests
import json
# Devnet sandbox uses self-signed certs - disable warnings
import urllib3
urllib3.disable_warnings()

# constants?
BASE_URL = "https://sbx-nxos-mgmt.cisco.com/api"
auth_url = BASE_URL + "/aaaLogin.json"
ipv4_url = BASE_URL + "/mo/sys/acl/ipv4/oName-web_servers.json"
TARGET_OBJECT_GROUP = "web_servers"

# TODO remove static credentials
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
            "name": TARGET_OBJECT_GROUP,
            "persistentOnReload": "true",
            "status": ""
        },
        "children": []
    }
}


def object_group_member(addr, seq):
    """
    returns a dictionary suitable for updating a host object group member
    """
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

    # recreate with updated members
    r = requests.put(ipv4_url, cookies=cookie,
                     json=OBJECT_GROUP, verify=False)
    print('NX-API Status Code: {}'.format(r.status_code))

if __name__ == "__main__":

    # JSON data representing service pool
    update = sys.stdin.read()
    data = json.loads(update)
    print("Service Change detected for {}".format(TARGET_OBJECT_GROUP))
    seq = 10

    # prepare object group updates
    ips = list()
    for d in data:
        addr = d['Node']['TaggedAddresses']['lan']
        ips.append(addr)
        members = OBJECT_GROUP['ipv4aclAddrGroup']['children']
        members.append(object_group_member(addr, seq))
        seq = seq + 10

    # profit!
    print("{} pool {}".format(TARGET_OBJECT_GROUP, ips))
    update_switch()
