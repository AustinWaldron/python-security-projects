# Python Security Projects

Python scripts and small projects for security work, built while learning with TryHackMe. Each project lives in its own folder with its own README.

## Projects

| Project | Status | What it does |
|---|---|---|
| [`password-checker`](password-checker/) | In progress | Rates a password as Weak, Medium, or Strong and explains what to fix |
| `log-parser` | Planned | Counts events per IP in a log file and flags unusual activity |
| `pcap-summarizer` | Planned | Uses `scapy` to pull top talkers and DNS queries from a capture, tied to my [malware traffic analysis](https://github.com/AustinWaldron/Malware-Traffic-Analysis-Portfolio) work |

## What I've covered

| Topic | Details |
|---|---|
| **Core syntax** | Variables, conditionals, strings, arithmetic and membership operators |
| **Data structures** | Lists and dictionaries |
| **Control flow** | `for` and `while` loops |
| **Functions** | Defining reusable functions with `def name(params):` |
| **Libraries** | Importing modules, reading documentation, installing packages with `pip`, and an introduction to `requests`, `scapy`, and `pwntools` |
| **File handling** | `open()` with `r`, `w`, and `a` modes, plus `read()`, `readlines()`, `write()`, and `close()` |

Completed on TryHackMe: **Python Basics** and **Python: Core Concepts**.

**Python Basics**

Linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7523891860864667648/

**Python: Core Concepts**

Linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7525471334437486592/

## Why this matters for security

- **Lists and dictionaries** model real data: IP addresses to scan, open ports per host, and port-to-service mappings (22 → SSH, 80 → HTTP).
- **File handling** is the basis for log parsing and report generation.
- **Libraries** like `requests` (HTTP), `scapy` (packet analysis), and `pwntools` (CTF tooling) are common in security scripting.

## Skill level

Basic scripting. I'm actively building toward security-focused automation.
