# Okta

## Overview

Okta is a leading identity and access management platform that provides secure authentication and authorization services for applications and users. It enables organizations to manage user identities, implement single sign-on (SSO), and enforce multi-factor authentication (MFA) across their digital environments. Okta's robust features help enhance security, streamline user access, and improve compliance with industry standards.

## Categories

- identity and access management
- single sign-on
- multi-factor authentication

## Capabilities

| Capability | ID | Phase | Description |
|------------|----|-------|-------------|
| [Revoke Authentication Credentials](C4601.md) | [C4601](../../capability/eradication/C4601.md) | Eradication | This capability outlines the process of revoking authentication credentials for users or systems that are no longer authorized to access resources. It includes steps for identifying the credentials to be revoked, executing the revocation, and ensuring that access is effectively terminated to prevent unauthorized use. This capability is essential for maintaining security and compliance during incident response. |
| [Remove User Account](C4602.md) | [C4602](../../capability/eradication/C4602.md) | Eradication | This capability outlines the process of removing a user account from a system. It includes steps for identifying the user account to be removed, ensuring that it is safe to delete, and executing the removal in a manner that maintains system integrity. This capability is essential for managing user accounts during incident response, particularly when dealing with compromised or unnecessary accounts. |
| [Unlock Locked User Account](C5601.md) | [C5601](../../capability/recovery/C5601.md) | Recovery | This capability outlines the process of unlocking a user account that has been locked due to security policies or multiple failed login attempts. It includes steps for verifying the user's identity, ensuring the account is safe to unlock, and executing the unlock process. |

## MITRE ATT&CK Data Sources

- User Account: User Account Creation
- User Account: User Account Modification
- User Account: User Account Deletion
- User Account: User Account Authentication
- User Account: User Account Metadata