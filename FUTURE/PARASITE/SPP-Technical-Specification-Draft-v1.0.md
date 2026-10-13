# SPP Technical Specification Draft

Version: 1.0

Status: Draft

Maturity Level: Research Architecture

Implementation Status: Not Implemented

Classification: Experimental Reasoning Framework

Repository: MIN/FUTURE/PARASITE

---

# Abstract

Shadow-Parasite Protocol (SPP) is an experimental reasoning architecture that explores whether activation steering, structured decoding, and runtime artifact reduction can improve task-specific reasoning efficiency without modifying foundation model weights.

SPP does not introduce a new language model.

Instead, it investigates whether existing models can be guided through external control layers and grammar constraints.

The protocol currently consists of three research domains:

- Activation Steering
- Grammar-Constrained Decoding
- Runtime Artifact Reduction

This document defines a candidate architecture and should be interpreted as a research draft rather than a validated implementation.

---

# 1. Purpose

## Problem Statement

Modern AI deployments face several recurring challenges:

- Cloud dependency
- Recurring API costs
- Output inconsistency
- Long reasoning chains
- Data persistence concerns
- Model-version drift
- Limited local autonomy

SPP investigates whether some of these challenges can be mitigated through external steering mechanisms.

---

## Research Objective

Determine whether structured external constraints can improve:

- Reasoning consistency
- Output quality
- Resource efficiency
- Runtime privacy

without retraining or modifying model weights.

---

# 2. Architectural Overview

```text
Input

↓

Host Model

↓

Representation Extraction

↓

Steering Layer

↓

Grammar Layer

↓

Inference

↓

Artifact Reduction

↓

Output
```

---

## Design Philosophy

SPP treats the model as a host system.

Reasoning behavior is influenced through:

- Intermediate representations
- Structured output constraints
- Runtime control layers

rather than through weight updates.

---

# 3. Online Phase

## Purpose

Obtain information that may be useful for steering experiments.

---

## Assumptions

The protocol assumes access to one or more of:

- Hidden States
- Logits
- Attention Statistics

Availability depends on model providers and runtime environments.

Many commercial APIs do not currently expose these interfaces.

---

## Candidate Representation Extraction

```text
R_hidden

R_logits

R_attention
```

These representations are treated as candidate signals.

SPP does not assume they directly correspond to:

- Logic
- Reasoning
- Noise

---

## Research Question

Can intermediate representations be used to derive useful steering signals?

---

# 4. Steering Layer

## Candidate Steering Vector

SPP defines:

```text
v_task

=

A_target

-

A_reference
```

Where:

```text
A_target
```

represents activations associated with desired behavior.

```text
A_reference
```

represents activations associated with baseline behavior.

---

## Example

```text
v_sag

=

A_logic

-

A_reference
```

The vector is treated as a candidate steering direction.

Its effectiveness must be validated experimentally.

---

## Mid-Layer Injection

Candidate injection rule:

```text
h'

=

h

+

λ · v_task
```

Where:

```text
h
```

Original activation state.

```text
λ
```

Steering gain coefficient.

---

## Research Questions

- Does steering improve task accuracy?
- Does steering improve consistency?
- Does steering reduce output variance?
- Does steering transfer across tasks?
- Does steering transfer across model families?

---

# 5. Grammar Constraint Layer

## Purpose

Constrain output structure.

---

## Motivation

Many reasoning failures originate from malformed or inconsistent outputs.

Grammar layers may improve:

- Structural consistency
- Machine readability
- Output predictability

---

## Example Grammar

```gbnf
<root> ::= <statement>

<statement> ::= <term>
              | <term> <statement>

<term> ::= <word>
```

---

## Candidate Constraint Domains

- GBNF
- JSON Schema
- DSL Specifications
- State Machine Grammars
- Protocol Grammars

---

## Expected Benefits

Potential benefits include:

- Reduced syntax errors
- Reduced output entropy
- Improved structural consistency

---

## Non-Claim

Grammar constraints do not automatically improve reasoning quality.

This remains an open research question.

---

# 6. Offline Phase

## Purpose

Support local execution without continuous cloud dependency.

---

## Reference Environment

Model Class:

```text
1.5B – 3B
```

Execution Target:

```text
CPU
```

---

## Candidate Workflow

```text
Input

↓

Local Model

↓

Steering Layer

↓

Grammar Layer

↓

Output
```

---

## Candidate Runtime

```python
local_output = local_model(
    input=input,
    steering=v_task
)
```

---

## Research Questions

- Can constraints compensate for smaller models?
- Can steering improve bounded-domain reasoning?
- Can local execution reduce cloud dependency?
- What performance trade-offs emerge?

---

# 7. Runtime Artifact Reduction

## Purpose

Reduce recoverable runtime artifacts after execution.

---

## Scope

SPP focuses on:

- Temporary buffers
- Runtime state
- Inference cache
- Intermediate vectors

---

## Candidate Cleanup Actions

```c
memset(buffer, 0, sizeof(buffer));

munmap(page);

vector = NULL;
```

---

## Candidate Cleanup Targets

- Temporary Memory
- Context Buffers
- Intermediate Activations
- Cache Structures

---

## Objective

Reduce recoverable execution artifacts.

---

## Non-Claim

SPP does not claim:

- Perfect stealth
- Complete forensic erasure
- Zero thermodynamic cost
- Elimination of all execution traces

---

# 8. Security Model

## Goals

- Preserve runtime integrity
- Reduce residual data exposure
- Avoid persistent model modification

---

## Threats

- Memory leakage
- Temporary file exposure
- Cache persistence
- Provider-side retention
- Runtime inspection

---

## Security Scope

SPP currently addresses:

```text
Local Runtime Hygiene
```

---

## Out of Scope

SPP currently does not address:

```text
Network Surveillance

Provider Logging

Physical Side Channels

Supply Chain Risks

Hardware Implants
```

---

# 9. Validation Framework

## Experimental Groups

### Group A

Baseline

---

### Group B

Steering

---

### Group C

Grammar Constraints

---

### Group D

Steering + Grammar Constraints

---

## Evaluation Metrics

### Quality

- Task Accuracy
- Benchmark Score
- Constraint Satisfaction

### Efficiency

- Token Usage
- Latency
- Memory Consumption

### Stability

- Output Variance
- Failure Rate

### Runtime Hygiene

- Residual Memory
- Recoverable Buffers
- Temporary Artifacts

---

## Success Criteria

SPP should demonstrate measurable improvement in at least one of the following:

- Structured reasoning
- Reasoning consistency
- Runtime hygiene
- Output predictability
- Resource usage

without modifying base model weights.

---

# 10. Integration Constraints

## Provider Requirements

SPP may require access to:

- Hidden States
- Logits
- Attention Statistics

Many commercial APIs do not currently expose these interfaces.

Provider compatibility remains a major implementation limitation.

---

## Open-Source Runtime Compatibility

SPP is more readily evaluated on systems that expose internal representations.

Potential candidates include:

- Llama
- Qwen
- Gemma
- Mistral

---

## Runtime Dependencies

Potential dependencies include:

- Custom inference runtimes
- Grammar-constrained decoders
- Steering-capable execution engines

---

# 11. Potential Operational Benefits

The following are research hypotheses and require validation.

Potential outcomes include:

- Reduced cloud inference demand
- Improved local autonomy
- Better structured outputs
- Reduced recurring API usage
- Improved runtime hygiene
- Lower operational cost in bounded domains

No operational benefit is assumed until benchmark evidence exists.

---

# 12. Limitations

Current architecture assumes:

- Steering-capable runtimes
- Access to intermediate representations
- Grammar-constrained decoding support

---

The protocol has not demonstrated:

- Universal steering vectors
- Cross-model transferability
- Reduced total energy consumption
- Superior reasoning performance
- Complete artifact elimination
- General-purpose intelligence improvement

---

# 13. Relationship to Other MIN Projects

## RTCP

Focus Areas:

```text
Governance

Economics

Computation Accounting
```

---

## SPP

Focus Areas:

```text
Reasoning

Inference Control

Runtime Hygiene
```

---

## Combined Vision

Future integration may explore:

```text
Governance

+

Reasoning

+

Resource Accounting
```

within a broader civilization-scale architecture.

---

# Future Work

Phase 1

Activation Steering Experiments

↓

Phase 2

Grammar-Constrained Benchmarking

↓

Phase 3

Cross-Model Validation

↓

Phase 4

Runtime Artifact Measurement

↓

Phase 5

Reference Implementation

↓

Phase 6

Open Evaluation Framework

---

# Status Declaration

SPP remains an experimental architecture.

All major technical claims should be considered research hypotheses until validated through reproducible benchmarks and independent evaluation.

---

# Motto

Measure First.

Claim Later.

Evidence Before Architecture.
