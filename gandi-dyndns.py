import requests

api_key = "TODO: Replace me with the Gandi API key!"
api_args = {
		"domain": "lienhard.io",
		"rrname": "zh",
		"rrtype": "A",
}
url_template = "https://api.gandi.net/v5/livedns/domains/{domain}/records/{rrname}/{rrtype}"
url = url_template.format(**api_args)
headers = {
		"Authorization": f"Apikey {api_key}",
}

def get_dns_record_ip_address():
	response = requests.get(url, headers=headers)
	assert response.status_code == 200
	return response.json()["rrset_values"][0]

def update_dns_record(ttl, new_ip):
	values = {
			"rrset_ttl": ttl,
			"rrset_values": [new_ip],
	}
	response = requests.put(url, headers=headers, json=values)
	assert response.status_code == 201

def get_router_ip_address():
	url = "https://api.ipify.org"
	response = requests.get(url)
	assert response.status_code == 200
	return response.text

ip_dns = get_dns_record_ip_address()
ip_cur = get_router_ip_address()
if ip_dns is not ip_cur:
	update_dns_record(600, ip_cur)

