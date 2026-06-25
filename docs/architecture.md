# Opportunity OS — Architecture

## System Overview

Opportunity OS is a multi-agent intelligence pipeline that converts raw world data into structured opportunities.

---

## High-Level Architecture
World
↓
Source Discovery Agent
↓
Observation Agent
↓
Problem Formation Agent
↓
Opportunity Generation Agent
↓
Scoring Agent
↓
UI Layer

---

## Core Agents

### 1. Orchestrator Agent

Responsibilities:
- Controls pipeline execution
- Triggers agent workflows
- Manages domain processing
- Coordinates continuous and on-demand modes

---

### 2. Source Discovery Agent

Goal:
Find high-signal sources for a domain.

Behavior:
- Searches web, forums, papers, communities
- Evaluates source quality
- Dynamically updates source list

Output:
- Ranked source nodes with relevance scores

---

### 3. Observation Agent

Goal:
Convert raw content into structured observations.

Behavior:
- Extracts meaningful signals
- Filters noise
- Normalizes language

Output:
- Observation objects linked to sources

---

### 4. Problem Formation Agent

Goal:
Cluster observations into meaningful problems.

Behavior:
- Semantic clustering
- Deduplication
- Problem labeling

Output:
- Problem nodes with supporting observations

---

### 5. Opportunity Generation Agent

Goal:
Convert problems into solution spaces.

Behavior:
- Generates multiple solution directions
- Evaluates feasibility
- Covers multiple categories:
  - software
  - services
  - hardware
  - workflows

Output:
- Opportunity nodes

---

### 6. Trend Agent

Goal:
Predict future opportunities.

Behavior:
- Tracks emerging technologies
- Maps tech → problem intersections
- Updates opportunity relevance over time

---

### 7. Scoring Agent

Goal:
Provide structured evaluation metrics.

Important:
- Does NOT decide ranking
- Only provides dimensions

Metrics:
- Market size
- Pain severity
- Competition
- Feasibility
- Evidence strength
- Trend momentum

---

## Data Model

### Observation
- source_id
- domain
- raw_text
- structured_insight
- confidence
- timestamp

### Problem
- name
- description
- supporting_observations[]
- confidence_score

### Opportunity
- linked_problem
- solution_types[]
- feasibility
- market_signals
- future_potential

### Source
- url
- type
- domain_relevance
- signal_quality

---

## System Modes

### Continuous Mode
- Always-on domain monitoring
- Updates knowledge graph in real time

### On-Demand Mode
- User-triggered analysis
- Instant report generation

---

## Key Design Principle

Every layer is agent-driven but strictly scoped:

> Each agent has a single responsibility and operates in a controlled loop.