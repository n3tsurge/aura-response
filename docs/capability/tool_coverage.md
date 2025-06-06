# Tool Coverage Matrix

This matrix shows the coverage of capabilities across different tools.

| Capability | Phase | [Cisco Firewall (ASA/NGFW)](../tool/cisco-fw/index.md) | [Guardicore](../tool/guardicore/index.md) | [Okta](../tool/okta/index.md) | [Palo Alto Firewall](../tool/palo-alto-fw/index.md) | [Proofpoint](../tool/proofpoint/index.md) | [Rapid7 InsightVM](../tool/rapid7-insightvm/index.md) | [SentinelOne](../tool/sentinelone/index.md) | [Wiz.io](../tool/wiz/index.md) | [Zscaler Internet Access (ZIA)](../tool/zscaler-zia/index.md) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Access Vulnerability Management System Logs (C1013)](C1013.md) | Preparation |  |  |  |  |  | [:white_check_mark:](../tool/rapid7-insightvm/C1013.md) | [:white_check_mark:](../tool/sentinelone/C1013.md) |  |  |
| [Access External Flow Logs (C1101)](C1101.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1101.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1101.md) |  |  |  |  |  |
| [Access Internal Flow Logs (C1102)](C1102.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1102.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1102.md) |  |  |  |  |  |
| [Access Internal HTTP Logs (C1103)](C1103.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1103.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1103.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1103.md) |  |  |
| [Access External HTTP Logs (C1104)](C1104.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1104.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1104.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1104.md) |  | [:white_check_mark:](../tool/zscaler-zia/C1104.md) |
| [Access Internal DNS Logs (C1105)](C1105.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1105.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1105.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1105.md) |  |  |
| [Access External DNS Logs (C1106)](C1106.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1106.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1106.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1106.md) |  | [:white_check_mark:](../tool/zscaler-zia/C1106.md) |
| [Access VPN Logs (C1107)](C1107.md) | Preparation |  |  |  |  |  |  |  |  |  |
| [Access DHCP Logs (C1108)](C1108.md) | Preparation |  |  |  |  |  |  |  |  |  |
| [Access Internal Packet Capture Data (C1109)](C1109.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1109.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1109.md) |  |  |  |  |  |
| [Access External Packet Capture Data (C1109)](C1109.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1109.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1109.md) |  |  |  |  |  |
| [List Alert Victims (C2001)](C2001.md) | Identification |  |  |  |  |  |  | [:white_check_mark:](../tool/sentinelone/C2001.md) |  |  |
| [List Host Vulnerabilities (C2002)](C2002.md) | Identification |  |  |  |  |  | [:white_check_mark:](../tool/rapid7-insightvm/C2002.md) | [:white_check_mark:](../tool/sentinelone/C2002.md) | [:white_check_mark:](../tool/wiz/C2002.md) |  |
| [List Registry Key Modifications (C2501)](C2501.md) | Identification |  |  |  |  |  |  | [:white_check_mark:](../tool/sentinelone/C2501.md) |  |  |
| [Report Incident to External Entity (C4001)](C4001.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove Rogue Network Device (C4101)](C4101.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Delete Email Message (C4201)](C4201.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove File (C4301)](C4301.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove Registry Key (C4501)](C4501.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove Service (C4502)](C4502.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Revoke Authentication Credentials (C4601)](C4601.md) | Eradication |  |  | [:white_check_mark:](../tool/okta/C4601.md) |  |  |  |  |  |  |
| [Remove User Account (C4602)](C4602.md) | Eradication |  |  | [:white_check_mark:](../tool/okta/C4602.md) |  |  |  |  |  |  |
| [Reinstall Host from Golden Image (C5001)](C5001.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Restore Data from Backup (C5002)](C5002.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked IP (C5101)](C5101.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked Domain (C5102)](C5102.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked URL (C5103)](C5103.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked Port (C5104)](C5104.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked Port (C5105)](C5105.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Domain on Email (C5201)](C5201.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5201.md) |  |  |  |  |
| [Unblock Sender on Email (C5202)](C5202.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5202.md) |  |  |  |  |
| [Restore Quarantined Email Message (C5203)](C5203.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5203.md) |  |  |  |  |
| [Restore Quarantined File (C5203)](C5203.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5203.md) |  |  |  |  |
| [Unblock Blocked Process (C5401)](C5401.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Enable Disabled Service (C5501)](C5501.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unlock Locked User Account (C5601)](C5601.md) | Recovery |  |  | [:white_check_mark:](../tool/okta/C5601.md) |  |  |  |  |  |  |