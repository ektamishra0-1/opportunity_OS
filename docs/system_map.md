# System Map — Opportunity OS

## Overview

Opportunity OS is a multi-agent pipeline that converts real-world data into structured opportunity intelligence.

---

## System Flow
Sources
↓
Source Discovery Agent
↓
Raw Content
↓
Observation Agent
↓
Observations
↓
Problem Formation Agent
↓
Problems
↓
Opportunity Generation Agent
↓
Opportunities
↓
Scoring Agent
↓
Dashboard / Feed / Search UI
---

## Core Components

### 1. Source Layer
External data sources:
- research papers
- forums
- job boards
- news
- communities

---

### 2. Observation Layer
Transforms raw data into structured signals.

Output: Observations

---

### 3. Problem Layer
Clusters observations into real-world problems.

Output: Problem objects with evidence

---

### 4. Opportunity Layer
Generates solution spaces from problems.

Output: Opportunities

---

### 5. Evaluation Layer
Scores opportunities using multiple dimensions.

Output: structured metrics (not final decisions)

---

## Data Flow Principle

Each layer ONLY communicates with the next layer.

No skipping allowed.

---

## System Modes

### Continuous Mode
- system runs automatically
- updates knowledge graph

### On-Demand Mode
- user queries system
- system composes response from stored knowledge