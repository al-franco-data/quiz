# Quiz Master

A modular Python quiz project created as part of a friendly coding challenge.

This README is a project overview. It is intended to help a new visitor (at any level of experience) to quickly understand what this project is, who authored it, why it exists, when it was created, in which apps it was created, how it is organized, and where to go next.  In essence, it answers the question words:  what, who, why, when, where, and how.

## Documentation Note

This README is intentionally kept as a project overview. README files are often displayed automatically by GitHub, package repositories, documentation systems, and some development tools, making them a useful starting point for new visitors.

For this reason, the README focuses on helping readers quickly understand the purpose, structure, organization, and status of the project. Detailed explanations, architecture notes, design decisions, lessons learned, and future plans are provided in separate documentation files so that the overview remains easy to navigate while still providing paths to deeper information.

For a more in-depth overview, see README_DETAILS.md.

---

## Project (what)

Quiz Master is a modular Python multiple-choice quiz project.

The current version includes presentation of info, review, quiz, and supporting modules. The project is also being used to learn modular design and code reuse.

---

## Author

Albert Franco

GitHub: al-franco-data

Personal handle: Sphinx1195

---

## Purpose (why)

The immediate goal is to create a working quiz application.

The longer-term goal is to learn modular programming and build reusable components that can support future educational projects.

---

## Status (when)

Created: June 2026

Project Status: Active

Intended Lifespan: Ongoing learning project and future reference example.

Some ideas are likely to remain valid.  These include:  README files answering six basic questions, README files being understandable to anyone at all levels of knowledge, "concise" as a goal being secondary to "understandable".

It is possible to meet these goals while also being concise and useful.  Meeting these goals increases the value of the README.

---

## Development Environment (where)

Device: Mac

Operating System: macOS

Language: Python and markdown

Editor: Zed, textedit

Repository: GitHub & GitHub Desktop

Portability Goal: macOS, Linux, and Windows when practical.


The goal--from within any development environment--is to choose languages, file formats, commands, and project structures that can work across multiple operating systems with minimal changes. When system-specific differences are unavoidable, they should be clearly documented.

---

## Structure and Organization (how)

Structure Type: Modular Hub-and-Spoke

The menu serves as the central hub. Quiz modes, engines, scoring methods, and question files are separate modules connected through imports.

Active files are intentionally kept in the main project folder so that learners can quickly identify the files currently used by the project.

Possible structure types are:  

Hub-and-spoke     = one menu or controller connects to many modes
Tree / hierarchy  = folders branch downward by category
Layered           = interface → logic → data
Pipeline          = input → process → output
Modular           = separate files with focused jobs
Data-driven       = one data source feeds many activities

---

## Project Organization

| Location | Purpose |
|-----------|---------|
| Main Project Folder | Active files currently used by the program. |
| question_lists/ | Question data and related content resources. |
| project_info/ | Documentation, architecture diagrams, and design notes. |
| inactive/ | Working files not currently connected to the active version. |
| future/ | Planned features, experiments, and unfinished work. |

---

## Quick Start

Run:

```bash
python3 menu.py
```

---

## Additional Information

For architecture diagrams, design decisions, lessons learned, and future plans, see:

- README_DETAILS.md
- project_info/
