import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
ARANGODB = os.getenv("ARANGODB")

# Admin credentials
ADMIN_USERNAME = "root"
ADMIN_PASSWORD = ""

# Define the base API URL using environment variables
BASE_API_URL = f"{ARANGODB}_db/_system/_api/"
ARANGODB_USER_API_URL = f"{BASE_API_URL}user"
ARANGODB_PERMISSION_API_URL = f"{BASE_API_URL}user/{{}}/database/{{}}"
ARANGODB_DATABASE_URL = f"{BASE_API_URL}database"
ARANGODB_COLLECTION_PERMISSION_URL = f"{BASE_API_URL}user/{{}}/collection/{{}}"

# User credentials to be added
users = {
    "read_write_user": "testing123",
    "read_user": "testing123",
    "no_access_user": "testing123",
    "bad_permission_user": "testing123",
}

# Collections for which users will have specific permissions
collections = [
    "mitre_attack_enterprise_vertex_collection",
    "mitre_attack_enterprise_edge_collection",
    "mitre_attack_ics_vertex_collection",
    "mitre_attack_ics_edge_collection",
    "mitre_attack_mobile_vertex_collection",
    "mitre_attack_mobile_edge_collection"
]

def add_user(username, password):
    """Add a user to ArangoDB."""
    url = ARANGODB_USER_API_URL
    auth = HTTPBasicAuth(ADMIN_USERNAME, ADMIN_PASSWORD)
    headers = {"Content-Type": "application/json"}
    payload = {
        "user": username,
        "passwd": password,
        "active": True,
        "extra": {}
    }
    
    response = requests.post(url, auth=auth, headers=headers, json=payload)
    
    if response.status_code == 201:
        print(f"Successfully added user: {username}")
    elif response.status_code == 409:
        print(f"User {username} already exists.")
    else:
        print(f"Failed to add user {username}: {response.status_code} - {response.text}")

def set_database_permissions(username, database, permission):
    """Set permissions for a user on a specific database."""
    url = ARANGODB_PERMISSION_API_URL.format(username, database)
    auth = HTTPBasicAuth(ADMIN_USERNAME, ADMIN_PASSWORD)
    headers = {"Content-Type": "application/json"}
    payload = {"grant": permission}
    
    response = requests.put(url, auth=auth, headers=headers, json=payload)
    
    if response.status_code == 200:
        print(f"Successfully set {permission} permission for {username} on database {database}")
    else:
        print(f"Failed to set {permission} permission for {username} on database {database}: {response.status_code} - {response.text}")

def set_collection_permissions(username, database, collection, permission):
    """Set permissions for a user on a specific collection within a specific database."""
    url = ARANGODB_COLLECTION_PERMISSION_URL.format(username, collection)
    auth = HTTPBasicAuth(ADMIN_USERNAME, ADMIN_PASSWORD)
    headers = {"Content-Type": "application/json"}
    payload = {"grant": permission}
    
    response = requests.put(url, auth=auth, headers=headers, json=payload)
    
    if response.status_code == 200:
        print(f"Successfully set {permission} permission for {username} on {collection}")
    else:
        print(f"Failed to set {permission} permission for {username} on {collection}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Add users to ArangoDB
    for username, password in users.items():
        add_user(username, password)
        # Revoke access to the _system database for each user
        set_database_permissions(username, "_system", "none")
        # Grant access to the arango_cti_processor_tests_database
        set_database_permissions(username, "arango_cti_processor_tests_database", "rw")
    
    # Set read/write permissions for read_write_user on specified collections
    for collection in collections:
        set_collection_permissions("read_write_user", "arango_cti_processor_tests_database", collection, "rw")
    
    # Set read permissions for read_user on specified collections
    for collection in collections:
        set_collection_permissions("read_user", "arango_cti_processor_tests_database", collection, "ro")
    
    # Set no access permissions for no_access_user on specified collections
    for collection in collections:
        set_collection_permissions("no_access_user", "arango_cti_processor_tests_database", collection, "none")
    
    # Set permissions for bad_permission_user
    set_collection_permissions("bad_permission_user", "arango_cti_processor_tests_database", "mitre_attack_enterprise_vertex_collection", "rw")
    for collection in collections:
        if collection != "mitre_attack_enterprise_vertex_collection":
            set_collection_permissions("bad_permission_user", "arango_cti_processor_tests_database", collection, "none")
