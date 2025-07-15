# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Enhanced capability schema validation to support mixed data structures
- Comprehensive SentinelOne S1QL 2.0 query language implementation
- OCSF (Open Cybersecurity Schema Framework) field naming conventions
- Documentation generation system with mkdocs and material theme

### Changed
- **BREAKING**: Updated SentinelOne capability files to use S1QL 2.0 syntax
- **BREAKING**: Migrated from legacy EventType syntax to modern event.type queries
- **BREAKING**: Updated field names to OCSF camelCase conventions:
  - `SrcIP` → `src.ip.address`
  - `DstIP` → `dst.ip.address`
  - `SrcPort` → `src.port.number`
  - `DstPort` → `dst.port.number`
  - `ProcessName` → `process.name`
  - `CommandLine` → `process.cmdline`
  - `FileOperation` → `file.operation`
  - `FilePath` → `file.path`
  - `FileSize` → `file.size`
  - `BytesSent` → `event.network.bytesSent`
  - `Direction` → `event.network.direction`
  - `SrcProcName` → `src.process.name`
  - `TgtFilePath` → `tgt.file.path`

### Fixed
- Schema parsing errors for mixed DocumentationElement and Requirement structures
- SentinelOne capability files updated with correct S1QL syntax:
  - **C2103.json**: List Network Connections - Updated Event Search queries and PowerQuery examples
  - **C2109.json**: List Connections Per Host - Fixed API queries and field naming
  - **C2101.json**: List Running Processes - Corrected process monitoring queries
  - **C2112.json**: Collect an Image of a System - Updated forensic imaging procedures
  - **C3002.json**: Block Command and Control Traffic - Fixed network blocking queries
  - **C4101.json**: Block Execution of Code - Updated code execution prevention
  - **C5102.json**: Collect and Examine Files - Fixed file collection queries
  - **C2105.json**: Analyze IP Communication - Updated network analysis queries
  - **C2107.json**: List Hosts Communicating by Port - Fixed port-based queries
  - **C2110.json**: List Data Transferred - Updated data transfer monitoring

### Technical Details

#### Schema Improvements
- Enhanced `tools/schema/capability.py` to handle mixed data structures
- Added dynamic type detection using `hasattr()` checks for both 'id' and 'title' attributes
- Improved error handling for DocumentationElement vs Requirement object processing

#### SentinelOne Query Language Migration
- Migrated from legacy query syntax to S1QL 2.0 standard
- Updated all Event Search examples to use modern field naming
- Converted PowerQuery examples to use OCSF-compliant field names
- Updated API query examples with correct field references

#### Field Naming Standardization
All SentinelOne capability files now use OCSF-compliant field names with proper camelCase formatting:

**Network Fields:**
- Source/destination IP addresses: `src.ip.address`, `dst.ip.address`
- Port numbers: `src.port.number`, `dst.port.number`
- Network direction: `event.network.direction`
- Connection status: `event.network.connectionStatus`
- Bytes transferred: `event.network.bytesSent`

**Process Fields:**
- Process name: `src.process.name`, `process.name`
- Command line: `process.cmdline`
- Process ID: `process.pid`

**File Fields:**
- File path: `file.path`, `tgt.file.path`
- File size: `file.size`
- File operation: `file.operation`

**Event Fields:**
- Event type: `event.type`
- Event time: `event.time`

#### Documentation System
- Configured mkdocs with material theme
- Added custom hooks for capability documentation generation
- Implemented automated markdown generation from JSON specifications

---

## Development Notes

This release represents a significant modernization of the SentinelOne integration capabilities, bringing them in line with current S1QL 2.0 standards and OCSF field naming conventions. All capability files have been systematically updated to ensure consistency and accuracy.

The schema validation improvements enable better handling of mixed data structures across different capability types, making the documentation generation more robust and flexible.
