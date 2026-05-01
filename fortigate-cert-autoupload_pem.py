import requests
import os
import base64
from datetime import datetime


### Certificate Information ###
cert_data = [
    {
        "cert_name" : "wild.example.cz",
        "cert_path": "cert_example.pem",
        "cert_key_path": "cert_example.key",
        "ssl_profile_name": "example_ssl"
    },
    {
        "cert_name" : "wild.example2.cz",
        "cert_path": "cert_example2.pem",
        "cert_key_path": "cert_example2.key",
        "ssl_profile_name": "example2_ssl"
    },
]

### Firewall Information ###
firewall_ip = "10.10.12.1:10443"
firewall_key = os.getenv("FIREWALL_KEY")
firewall_url = f"https://{firewall_ip}"


def change_certificate(cert_name, cert_path, cert_key_path, ssl_profile_name):
    
    # Define API endpoints
    firewall_cert_url = "/api/v2/monitor/vpn-certificate/local/import"
    firewall_ssl_url = f"/api/v2/cmdb/firewall/ssl-ssh-profile/{ssl_profile_name}"    
    full_cert_url = f"{firewall_url}{firewall_cert_url}"
    full_ssl_url = f"{firewall_url}{firewall_ssl_url}"
    
    # Append timestamp to certificate name to avoid conflicts
    timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d")
    cert_name = f"{cert_name}-{timestamp}"

    # Read and encode certificate and key files
    with open(cert_path, "rb") as cert_file:
        cert_content = base64.b64encode(cert_file.read()).decode("utf-8")
        
    with open(cert_key_path, "rb") as key_file:
        key_content = base64.b64encode(key_file.read()).decode("utf-8")
      
    # Set headers for API requests    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {firewall_key}"
    }

    # Prepare payloads for certificate upload and SSL profile update
    cert_payload = {
        "type": "regular",
        "certname": cert_name,
        "scope": "global",
        "file_content": cert_content,
        "key_file_content": key_content
    }
    
    ssl_payload = {
        "server-cert": [
            {
                "name": cert_name
            }
        ]
    }

    # Make API requests to upload certificate and update SSL profile
    upload_cert = requests.post(full_cert_url, headers=headers, verify=False, json=cert_payload)
    change_cert_in_ssl = requests.put(full_ssl_url, headers=headers, verify=False, json=ssl_payload)
    
    print(upload_cert.text)
    print(change_cert_in_ssl.text)


# Main execution
if __name__ == "__main__":
    for cert in cert_data:
        change_certificate(**cert)