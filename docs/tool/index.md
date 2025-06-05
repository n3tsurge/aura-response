# Tool

| Tool | Category | ID | Description |
|------|----------|----|-------------|
| [Cisco Firewall (ASA/NGFW)](../tool/T0007.md) | network monitoring | T0007 | Cisco Firewall (ASA/NGFW) is a family of network security devices that provide advanced threat protection and secure access control. It is designed to protect networks from unauthorized access, malware, and other cyber threats. The firewall offers features such as stateful inspection, VPN support, intrusion prevention, and application visibility, making it an essential tool for maintaining network security and compliance. |
| [Guardicore](../tool/T0003.md) | microsegmentation, network security | T0003 | Guardicore is a micro-segmentation and data center security solution that provides visibility and control over network traffic. It helps organizations to protect their critical assets by segmenting their networks, monitoring traffic patterns, and enforcing security policies. Guardicore's advanced threat detection capabilities enable rapid response to potential threats, ensuring that sensitive data remains secure while maintaining operational efficiency. |
| [Palo Alto Firewall](../tool/T0008.md) | network firewall | T0008 | Palo Alto Firewall is a next-generation firewall that provides advanced security features to protect networks from cyber threats. It offers capabilities such as application visibility and control, intrusion prevention, and threat intelligence integration. Palo Alto Firewalls are designed to secure both on-premises and cloud environments, making them a versatile solution for organizations looking to enhance their network security posture. |
| [Rapid7 InsightVM](../tool/T0004.md) | vulnerability management | T0004 | Rapid7 InsightVM is a vulnerability management solution that provides near real-time visibility into the security posture of an organization's IT environment. It helps identify, prioritize, and remediate vulnerabilities across networks, endpoints, and cloud environments. InsightVM offers advanced analytics, reporting capabilities, and integration with other security tools to enhance an organization's overall security strategy. Its continuous monitoring and assessment features enable proactive risk management and compliance with industry standards. |
| [SentinelOne - Access External HTTP Logs](../tool/T0001.C1104.md) |  | T0001.C1104 | This capability allows the tool to access external HTTP logs, which can be crucial for identifying and analyzing security incidents. By examining these logs, security teams can gain insights into potential threats, track user activities, and understand the context of events that may indicate a security breach.

## Workflow

External HTTP logs can be accessed through the SentinelOne Event Search page in the user interface. The following steps outline the process:

1. **Navigate to the Event Search Page**: Open the SentinelOne console and go to the Event Search section.
2. **Search for Events**: Use the search functionality to filter events based on criteria such as `url.address` or `event.url.action`.
3. **Review Results**: Analyze the search results to identify relevant events that may indicate security incidents or user activities of interest.
4. **Export Data**: If necessary, export the search results for further analysis or reporting.

This capability is essential for security analysts and incident responders to monitor and investigate web-related activities within the network. |
| [SentinelOne - List Alert Victims](../tool/T0001.C2001.md) |  | T0001.C2001 | This tool capability allows stakeholders to list all victims affected by the incident using SentinelOne. It provides a comprehensive overview of those impacted, enabling better resource allocation and response planning.

### How to List Alert Victims via SentinelOne Console (GUI)

1. **Log into the SentinelOne Management Console.**
2. Navigate to the **'Incidents'** or **'Threats'** tab depending on how your console is configured.
3. Apply relevant **filters** such as date range, threat type, severity, or site.
4. Click on an individual incident or alert to open its detail view.
5. Within the detail pane, locate the **'Affected Endpoints'**, **'Agent'**, or **'User'** sections. These contain victim information:
   - `Machine Name`
   - `Username`
   - `Group Name` or `Site`
6. Use the **'Export'** button (top-right) to download the full victim list as a CSV if needed.
7. Optionally, use the **'Comment'** or **'Tag'** features to track and annotate victim systems.

This method enables quick identification of affected assets directly within the SentinelOne UI. |
| [SentinelOne - List Registry Key Modifications](../tool/T0001.C2501.md) |  | T0001.C2501 | This tool capability enables security analysts and incident responders to identify registry key modifications using SentinelOne. Registry changes are common indicators of persistence, privilege escalation, or configuration tampering. # Workflow

## Searching within SentinelOne EDR/XDR

The below query will identify all registry key modifictions per host and source process. When it is necessary, filtering the logs for a specific host is possible by adding `| filter endpoint.name == "HOSTNAMEHERE"` before the `group` clause.

```php

event.type in ('Registry Value Modified')

| group count=count() by endpoint.name,registry.keyPath,src.process.image.path

```

 |
| [SentinelOne](../tool/T0001.md) | EDR, EPP, XDR | T0001 | SentinelOne is an advanced endpoint protection platform that uses AI to detect, prevent, and respond to cyber threats in real-time. It provides comprehensive security for endpoints, including threat intelligence, automated response capabilities, and detailed analytics to help organizations protect their systems from sophisticated attacks. |
| [Statseeker](../tool/T0006.md) | network monitoring | T0006 | Statseeker is a network monitoring tool that provides real-time visibility into network performance and health. It helps organizations to monitor their network infrastructure, identify issues, and optimize performance. Statseeker's capabilities include network traffic analysis, device monitoring, and alerting, making it a valuable tool for maintaining network reliability and efficiency. |
| [Wiz.io](../tool/T0005.md) | cloud security, vulnerability management, compliance | T0005 | Wiz.io is a cloud security platform that provides comprehensive visibility and security for cloud environments. It helps organizations to identify and remediate vulnerabilities, misconfigurations, and compliance issues across their cloud infrastructure. Wiz.io's advanced threat detection capabilities enable proactive security measures, ensuring that cloud resources are protected against potential threats while maintaining operational efficiency. |
| [Zscaler Internet Access (ZIA)](../tool/T0002.md) | SaaS, Web Security, Cloud Security | T0002 | Zscaler Internet Access (ZIA) is a cloud-based security platform that provides secure internet access for users, regardless of their location. It offers comprehensive protection against web threats, data loss, and malicious content by inspecting all traffic in real-time. ZIA enables organizations to enforce security policies, control access to applications, and ensure compliance with regulatory requirements, all while delivering a seamless user experience. |