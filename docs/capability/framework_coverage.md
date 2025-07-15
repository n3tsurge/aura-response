# Framework Coverage Matrix

This matrix shows the coverage of capabilities across different frameworks by phases.

## Containment Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Patch Vulnerability (C3001)](containment/C3001.md) |  | A.12.6.1, A.8.2.3, A.5.37, A.16.1.5 | PR.IP-12, PR.MA-1, ID.RA-1 |
| [Block External IP Address (C3101)](containment/C3101.md) |  | A.13.1.1, A.13.1.2, A.16.1.5, A.12.4.1 | PR.AC-4, PR.PT-4, DE.CM-1, RS.IM-1 |
| [Block Internal IP Address (C3102)](containment/C3102.md) |  | A.13.1.1, A.13.1.2, A.16.1.5, A.12.4.1 | PR.AC-4, PR.PT-4, DE.CM-1, RS.IM-1 |
| [Block External Domain (C3103)](containment/C3103.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Internal Domain (C3104)](containment/C3104.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block External URL (C3105)](containment/C3105.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Internal URL (C3106)](containment/C3106.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Port External Communication (C3107)](containment/C3107.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.13.2.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Port Internal Communication (C3108)](containment/C3108.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.13.2.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block User External Communication (C3109)](containment/C3109.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block User Internal Communication (C3110)](containment/C3110.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Data Transfer by Content Pattern (C3111)](containment/C3111.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Email Domain (C3201)](containment/C3201.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Email Sender (C3202)](containment/C3202.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Email Sender (C3203)](containment/C3203.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Quarantine File by Format (C3301)](containment/C3301.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Quarantine File by Hash (C3302)](containment/C3302.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Quarantine File by Path (C3303)](containment/C3303.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Quarantine File by Content Pattern (C3304)](containment/C3304.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Block Process by Path (C3401)](containment/C3401.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Process by Metadata (C3402)](containment/C3402.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Block Process by Format (C3403)](containment/C3403.md) |  | A.8.22, A.8.3, A.5.23, A.8.16 | PR.AC-4, PR.PT-3, DE.CM-1, RS.IM-1 |
| [Block Process by Hash (C3404)](containment/C3404.md) |  | A.8.22, A.8.3, A.5.23, A.8.16 | PR.AC-4, PR.PT-3, DE.CM-1, RS.IM-1 |
| [Block Process by Content Pattern (C3405)](containment/C3405.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Disable System Service (C3501)](containment/C3501.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Block Access to IO Port (C3502)](containment/C3502.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.13.2.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Lock User Account (C3601)](containment/C3601.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Remove User Permission (C3602)](containment/C3602.md) |  | A.9.1.1, A.9.1.2, A.9.2.1, A.9.4.1 | PR.AC-1, PR.AC-6, PR.AC-7, ID.AM-3 |

## Eradication Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Report Incident to External Entity (C4001)](eradication/C4001.md) |  | A.16.1.2, A.16.1.3, A.5.29, A.7.4 | RS.CO-1, RS.CO-2, RS.CO-3, PR.IP-9 |
| [Remove Rogue Network Device (C4101)](eradication/C4101.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Delete Email Message (C4201)](eradication/C4201.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Remove File (C4301)](eradication/C4301.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Remove Registry Key (C4501)](eradication/C4501.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Remove Service (C4502)](eradication/C4502.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Revoke Authentication Credentials (C4601)](eradication/C4601.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Remove User Account (C4602)](eradication/C4602.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |

## Identification Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [List Alert Victims (C2001)](identification/C2001.md) |  | A.16.1.2, A.16.1.3, A.5.29, A.7.4 | RS.CO-1, RS.CO-2, RS.CO-3, PR.IP-9 |
| [List Host Vulnerabilities (C2002)](identification/C2002.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Place Compromised Accounts on Watchlist (C2003)](identification/C2003.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [List Hosts Communicating with Internal Domain (C2101)](identification/C2101.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Hosts Communicating with Internal IP (C2102)](identification/C2102.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Hosts Communicating with Internal URL (C2103)](identification/C2103.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Analyze Domain Name (C2104)](identification/C2104.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Analyze IP Communication (C2105)](identification/C2105.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Analyze URI Communication (C2106)](identification/C2106.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [List Hosts Communicating by Port (C2107)](identification/C2107.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Hosts Connected to VPN (C2108)](identification/C2108.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Hosts Connected to Intranet (C2109)](identification/C2109.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Data Transferred (C2110)](identification/C2110.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Collect Transferred Data (C2111)](identification/C2111.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Identify Transferred Data (C2112)](identification/C2112.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Hosts Communicating with External Domain (C2113)](identification/C2113.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Hosts Communicating with External IP (C2114)](identification/C2114.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [List Hosts Communicating with External URL (C2115)](identification/C2115.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Find Data Transferred by Content Pattern (C2116)](identification/C2116.md) |  | A.8.2.1, A.8.3.1, A.8.3.2, A.11.1.4 | PR.DS-1, PR.DS-3, PR.IP-4, RC.RP-1 |
| [List Email Openers (C2201)](identification/C2201.md) |  | A.12.2.1, A.12.6.1, A.16.1.7 | ID.AM-5, ID.RA-1, DE.CM-1 |
| [List Email Recipients (C2203)](identification/C2203.md) |  | A.12.2.1, A.12.6.1, A.16.1.7 | ID.AM-5, ID.RA-1, DE.CM-1 |
| [Verify Phishing Email (C2204)](identification/C2204.md) |  | A.12.2.1, A.12.6.1, A.16.1.5 | ID.RA-2, DE.AE-2, DE.CM-1 |
| [Extract Email Observables (C2205)](identification/C2205.md) |  | A.12.6.1, A.16.1.5, A.16.1.7 | ID.RA-2, DE.AE-2, DE.CM-4 |
| [Analyze JAR Files (C2319)](identification/C2319.md) |  | A.12.6.1, A.14.2.1, A.16.1.5 | DE.AE-2, DE.CM-4, RS.AN-3 |
| [Analyze Filenames (C2320)](identification/C2320.md) |  | A.12.6.1, A.14.2.1, A.16.1.5 | DE.AE-2, DE.CM-1, ID.RA-2 |
| [List Registry Key Modifications (C2501)](identification/C2501.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [List Registry Keys Deleted (C2502)](identification/C2502.md) |  | A.12.4.1, A.12.6.1, A.16.1.4 | DE.CM-1, DE.CM-7, DE.AE-2 |
| [List Registry Keys Accessed (C2503)](identification/C2503.md) |  | A.12.4.1, A.12.6.1, A.16.1.4 | DE.CM-1, DE.CM-7, ID.AM-3 |
| [List Registry Keys Created (C2504)](identification/C2504.md) |  | A.12.4.1, A.12.6.1, A.16.1.4 | DE.CM-1, DE.CM-7, DE.AE-2 |
| [List Services Created (C2505)](identification/C2505.md) |  | A.12.4.1, A.12.6.1, A.16.1.4 | DE.CM-1, DE.CM-7, DE.AE-2 |
| [List Services Modified (C2506)](identification/C2506.md) |  | A.12.4.1, A.12.6.1, A.16.1.4 | DE.CM-1, DE.CM-7, DE.AE-3 |
| [List Services Deleted (C2507)](identification/C2507.md) |  | A.12.4.1, A.12.6.1, A.16.1.4 | DE.CM-1, DE.CM-7, DE.AE-2 |
| [Analyze Registry Key (C2508)](identification/C2508.md) |  | A.12.6.1, A.16.1.4, A.16.1.5 | DE.AE-2, DE.CM-4, RS.AN-3 |
| [List Authenticated Users (C2601)](identification/C2601.md) |  | A.9.2.1, A.9.2.6, A.12.4.1 | DE.CM-1, DE.CM-3, ID.AM-5 |
| [List User Accounts (C2602)](identification/C2602.md) |  | A.9.2.1, A.9.2.2, A.9.2.5 | ID.AM-5, PR.AC-1, DE.CM-3 |

## Lessons-learned Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Develop Incident Report (C6001)](lessons-learned/C6001.md) |  | A.16.1.2, A.16.1.3, A.5.29, A.7.4 | RS.CO-1, RS.CO-2, RS.CO-3, PR.IP-9 |
| [Conduct Lessons Learned Exercise (C6002)](lessons-learned/C6002.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |

## Operations Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Define Key Performance Indicators (KPIs) (C7001)](operations/C7001.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Maintain a Risk Register (C7002)](operations/C7002.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Maintain a Team Knowledge Base (C7003)](operations/C7003.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Maintain Leadership Reporting and Awareness (C7004)](operations/C7004.md) |  | A.16.1.2, A.16.1.3, A.5.29, A.7.4 | RS.CO-1, RS.CO-2, RS.CO-3, PR.IP-9 |

## Preparation Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Practice (C1001)](preparation/C1001.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Training (C1002)](preparation/C1002.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Personnel Awareness (C1003)](preparation/C1003.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Personnel Reporting of Suspicious Activity (C1004)](preparation/C1004.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Relevant Data Collection (C1005)](preparation/C1005.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Centralized Long-term Log Storage (C1006)](preparation/C1006.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Establish a Communication Map (C1007)](preparation/C1007.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Ensure Backup Integrity (C1008)](preparation/C1008.md) |  | A.8.2.1, A.8.3.1, A.8.3.2, A.11.1.4 | PR.DS-1, PR.DS-3, PR.IP-4, RC.RP-1 |
| [Establish Access to Network/Architecture Diagrams (C1009)](preparation/C1009.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Access to Access Control Matrices (C1010)](preparation/C1010.md) |  | A.9.1.1, A.9.1.2, A.9.2.1, A.9.4.1 | PR.AC-1, PR.AC-6, PR.AC-7, ID.AM-3 |
| [Establish an Asset Knowledge Base (C1011)](preparation/C1011.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Validate Analyst Toolset (C1012)](preparation/C1012.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Access Vulnerability Management System Logs (C1013)](preparation/C1013.md) |  | A.12.4.1, A.12.4.2, A.12.4.3, A.16.1.7 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Connect with Trusted Communities (C1014)](preparation/C1014.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Access External Flow Logs (C1101)](preparation/C1101.md) |  | A.12.4.1, A.12.4.2, A.12.4.3, A.16.1.7 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access Internal Flow Logs (C1102)](preparation/C1102.md) |  | A.12.4.1, A.12.4.2, A.12.4.3, A.16.1.7 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access Internal HTTP Logs (C1103)](preparation/C1103.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access External HTTP Logs (C1104)](preparation/C1104.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access Internal DNS Logs (C1105)](preparation/C1105.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access External DNS Logs (C1106)](preparation/C1106.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access VPN Logs (C1107)](preparation/C1107.md) |  | A.12.4.1, A.12.4.2, A.12.4.3, A.16.1.7 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access DHCP Logs (C1108)](preparation/C1108.md) |  | A.12.4.1, A.12.4.2, A.12.4.3, A.16.1.7 | DE.CM-1, DE.AE-3, PR.PT-1, RS.AN-1 |
| [Access Internal Packet Capture Data (C1109)](preparation/C1109.md) |  | A.9.1.1, A.9.1.2, A.9.2.1, A.9.4.1 | PR.AC-1, PR.AC-6, PR.AC-7, ID.AM-3 |
| [Access External Packet Capture Data (C1109)](preparation/C1109.md) |  | A.9.1.1, A.9.1.2, A.9.2.1, A.9.4.1 | PR.AC-1, PR.AC-6, PR.AC-7, ID.AM-3 |
| [Establish Ability to Block External IP Addresses (C1111)](preparation/C1111.md) |  | A.13.1.1, A.13.1.2, A.16.1.5, A.12.4.1 | PR.AC-4, PR.PT-4, DE.CM-1, RS.IM-1 |
| [Establish Ability to Block Internal IP Addresses (C1112)](preparation/C1112.md) |  | A.13.1.1, A.13.1.2, A.16.1.5, A.12.4.1 | PR.AC-4, PR.PT-4, DE.CM-1, RS.IM-1 |
| [Establish Ability to Block External Domains (C1113)](preparation/C1113.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Internal Domains (C1114)](preparation/C1114.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block External URLs (C1115)](preparation/C1115.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Internal URLs (C1116)](preparation/C1116.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block External Ports (C1117)](preparation/C1117.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.13.2.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Internal Ports (C1118)](preparation/C1118.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.13.2.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block User External Communication (C1119)](preparation/C1119.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block User Internal Communication (C1120)](preparation/C1120.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Find Transferred Data by Content Pattern (C1121)](preparation/C1121.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Block Transferred Data by Content Pattern (C1122)](preparation/C1122.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to List Data Transferred (C1123)](preparation/C1123.md) |  | A.8.2.1, A.8.3.1, A.8.3.2, A.11.1.4 | PR.DS-1, PR.DS-3, PR.IP-4, RC.RP-1 |
| [Establish Ability to Collect Data Transferred (C1124)](preparation/C1124.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Identify Data Transferred (C1125)](preparation/C1125.md) |  | A.8.2.1, A.8.3.1, A.8.3.2, A.11.1.4 | PR.DS-1, PR.DS-3, PR.IP-4, RC.RP-1 |
| [Establish Ability to Analyze User Agent (C1127)](preparation/C1127.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to List Firewall Rules (C1128)](preparation/C1128.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Users' Email Interaction (C1201)](preparation/C1201.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze User Agent (C1202)](preparation/C1202.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Block Email Domain (C1203)](preparation/C1203.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Email Sender (C1204)](preparation/C1204.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Delete Email Message (C1205)](preparation/C1205.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Quarantine Email Message (C1206)](preparation/C1206.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Establish Ability to Collect Email Messages (C1207)](preparation/C1207.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze Email Addresses (C1208)](preparation/C1208.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to List Files Created (C1301)](preparation/C1301.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Files Modified (C1302)](preparation/C1302.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Files Deleted (C1303)](preparation/C1303.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Files Downloaded (C1304)](preparation/C1304.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Files with Modified Timestamps (C1305)](preparation/C1305.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Find File by Path (C1306)](preparation/C1306.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Find File by Metadata (C1307)](preparation/C1307.md) |  | A.8.2.1, A.8.3.1, A.8.3.2, A.11.1.4 | PR.DS-1, PR.DS-3, PR.IP-4, RC.RP-1 |
| [Establish Ability to Find File by Metadata (C1308)](preparation/C1308.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Find File by Format (C1309)](preparation/C1309.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Find File by Content Pattern (C1310)](preparation/C1310.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Collect File (C1311)](preparation/C1311.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Quarantine File by Path (C1312)](preparation/C1312.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Establish Ability to Quarantine File by Hash (C1313)](preparation/C1313.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Establish Ability to Quarantine File by Format (C1314)](preparation/C1314.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Establish Ability to Quarantine File by Content Pattern (C1315)](preparation/C1315.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Establish Ability to Remove File (C1316)](preparation/C1316.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Analyze File Hash (C1317)](preparation/C1317.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze Windows PE (C1318)](preparation/C1318.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze macOS Mach-O (C1319)](preparation/C1319.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze Unix ELF (C1320)](preparation/C1320.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze Microsoft Office File (C1321)](preparation/C1321.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze PDF File (C1322)](preparation/C1322.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Analyze Scripts (C1323)](preparation/C1323.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to List Processes Executed (C1401)](preparation/C1401.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Find Processes by Path (C1402)](preparation/C1402.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Find Processes by Metadata (C1403)](preparation/C1403.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Find Processes by Hash (C1404)](preparation/C1404.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Find Processes by Fromat (C1405)](preparation/C1405.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Find Processes by Content Pattern (C1406)](preparation/C1406.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to Block Processes by Path (C1407)](preparation/C1407.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Processes by Metadata (C1408)](preparation/C1408.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Processes by Hash (C1409)](preparation/C1409.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Processes by Format (C1410)](preparation/C1410.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Establish Ability to Block Processes by Content Pattern (C1411)](preparation/C1411.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Manage Remote Computer System Policies (C1501)](preparation/C1501.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Registry Keys Modified (C1502)](preparation/C1502.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to List Registry Keys Deleted (C1503)](preparation/C1503.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to List Registry Keys Accessed (C1504)](preparation/C1504.md) |  | A.9.1.1, A.9.1.2, A.9.2.1, A.9.4.1 | PR.AC-1, PR.AC-6, PR.AC-7, ID.AM-3 |
| [Establish Ability to List Registry Keys Created (C1505)](preparation/C1505.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish Ability to List Services Created (C1506)](preparation/C1506.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Services Modified (C1507)](preparation/C1507.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Services Deleted (C1508)](preparation/C1508.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Remove Registry Key (C1509)](preparation/C1509.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Remove Service (C1510)](preparation/C1510.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Analyze Registry Key (C1512)](preparation/C1512.md) |  | A.12.4.1, A.12.2.1, A.16.1.1, A.12.6.1 | DE.CM-1, DE.CM-4, DE.AE-2, ID.RA-5 |
| [Establish ability to Manage Identity Management System (C1601)](preparation/C1601.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Lock User Account (C1602)](preparation/C1602.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List Authenticated Users (C1603)](preparation/C1603.md) |  | A.9.1.1, A.9.1.2, A.9.2.1, A.9.4.1 | PR.AC-1, PR.AC-6, PR.AC-7, ID.AM-3 |
| [Establish Ability to Revoke Auth Credentials (C1604)](preparation/C1604.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to Remove User Account (C1605)](preparation/C1605.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Establish Ability to List User Accounts (C1606)](preparation/C1606.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |

## Recovery Phase

| Capability | [MITRE ATT&CK](../frameworks/F0001.md) | [ISO/IEC 27001:2022](../frameworks/F0002.md) | [NIST CSF](../frameworks/F0003.md) |
| :--- | :--- | :--- | :--- |
| [Reinstall Host from Golden Image (C5001)](recovery/C5001.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Restore Data from Backup (C5002)](recovery/C5002.md) |  | A.8.2.1, A.8.3.1, A.8.3.2, A.11.1.4 | PR.DS-1, PR.DS-3, PR.IP-4, RC.RP-1 |
| [Unblock Blocked IP (C5101)](recovery/C5101.md) |  | A.13.1.1, A.13.1.2, A.16.1.5, A.12.4.1 | PR.AC-4, PR.PT-4, DE.CM-1, RS.IM-1 |
| [Unblock Blocked Domain (C5102)](recovery/C5102.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Unblock Blocked URL (C5103)](recovery/C5103.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Unblock Blocked Port (C5104)](recovery/C5104.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.13.2.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Unblock Blocked Port (C5105)](recovery/C5105.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.13.2.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Unblock Blocked User (C5106)](recovery/C5106.md) |  | A.9.2.1, A.9.2.6, A.16.1.5, A.5.24 | PR.AC-1, PR.AC-4, RS.RP-1, RC.RP-1 |
| [Unblock Domain on Email (C5201)](recovery/C5201.md) |  | A.13.1.1, A.13.1.3, A.12.4.1, A.12.6.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Unblock Sender on Email (C5202)](recovery/C5202.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Restore Quarantined Email Message (C5203)](recovery/C5203.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Restore Quarantined File (C5301)](recovery/C5301.md) |  | A.13.1.3, A.16.1.5, A.13.2.1, A.12.4.1 | PR.AC-3, PR.PT-4, RS.IM-1, RS.IM-2 |
| [Unblock Blocked Process (C5401)](recovery/C5401.md) |  | A.13.1.1, A.13.1.3, A.12.4.1 | PR.AC-4, PR.PT-3, DE.CM-1 |
| [Enable Disabled Service (C5501)](recovery/C5501.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |
| [Unlock Locked User Account (C5601)](recovery/C5601.md) |  | A.16.1.1, A.5.10, A.5.12, A.12.4.1 | DE.AE-1, RS.IM-1, PR.IP-1 |