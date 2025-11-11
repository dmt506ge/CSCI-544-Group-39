# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\condorcet_framework.png`
- **Reference**: `..\ground_png\condorcet_framework.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.143
- **Recall**: 0.333
- **F1 Score**: 0.200

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Prompt
- **node2**: Sample
- **node3**: LLM
- **node4**: Set of Answers
- **node5**: Compute Empirical Probabilities
- **node6**: SNR or Entropy-Based Reward Calc.
- **node7**: A Calculations
- **node8**: Feedback Loop: Generate New Sample
- **node9**: Compute SNR for Prompt Difficulty
- **node10**: MMC Stopping Criteria
- **node11**: GO
- **node12**: STOP
- **node13**: Estimate Probability
- **node14**: Feedback Loop

### Edges

- Prompt → Feedback Loop: Generate New Sample
- Set of Answers → Compute Empirical Probabilities
- Compute SNR for Prompt Difficulty → Estimate Probability
- LLM → Compute Empirical Probabilities
- MMC Stopping Criteria → STOP
- Prompt → SNR or Entropy-Based Reward Calc.
- Prompt → A Calculations
- Prompt → STOP
- SNR or Entropy-Based Reward Calc. → Feedback Loop: Generate New Sample
- Prompt → LLM
- Prompt → Set of Answers
- Set of Answers → GO
- LLM → MMC Stopping Criteria
- Compute Empirical Probabilities → Feedback Loop: Generate New Sample
- LLM → Feedback Loop: Generate New Sample
- Set of Answers → Feedback Loop: Generate New Sample
- Prompt → GO
- SNR or Entropy-Based Reward Calc. → A Calculations
- MMC Stopping Criteria → GO
- Prompt → MMC Stopping Criteria
- Compute Empirical Probabilities → MMC Stopping Criteria
- Prompt → Compute Empirical Probabilities
- Compute Empirical Probabilities → SNR or Entropy-Based Reward Calc.
- Compute Empirical Probabilities → A Calculations
- LLM → SNR or Entropy-Based Reward Calc.
- Set of Answers → SNR or Entropy-Based Reward Calc.
- Compute Empirical Probabilities → STOP
- A Calculations → Feedback Loop: Generate New Sample
- LLM → STOP
- Set of Answers → STOP
- LLM → A Calculations
- Set of Answers → A Calculations
- LLM → Set of Answers
- Compute Empirical Probabilities → GO
- LLM → GO
- Set of Answers → MMC Stopping Criteria

## Reference Graph

### Nodes

- **node1**: Start
- **node2**: Data Collection
- **node3**: Data Processing
- **node4**: Analysis
- **node5**: Results
- **node6**: Conclusion

### Edges

- Data Processing → Analysis
- Start → Data Processing
- Start → Data Collection
- Start → Analysis
- Data Collection → Data Processing
- Analysis → Results
- Start → Results
- Data Collection → Analysis
- Data Processing → Results
- Results → Conclusion
- Data Collection → Results
- Data Collection → Conclusion
- Data Processing → Conclusion
- Analysis → Conclusion
- Start → Conclusion

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Prompt | Start |
| Sample | Data Collection |

## Path Alignment Matches

*(No matched paths)*