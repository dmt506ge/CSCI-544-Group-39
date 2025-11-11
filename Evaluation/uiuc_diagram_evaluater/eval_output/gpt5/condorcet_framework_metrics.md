# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\condorcet_framework.png`
- **Reference**: `..\ground_png\condorcet_framework.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Test time training
- **node2**: Prompt
- **node3**: LLM
- **node4**: Set of answers
- **node5**: Compute empirical probabilities
- **node6**: SNR or entropy based reward calculation
- **node7**: A calculations
- **node8**: Policy update
- **node9**: Inference
- **node10**: Compute SNR for prompt difficulty estimation
- **node11**: MMC stopping criteria
- **node12**: Truncated Beta prior
- **node13**: Updating plug in prior
- **node14**: Counts tracker
- **node15**: s_n t_n o_n
- **node16**: rho_run and rho_oth ratio updates
- **node17**: E process run
- **node18**: E process oth
- **node19**: Stopping rule and budget check
- **node20**: Certify when e_run >= 1/eps and e_oth >= 1/eps
- **node21**: Report certified majority
- **node22**: Abstain
- **node23**: budget reached N_budget

### Edges

- Prompt → Compute empirical probabilities
- rho_run and rho_oth ratio updates → Abstain
- LLM → E process run
- rho_run and rho_oth ratio updates → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Test time training → Stopping rule and budget check
- Updating plug in prior → Counts tracker
- Updating plug in prior → Abstain
- Updating plug in prior → s_n t_n o_n
- Set of answers → E process run
- LLM → Report certified majority
- A calculations → Policy update
- Test time training → Policy update
- Prompt → Counts tracker
- Compute empirical probabilities → Policy update
- Counts tracker → Stopping rule and budget check
- Test time training → Abstain
- Prompt → SNR or entropy based reward calculation
- Set of answers → Compute empirical probabilities
- Test time training → s_n t_n o_n
- Test time training → Certify when e_run >= 1/eps and e_oth >= 1/eps
- LLM → Counts tracker
- Counts tracker → rho_run and rho_oth ratio updates
- Truncated Beta prior → Report certified majority
- Set of answers → Counts tracker
- Set of answers → SNR or entropy based reward calculation
- rho_run and rho_oth ratio updates → E process run
- Prompt → Compute SNR for prompt difficulty estimation
- LLM → Compute SNR for prompt difficulty estimation
- Test time training → E process run
- Updating plug in prior → Report certified majority
- LLM → E process oth
- LLM → MMC stopping criteria
- E process oth → Stopping rule and budget check
- Set of answers → Compute SNR for prompt difficulty estimation
- Test time training → Compute empirical probabilities
- Prompt → Report certified majority
- s_n t_n o_n → Stopping rule and budget check
- Set of answers → MMC stopping criteria
- E process oth → Abstain
- SNR or entropy based reward calculation → A calculations
- s_n t_n o_n → rho_run and rho_oth ratio updates
- E process oth → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Truncated Beta prior → E process oth
- Certify when e_run >= 1/eps and e_oth >= 1/eps → Abstain
- Test time training → Counts tracker
- s_n t_n o_n → Abstain
- Test time training → SNR or entropy based reward calculation
- s_n t_n o_n → Certify when e_run >= 1/eps and e_oth >= 1/eps
- E process run → Stopping rule and budget check
- Set of answers → Report certified majority
- Compute empirical probabilities → SNR or entropy based reward calculation
- Counts tracker → Abstain
- Counts tracker → s_n t_n o_n
- E process run → Abstain
- Counts tracker → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Updating plug in prior → E process oth
- E process run → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Stopping rule and budget check → Abstain
- Test time training → LLM
- Test time training → Compute SNR for prompt difficulty estimation
- Prompt → LLM
- Stopping rule and budget check → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Compute empirical probabilities → Compute SNR for prompt difficulty estimation
- Prompt → E process oth
- Test time training → MMC stopping criteria
- Prompt → MMC stopping criteria
- rho_run and rho_oth ratio updates → Report certified majority
- s_n t_n o_n → E process run
- Prompt → rho_run and rho_oth ratio updates
- LLM → Stopping rule and budget check
- Test time training → Report certified majority
- Set of answers → E process oth
- Counts tracker → E process run
- LLM → rho_run and rho_oth ratio updates
- Counts tracker → Report certified majority
- Prompt → Set of answers
- Set of answers → rho_run and rho_oth ratio updates
- Truncated Beta prior → Stopping rule and budget check
- Stopping rule and budget check → Report certified majority
- LLM → Set of answers
- Truncated Beta prior → rho_run and rho_oth ratio updates
- rho_run and rho_oth ratio updates → E process oth
- Truncated Beta prior → Abstain
- Prompt → A calculations
- SNR or entropy based reward calculation → Policy update
- Truncated Beta prior → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Test time training → Prompt
- Compute SNR for prompt difficulty estimation → MMC stopping criteria
- LLM → A calculations
- Updating plug in prior → Stopping rule and budget check
- Test time training → E process oth
- Compute empirical probabilities → MMC stopping criteria
- Updating plug in prior → rho_run and rho_oth ratio updates
- Set of answers → A calculations
- Prompt → Stopping rule and budget check
- E process oth → Report certified majority
- LLM → Compute empirical probabilities
- Counts tracker → E process oth
- Certify when e_run >= 1/eps and e_oth >= 1/eps → Report certified majority
- Updating plug in prior → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Test time training → rho_run and rho_oth ratio updates
- s_n t_n o_n → Report certified majority
- Prompt → Policy update
- Prompt → Abstain
- Prompt → s_n t_n o_n
- Truncated Beta prior → E process run
- Prompt → Certify when e_run >= 1/eps and e_oth >= 1/eps
- LLM → Policy update
- Set of answers → Stopping rule and budget check
- LLM → Abstain
- LLM → SNR or entropy based reward calculation
- LLM → s_n t_n o_n
- Test time training → Set of answers
- LLM → Certify when e_run >= 1/eps and e_oth >= 1/eps
- E process run → Report certified majority
- Set of answers → Policy update
- Set of answers → Abstain
- Set of answers → s_n t_n o_n
- Set of answers → Certify when e_run >= 1/eps and e_oth >= 1/eps
- Truncated Beta prior → Counts tracker
- Updating plug in prior → E process run
- Truncated Beta prior → s_n t_n o_n
- Test time training → A calculations
- rho_run and rho_oth ratio updates → Stopping rule and budget check
- Compute empirical probabilities → A calculations
- Prompt → E process run
- s_n t_n o_n → E process oth

## Reference Graph

### Nodes

- **node1**: Research Problem
- **node2**: Literature Review
- **node3**: Research Methodology
- **node4**: Data Collection
- **node5**: Data Analysis
- **node6**: Conclusion

### Edges

- Research Problem → Data Collection
- Research Problem → Research Methodology
- Literature Review → Research Methodology
- Literature Review → Data Analysis
- Research Problem → Literature Review
- Research Problem → Data Analysis
- Literature Review → Conclusion
- Research Methodology → Data Collection
- Data Collection → Data Analysis
- Research Methodology → Data Analysis
- Research Problem → Conclusion
- Data Collection → Conclusion
- Literature Review → Data Collection
- Research Methodology → Conclusion
- Data Analysis → Conclusion

## Node Alignment Matches

*(No matches)*

## Path Alignment Matches

*(No matched paths)*