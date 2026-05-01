# fortigate-cert-ssl-autoupload

## Description

This Python script automates uploading certificates to a FortiGate firewall using the REST API. It uploads a certificate along with its private key, assigns a unique timestamped name to avoid conflicts, and updates a specified SSL/SSH profile to use the newly imported certificate.

The script supports multiple certificates in a single run, making it suitable for automated certificate rotation and consistent configuration management across environments.

Two variants of the script are available:

One version handles certificates in PFX (PKCS#12) format.
The other version works with PEM-encoded certificates and private keys.

---

## Prerequisites

### System Requirements

* Python 3.x

### Python Dependencies

Install required library:

```bash
pip install requests
```

### FortiGate Requirements

* HTTPS API access enabled on the FortiGate
* Valid API token with permissions "Firewall -> Custom -> Others (Read/Write)

### Environment Variables

Set your API key as an environment variable:

```bash
export FIREWALL_KEY="your_api_token_here"
```

(on Windows)

```cmd
set FIREWALL_KEY=your_api_token_here
```

---

## Configuration

Update the script variables as needed:

```python
cert_data = [
    {
        "cert_name": "wild.example.com",
        "cert_path": "cert.pem",
        "cert_key_path": "cert.key",
        "ssl_profile_name": "your_ssl_profile"
    }
]
```

And firewall connection:

```python
firewall_ip = "10.10.12.1:10443"
```

---


