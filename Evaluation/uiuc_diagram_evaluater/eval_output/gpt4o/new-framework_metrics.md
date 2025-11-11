# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\new-framework.png`
- **Reference**: `..\ground_png\new-framework.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.643
- **Recall**: 0.500
- **F1 Score**: 0.563

### Path Alignment
- **Precision**: 0.167
- **Recall**: 0.039
- **F1 Score**: 0.063

## Generated Graph

### Nodes

- **node1**: Server Interaction
- **node2**: Server Aggregation
- **node3**: Global item embedding (C)
- **node4**: Server aggregates models
- **node5**: Personalization
- **node6**: Enforce Difference
- **node7**: Difference enforced to personalize
- **node8**: Local item embedding (Di)
- **node9**: User embedding (ui)
- **node10**: Reconstruction Error
- **node11**: User ratings (ri)
- **node12**: Compute Loss
- **node13**: Predicted user ratings (ri_hat)
- **node14**: Loss computed for optimization

### Edges

- Difference enforced to personalize → Local item embedding (Di)
- Enforce Difference → User embedding (ui)
- Local item embedding (Di) → Loss computed for optimization
- Difference enforced to personalize → Predicted user ratings (ri_hat)
- Compute Loss → Loss computed for optimization
- User ratings (ri) → Loss computed for optimization
- Difference enforced to personalize → User embedding (ui)
- Predicted user ratings (ri_hat) → Loss computed for optimization
- User embedding (ui) → Loss computed for optimization
- Local item embedding (Di) → Compute Loss
- Enforce Difference → Loss computed for optimization
- User ratings (ri) → Compute Loss
- Difference enforced to personalize → Loss computed for optimization
- User embedding (ui) → Compute Loss
- Predicted user ratings (ri_hat) → Compute Loss
- Local item embedding (Di) → Predicted user ratings (ri_hat)
- Enforce Difference → Compute Loss
- Local item embedding (Di) → User embedding (ui)
- User embedding (ui) → Predicted user ratings (ri_hat)
- Enforce Difference → Local item embedding (Di)
- Difference enforced to personalize → Compute Loss
- Enforce Difference → Predicted user ratings (ri_hat)
- Server Aggregation → Global item embedding (C)

## Reference Graph

### Nodes

- **node1**: Server Aggregation
- **node2**: C
- **node3**: Enforce Difference
- **node4**: D(i)
- **node5**: Additive Personalization
- **node6**: ui
- **node7**: Enforce Sparsity
- **node8**: ri
- **node9**: Compute Loss
- **node10**: r̂i
- **node11**: Reconstruction Error
- **node12**: Client i
- **node13**: Legend
- **node14**: ri: User ratings
- **node15**: r̂i: Predicted user ratings
- **node16**: ui: User embedding
- **node17**: D(i): Local item embedding
- **node18**: C: Global item embedding

### Edges

- Additive Personalization → ri
- Enforce Sparsity → ri
- ui → Compute Loss
- C → Enforce Sparsity
- Enforce Difference → D(i)
- Compute Loss → r̂i
- C → ri
- Server Aggregation → C
- ui → r̂i
- Server Aggregation → D(i)
- Additive Personalization → Enforce Sparsity
- Additive Personalization → Compute Loss
- Enforce Sparsity → Compute Loss
- Enforce Difference → Additive Personalization
- C → Compute Loss
- Additive Personalization → r̂i
- D(i) → Additive Personalization
- Enforce Difference → Reconstruction Error
- Server Aggregation → Enforce Difference
- Server Aggregation → Additive Personalization
- Enforce Sparsity → r̂i
- ri → Reconstruction Error
- Server Aggregation → Reconstruction Error
- D(i) → Reconstruction Error
- C → r̂i
- Enforce Difference → Enforce Sparsity
- Enforce Difference → ri
- D(i) → Enforce Sparsity
- Server Aggregation → Enforce Sparsity
- D(i) → ri
- Server Aggregation → ri
- Compute Loss → Reconstruction Error
- ui → Additive Personalization
- Enforce Difference → Compute Loss
- ui → Reconstruction Error
- r̂i → Reconstruction Error
- C → D(i)
- ri → Compute Loss
- Server Aggregation → Compute Loss
- D(i) → Compute Loss
- ui → Enforce Sparsity
- Enforce Difference → r̂i
- ui → ri
- ri → r̂i
- Additive Personalization → Reconstruction Error
- C → Enforce Difference
- C → Additive Personalization
- D(i) → r̂i
- Enforce Sparsity → Reconstruction Error
- Server Aggregation → r̂i
- C → Reconstruction Error

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Server Aggregation | Server Aggregation |
| Global item embedding (C) | C: Global item embedding |
| Enforce Difference | Enforce Difference |
| Local item embedding (Di) | D(i): Local item embedding |
| User embedding (ui) | ui |
| Reconstruction Error | Reconstruction Error |
| User ratings (ri) | ri: User ratings |
| Compute Loss | Compute Loss |
| Predicted user ratings (ri_hat) | r̂i: Predicted user ratings |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Enforce Difference | Compute Loss |
| ui | Compute Loss |