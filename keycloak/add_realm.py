#!/usr/bin/env python3
import argparse

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
print(args)
