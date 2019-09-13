existing = {
   "l3extOut": {
      "attributes": {
         "dn": "uni/tn-HashiCorp/out-consul_services",
         "ownerKey": "",
         "name": "consul_services",
         "descr": "Rename",
         "targetDscp": "unspecified",
         "enforceRtctrl": "export",
         "nameAlias": "outside_network",
         "ownerTag": "",
         "annotation": "tag_l3out"
      },
      "children": [
         {
            "l3extInstP": {
               "attributes": {
                  "matchT": "AtleastOne",
                  "name": "web_service",
                  "descr": "This EPG mirrors the web service in Consul",
                  "targetDscp": "unspecified",
                  "prefGrMemb": "exclude",
                  "exceptionTag": "2",
                  "floodOnEncap": "disabled",
                  "nameAlias": "web.service.consul",
                  "prio": "level1",
                  "annotation": "tag_network_profile"
               },
               "children": [
                  {
                     "fvRsProv": {
                        "attributes": {
                           "tnVzBrCPName": "web",
                           "matchT": "AtleastOne",
                           "annotation": "",
                           "prio": "unspecified"
                        }
                     }
                  },
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "web3",
                           "descr": "",
                           "ip": "172.20.0.6/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  },
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "web2",
                           "descr": "",
                           "ip": "172.20.0.2/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  },
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "web1",
                           "descr": "",
                           "ip": "172.20.0.4/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  },
                  {
                     "fvRsCustQosPol": {
                        "attributes": {
                           "annotation": "",
                           "tnQosCustomPolName": ""
                        }
                     }
                  }
               ]
            }
         },
         {
            "l3extInstP": {
               "attributes": {
                  "matchT": "AtleastOne",
                  "name": "web.service.consul",
                  "descr": "This EPG mirrors the web service in Consul",
                  "targetDscp": "unspecified",
                  "prefGrMemb": "exclude",
                  "exceptionTag": "2",
                  "floodOnEncap": "disabled",
                  "nameAlias": "web.service.consul",
                  "prio": "level1",
                  "annotation": "tag_network_profile"
               },
               "children": [
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "20",
                           "descr": "",
                           "ip": "172.20.0.6/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  },
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "20",
                           "descr": "",
                           "ip": "172.20.0.2/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  },
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "10",
                           "descr": "",
                           "ip": "172.20.0.4/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  },
                  {
                     "fvRsCustQosPol": {
                        "attributes": {
                           "annotation": "",
                           "tnQosCustomPolName": ""
                        }
                     }
                  }
               ]
            }
         },
         {
            "l3extInstP": {
               "attributes": {
                  "matchT": "AtleastOne",
                  "name": "demo_inst_prof",
                  "descr": "TODO: RENAME",
                  "targetDscp": "unspecified",
                  "prefGrMemb": "exclude",
                  "exceptionTag": "2",
                  "floodOnEncap": "disabled",
                  "nameAlias": "alias_profile",
                  "prio": "level1",
                  "annotation": "tag_network_profile"
               },
               "children": [
                  {
                     "fvRsCustQosPol": {
                        "attributes": {
                           "annotation": "",
                           "tnQosCustomPolName": ""
                        }
                     }
                  }
               ]
            }
         }
      ]
   }
}

desired = {
   "l3extOut": {
      "attributes": {
         "dn": "uni/tn-HashiCorp/out-consul_services",
         "ownerKey": "",
         "targetDscp": "unspecified",
         "name": "consul_services",
         "descr": "Rename",
         "nameAlias": "outside_network",
         "ownerTag": "",
         "annotation": "tag_l3out",
         "enforceRtctrl": "export"
      },
      "children": [
         {
            "l3extInstP": {
               "attributes": {
                  "exceptionTag": "2",
                  "floodOnEncap": "disabled",
                  "matchT": "AtleastOne",
                  "name": "web_service",
                  "descr": "This EPG mirrors the web service in Consul",
                  "nameAlias": "web.service.consul",
                  "prio": "level1",
                  "targetDscp": "unspecified",
                  "annotation": "tag_network_profile",
                  "prefGrMemb": "exclude"
               },
               "children": [
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "web1",
                           "descr": "",
                           "ip": "172.20.0.4/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  },
                  {
                     "l3extSubnet": {
                        "attributes": {
                           "name": "web2",
                           "descr": "",
                           "ip": "172.20.0.2/32",
                           "nameAlias": "",
                           "aggregate": "",
                           "scope": "import-security",
                           "annotation": ""
                        }
                     }
                  }
               ]
            }
         }
      ]
   }
}
