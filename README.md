# consul-n9k-object-groups

Proof of concept demo for using service discovery provided by [Consul](https://www.consul.io/)
to maintain object group configuration on Nexus 9000 switches.  

# Steal Underpants!

Docker Compose gives us a low toil way to launch the demo environment.  The file describes
a sample environment made up of a consul cluster, and three "web" nodes. Consul can provide
L7 based routing, simple round robin load balancing, canary deployments, or
disaster recovery solutions. But for now, let's see what it can do in a "crawl phase"

```
docker-compose up
```


# ????

This POC leverages the Nexus 9K Always-On Sandbox provided by Cisco DevNet.  
You can access the Nexus 9000 we are using by connecting to the following device

Object groups are commonly used to make managing things like ACL's and QoS policies.  
These are largely managed manually, and are error-prone for two reasons:
1. generally managed manually
2. Garbage in, garbage out! Where's my source of truth? Is it accurate? Is the rate of churn increasing?


```
ssh admin@sbx-nxos-mgmt.cisco.com -p 8181
```

Credentials are `admin/Admin_1234!`


The object groups can be monitored using the `show object-group` command
```
sbx-n9kv-ao# show object-group
IPv4 address object-group web_servers
	10 host 172.28.0.5
	20 host 172.28.0.3
	30 host 172.28.0.4

```

# Profit!

Try exploring things like `docker-compose stop web3` and observe the object groups reacting.
