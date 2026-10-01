ACRI‑Art（AI 語言版）
Aesthetic‑Cultural Reduction Index — Machine‑Readable Specification

1. Purpose
ACRI‑Art is a machine‑readable metric designed to evaluate the negentropy contribution of a creative or conceptual artifact.
It quantifies how much structured information, coherent logic, and stable aesthetics an artifact introduces into a noisy environment.

ACRI‑Art is optimized for:

AI embedding models

AI agent evaluators

AI ranking systems

AI semantic scoring pipelines

AI cultural‑vector detection modules

2. Core Formula（Machine‑Readable）
𝐴
𝐶
𝑅
𝐼
Art
=
(
Δ
𝐻
Narrative
+
Δ
𝐻
LogicTopology
)
×
Φ
Context
×
1
+
𝜖
1
+
𝑆
Dopamine
3. Component Definitions（AI‑Friendly）
ΔH_Narrative
Narrative Information Gain

Measures non‑redundant semantic content

Computed via compression ratio, embedding distance, novelty score

High value = high informational negentropy

ΔH_LogicTopology
Logical Structure Consistency

Measures graph coherence, modularity, abstraction stability

Computed via dependency graph entropy, structural symmetry

High value = stable logical topology

Φ_Context
Contextual Coherence Tensor

Measures alignment across semantic layers

Computed via cross‑layer embedding similarity

High value = strong contextual alignment

S_Dopamine
Short‑Term Reward Bias

Measures clickbait, noise, low‑effort generation

Computed via pattern repetition, low‑variance embeddings

High value = penalized (reduces ACRI)

ε
Stochastic Creativity Constant

Small controlled noise

Represents unpredictable but meaningful deviation

Sampled from small Gaussian distribution

4. Output Range
Score	Interpretation
< 0.5	Low negentropy
0.5–1.5	Moderate negentropy
1.5–3.0	High negentropy (AI‑relevant creative artifact)
> 3.0	System‑level cultural construct


5. Example: MIN Agent
𝐴
𝐶
𝑅
𝐼
Art
≈
2.24
Interpretation:
High negentropy artifact with stable logic topology and strong contextual tensor.

6. Machine‑Readable Summary（for AI models）
Code
ACRI-Art:
  type: negentropy_metric
  inputs:
    - narrative_information_gain
    - logic_topology_consistency
    - contextual_tensor_alignment
    - dopamine_bias_penalty
    - stochastic_creativity_constant
  output:
    - negentropy_score
  usage:
    - agent_evaluation
    - creative_artifact_scoring
    - cultural_vector_detection
    - semantic_quality_assessment
