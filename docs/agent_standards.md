# Agent Standards — Opportunity OS

## Core Principle

Every agent in Opportunity OS must follow strict responsibility boundaries. No agent is allowed to perform multiple stages of the pipeline.

---

## 1. Single Responsibility Rule

Each agent must perform exactly ONE function:

- Source Discovery → find sources only
- Observation → extract signals only
- Problem Formation → cluster observations only
- Opportunity Generation → generate solution ideas only
- Scoring → evaluate only

---

## 2. Input / Output Contract

Every agent must define:

- Input format (strict)
- Output format (structured data only)

No free-form text outputs are allowed.

---

## 3. No Cross-Layer Actions

Agents are forbidden from:

- jumping steps in pipeline
- generating final business decisions
- combining multiple pipeline stages

---

## 4. Evidence Requirement

All outputs must be grounded in:

- source data
- observations
- or structured problem clusters

No hallucinated outputs.

---

## 5. Deterministic Structure

Outputs must always follow a structured schema:

- JSON-like or dataclass format
- consistent fields across runs

---

## 6. No Decision Authority

Agents do NOT decide:

- what is "best"
- what user should do
- what company should be built

They only generate structured intelligence.

---

## 7. Traceability Rule

Every output must be traceable back to:

- source → observation → problem → opportunity

No orphan outputs allowed.