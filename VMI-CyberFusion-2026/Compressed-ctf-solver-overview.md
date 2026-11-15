# VMI CyberFusion 26: Project Writeup

## Project Overview
This tool was engineered specifically for **VMI CyberFusion 26** to maximize efficiency and placement potential through automation. It functions as a hybrid **CTF Orchestrator** and **AI Solver**.

## Technical Architecture

### 1. The Core (Flask + Socket.IO)
The application is built on **Flask**, providing a lightweight yet extensible backend. **Socket.IO** is utilized for full-duplex communication, allowing the server to push real-time terminal logs, agent thoughts, and flag submissions to the frontend without polling.

### 2. The Runtime (Docker)
Security and consistency are paramount. The system leverages **Docker** to spawn ephemeral containers based on a custom `ctf-kali` image.
- **Isolation**: Malicious challenges or unstable exploits cannot harm the host.
- **Tooling**: The `ctf-kali:latest` image ensures all necessary binaries (nmap, gdb, pwntools) are pre-installed and available to the agent.

### 3. The Brain (OpenAI API)
The defining feature is the **OpenAI-powered agent**.
- **Context Awareness**: The agent consumes challenge descriptions and file metadata.
- **Action Loop**: It operates in a loop proposing a command, executing it in Docker, observing the output, and refining the strategy.
- **Autonomy**: Capable of solving standard categories (crypto, misc, basic pwn).

## Strategic Value

In a time-constrained environment like VMI CyberFusion, this tool provides:

*   **Parallelism**: The agent can work on "easy" challenges while human operators focus on "hard" ones.
*   **Expertise**: While many ctf competitions can be completed solo, teams are usually involved in order to cover topics more thuroughly. AI can fill in gaps for solo competitors so they can either improve on areas they dont know or straight solve them as a teammate.

## Deployment

The system is designed for "drop-in" usage:

1.  **Installation**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configuration**:
    Add your API key to `config.json`.
3.  **Launch**:
    ```bash
    python3 server.py
    ```
    Access the dashboard at `http://localhost:7331`.

## Conclusion
This project demonstrates how modern DevOps practices and Generative AI can be applied to offensive security competitions, transforming the traditional solver into a force-multiplied command center.