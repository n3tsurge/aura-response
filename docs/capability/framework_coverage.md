# Framework Coverage Matrix

This matrix shows the coverage of capabilities across different frameworks by phases.

## Containment Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Patch Vulnerability (C3001)](containment/C3001.md) |  |  |  |
| [Block External IP Address (C3101)](containment/C3101.md) |  |  |  |
| [Block Internal IP Address (C3102)](containment/C3102.md) |  |  |  |
| [Block External Domain (C3103)](containment/C3103.md) |  |  |  |
| [Block Internal Domain (C3104)](containment/C3104.md) |  |  |  |
| [Block External URL (C3105)](containment/C3105.md) |  |  |  |
| [Block Internal URL (C3106)](containment/C3106.md) |  |  |  |
| [Block Port External Communication (C3107)](containment/C3107.md) |  |  |  |
| [Block Port Internal Communication (C3108)](containment/C3108.md) |  |  |  |

## Eradication Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Report Incident to External Entity (C4001)](eradication/C4001.md) |  |  |  |
| [Remove Rogue Network Device (C4101)](eradication/C4101.md) |  |  |  |
| [Delete Email Message (C4201)](eradication/C4201.md) |  |  |  |
| [Remove File (C4301)](eradication/C4301.md) |  |  |  |
| [Remove Registry Key (C4501)](eradication/C4501.md) |  |  |  |
| [Remove Service (C4502)](eradication/C4502.md) |  |  |  |
| [Revoke Authentication Credentials (C4601)](eradication/C4601.md) |  |  |  |
| [Remove User Account (C4602)](eradication/C4602.md) |  |  |  |

## Identification Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [List Alert Victims (C2001)](identification/C2001.md) |  | A.5.30, A.5.23, A.5.34, A.6.1, A.5.27, A.8.1, A.8.9 | DE.AE-1, DE.AE-2, DE.AE-3, DE.AE-5, RS.AN-1, RS.AN-2, RS.AN-3, RS.AN-4 |
| [List Host Vulnerabilities (C2002)](identification/C2002.md) |  | A.12.6.1, A.12.6.2 | PR.IP-8, DE.CM-8 |
| [Place Compromised Accounts on Watchlist (C2003)](identification/C2003.md) |  |  |  |
| [List Hosts Communicating with Internal Domain (C2101)](identification/C2101.md) |  |  |  |
| [List Hosts Communicating with Internal IP (C2102)](identification/C2102.md) |  |  |  |
| [List Hosts Communicating with Internal URL (C2103)](identification/C2103.md) |  |  |  |
| [Analyze Domain Name (C2104)](identification/C2104.md) |  |  |  |
| [Analyze IP Communication (C2105)](identification/C2105.md) |  |  |  |
| [Analyze URI Communication (C2106)](identification/C2106.md) |  |  |  |
| [List Hosts Communicating by Port (C2107)](identification/C2107.md) |  |  |  |
| [List Hosts Connected to VPN (C2108)](identification/C2108.md) |  |  |  |
| [List Hosts Connected to Intranet (C2109)](identification/C2109.md) |  |  |  |
| [List Data Transferred (C2110)](identification/C2110.md) |  |  |  |
| [Collect Transferred Data (C2111)](identification/C2111.md) |  |  |  |
| [List Hosts Communicating with External Domain (C2113)](identification/C2113.md) |  |  |  |
| [List Registry Key Modifications (C2501)](identification/C2501.md) |  | A.5.27, A.8.7, A.8.9, A.5.32, A.8.16 | DE.CM-1, DE.CM-7, RS.AN-1, RS.AN-2 |

## Lessons-learned Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Develop Incident Report (C6001)](lessons-learned/C6001.md) |  |  |  |
| [Conduct Lessons Learned Exercise (C6002)](lessons-learned/C6002.md) |  |  |  |

## Preparation Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Practice (C1001)](preparation/C1001.md) |  |  |  |
| [Training (C1002)](preparation/C1002.md) |  |  |  |
| [Personnel Awareness (C1003)](preparation/C1003.md) |  |  |  |
| [Personnel Reporting of Suspicious Activity (C1004)](preparation/C1004.md) |  |  |  |
| [Establish Relevant Data Collection (C1005)](preparation/C1005.md) |  |  |  |
| [Establish Centralized Long-term Log Storage (C1006)](preparation/C1006.md) |  |  |  |
| [Establish a Communication Map (C1007)](preparation/C1007.md) |  |  |  |
| [Ensure Backup Integrity (C1008)](preparation/C1008.md) |  |  |  |
| [Establish Access to Network/Architecture Diagrams (C1009)](preparation/C1009.md) |  |  |  |
| [Establish Access to Access Control Matrices (C1010)](preparation/C1010.md) |  |  |  |
| [Establish an Asset Knowledge Base (C1011)](preparation/C1011.md) |  |  |  |
| [Validate Analyst Toolset (C1012)](preparation/C1012.md) |  |  |  |
| [Access Vulnerability Management System Logs (C1013)](preparation/C1013.md) |  | A.5.10, A.5.12, A.5.14, A.5.23, A.5.30, A.8.8 | ID.RA-1, ID.RA-2, ID.RA-5, PR.IP-12, PR.MA-1, DE.CM-8, RS.IM-1 |
| [Connect with Trusted Communities (C1014)](preparation/C1014.md) |  |  |  |
| [Access External Flow Logs (C1101)](preparation/C1101.md) |  | A.5.7, A.8.16, A.5.23, A.5.28, A.5.30 | DE.CM-1, DE.CM-7, DE.AE-1, PR.PT-1 |
| [Access Internal Flow Logs (C1102)](preparation/C1102.md) |  | A.5.7, A.8.16, A.5.23, A.5.28, A.5.30 | DE.CM-1, DE.CM-7, DE.AE-1, PR.PT-1 |
| [Access Internal HTTP Logs (C1103)](preparation/C1103.md) |  | A.8.15 |  |
| [Access External HTTP Logs (C1104)](preparation/C1104.md) |  | A.8.15 |  |
| [Access Internal DNS Logs (C1105)](preparation/C1105.md) |  | A.5.7, A.5.23, A.5.30, A.5.28 | DE.CM-1, DE.CM-3, PR.PT-1, RS.AN-1 |
| [Access External DNS Logs (C1106)](preparation/C1106.md) |  | A.5.7, A.5.23, A.5.30, A.5.28 | DE.CM-1, DE.CM-3, PR.PT-1, RS.AN-1 |
| [Access VPN Logs (C1107)](preparation/C1107.md) |  | A.5.15, A.5.17, A.5.18, A.5.23, A.5.30 | PR.AC-1, PR.AC-3, PR.PT-1, DE.CM-1, DE.CM-3, DE.CM-7, RS.AN-1 |
| [Access DHCP Logs (C1108)](preparation/C1108.md) |  | A.5.9, A.5.10, A.5.23, A.5.30, A.5.28 | ID.AM-1, ID.AM-2, PR.PT-1, PR.AC-3, DE.CM-1, DE.CM-7 |
| [Access Internal Packet Capture Data (C1109)](preparation/C1109.md) |  |  |  |
| [Access External Packet Capture Data (C1109)](preparation/C1109.md) |  |  |  |

## Recovery Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Reinstall Host from Golden Image (C5001)](recovery/C5001.md) |  |  |  |
| [Restore Data from Backup (C5002)](recovery/C5002.md) |  |  |  |
| [Unblock Blocked IP (C5101)](recovery/C5101.md) |  |  |  |
| [Unblock Blocked Domain (C5102)](recovery/C5102.md) |  |  |  |
| [Unblock Blocked URL (C5103)](recovery/C5103.md) |  |  |  |
| [Unblock Blocked Port (C5104)](recovery/C5104.md) |  |  |  |
| [Unblock Blocked Port (C5105)](recovery/C5105.md) |  |  |  |
| [Unblock Domain on Email (C5201)](recovery/C5201.md) |  |  |  |
| [Unblock Sender on Email (C5202)](recovery/C5202.md) |  |  |  |
| [Restore Quarantined Email Message (C5203)](recovery/C5203.md) |  |  |  |
| [Restore Quarantined File (C5203)](recovery/C5203.md) |  |  |  |
| [Unblock Blocked Process (C5401)](recovery/C5401.md) |  |  |  |
| [Enable Disabled Service (C5501)](recovery/C5501.md) |  |  |  |
| [Unlock Locked User Account (C5601)](recovery/C5601.md) |  |  |  |