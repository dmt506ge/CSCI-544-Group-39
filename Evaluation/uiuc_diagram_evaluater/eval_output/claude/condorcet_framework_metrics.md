# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\condorcet_framework.png`
- **Reference**: `..\ground_png\condorcet_framework.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.053
- **Recall**: 0.100
- **F1 Score**: 0.069

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Test-time training
- **node2**: Training: Adapt terminal distribution via SNR/entropy rewards
- **node3**: Inference
- **node4**: Inference: Sequential sampling with MMC certification
- **node5**: Prompt
- **node6**: LLM
- **node7**: Set of answers Majority Voting/Mode Estimation
- **node8**: Compute e-values Beta/Plug-in priors (theta^*, lambda^*)
- **node9**: SNR or entropy-based reward calculation
- **node10**: Gradient calculations
- **node11**: Prompt
- **node12**: LLM n=1,2,...
- **node13**: Set of answers Majority Voting/Mode Estimation
- **node14**: Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- **node15**: MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- **node16**: Budget Check ABSTAIN if N > N_budget
- **node17**: Estimate probability
- **node18**: Compute SNR for prompt difficulty estimation (monitoring only)
- **node19**: Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others

### Edges

- Compute e-values Truncated Beta Prior OR Updating Plug-in Prior → Budget Check ABSTAIN if N > N_budget
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Set of answers Majority Voting/Mode Estimation
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Prompt
- LLM → Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- Prompt → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- Prompt → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- Prompt → Set of answers Majority Voting/Mode Estimation
- Prompt → Prompt
- Prompt → LLM n=1,2,...
- Prompt → Compute SNR for prompt difficulty estimation (monitoring only)
- Prompt → Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- LLM n=1,2,... → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- Prompt → LLM
- Prompt → Gradient calculations
- LLM n=1,2,... → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- LLM n=1,2,... → Compute SNR for prompt difficulty estimation (monitoring only)
- LLM → Set of answers Majority Voting/Mode Estimation
- LLM n=1,2,... → Estimate probability
- Set of answers Majority Voting/Mode Estimation → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- Prompt → Set of answers Majority Voting/Mode Estimation
- LLM n=1,2,... → Budget Check ABSTAIN if N > N_budget
- Set of answers Majority Voting/Mode Estimation → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- LLM → SNR or entropy-based reward calculation
- Set of answers Majority Voting/Mode Estimation → SNR or entropy-based reward calculation
- Set of answers Majority Voting/Mode Estimation → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- Prompt → Compute e-values Beta/Plug-in priors (theta^*, lambda^*)
- Set of answers Majority Voting/Mode Estimation → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- Set of answers Majority Voting/Mode Estimation → Compute SNR for prompt difficulty estimation (monitoring only)
- Prompt → Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- Set of answers Majority Voting/Mode Estimation → Estimate probability
- Set of answers Majority Voting/Mode Estimation → Compute SNR for prompt difficulty estimation (monitoring only)
- Set of answers Majority Voting/Mode Estimation → Budget Check ABSTAIN if N > N_budget
- LLM n=1,2,... → Set of answers Majority Voting/Mode Estimation
- LLM → Estimate probability
- Set of answers Majority Voting/Mode Estimation → Estimate probability
- LLM → Budget Check ABSTAIN if N > N_budget
- Set of answers Majority Voting/Mode Estimation → Budget Check ABSTAIN if N > N_budget
- Set of answers Majority Voting/Mode Estimation → Gradient calculations
- LLM n=1,2,... → Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- SNR or entropy-based reward calculation → Gradient calculations
- LLM → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- LLM → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- Set of answers Majority Voting/Mode Estimation → Set of answers Majority Voting/Mode Estimation
- Prompt → Estimate probability
- Prompt → Budget Check ABSTAIN if N > N_budget
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → SNR or entropy-based reward calculation
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- LLM → Prompt
- Set of answers Majority Voting/Mode Estimation → Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- Set of answers Majority Voting/Mode Estimation → Prompt
- Prompt → Set of answers Majority Voting/Mode Estimation
- LLM → LLM n=1,2,...
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- Set of answers Majority Voting/Mode Estimation → LLM n=1,2,...
- MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run → Estimate probability
- MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run → Budget Check ABSTAIN if N > N_budget
- LLM → Compute SNR for prompt difficulty estimation (monitoring only)
- LLM → Compute e-values Beta/Plug-in priors (theta^*, lambda^*)
- Set of answers Majority Voting/Mode Estimation → Compute e-values Beta/Plug-in priors (theta^*, lambda^*)
- Set of answers Majority Voting/Mode Estimation → Compute e-values Truncated Beta Prior OR Updating Plug-in Prior
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → LLM n=1,2,...
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Compute SNR for prompt difficulty estimation (monitoring only)
- Prompt → SNR or entropy-based reward calculation
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Estimate probability
- Prompt → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- Compute e-values Truncated Beta Prior OR Updating Plug-in Prior → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- LLM → Gradient calculations
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Budget Check ABSTAIN if N > N_budget
- Prompt → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- Compute e-values Truncated Beta Prior OR Updating Plug-in Prior → MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run
- MMC Stopping Criteria e^run_n (top-2 test) A_n vs. B_n o^oth_n (others test) others vs. top-2 STOP if both e^run_n < ϵ/run → Roll-out (inference) Go/No-Go (partial steps i.o.a, i.o.a, t.o.g.) Top-2: A_n (1st), B_n (2nd), others
- Compute e-values Beta/Plug-in priors (theta^*, lambda^*) → Gradient calculations
- Prompt → LLM n=1,2,...
- Prompt → Compute SNR for prompt difficulty estimation (monitoring only)
- Compute e-values Truncated Beta Prior OR Updating Plug-in Prior → Compute SNR for prompt difficulty estimation (monitoring only)
- Prompt → Estimate probability
- LLM → Set of answers Majority Voting/Mode Estimation
- Prompt → Budget Check ABSTAIN if N > N_budget
- Compute e-values Truncated Beta Prior OR Updating Plug-in Prior → Estimate probability

## Reference Graph

### Nodes

- **node1**: Problem Observation
- **node2**: Research Question
- **node3**: Literature Review
- **node4**: Hypothesis
- **node5**: Research Methodology
- **node6**: Data Collection
- **node7**: Data Analysis
- **node8**: Results
- **node9**: Conclusion
- **node10**: Recommendations

### Edges

- Hypothesis → Results
- Literature Review → Research Methodology
- Literature Review → Data Collection
- Literature Review → Recommendations
- Research Methodology → Data Analysis
- Research Question → Research Methodology
- Research Question → Data Collection
- Research Question → Recommendations
- Data Collection → Results
- Research Methodology → Data Collection
- Data Analysis → Results
- Research Methodology → Recommendations
- Hypothesis → Data Analysis
- Literature Review → Conclusion
- Problem Observation → Hypothesis
- Research Question → Conclusion
- Hypothesis → Research Methodology
- Hypothesis → Data Collection
- Hypothesis → Recommendations
- Research Question → Literature Review
- Problem Observation → Results
- Research Methodology → Conclusion
- Data Collection → Data Analysis
- Problem Observation → Research Question
- Data Analysis → Recommendations
- Data Collection → Recommendations
- Problem Observation → Data Analysis
- Hypothesis → Conclusion
- Literature Review → Hypothesis
- Conclusion → Recommendations
- Research Question → Hypothesis
- Problem Observation → Research Methodology
- Problem Observation → Data Collection
- Problem Observation → Recommendations
- Literature Review → Results
- Results → Recommendations
- Data Collection → Conclusion
- Research Question → Results
- Data Analysis → Conclusion
- Research Methodology → Results
- Results → Conclusion
- Problem Observation → Conclusion
- Literature Review → Data Analysis
- Problem Observation → Literature Review
- Research Question → Data Analysis

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| LLM | Data Collection |

## Path Alignment Matches

*(No matched paths)*