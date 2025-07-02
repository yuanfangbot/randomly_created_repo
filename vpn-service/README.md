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

## Configuration

- Server address: vpn.example.com
- Port: 1194
- Protocol: UDP
- Cipher: AES-256-CBC
- Auth: SHA256

## Contact

For any questions or issues, please contact:
Your Name - [your.email@example.com](mailto:your.email@example.com)