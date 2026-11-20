# TraceGuard AI

**AI-Powered Security Log Analyzer using LLM Tool Calling**

TraceGuard AI is a web-based security log analysis application designed to help users investigate authentication activity, identify suspicious patterns, and understand potential security incidents using an LLM-powered agent.

The project combines Python-based log analysis tools with an LLM that can select appropriate tools based on a user's natural-language investigation request.

> **Project Status:** Under Development 🚧

---

## 1. Project Overview

Security logs contain valuable information about authentication attempts and suspicious activities. However, manually examining large log files can be time-consuming.

TraceGuard AI aims to simplify this process.

Users will be able to upload security log files and ask questions such as:

- Which IP address has the most failed login attempts?
- Are there any suspicious login patterns?
- Did any successful login occur after repeated failures?
- Can you generate a security investigation summary?

The LLM will determine which predefined Python analysis tool is appropriate, execute the selected tool through the application, and explain the results.

## 2. Project Objectives

- Automate basic security log analysis.
- Identify repeated failed login attempts.
- Extract and analyze IP address activity.
- Detect potentially suspicious authentication patterns.
- Integrate LLM-based tool calling.
- Generate understandable security investigation summaries.
- Build an interactive security operations dashboard.

## 3. How It Will Work

The planned workflow:

1. User uploads a security log file.
2. Python parses the uploaded logs.
3. User asks a question in natural language.
4. The LLM selects an appropriate analysis tool.
5. The application executes the selected Python function.
6. The tool returns structured results.
7. The LLM interprets the results and generates an explanation.
8. The dashboard displays findings and recommendations.

## 4. Planned Architecture

```text
                 USER
                   |
                   v
            Flask Web Interface
                   |
                   v
              AI Agent
                   |
                   v
             LLM / Model
                   |
             Tool Selection
                   |
                   v
          Python Analysis Tools
                   |
          +--------+---------+
          |        |         |
        Parse    Analyze   Detect
        Logs     IPs       Patterns
          |        |         |
          +--------+---------+
                   |
                   v
            Structured Results
                   |
                   v
           LLM Interpretation
                   |
                   v
          Security Investigation
                 Report
```

## 5. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Animations | GSAP |
| AI Integration | LLM with Tool Calling |
| Model Runtime | To be finalized |
| Log Analysis | Custom Python Functions |
| Version Control | Git and GitHub |

## 6. Current Implementation

### Completed

- [x] Created the ML-Journey repository structure.
- [x] Cloned the repository locally.
- [x] Configured Python 3.11.9.
- [x] Created and activated a virtual environment.
- [x] Installed Flask.
- [x] Created the initial Flask application.
- [x] Verified that the Flask server runs locally.
- [x] Created the project folder structure.
- [x] Created a sample authentication log file.
- [x] Implemented Python log analysis functions.
- [x] Tested the analysis functions using sample logs.
- [x] Configured Git version control and `.gitignore`.

### Python Analysis Tools Implemented

| Function | Purpose |
|---|---|
| `parse_logs()` | Reads log files and extracts non-empty entries. |
| `count_failed_logins()` | Counts failed login attempts by IP. |
| `extract_ips()` | Extracts unique IP addresses. |
| `analyze_ip_activity()` | Tracks successful and failed logins by IP. |
| `detect_suspicious_patterns()` | Identifies repeated failed login patterns. |
| `generate_summary()` | Generates an overall analysis summary. |

### Initial Test Results

The analysis engine was tested using a sample authentication log containing 12 entries.

- Total log entries: 12
- Unique IP addresses: 4
- Failed login attempts: 7
- Successful login attempts: 5
- IP addresses flagged by the current detection rule: 1

The sample includes repeated failed login attempts followed by a successful login from the same IP address.

The HIGH severity label is based on the project's current detection rule. It is an investigative signal, not proof of account compromise.

## 7. Project Structure

```text
TraceGuard-AI/
│
├── agent/
│   ├── __init__.py
│   ├── agent.py
│   └── tools.py
│
├── logs/
│   └── sample_auth.log
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 8. Upcoming Development

### Phase 1 — LLM Fundamentals

- Understand LLM fundamentals.
- Learn prompts, tokens, and context windows.
- Understand how Python communicates with an LLM.
- Learn function calling and tool calling.

### Phase 2 — Agent Development

- Select a suitable tool-calling model.
- Connect the LLM to the Python analysis functions.
- Implement tool selection and execution.
- Handle model responses and tool results.
- Test natural-language security investigations.

### Phase 3 — Frontend Development

- Build a security operations dashboard.
- Add log file upload functionality.
- Create an investigation chat interface.
- Display suspicious IPs and authentication statistics.
- Add severity indicators and investigation reports.
- Integrate GSAP animations.

### Phase 4 — Testing and Deployment

- Test with different sample log files.
- Handle malformed and unsupported log entries.
- Validate agent tool selection.
- Test edge cases and application security.
- Deploy the completed Version 1 application.

## 9. Future Scope — Version 2

Possible improvements:

- Multi-step autonomous investigations.
- Correlation of events across multiple log files.
- Investigation history and memory.
- More advanced anomaly detection.
- Evidence-based incident timelines.
- Expanded log format support.

## 10. Security Considerations

TraceGuard AI is intended as a defensive security analysis project.

- Analysis tools will use predefined, controlled functions.
- Uploaded logs will be treated as untrusted input.
- The agent will not execute arbitrary shell commands.
- The application will not automatically block IP addresses or modify servers.
- Findings will be presented as investigation leads rather than confirmed compromises.

---

**Built as a hands-on learning project to explore Agentic AI, LLM Tool Calling, Python, and Cybersecurity.**
