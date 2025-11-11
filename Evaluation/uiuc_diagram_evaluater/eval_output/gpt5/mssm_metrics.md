# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\mssm.png`
- **Reference**: `..\ground_png\mssm.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.433
- **Recall**: 0.325
- **F1 Score**: 0.371

### Path Alignment
- **Precision**: 0.061
- **Recall**: 0.039
- **F1 Score**: 0.048

## Generated Graph

### Nodes

- **node1**: Observation
- **node2**: z_theta
- **node3**: Statics Propagation
BEV features
- **node4**: b_hat
- **node5**: b1
- **node6**: x1
- **node7**: Dynamics Memory
- **node8**: Dynamic memory bank with interaction
- **node9**: y_hat1
- **node10**: l_theta
- **node11**: z_1
- **node12**: m_theta
- **node13**: y_hat_T
- **node14**: f_theta
- **node15**: h1
- **node16**: h_T
- **node17**: mu_theta, sigma_theta
prior
- **node18**: s1
- **node19**: mu_phi, sigma_phi
posterior
- **node20**: MLN
- **node21**: s1_T
- **node22**: h_Tplus1
- **node23**: pi_theta
- **node24**: mu_theta, sigma_theta
prior
- **node25**: a_hat_T
- **node26**: s_Tplus1
- **node27**: mu_phi, sigma_phi
posterior
- **node28**: MLN
- **node29**: y_hat_Tplus1
- **node30**: Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation

### Edges

- Statics Propagation
BEV features → f_theta
- z_theta → a_hat_T
- z_1 → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- s1_T → h_Tplus1
- mu_phi, sigma_phi
posterior → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- h_T → h_Tplus1
- h_Tplus1 → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- z_1 → MLN
- b_hat → MLN
- h1 → pi_theta
- m_theta → y_hat_Tplus1
- z_theta → mu_phi, sigma_phi
posterior
- mu_phi, sigma_phi
posterior → MLN
- z_1 → f_theta
- mu_phi, sigma_phi
posterior → MLN
- b_hat → z_1
- z_theta → pi_theta
- h1 → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- b_hat → y_hat_Tplus1
- h1 → MLN
- b_hat → h_Tplus1
- pi_theta → MLN
- h1 → f_theta
- s_Tplus1 → pi_theta
- z_theta → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- mu_theta, sigma_theta
prior → pi_theta
- z_theta → m_theta
- z_theta → MLN
- MLN → y_hat_Tplus1
- z_theta → f_theta
- m_theta → h_T
- s_Tplus1 → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- mu_theta, sigma_theta
prior → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- s_Tplus1 → mu_phi, sigma_phi
posterior
- s_Tplus1 → MLN
- Statics Propagation
BEV features → s1_T
- a_hat_T → y_hat_Tplus1
- b_hat → h_T
- a_hat_T → h_Tplus1
- f_theta → h_Tplus1
- z_1 → s1_T
- Statics Propagation
BEV features → MLN
- s1_T → mu_phi, sigma_phi
posterior
- h_T → mu_phi, sigma_phi
posterior
- Statics Propagation
BEV features → z_1
- z_1 → MLN
- s_Tplus1 → a_hat_T
- m_theta → h_Tplus1
- h_T → mu_theta, sigma_theta
prior
- s1_T → pi_theta
- mu_theta, sigma_theta
prior → a_hat_T
- Statics Propagation
BEV features → y_hat_Tplus1
- h1 → s1_T
- h_T → pi_theta
- Statics Propagation
BEV features → h_Tplus1
- s_Tplus1 → mu_theta, sigma_theta
prior
- z_theta → Statics Propagation
BEV features
- z_theta → s1_T
- z_1 → y_hat_Tplus1
- s1_T → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- y_hat_Tplus1 → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- h_T → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- b_hat → mu_phi, sigma_phi
posterior
- h1 → MLN
- z_1 → h_Tplus1
- z_theta → x1
- s1_T → MLN
- h_T → MLN
- b_hat → mu_theta, sigma_theta
prior
- h_T → f_theta
- b_hat → pi_theta
- z_theta → MLN
- MLN → h_Tplus1
- Statics Propagation
BEV features → b1
- h1 → y_hat_Tplus1
- pi_theta → y_hat_Tplus1
- Statics Propagation
BEV features → h_T
- b_hat → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- pi_theta → h_Tplus1
- z_theta → z_1
- mu_theta, sigma_theta
prior → MLN
- z_theta → y_hat_Tplus1
- z_1 → h_T
- m_theta → h1
- f_theta → mu_phi, sigma_phi
posterior
- s1_T → a_hat_T
- Statics Propagation
BEV features → b_hat
- h_T → a_hat_T
- s_Tplus1 → y_hat_Tplus1
- b_hat → l_theta
- f_theta → pi_theta
- b_hat → h1
- h1 → h_T
- a_hat_T → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- m_theta → mu_phi, sigma_phi
posterior
- f_theta → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- z_theta → b1
- b_hat → a_hat_T
- f_theta → MLN
- m_theta → mu_theta, sigma_theta
prior
- z_theta → h_T
- Statics Propagation
BEV features → mu_phi, sigma_phi
posterior
- h_T → s1_T
- m_theta → pi_theta
- Statics Propagation
BEV features → mu_theta, sigma_theta
prior
- mu_phi, sigma_phi
posterior → y_hat_Tplus1
- Statics Propagation
BEV features → pi_theta
- h_Tplus1 → y_hat_Tplus1
- z_1 → mu_phi, sigma_phi
posterior
- mu_phi, sigma_phi
posterior → h_Tplus1
- m_theta → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- s1_T → MLN
- z_theta → b_hat
- h_T → MLN
- z_1 → mu_theta, sigma_theta
prior
- m_theta → MLN
- Statics Propagation
BEV features → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- m_theta → f_theta
- h1 → h_Tplus1
- f_theta → a_hat_T
- s1_T → y_hat_Tplus1
- h_T → y_hat_Tplus1
- b_hat → m_theta
- b_hat → MLN
- h1 → mu_theta, sigma_theta
prior
- b_hat → f_theta
- z_theta → h_Tplus1
- Statics Propagation
BEV features → l_theta
- MLN → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- Statics Propagation
BEV features → h1
- z_theta → mu_theta, sigma_theta
prior
- mu_theta, sigma_theta
prior → y_hat_Tplus1
- m_theta → a_hat_T
- s_Tplus1 → h_Tplus1
- pi_theta → Temporal aware path via MLN and memory, Spatial aware path via BEV static propagation
- mu_theta, sigma_theta
prior → h_Tplus1
- f_theta → s1_T
- z_1 → h1
- Statics Propagation
BEV features → a_hat_T
- a_hat_T → MLN
- z_1 → a_hat_T
- f_theta → MLN
- m_theta → s1_T
- z_theta → l_theta
- z_theta → h1
- f_theta → y_hat_Tplus1
- z_1 → pi_theta
- h1 → a_hat_T
- Statics Propagation
BEV features → x1
- pi_theta → a_hat_T
- b_hat → s1_T
- m_theta → MLN
- Statics Propagation
BEV features → m_theta
- Statics Propagation
BEV features → MLN
- h1 → mu_phi, sigma_phi
posterior

## Reference Graph

### Nodes

- **node1**: b̂
- **node2**: zθ
- **node3**: Statics Propagation
- **node4**: b'
- **node5**: s₁
- **node6**: s₁
- **node7**: x₁
- **node8**: b₁
- **node9**: h₁
- **node10**: mθ
- **node11**: ŷ₁
- **node12**: â₁
- **node13**: θ
- **node14**: μθ₀, σθ₀
- **node15**: fθ
- **node16**: MIN
- **node17**: Dynamics Memory
- **node18**: aₜ₋₁
- **node19**: xₜ
- **node20**: bₜ
- **node21**: hₜ
- **node22**: mθ
- **node23**: ŷₜ
- **node24**: âₜ
- **node25**: θ
- **node26**: μθ, σθ
- **node27**: fθ
- **node28**: MIN
- **node29**: Dynamics Memory
- **node30**: sₜ
- **node31**: bₜ
- **node32**: hₜ₊₁
- **node33**: mθ
- **node34**: ŷₜ₊₁
- **node35**: âₜ₊₁
- **node36**: θ
- **node37**: μθ, σθ
- **node38**: sₜ₊₁
- **node39**: Observation
- **node40**: Prediction

### Edges

- Dynamics Memory → ŷₜ
- s₁ → MIN
- hₜ → mθ
- Statics Propagation → b'
- Statics Propagation → b₁
- h₁ → MIN
- b' → b₁
- x₁ → b₁
- s₁ → â₁
- Dynamics Memory → mθ
- mθ → âₜ₊₁
- Dynamics Memory → hₜ
- h₁ → â₁
- xₜ → bₜ
- hₜ₊₁ → mθ
- hₜ → âₜ
- h₁ → μθ₀, σθ₀
- s₁ → μθ₀, σθ₀
- Dynamics Memory → MIN
- hₜ → ŷₜ
- μθ₀, σθ₀ → MIN
- h₁ → mθ
- s₁ → mθ
- zθ → Statics Propagation
- Dynamics Memory → sₜ
- h₁ → ŷ₁
- mθ → â₁
- s₁ → ŷ₁
- Dynamics Memory → aₜ₋₁
- Dynamics Memory → âₜ₊₁
- hₜ₊₁ → âₜ₊₁
- mθ → ŷₜ₊₁
- s₁ → h₁
- hₜ → MIN
- b̂ → Statics Propagation
- Dynamics Memory → μθ, σθ
- zθ → b₁
- zθ → b'
- zθ → b̂
- μθ, σθ → MIN
- Dynamics Memory → mθ
- mθ → ŷ₁
- b̂ → b'
- mθ → âₜ
- Dynamics Memory → ŷₜ₊₁
- hₜ₊₁ → ŷₜ₊₁
- mθ → ŷₜ
- hₜ → μθ, σθ
- Dynamics Memory → hₜ₊₁
- Dynamics Memory → âₜ
- b̂ → b₁

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Observation | Observation |
| z_theta | zθ |
| Statics Propagation
BEV features | Statics Propagation |
| b_hat | b̂ |
| Dynamic memory bank with interaction | Dynamics Memory |
| y_hat1 | ŷ₁ |
| l_theta | θ |
| m_theta | mθ |
| f_theta | fθ |
| mu_theta, sigma_theta
prior | μθ, σθ |
| MLN | MIN |
| a_hat_T | âₜ₊₁ |
| y_hat_Tplus1 | ŷₜ₊₁ |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| zθ | b̂ |
| zθ | Statics Propagation |