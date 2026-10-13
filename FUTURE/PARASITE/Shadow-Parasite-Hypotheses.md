# Shadow Parasite

Revised Technical Hypotheses

Version: 0.2

Status: Research Draft

Classification: Testable Research Program

Repository: MIN/FUTURE/PARASITE

---

# Purpose

This document reformulates Shadow Parasite into a set of falsifiable and experimentally testable claims.

The objective is not to assert capability.

The objective is to define measurable hypotheses.

---

# Hypothesis 01

## Latent Steering Improves Task Efficiency

Original Claim

A single steering vector can collapse a model into a superior reasoning state.

---

Revised Claim

Activation steering may improve task-specific reasoning performance without modifying model weights.

---

Measurement

Compare:

- Baseline Model
- Activation-Steered Model

Across:

- Mathematical Tasks
- Structured Planning Tasks
- Governance Tasks
- Specification Writing Tasks

---

Metric

```text
Task Success Rate

Reasoning Accuracy

Token Efficiency
```

---

Success Condition

Steered model achieves statistically significant improvement over baseline.

---

# Hypothesis 02

## Grammar Constraints Reduce Output Entropy

Original Claim

Grammar masks force models into pure logic states.

---

Revised Claim

Grammar-constrained decoding reduces output entropy and structural variance.

---

Measurement

Compare:

- Free Decoding
- Grammar-Constrained Decoding

---

Metrics

```text
Syntax Error Rate

Output Variance

Token Entropy

Constraint Satisfaction Rate
```

---

Success Condition

Grammar-constrained outputs exhibit lower variance and higher structural consistency.

---

# Hypothesis 03

## Small Models Benefit From Strong Constraints

Original Claim

Small models can behave like 100B+ models.

---

Revised Claim

Small models can achieve competitive performance on constrained domains when paired with strong steering and grammar restrictions.

---

Measurement

Compare:

- 3B Model + Constraints
- 70B Model Baseline

Task Types

- Decision Trees
- Rule Systems
- Specifications
- Structured Outputs

---

Metrics

```text
Task Completion Rate

Accuracy

Tokens Consumed

Latency
```

---

Success Condition

Small models achieve acceptable performance relative to larger models within limited domains.

---

# Hypothesis 04

## Steering Vectors Are Transferable

Original Claim

A universal logic vector exists.

---

Revised Claim

Certain steering directions may transfer across multiple tasks within the same model family.

---

Measurement

Extract steering vector from:

```text
Task A
```

Evaluate on:

```text
Task B
Task C
Task D
```

---

Metrics

```text
Accuracy Change

Response Quality

Consistency
```

---

Success Condition

Cross-task performance remains positive.

---

Note

This hypothesis does not assume a universal vector exists.

---

# Hypothesis 05

## Resource-Efficient Inference Layer

Original Claim

High-quality reasoning can emerge without large local infrastructure.

---

Revised Claim

External steering combined with lightweight local models can reduce hardware requirements for specific reasoning tasks.

---

Measurement

Compare:

```text
Local 3B + Steering

vs

Local 70B Baseline
```

---

Metrics

```text
Memory Usage

Power Consumption

Latency

Task Quality
```

---

Success Condition

Meaningful reduction in resource consumption while preserving useful performance.

---

# Hypothesis 06

## Runtime State Minimization

Original Claim

NET = 0

---

Revised Claim

Runtime artifacts can be reduced through memory hygiene and process cleanup.

---

Measurement

Evaluate:

- Memory Pages
- Temporary Files
- Process Artifacts
- Cached Buffers

Before and After Cleanup

---

Metrics

```text
Residual Memory

Temporary Storage

Persistent Artifacts
```

---

Success Condition

Measured runtime residue decreases after cleanup procedures.

---

Note

Physical computation cannot produce zero thermodynamic cost.

---

# Hypothesis 07

## Forensic Exposure Reduction

Original Claim

The computation effectively never existed.

---

Revised Claim

Certain operational patterns may reduce recoverable local artifacts.

---

Measurement

Compare:

```text
Normal Runtime

vs

Cleanup Runtime
```

---

Metrics

```text
Recoverable Buffers

Process Traces

Cache Artifacts
```

---

Success Condition

Lower observable artifact count after execution.

---

Note

This does not imply complete invisibility.

---

# Hypothesis 08

## Host-Agnostic Steering Framework

Original Claim

The parasite can operate on any host.

---

Revised Claim

A steering framework may be portable across multiple model architectures with adaptation.

---

Measurement

Evaluate on:

- Llama
- Qwen
- Gemma
- Mistral

---

Metrics

```text
Transfer Performance

Calibration Cost

Performance Retention
```

---

Success Condition

The framework remains usable across multiple architectures.

---

# Non-Claims

The project does not currently claim:

- Universal Logic Vectors
- Intelligence Amplification Beyond Model Knowledge
- Zero Thermodynamic Cost
- Perfect Stealth
- Infinite Scaling
- Complete Forensic Erasure

---

# Research Roadmap

Phase 1
