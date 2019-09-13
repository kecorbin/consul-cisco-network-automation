#!/usr/bin/env python
import sys
import requests
import json
# Devnet sandbox uses self-signed certs - disable warnings
import urllib3
urllib3.disable_warnings()

# constants?
BASE_URL = "https://sandboxapicdc.cisco.com/api"
auth_url = BASE_URL + "/aaaLogin.json"
L3OUT_URL = BASE_URL + "/node/mo/uni/tn-HashiCorp/out-consul_services.json"
L3EPG_URL = BASE_URL + "/node/mo/uni/tn-HashiCorp/out-consul_services/instP-web_service.json"
#ipv4_url = BASE_URL + "/mo/sys/acl/ipv4/oName-web_servers.json"
#TARGET_OBJECT_GROUP = "web_servers"

# TODO remove static credentials
AUTH_PAYLOAD = {
    "aaaUser": {
        "attributes": {
          "name": "admin",
          "pwd": "ciscopsdt"
           }
    }
}

L3OUT_DICT =   {
    "l3extOut": {
        "attributes": {
          "annotation": "tag_l3out",
          "descr": "Rename",
          "dn": "uni/tn-HashiCorp/out-consul_services",
          "enforceRtctrl": "export",
          "name": "consul_services",
          "nameAlias": "outside_network",
          "ownerKey": "",
          "ownerTag": "",
          "targetDscp": "unspecified"
        },
    "children": []
    }
}

INSTANCE_PROFILE = {
    "l3extInstP": {
      "attributes": {
        "annotation": "tag_network_profile",
        "descr": "This EPG mirrors the web service in Consul",
        "exceptionTag": "2",
        "floodOnEncap": "disabled",
        "matchT": "AtleastOne",
        "name": "web_service",
        "nameAlias": "web.service.consul",
        "prefGrMemb": "exclude",
        "prio": "level1",
        "targetDscp": "unspecified"
      },
      "children": []
    }
}

def l3_external_subnet(addr, name):
    """
    returns a dictionary suitable for updating a l3 external EPG
    """
    subnet = {
          "l3extSubnet": {
            "attributes": {
              "aggregate": "",
              "annotation": "",
              "descr": "",
              "ip": "{}/32".format(addr),
              "name": "{}".format(name),
              "nameAlias": "",
              "scope": "import-security"
            }
        }
    }
    return subnet




def update_aci():
    # login and get token
    r = requests.post(auth_url, json=AUTH_PAYLOAD, verify=False)
    r_json = r.json()
    token = r_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {'APIC-cookie':token}
    options = "?rsp-subtree=full&rsp-prop-include=config-only&rsp-subtree-class=l3extInstP"
    existing_req = requests.get(L3OUT_URL + options, cookies=cookie, verify=False)
    # delete external EPG
    delete_req = requests.delete(L3EPG_URL, cookies=cookie, verify=False)
    # recreate with updated members
    update_req = requests.post(L3OUT_URL, cookies=cookie,
                     data=json.dumps(L3OUT_DICT), verify=False)
    print('ACI Response: {}'.format(update_req.text))


if __name__ == "__main__":

    # JSON data representing service pool
    update = sys.stdin.read()
    data = json.loads(update)
    print("Service Change detected for L3 Out: {}".format(L3OUT_URL))
    seq = 10

    # prepare object group updates
    ips = list()
    for d in data:
        name = d['Node']['Node']
        addr = d['Node']['TaggedAddresses']['lan']
        ips.append(addr)
        members = INSTANCE_PROFILE['l3extInstP']['children']
        members.append(l3_external_subnet(addr, name))
        seq = seq + 10
    L3OUT_DICT['l3extOut']['children'].append(INSTANCE_PROFILE)

    #
    # # profit!
    # print("{} pool {}".format(TARGET_OBJECT_GROUP, ips))
    update_aci()
