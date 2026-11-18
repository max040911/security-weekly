# RAW: NVD CVE records

- url: https://services.nvd.nist.gov/rest/json/cves/2.0
- fetched: 2026-11-18
- license: U.S. Government work (public domain)
- 本檔為原始資料，ingest 後不得修改。

---

## CVE-2024-3094

- published: 2024-03-29T17:15:21.150
- cvss: 10.0 CRITICAL (cvssMetricV31, source: secalert@redhat.com)

Malicious code was discovered in the upstream tarballs of xz, starting with version 5.6.0. 
Through a series of complex obfuscations, the liblzma build process extracts a prebuilt object file from a disguised test file existing in the source code, which is then used to modify specific functions in the liblzma code. This results in a modified liblzma library that can be used by any software linked against this library, intercepting and modifying the data interaction with this library.

## CVE-2021-44228

- published: 2021-12-10T10:15:09.143
- cvss: 10.0 CRITICAL (cvssMetricV31, source: nvd@nist.gov)

Apache Log4j2 2.0-beta9 through 2.15.0 (excluding security releases 2.12.2, 2.12.3, and 2.3.1) JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. An attacker who can control log messages or log message parameters can execute arbitrary code loaded from LDAP servers when message lookup substitution is enabled. From log4j 2.15.0, this behavior has been disabled by default. From version 2.16.0 (along with 2.12.2, 2.12.3, and 2.3.1), this functionality has been completely removed. Note that this vulnerability is specific to log4j-core and does not affect log4net, log4cxx, or other Apache Logging Services projects.

## CVE-2021-45046

- published: 2021-12-14T19:15:07.733
- cvss: 9.0 CRITICAL (cvssMetricV31, source: nvd@nist.gov)

It was found that the fix to address CVE-2021-44228 in Apache Log4j 2.15.0 was incomplete in certain non-default configurations. This could allows attackers with control over Thread Context Map (MDC) input data when the logging configuration uses a non-default Pattern Layout with either a Context Lookup (for example, $${ctx:loginId}) or a Thread Context Map pattern (%X, %mdc, or %MDC) to craft malicious input data using a JNDI Lookup pattern resulting in an information leak and remote code execution in some environments and local code execution in all environments. Log4j 2.16.0 (Java 8) and 2.12.2 (Java 7) fix this issue by removing support for message lookup patterns and disabling JNDI functionality by default.

## CVE-2021-44832

- published: 2021-12-28T20:15:08.400
- cvss: 6.6 MEDIUM (cvssMetricV31, source: nvd@nist.gov)

Apache Log4j2 versions 2.0-beta7 through 2.17.0 (excluding security fix releases 2.3.2 and 2.12.4) are vulnerable to a remote code execution (RCE) attack when a configuration uses a JDBC Appender with a JNDI LDAP data source URI when an attacker has control of the target LDAP server. This issue is fixed by limiting JNDI data source names to the java protocol in Log4j2 versions 2.17.1, 2.12.4, and 2.3.2.
