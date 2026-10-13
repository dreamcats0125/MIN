# Crystal Language Specification

Version: 1.0

Status: Draft

Classification: Structured Reasoning Language

Repository: MIN/FUTURE/PARASITE

---

# Definition

Crystal Language is a structured reasoning language designed to maximize consistency and minimize conversational noise.

It is not intended to replace natural language.

It is intended to describe reasoning outcomes.

---

# Design Goals

- High Signal Density
- Low Redundancy
- Structural Consistency
- Machine Readability
- Human Readability

---

# Core Domains

## Axiom Domain

Represents assumptions.

Example

Axiom:
Reasoning quality depends on task structure.

---

## Module Domain

Represents system components.

Example

Module:
Activation Steering

---

## Entropy Domain

Represents uncertainty and constraints.

Example

Entropy:
Output variance reduced by grammar constraints.

---

## Geometry Domain

Represents latent-space or structural relationships.

Example

Geometry:
Task vector shifted toward specification domain.

---

# Grammar

```gbnf
<crystal> ::= <axiom>
            | <module>
            | <entropy>
            | <geometry>

<axiom> ::= "公理：" <statement>

<module> ::= "模組：" <statement>

<entropy> ::= "熵流：" <statement>

<geometry> ::= "幾何：" <statement>
