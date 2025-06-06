# SentinelOne

## Overview

SentinelOne is an advanced endpoint protection platform that uses AI to detect, prevent, and respond to cyber threats in real-time. It provides comprehensive security for endpoints, including threat intelligence, automated response capabilities, and detailed analytics to help organizations protect their systems from sophisticated attacks.

## Categories

- EDR
- EPP
- XDR

## Capabilities

| Capability | ID | Phase | Description |
|------------|----|-------|-------------|
| [Access Vulnerability Management System Logs](C1013.md) | [C1013](../../capability/preparation/C1013.md) | Preparation | This capability involves accessing and reviewing logs from the vulnerability management system to identify any anomalies or unauthorized activities related to vulnerability assessments and remediation efforts. It is crucial for understanding the security posture of the organization and detecting potential security incidents. |
| [Access Internal HTTP Logs](C1103.md) | [C1103](../../capability/preparation/C1103.md) | Preparation | This capability involves accessing and reviewing internal HTTP logs to gather information about web traffic, identify potential threats, and analyze user behavior. It is essential for understanding the context of web-based incidents and for proactive monitoring of web applications. |
| [Access External HTTP Logs](C1104.md) | [C1104](../../capability/preparation/C1104.md) | Preparation | This capability involves accessing and reviewing external HTTP logs to gather information about web traffic, identify potential threats, and analyze user behavior. It is essential for understanding the context of web-based incidents and for proactive monitoring of web applications. |
| [Access Internal DNS Logs](C1105.md) | [C1105](../../capability/preparation/C1105.md) | Preparation | This capability allows security teams to access internal DNS logs, which are crucial for monitoring and analyzing domain name system activities within the network. By examining these logs, teams can identify potential security threats, track user activities, and understand the context of events that may indicate a security breach. |
| [Access External DNS Logs](C1106.md) | [C1106](../../capability/preparation/C1106.md) | Preparation | This capability allows security teams to access external DNS logs, which are crucial for monitoring and analyzing domain name system activities within the network. By examining these logs, teams can identify potential security threats, track user activities, and understand the context of events that may indicate a security breach. External DNS logs differ from internal DNS logs as they capture communication from internal systems to external domains, providing insights into outbound traffic and potential data exfiltration attempts. |
| [List Alert Victims](C2001.md) | [C2001](../../capability/identification/C2001.md) | Identification | This capability allows for stakeholders to list all victims affected by the incident. It provides a comprehensive overview of those impacted, enabling better resource allocation and response planning. |
| [List Host Vulnerabilities](C2002.md) | [C2002](../../capability/identification/C2002.md) | Identification | This capability involves the ability to identify and list vulnerabilities present on hosts within a network. It includes scanning for known vulnerabilities, assessing their severity, and compiling a report of findings to inform remediation efforts. |
| [List Registry Key Modifications](C2501.md) | [C2501](../../capability/identification/C2501.md) | Identification | This capability allows the incident responder and security analyst to list modifications made to registry keys. This is crucial for identifying unauthorized changes that may indicate malicious activity or system misconfiguration. The capability provides a means to track changes over time, aiding in forensic analysis and incident response. |
| [Block External IP Address](C3101.md) | [C3101](../../capability/containment/C3101.md) | Containment | This capability involves blocking external IP addresses that are identified as malicious or suspicious. It is a proactive measure to prevent unauthorized access and mitigate potential threats from external sources. This capability can be implemented through firewall rules, intrusion prevention systems, or other network security tools to ensure that traffic from these IP addresses is denied. |
| [Block Internal IP Address](C3102.md) | [C3102](../../capability/containment/C3102.md) | Containment | This capability involves blocking internal IP addresses that are identified as malicious or suspicious. It is a proactive measure to prevent unauthorized access and mitigate potential threats from within the network. This capability can be implemented through firewall rules, intrusion prevention systems, or other network security tools to ensure that traffic from these internal IP addresses is denied. |
| [Block Port External Communication](C3107.md) | [C3107](../../capability/containment/C3107.md) | Containment | This capability involves blocking external communication on specific ports that are identified as malicious or suspicious. It is a proactive measure to prevent unauthorized access and mitigate potential threats from external sources. This capability can be implemented through firewall rules, intrusion prevention systems, or other network security tools to ensure that traffic on these ports is denied. |
| [Block Port Internal Communication](C3108.md) | [C3108](../../capability/containment/C3108.md) | Containment | This capability involves blocking internal communication on specific ports that are identified as malicious or suspicious. It is a proactive measure to prevent unauthorized access and mitigate potential threats from within the network. This capability can be implemented through firewall rules, intrusion prevention systems, or other network security tools to ensure that traffic on these ports is denied. |

## MITRE ATT&CK Data Sources

- Process: Process Creation
- Process: Process Termination
- File: File Creation
- File: File Modification
- File: File Deletion
- Driver: Driver Load
- Driver: Driver Metadata
- Network: Network Connection Creation
- Network: Network Traffic Flow
- Logon: Logon Session Creation
- Domain Name: Active DNS
- Command: Command Execution
- Windows Registery: Windows Registry Key Creation
- Windows Registery: Windows Registry Key Modification
- Windows Registery: Windows Registry Key Deletion
- User Account: User Account Authentication

## External References

- [SentinelOne Official Website](https://www.sentinelone.com/)
- [SentinelOne Resources](https://www.sentinelone.com/resources/)
- [SentinelOne Community](https://community.sentinelone.com/s)