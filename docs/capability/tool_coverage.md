# Tool Coverage Matrix

This matrix shows the coverage of capabilities across different tools. A CSV representation of this matrix can be found here [tool_coverage.csv](../../files/tool_coverage.csv).

| Capability | Phase | [Cisco Firewall (ASA/NGFW)](../tool/cisco-fw/index.md) | [Guardicore](../tool/guardicore/index.md) | [Okta](../tool/okta/index.md) | [Palo Alto Firewall](../tool/palo-alto-fw/index.md) | [Proofpoint](../tool/proofpoint/index.md) | [Rapid7 InsightVM](../tool/rapid7-insightvm/index.md) | [SentinelOne](../tool/sentinelone/index.md) | [Wiz.io](../tool/wiz/index.md) | [Zscaler Internet Access (ZIA)](../tool/zscaler-zia/index.md) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Patch Vulnerability (C3001)](containment/C3001.md) | Containment |  |  |  |  |  |  |  |  |  |
| [Block External IP Address (C3101)](containment/C3101.md) | Containment | [:white_check_mark:](../tool/cisco-fw/C3101.md) | [:white_check_mark:](../tool/guardicore/C3101.md) |  | [:white_check_mark:](../tool/palo-alto-fw/C3101.md) |  |  | [:white_check_mark:](../tool/sentinelone/C3101.md) |  | [:white_check_mark:](../tool/zscaler-zia/C3101.md) |
| [Block Internal IP Address (C3102)](containment/C3102.md) | Containment | [:white_check_mark:](../tool/cisco-fw/C3102.md) | [:white_check_mark:](../tool/guardicore/C3102.md) |  | [:white_check_mark:](../tool/palo-alto-fw/C3102.md) |  |  | [:white_check_mark:](../tool/sentinelone/C3102.md) |  |  |
| [Block External Domain (C3103)](containment/C3103.md) | Containment |  |  |  |  |  |  |  |  |  |
| [Block Internal Domain (C3104)](containment/C3104.md) | Containment |  |  |  |  |  |  |  |  |  |
| [Block External URL (C3105)](containment/C3105.md) | Containment |  |  |  |  |  |  |  |  |  |
| [Block Internal URL (C3106)](containment/C3106.md) | Containment |  |  |  |  |  |  |  |  |  |
| [Block Port External Communication (C3107)](containment/C3107.md) | Containment | [:white_check_mark:](../tool/cisco-fw/C3107.md) | [:white_check_mark:](../tool/guardicore/C3107.md) |  | [:white_check_mark:](../tool/palo-alto-fw/C3107.md) |  |  | [:white_check_mark:](../tool/sentinelone/C3107.md) |  | [:white_check_mark:](../tool/zscaler-zia/C3107.md) |
| [Block Port Internal Communication (C3108)](containment/C3108.md) | Containment | [:white_check_mark:](../tool/cisco-fw/C3108.md) | [:white_check_mark:](../tool/guardicore/C3108.md) |  | [:white_check_mark:](../tool/palo-alto-fw/C3108.md) |  |  | [:white_check_mark:](../tool/sentinelone/C3108.md) |  |  |
| [Report Incident to External Entity (C4001)](eradication/C4001.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove Rogue Network Device (C4101)](eradication/C4101.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Delete Email Message (C4201)](eradication/C4201.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove File (C4301)](eradication/C4301.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove Registry Key (C4501)](eradication/C4501.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Remove Service (C4502)](eradication/C4502.md) | Eradication |  |  |  |  |  |  |  |  |  |
| [Revoke Authentication Credentials (C4601)](eradication/C4601.md) | Eradication |  |  | [:white_check_mark:](../tool/okta/C4601.md) |  |  |  |  |  |  |
| [Remove User Account (C4602)](eradication/C4602.md) | Eradication |  |  | [:white_check_mark:](../tool/okta/C4602.md) |  |  |  |  |  |  |
| [List Alert Victims (C2001)](identification/C2001.md) | Identification |  |  |  |  |  |  | [:white_check_mark:](../tool/sentinelone/C2001.md) |  |  |
| [List Host Vulnerabilities (C2002)](identification/C2002.md) | Identification |  |  |  |  |  | [:white_check_mark:](../tool/rapid7-insightvm/C2002.md) | [:white_check_mark:](../tool/sentinelone/C2002.md) | [:white_check_mark:](../tool/wiz/C2002.md) |  |
| [List Registry Key Modifications (C2501)](identification/C2501.md) | Identification |  |  |  |  |  |  | [:white_check_mark:](../tool/sentinelone/C2501.md) |  |  |
| [Access Vulnerability Management System Logs (C1013)](preparation/C1013.md) | Preparation |  |  |  |  |  | [:white_check_mark:](../tool/rapid7-insightvm/C1013.md) | [:white_check_mark:](../tool/sentinelone/C1013.md) |  |  |
| [Access External Flow Logs (C1101)](preparation/C1101.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1101.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1101.md) |  |  |  |  |  |
| [Access Internal Flow Logs (C1102)](preparation/C1102.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1102.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1102.md) |  |  |  |  |  |
| [Access Internal HTTP Logs (C1103)](preparation/C1103.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1103.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1103.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1103.md) |  |  |
| [Access External HTTP Logs (C1104)](preparation/C1104.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1104.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1104.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1104.md) |  | [:white_check_mark:](../tool/zscaler-zia/C1104.md) |
| [Access Internal DNS Logs (C1105)](preparation/C1105.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1105.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1105.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1105.md) |  |  |
| [Access External DNS Logs (C1106)](preparation/C1106.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1106.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1106.md) |  |  | [:white_check_mark:](../tool/sentinelone/C1106.md) |  | [:white_check_mark:](../tool/zscaler-zia/C1106.md) |
| [Access VPN Logs (C1107)](preparation/C1107.md) | Preparation |  |  |  |  |  |  |  |  |  |
| [Access DHCP Logs (C1108)](preparation/C1108.md) | Preparation |  |  |  |  |  |  |  |  |  |
| [Access Internal Packet Capture Data (C1109)](preparation/C1109.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1109.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1109.md) |  |  |  |  |  |
| [Access External Packet Capture Data (C1109)](preparation/C1109.md) | Preparation | [:white_check_mark:](../tool/cisco-fw/C1109.md) |  |  | [:white_check_mark:](../tool/palo-alto-fw/C1109.md) |  |  |  |  |  |
| [Reinstall Host from Golden Image (C5001)](recovery/C5001.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Restore Data from Backup (C5002)](recovery/C5002.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked IP (C5101)](recovery/C5101.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked Domain (C5102)](recovery/C5102.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked URL (C5103)](recovery/C5103.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked Port (C5104)](recovery/C5104.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Blocked Port (C5105)](recovery/C5105.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unblock Domain on Email (C5201)](recovery/C5201.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5201.md) |  |  |  |  |
| [Unblock Sender on Email (C5202)](recovery/C5202.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5202.md) |  |  |  |  |
| [Restore Quarantined Email Message (C5203)](recovery/C5203.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5203.md) |  |  |  |  |
| [Restore Quarantined File (C5203)](recovery/C5203.md) | Recovery |  |  |  |  | [:white_check_mark:](../tool/proofpoint/C5203.md) |  |  |  |  |
| [Unblock Blocked Process (C5401)](recovery/C5401.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Enable Disabled Service (C5501)](recovery/C5501.md) | Recovery |  |  |  |  |  |  |  |  |  |
| [Unlock Locked User Account (C5601)](recovery/C5601.md) | Recovery |  |  | [:white_check_mark:](../tool/okta/C5601.md) |  |  |  |  |  |  |