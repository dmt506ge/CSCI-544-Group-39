# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\mssm.png`
- **Reference**: `..\ground_png\mssm.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.263
- **Recall**: 0.139
- **F1 Score**: 0.182

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: z_theta
- **node2**: Statics Propagation
- **node3**: b_hat
- **node4**: b1
- **node5**: x1
- **node6**: Dynamics Memory
- **node7**: h1
- **node8**: h_T
- **node9**: h_T+1
- **node10**: y_hat1
- **node11**: y_hatT
- **node12**: y_hatT+1
- **node13**: s1
- **node14**: mu_phi, sigma_phi
- **node15**: s_T
- **node16**: mu_theta, sigma_theta
- **node17**: s_T+1
- **node18**: a_hatT
- **node19**: a_hatT+1

### Edges

- b1 → x1
- h_T → h_T+1
- Statics Propagation → b_hat
- h1 → y_hat1
- Statics Propagation → x1
- h1 → h_T+1
- z_theta → b_hat
- z_theta → x1
- Dynamics Memory → y_hat1
- s_T → mu_theta, sigma_theta
- Dynamics Memory → h_T+1
- h_T → y_hatT+1
- z_theta → Statics Propagation
- h1 → h_T
- h1 → y_hatT+1
- b_hat → b1
- h_T → y_hatT
- Dynamics Memory → h_T
- Dynamics Memory → h1
- Dynamics Memory → y_hatT+1
- h1 → y_hatT
- b_hat → x1
- Statics Propagation → b1
- Dynamics Memory → y_hatT
- h_T+1 → y_hatT+1
- s1 → mu_phi, sigma_phi
- z_theta → b1

## Reference Graph

### Nodes

- **node1**: b̂
- **node2**: Statics Propagation
- **node3**: zₑ
- **node4**: bʼ
- **node5**: b₁
- **node6**: x₁
- **node7**: h₁
- **node8**: mₑ
- **node9**: ŷ₁
- **node10**: â₁
- **node11**: Dynamics Memory
- **node12**: lₑ
- **node13**: πₑ
- **node14**: s₁
- **node15**: µₑ, σₑ
- **node16**: µₑ, σₑ
- **node17**: sₜ
- **node18**: bₜ
- **node19**: xₜ
- **node20**: hₜ
- **node21**: mₑ
- **node22**: ŷₜ
- **node23**: âₜ
- **node24**: Dynamics Memory
- **node25**: aₜ₋₁
- **node26**: min KL
- **node27**: Tν
- **node28**: fₑ
- **node29**: sₜ₊₁
- **node30**: hₜ₊₁
- **node31**: mₑ
- **node32**: ŷₜ₊₁
- **node33**: âₜ₊₁
- **node34**: Dynamics Memory
- **node35**: Observation
- **node36**: Prediction

### Edges

- bₜ → Dynamics Memory
- µₑ, σₑ → âₜ
- xₜ → sₜ₊₁
- h₁ → â₁
- mₑ → sₜ
- s₁ → Dynamics Memory
- h₁ → ŷ₁
- bʼ → sₜ₊₁
- µₑ, σₑ → µₑ, σₑ
- xₜ → âₜ₊₁
- xₜ → πₑ
- b̂ → s₁
- µₑ, σₑ → s₁
- bʼ → πₑ
- sₜ → ŷₜ
- hₜ₊₁ → ŷₜ₊₁
- mₑ → µₑ, σₑ
- bₜ → ŷₜ₊₁
- b̂ → Dynamics Memory
- µₑ, σₑ → Dynamics Memory
- hₜ → πₑ
- mₑ → s₁
- bₜ → sₜ₊₁
- hₜ → Dynamics Memory
- Statics Propagation → hₜ₊₁
- mₑ → Dynamics Memory
- hₜ₊₁ → âₜ₊₁
- x₁ → ŷₜ₊₁
- hₜ₊₁ → πₑ
- bₜ → âₜ₊₁
- Statics Propagation → Dynamics Memory
- bₜ → πₑ
- b₁ → h₁
- ŷₜ → πₑ
- Dynamics Memory → hₜ
- Statics Propagation → bₜ
- b₁ → µₑ, σₑ
- x₁ → sₜ₊₁
- Dynamics Memory → âₜ
- sₜ → πₑ
- Statics Propagation → bʼ
- µₑ, σₑ → ŷₜ
- x₁ → âₜ₊₁
- x₁ → πₑ
- zₑ → Statics Propagation
- sₜ → Dynamics Memory
- µₑ, σₑ → hₜ
- b₁ → πₑ
- Tν → Dynamics Memory
- b̂ → h₁
- µₑ, σₑ → h₁
- s₁ → πₑ
- bʼ → ŷₜ₊₁
- b̂ → µₑ, σₑ
- ŷ₁ → πₑ
- b̂ → b₁
- mₑ → πₑ
- min KL → ŷₜ₊₁
- mₑ → h₁
- µₑ, σₑ → sₜ
- Dynamics Memory → hₜ₊₁
- mₑ → Dynamics Memory
- Tν → ŷₜ₊₁
- sₜ₊₁ → hₜ₊₁
- min KL → Tν
- b₁ → ŷ₁
- µₑ, σₑ → πₑ
- b̂ → πₑ
- µₑ, σₑ → πₑ
- s₁ → â₁
- sₜ₊₁ → Dynamics Memory
- zₑ → bʼ
- s₁ → ŷ₁
- ŷ₁ → â₁
- min KL → âₜ₊₁
- min KL → πₑ
- mₑ → πₑ
- Dynamics Memory → ŷₜ
- Tν → âₜ₊₁
- Tν → πₑ
- â₁ → πₑ
- µₑ, σₑ → â₁
- âₜ → πₑ
- b̂ → ŷ₁
- µₑ, σₑ → ŷ₁
- mₑ → â₁
- mₑ → ŷ₁
- Statics Propagation → ŷₜ₊₁
- x₁ → xₜ
- Statics Propagation → sₜ₊₁
- Dynamics Memory → πₑ
- zₑ → hₜ₊₁
- Dynamics Memory → Dynamics Memory
- Statics Propagation → âₜ₊₁
- zₑ → Dynamics Memory
- Statics Propagation → πₑ
- xₜ → hₜ₊₁
- b₁ → â₁
- Dynamics Memory → Dynamics Memory
- zₑ → bₜ
- xₜ → Dynamics Memory
- bʼ → hₜ₊₁
- bʼ → Dynamics Memory
- xₜ → bₜ
- µₑ, σₑ → Dynamics Memory
- bʼ → bₜ
- h₁ → Dynamics Memory
- hₜ₊₁ → hₜ₊₁
- hₜ → ŷₜ
- b̂ → â₁
- sₜ₊₁ → ŷₜ₊₁
- zₑ → sₜ₊₁
- bₜ → hₜ₊₁
- hₜ₊₁ → Dynamics Memory
- hₜ → hₜ
- zₑ → âₜ₊₁
- hₜ → âₜ
- zₑ → πₑ
- Dynamics Memory → âₜ₊₁
- mₑ → µₑ, σₑ
- Dynamics Memory → πₑ
- x₁ → hₜ₊₁
- sₜ₊₁ → âₜ₊₁
- âₜ₊₁ → πₑ
- sₜ₊₁ → πₑ
- x₁ → Dynamics Memory
- bʼ → âₜ₊₁
- ŷₜ → âₜ
- x₁ → bₜ
- sₜ → hₜ
- sₜ → âₜ
- mₑ → ŷₜ
- h₁ → πₑ
- zₑ → ŷₜ₊₁
- s₁ → h₁
- mₑ → hₜ
- min KL → hₜ₊₁
- ŷₜ₊₁ → âₜ₊₁
- ŷₜ₊₁ → πₑ
- s₁ → µₑ, σₑ
- b₁ → s₁
- mₑ → âₜ
- min KL → Dynamics Memory
- xₜ → ŷₜ₊₁
- Dynamics Memory → ŷₜ₊₁
- Tν → hₜ₊₁
- b₁ → Dynamics Memory
- s₁ → s₁

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Statics Propagation | Statics Propagation |
| Dynamics Memory | Dynamics Memory |
| h1 | h₁ |
| mu_phi, sigma_phi | µₑ, σₑ |
| a_hatT+1 | âₜ₊₁ |

## Path Alignment Matches

*(No matched paths)*