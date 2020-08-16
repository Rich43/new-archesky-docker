#!/usr/bin/env python3
import argparse

import requests

parser = argparse.ArgumentParser(description='Add a realm to keycloak.')
parser.add_argument('--url', required=True, type=str,
                    help='Keycloak url e.g. http://localhost:8080')
parser.add_argument('--username', required=True, type=str,
                    help='Keycloak admin username')
parser.add_argument('--password', required=True, type=str,
                    help='Keycloak admin password')
parser.add_argument('--domain', required=True, type=str,
                    help='Realm domain e.g. localhost')
parser.add_argument('--port', required=False, type=int,
                    help='Realm port e.g. 3000 - this is optional')
args = parser.parse_args()

if args.port:
    args.port = f":{args.port}"
else:
    args.port = ""

response = requests.post(
    f"{args.url}/auth/realms/master/protocol/openid-connect/token",
    {
        "client_id": "admin-cli",
        "username": args.username,
        "password": args.password,
        "grant_type": "password"
    }
)

token = response.json()['access_token']
headers = {
    'Authorization': f"Bearer {token}",
    "Content-Type": "application/json"
}
data: str = open("archesky.json").read()
data = data.replace("$domainname", args.domain)
data = data.replace("$port", args.port)

response = requests.post(
    f"{args.url}/auth/admin/realms",
    data,
    headers=headers
)

print("Realm Added.")
