# VPN Service

A sample VPN service configuration.

## Features

- Secure connection
- OpenVPN protocol
- Strong encryption

## Setup

1. Install OpenVPN
2. Copy config file to OpenVPN directory
3. Connect to VPN
   ```bash
   sudo openvpn --config config.conf
   ```

## Security

- Uses AES-256-CBC cipher
- SHA256 authentication
- UDP protocol for better performance