# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\mssm.png`
- **Reference**: `..\ground_png\mssm.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.222
- **Recall**: 0.303
- **F1 Score**: 0.256

### Path Alignment
- **Precision**: 0.346
- **Recall**: 0.076
- **F1 Score**: 0.124

## Generated Graph

### Nodes

- **node1**: Memory State-Space Model (MSSM) Architecture
- **node2**: z_theta
- **node3**: Observation Input
- **node4**: Statics Propagation
- **node5**: BEV Feature Extract
- **node6**: Spatial Encoding
- **node7**: b-hat
- **node8**: o_1
- **node9**: b_1
- **node10**: x_1
- **node11**: Task Prompt (task-specific)
- **node12**: a_0
- **node13**: h_1
- **node14**: s_1
- **node15**: mu_phi, sigma_phi
- **node16**: (q_phi)
- **node17**: Dynamics Memory Bank Module
- **node18**: Temporal-Aware Encoding
- **node19**: MLN Integration
- **node20**: Memory Interaction and Update
- **node21**: t=1
- **node22**: t=T
- **node23**: t=T+1
- **node24**: h_T
- **node25**: s_T
- **node26**: h_T+1
- **node27**: s_T+1
- **node28**: mu_theta, sigma_theta
- **node29**: (q_theta)
- **node30**: KL(p_phi | p_theta)
- **node31**: y-hat_1
- **node32**: (3D occupancy)
- **node33**: y-hat_T
- **node34**: y-hat_T+1
- **node35**: l_theta
- **node36**: pi_theta
- **node37**: a-hat_T
- **node38**: (action)
- **node39**: pi_theta
- **node40**: a-hat_T+1
- **node41**: pi_theta
- **node42**: State Processing (MSSM Core)
- **node43**: Prediction Outputs
- **node44**: Observation Process
- **node45**: MLN

### Edges

- mu_theta, sigma_theta → y-hat_T
- a_0 → s_T
- Statics Propagation → x_1
- h_1 → s_T+1
- z_theta → h_T+1
- z_theta → Statics Propagation
- Spatial Encoding → b-hat
- x_1 → s_T+1
- BEV Feature Extract → h_T+1
- BEV Feature Extract → Statics Propagation
- Task Prompt (task-specific) → h_T
- MLN Integration → h_T
- mu_theta, sigma_theta → Dynamics Memory Bank Module
- o_1 → y-hat_T+1
- (q_theta) → h_1
- pi_theta → (action)
- Spatial Encoding → h_1
- (q_theta) → s_T
- pi_theta → a-hat_T+1
- KL(p_phi | p_theta) → s_T
- Spatial Encoding → s_T
- Observation Input → s_1
- x_1 → h_1
- x_1 → h_T+1
- mu_phi, sigma_phi → s_1
- KL(p_phi | p_theta) → y-hat_T+1
- o_1 → y-hat_T
- Task Prompt (task-specific) → s_1
- a_0 → y-hat_T
- h_1 → h_T
- mu_phi, sigma_phi → s_T
- s_1 → s_T
- x_1 → h_T
- Temporal-Aware Encoding → s_T+1
- Spatial Encoding → b_1
- Observation Input → b-hat
- (q_theta) → y-hat_T
- (q_phi) → s_T+1
- z_theta → s_1
- KL(p_phi | p_theta) → y-hat_T
- Memory Interaction and Update → h_T+1
- Temporal-Aware Encoding → h_T+1
- Observation Input → s_T
- KL(p_phi | p_theta) → Dynamics Memory Bank Module
- o_1 → x_1
- b_1 → y-hat_T+1
- (q_phi) → h_1
- h_1 → s_1
- (q_phi) → h_T+1
- x_1 → s_1
- mu_phi, sigma_phi → y-hat_T
- Task Prompt (task-specific) → s_T
- mu_phi, sigma_phi → (q_phi)
- s_1 → y-hat_T
- MLN Integration → s_T
- Statics Propagation → s_T+1
- s_T → y-hat_T+1
- BEV Feature Extract → s_T+1
- z_theta → b-hat
- BEV Feature Extract → b-hat
- Observation Input → b_1
- (q_phi) → h_T
- z_theta → h_1
- MLN Integration → y-hat_T+1
- h_T+1 → y-hat_T+1
- l_theta → (action)
- Statics Propagation → h_T+1
- BEV Feature Extract → h_1
- Observation Input → y-hat_T
- s_T → y-hat_T
- a_0 → y-hat_T+1
- h_T → h_T+1
- h_1 → s_T
- Temporal-Aware Encoding → s_1
- mu_theta, sigma_theta → s_T+1
- b-hat → s_T+1
- x_1 → s_T
- Task Prompt (task-specific) → y-hat_T
- MLN Integration → y-hat_T
- z_theta → h_T
- (q_phi) → s_1
- BEV Feature Extract → h_T
- b_1 → x_1
- Dynamics Memory Bank Module → s_T+1
- MLN Integration → Dynamics Memory Bank Module
- (q_theta) → y-hat_T+1
- b-hat → h_1
- z_theta → b_1
- Spatial Encoding → y-hat_T+1
- h_1 → y-hat_T+1
- mu_theta, sigma_theta → h_T+1
- BEV Feature Extract → b_1
- b-hat → h_T+1
- a-hat_T+1 → (action)
- Dynamics Memory Bank Module → h_T+1
- Memory Interaction and Update → s_T+1
- mu_phi, sigma_phi → y-hat_T+1
- Memory Interaction and Update → h_1
- Spatial Encoding → y-hat_T
- h_1 → y-hat_T
- b-hat → h_T
- BEV Feature Extract → s_1
- s_1 → y-hat_T+1
- Temporal-Aware Encoding → h_1
- x_1 → y-hat_T
- (q_theta) → Dynamics Memory Bank Module
- Dynamics Memory Bank Module → h_T
- b-hat → b_1
- o_1 → h_T+1
- (q_phi) → s_T
- Observation Input → y-hat_T+1
- Memory Interaction and Update → h_T
- Temporal-Aware Encoding → h_T
- mu_phi, sigma_phi → Dynamics Memory Bank Module
- Statics Propagation → b-hat
- mu_theta, sigma_theta → s_1
- b-hat → s_1
- Spatial Encoding → x_1
- KL(p_phi | p_theta) → h_T+1
- Task Prompt (task-specific) → a_0
- l_theta → pi_theta
- Statics Propagation → h_1
- Task Prompt (task-specific) → y-hat_T+1
- Dynamics Memory Bank Module → s_1
- pi_theta → a-hat_T
- z_theta → s_T
- BEV Feature Extract → s_T
- b_1 → s_T+1
- (q_phi) → y-hat_T
- Memory Interaction and Update → s_1
- mu_theta, sigma_theta → (q_theta)
- z_theta → y-hat_T+1
- (q_phi) → Dynamics Memory Bank Module
- BEV Feature Extract → y-hat_T+1
- Statics Propagation → h_T
- mu_theta, sigma_theta → h_1
- b_1 → h_T+1
- s_T → s_T+1
- Statics Propagation → b_1
- b-hat → s_T
- x_1 → y-hat_T+1
- Observation Input → x_1
- Dynamics Memory Bank Module → h_1
- MLN Integration → s_T+1
- z_theta → y-hat_T
- Dynamics Memory Bank Module → s_T
- y-hat_1 → (3D occupancy)
- BEV Feature Extract → y-hat_T
- b_1 → h_T
- o_1 → s_T+1
- Statics Propagation → s_1
- mu_theta, sigma_theta → h_T
- h_T → y-hat_T
- a_0 → s_T+1
- MLN Integration → h_T+1
- Memory Interaction and Update → s_T
- Temporal-Aware Encoding → s_T
- o_1 → h_1
- (q_theta) → s_T+1
- a_0 → h_T+1
- KL(p_phi | p_theta) → s_T+1
- Spatial Encoding → s_T+1
- b-hat → y-hat_T
- z_theta → x_1
- Temporal-Aware Encoding → y-hat_T+1
- Memory Interaction and Update → y-hat_T+1
- BEV Feature Extract → x_1
- b_1 → s_1
- Dynamics Memory Bank Module → y-hat_T
- KL(p_phi | p_theta) → h_1
- (q_phi) → y-hat_T+1
- (q_theta) → h_T+1
- a-hat_T → (action)
- o_1 → h_T
- Spatial Encoding → h_T+1
- Spatial Encoding → Statics Propagation
- h_1 → h_T+1
- a_0 → h_T
- mu_phi, sigma_phi → s_T+1
- o_1 → b_1
- Statics Propagation → s_T
- Memory Interaction and Update → y-hat_T
- s_1 → s_T+1
- Temporal-Aware Encoding → y-hat_T
- pi_theta → (action)
- Memory Interaction and Update → Dynamics Memory Bank Module
- Temporal-Aware Encoding → Dynamics Memory Bank Module
- mu_phi, sigma_phi → h_1
- b-hat → x_1
- MLN Integration → s_1
- s_T+1 → y-hat_T+1
- (q_theta) → h_T
- mu_phi, sigma_phi → h_T+1
- Spatial Encoding → h_T
- KL(p_phi | p_theta) → h_T
- Statics Propagation → y-hat_T+1
- Observation Input → s_T+1
- o_1 → s_1
- b_1 → h_1
- a_0 → s_1
- b_1 → s_T
- h_T → y-hat_T+1
- mu_theta, sigma_theta → s_T
- Observation Input → h_1
- mu_phi, sigma_phi → h_T
- Observation Input → h_T+1
- Observation Input → Statics Propagation
- Statics Propagation → y-hat_T
- Task Prompt (task-specific) → s_T+1
- (q_theta) → s_1
- KL(p_phi | p_theta) → s_1
- Spatial Encoding → s_1
- mu_theta, sigma_theta → y-hat_T+1
- b-hat → y-hat_T+1
- Task Prompt (task-specific) → h_1
- MLN Integration → h_1
- Task Prompt (task-specific) → h_T+1
- Dynamics Memory Bank Module → y-hat_T+1
- Observation Input → h_T
- z_theta → s_T+1
- l_theta → a-hat_T
- o_1 → s_T
- a_0 → h_1
- b_1 → y-hat_T

## Reference Graph

### Nodes

- **node1**: b̂
- **node2**: zθ
- **node3**: Statics Propagation
- **node4**: b'
- **node5**: b₁
- **node6**: x₁
- **node7**: âₜ₋₁
- **node8**: h₁
- **node9**: mθ
- **node10**: fθ
- **node11**: Dynamics Memory
- **node12**: âₜ
- **node13**: ŷₜ
- **node14**: μθₑ, σθₑ
- **node15**: s₁
- **node16**: min KL
- **node17**: μθ₀, σθ₀
- **node18**: sₜ₋₁
- **node19**: hₜ
- **node20**: fθ
- **node21**: min KL
- **node22**: sₜ
- **node23**: μθ₀, σθ₀
- **node24**: bₜ
- **node25**: aₜ₋₁
- **node26**: χₜ
- **node27**: sₜ₊₁
- **node28**: ŷₜ₊₁
- **node29**: âₜ₊₁
- **node30**: μθ₀, σθ₀
- **node31**: hₜ₊₁
- **node32**: Dynamics Memory
- **node33**: mθ

### Edges

- mθ → min KL
- s₁ → hₜ
- b' → fθ
- fθ → hₜ₊₁
- sₜ₋₁ → hₜ₊₁
- b₁ → fθ
- min KL → s₁
- Statics Propagation → h₁
- Statics Propagation → hₜ
- fθ → fθ
- h₁ → mθ
- h₁ → min KL
- hₜ → hₜ
- b₁ → s₁
- b' → hₜ₊₁
- x₁ → mθ
- âₜ₊₁ → mθ
- x₁ → min KL
- fθ → fθ
- sₜ₋₁ → fθ
- h₁ → fθ
- zθ → b̂
- mθ → hₜ₊₁
- âₜ₋₁ → s₁
- min KL → fθ
- Statics Propagation → b₁
- fθ → h₁
- fθ → hₜ
- s₁ → mθ
- s₁ → min KL
- Statics Propagation → mθ
- Dynamics Memory → ŷₜ₊₁
- b' → fθ
- Statics Propagation → mθ
- Statics Propagation → min KL
- h₁ → hₜ₊₁
- bₜ → fθ
- hₜ → mθ
- Dynamics Memory → âₜ₊₁
- mθ → fθ
- min KL → hₜ
- âₜ₊₁ → hₜ₊₁
- x₁ → hₜ₊₁
- aₜ₋₁ → sₜ
- b' → s₁
- b₁ → mθ
- âₜ₋₁ → fθ
- μθ₀, σθ₀ → fθ
- fθ → mθ
- s₁ → hₜ₊₁
- x₁ → mθ
- b₁ → h₁
- fθ → mθ
- b₁ → hₜ
- fθ → min KL
- h₁ → fθ
- bₜ → hₜ
- μθ₀, σθ₀ → s₁
- Statics Propagation → hₜ₊₁
- x₁ → fθ
- âₜ₋₁ → hₜ
- Dynamics Memory → âₜ
- hₜ → hₜ₊₁
- μθ₀, σθ₀ → hₜ
- h₁ → s₁
- min KL → mθ
- min KL → min KL
- fθ → hₜ
- sₜ₋₁ → hₜ
- mθ → fθ
- b' → mθ
- fθ → hₜ₊₁
- Statics Propagation → fθ
- b₁ → mθ
- aₜ₋₁ → χₜ
- b₁ → min KL
- s₁ → s₁
- b' → h₁
- bₜ → mθ
- b' → hₜ
- hₜ → fθ
- mθ → s₁
- Statics Propagation → s₁
- âₜ₋₁ → mθ
- âₜ₋₁ → min KL
- b₁ → fθ
- Dynamics Memory → mθ
- μθ₀, σθ₀ → mθ
- mθ → h₁
- mθ → hₜ
- μθ₀, σθ₀ → min KL
- min KL → hₜ₊₁
- x₁ → fθ
- fθ → fθ
- h₁ → mθ
- fθ → mθ
- sₜ₋₁ → mθ
- b' → b₁
- s₁ → fθ
- b₁ → hₜ₊₁
- h₁ → h₁
- sₜ₊₁ → min KL
- h₁ → hₜ
- hₜ₊₁ → mθ
- x₁ → s₁
- fθ → s₁
- bₜ → hₜ₊₁
- Statics Propagation → b'
- Statics Propagation → fθ
- b' → mθ
- b' → min KL
- x₁ → h₁
- x₁ → hₜ
- âₜ₋₁ → hₜ₊₁
- Dynamics Memory → ŷₜ
- mθ → mθ
- μθ₀, σθ₀ → hₜ₊₁
- Dynamics Memory → hₜ₊₁
- mθ → mθ

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| z_theta | zθ |
| Statics Propagation | Statics Propagation |
| b-hat | b̂ |
| b_1 | b₁ |
| x_1 | x₁ |
| h_1 | h₁ |
| s_1 | s₁ |
| Dynamics Memory Bank Module | Dynamics Memory |
| mu_theta, sigma_theta | μθₑ, σθₑ |
| y-hat_1 | ŷₜ |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| zθ | b̂ |
| Statics Propagation | s₁ |
| Statics Propagation | b₁ |
| Statics Propagation | h₁ |
| b₁ | s₁ |
| b₁ | h₁ |
| x₁ | s₁ |
| x₁ | h₁ |
| h₁ | s₁ |