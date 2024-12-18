from django.conf import settings
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

server_title=os.getenv('SERVER_TITLE', "Arango Taxii Server")
server_description = os.getenv('SERVER_DESCRIPTION', "Arango Taxii Server")
server_contact_email = os.getenv('SERVER_EMAIL', '')
server_contact_url = os.getenv('SERVER_SUPPORT', 'https://github.com/muchdogesec/arango_taxii_server')
server_max_content_length = int(os.getenv('SERVER_MAX_CONTENT_LENGTH', 10*1024*1024))
media_type = "application/stix+json;version=2.1"
taxii_type = "application/taxii+json;version=2.1"
server_host_path = os.environ['SERVER_BASE_URL']

