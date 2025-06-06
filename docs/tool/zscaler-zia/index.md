# Zscaler Internet Access (ZIA)

## Overview

Zscaler Internet Access (ZIA) is a cloud-based security platform that provides secure internet access for users, regardless of their location. It offers comprehensive protection against web threats, data loss, and malicious content by inspecting all traffic in real-time. ZIA enables organizations to enforce security policies, control access to applications, and ensure compliance with regulatory requirements, all while delivering a seamless user experience.

## Categories

- SaaS
- Web Security
- Cloud Security

## Capabilities

| Capability | ID | Phase | Description |
|------------|----|-------|-------------|
| [Access External HTTP Logs](C1104.md) | [C1104](../../capability/access-external-http-logs/index.md) | Preparation | This capability involves accessing and reviewing external HTTP logs to gather information about web traffic, identify potential threats, and analyze user behavior. It is essential for understanding the context of web-based incidents and for proactive monitoring of web applications. |
| [Access External DNS Logs](C1106.md) | [C1106](../../capability/access-external-dns-logs/index.md) | Preparation | This capability allows security teams to access external DNS logs, which are crucial for monitoring and analyzing domain name system activities within the network. By examining these logs, teams can identify potential security threats, track user activities, and understand the context of events that may indicate a security breach. External DNS logs differ from internal DNS logs as they capture communication from internal systems to external domains, providing insights into outbound traffic and potential data exfiltration attempts. |
| [Block External IP Address](C3101.md) | [C3101](../../capability/block-external-ip-address/index.md) | Containment | This capability involves blocking external IP addresses that are identified as malicious or suspicious. It is a proactive measure to prevent unauthorized access and mitigate potential threats from external sources. This capability can be implemented through firewall rules, intrusion prevention systems, or other network security tools to ensure that traffic from these IP addresses is denied. |
| [Block Port External Communication](C3107.md) | [C3107](../../capability/block-port-external-communication/index.md) | Containment | This capability involves blocking external communication on specific ports that are identified as malicious or suspicious. It is a proactive measure to prevent unauthorized access and mitigate potential threats from external sources. This capability can be implemented through firewall rules, intrusion prevention systems, or other network security tools to ensure that traffic on these ports is denied. |