import requests

PRIMARY_SERVER = "http://primary-server"
SECONDARY_SERVER = "http://secondary-server"

def check_primary_health():
    try:
        response = requests.get(PRIMARY_SERVER)
        return response.status_code == 200
    except Exception as e:
        return False

def initiate_failover():
    try:
        response = requests.post(SECONDARY_SERVER + "/failover")
        return response.status_code == 200
    except Exception as e:
        return False

if not check_primary_health():
    if initiate_failover():
        print("Failover initiated successfully")
    else:
        print("Failover failed")
else:
    print("Primary server is healthy")
