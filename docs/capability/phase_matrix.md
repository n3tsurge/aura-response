# Capability Phase Matrix

This matrix shows the capabilities grouped by their response phase.

Containment | Eradication | Identification | Lessons learned | Preparation | Recovery |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [Patch Vulnerability (C3001)](containment/C3001.md) | [Report Incident to External Entity (C4001)](eradication/C4001.md) | [List Alert Victims (C2001)](identification/C2001.md) | [Develop Incident Report (C6001)](lessons learned/C6001.md) | [Access Vulnerability Management System Logs (C1013)](preparation/C1013.md) | [Reinstall Host from Golden Image (C5001)](recovery/C5001.md) |
| [Block External IP Address (C3101)](containment/C3101.md) | [Remove Rogue Network Device (C4101)](eradication/C4101.md) | [List Host Vulnerabilities (C2002)](identification/C2002.md) | [Conduct Lessons Learned Exercise (C6002)](lessons learned/C6002.md) | [Access External Flow Logs (C1101)](preparation/C1101.md) | [Restore Data from Backup (C5002)](recovery/C5002.md) |
| [Block Internal IP Address (C3102)](containment/C3102.md) | [Delete Email Message (C4201)](eradication/C4201.md) | [Place Compromised Accounts on Watchlist (C2003)](identification/C2003.md) |  | [Access Internal Flow Logs (C1102)](preparation/C1102.md) | [Unblock Blocked IP (C5101)](recovery/C5101.md) |
| [Block External Domain (C3103)](containment/C3103.md) | [Remove File (C4301)](eradication/C4301.md) | [List Hosts Communicating with Internal Domain (C2101)](identification/C2101.md) |  | [Access Internal HTTP Logs (C1103)](preparation/C1103.md) | [Unblock Blocked Domain (C5102)](recovery/C5102.md) |
| [Block Internal Domain (C3104)](containment/C3104.md) | [Remove Registry Key (C4501)](eradication/C4501.md) | [List Hosts Communicating with Internal IP (C2102)](identification/C2102.md) |  | [Access External HTTP Logs (C1104)](preparation/C1104.md) | [Unblock Blocked URL (C5103)](recovery/C5103.md) |
| [Block External URL (C3105)](containment/C3105.md) | [Remove Service (C4502)](eradication/C4502.md) | [List Hosts Communicating with Internal URL (C2103)](identification/C2103.md) |  | [Access Internal DNS Logs (C1105)](preparation/C1105.md) | [Unblock Blocked Port (C5104)](recovery/C5104.md) |
| [Block Internal URL (C3106)](containment/C3106.md) | [Revoke Authentication Credentials (C4601)](eradication/C4601.md) | [Analyze Domain Name (C2104)](identification/C2104.md) |  | [Access External DNS Logs (C1106)](preparation/C1106.md) | [Unblock Blocked Port (C5105)](recovery/C5105.md) |
| [Block Port External Communication (C3107)](containment/C3107.md) | [Remove User Account (C4602)](eradication/C4602.md) | [Analyze IP Communication (C2105)](identification/C2105.md) |  | [Access VPN Logs (C1107)](preparation/C1107.md) | [Unblock Domain on Email (C5201)](recovery/C5201.md) |
| [Block Port Internal Communication (C3108)](containment/C3108.md) |  | [Analyze URI Communication (C2106)](identification/C2106.md) |  | [Access DHCP Logs (C1108)](preparation/C1108.md) | [Unblock Sender on Email (C5202)](recovery/C5202.md) |
|  |  | [List Hosts Communicating by Port (C2107)](identification/C2107.md) |  | [Access Internal Packet Capture Data (C1109)](preparation/C1109.md) | [Restore Quarantined Email Message (C5203)](recovery/C5203.md) |
|  |  | [List Hosts Connected to VPN (C2108)](identification/C2108.md) |  | [Access External Packet Capture Data (C1109)](preparation/C1109.md) | [Restore Quarantined File (C5203)](recovery/C5203.md) |
|  |  | [List Hosts Connected to Intranet (C2109)](identification/C2109.md) |  |  | [Unblock Blocked Process (C5401)](recovery/C5401.md) |
|  |  | [List Data Transferred (C2110)](identification/C2110.md) |  |  | [Enable Disabled Service (C5501)](recovery/C5501.md) |
|  |  | [Collect Transferred Data (C2111)](identification/C2111.md) |  |  | [Unlock Locked User Account (C5601)](recovery/C5601.md) |
|  |  | [List Hosts Communicating with External Domain (C2113)](identification/C2113.md) |  |  |  |
|  |  | [List Registry Key Modifications (C2501)](identification/C2501.md) |  |  |  |