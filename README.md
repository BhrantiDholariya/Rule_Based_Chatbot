# Rule-Based AI Chatbot 🤖

---

## Overview

A Rule-Based AI Chatbot built using pure Python. This project demonstrates control flow, decision-making logic, and basic AI concepts — without any external libraries.

---
 
## Main Functions & Concepts Used
 
### 1. `input()` — Taking User Input
Captures whatever the user types in the terminal.
 
### 2. `.lower().strip()` — Input Sanitization
Converts input to lowercase and removes extra spaces so "HELLO", "Hello", " hello " all match the same key in the dictionary.
 
### 3. `while True` — Infinite Loop
Keeps the chatbot alive and continuously waiting for the next user message.
 
### 4. `if / break` — Exit Strategy
Checks if the user typed `exit` and cleanly stops the loop.
 
### 5. Dictionary `{}` — Knowledge Base
Stores all predefined responses as key-value pairs. The user's input is the key, the bot's reply is the value.
 
### 6. `.get()` — Safe Lookup with Fallback
Looks up the user input in the dictionary. If found, returns the response. If not found, returns a default message instead of crashing.
