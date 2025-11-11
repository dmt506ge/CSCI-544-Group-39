# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\pc-module-single.png`
- **Reference**: `..\ground_png\pc-module-single.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.357
- **Recall**: 0.385
- **F1 Score**: 0.370

### Path Alignment
- **Precision**: 0.429
- **Recall**: 0.150
- **F1 Score**: 0.222

## Generated Graph

### Nodes

- **node1**: Initial Data
- **node2**: Current Data
- **node3**: Previous Data
- **node4**: Aggregated Data
- **node5**: Output Data
- **node6**: Voxelize Process
- **node7**: Merge Operation
- **node8**: Previous Memory
- **node9**: Updated Memory Store
- **node10**: Query Process
- **node11**: Sparsify Process
- **node12**: Aggregation
- **node13**: Add to Memory
- **node14**: Memory Loop

### Edges

- Aggregation → Aggregation
- Current Data → Memory Loop
- Aggregated Data → Sparsify Process
- Previous Data → Add to Memory
- Voxelize Process → Updated Memory Store
- Aggregated Data → Aggregated Data
- Sparsify Process → Memory Loop
- Add to Memory → Output Data
- Output Data → Sparsify Process
- Memory Loop → Add to Memory
- Output Data → Aggregated Data
- Query Process → Initial Data
- Aggregation → Add to Memory
- Add to Memory → Aggregation
- Current Data → Previous Data
- Sparsify Process → Previous Data
- Previous Memory → Updated Memory Store
- Add to Memory → Add to Memory
- Previous Data → Memory Loop
- Memory Loop → Memory Loop
- Aggregated Data → Output Data
- Aggregation → Memory Loop
- Output Data → Output Data
- Current Data → Sparsify Process
- Previous Data → Previous Data
- Aggregated Data → Aggregation
- Current Data → Aggregated Data
- Sparsify Process → Sparsify Process
- Sparsify Process → Aggregated Data
- Memory Loop → Previous Data
- Output Data → Aggregation
- Merge Operation → Updated Memory Store
- Add to Memory → Memory Loop
- Aggregation → Previous Data
- Aggregated Data → Add to Memory
- Aggregation → Output Data
- Output Data → Add to Memory
- Add to Memory → Previous Data
- Previous Data → Sparsify Process
- Memory Loop → Sparsify Process
- Previous Data → Aggregated Data
- Memory Loop → Aggregated Data
- Current Data → Output Data
- Sparsify Process → Output Data
- Aggregation → Sparsify Process
- Aggregated Data → Memory Loop
- Aggregation → Aggregated Data
- Current Data → Aggregation
- Sparsify Process → Aggregation
- Output Data → Memory Loop
- Memory Loop → Aggregation
- Voxelize Process → Merge Operation
- Add to Memory → Sparsify Process
- Add to Memory → Aggregated Data
- Current Data → Add to Memory
- Aggregated Data → Previous Data
- Sparsify Process → Add to Memory
- Previous Data → Output Data
- Memory Loop → Output Data
- Output Data → Previous Data
- Previous Data → Aggregation

## Reference Graph

### Nodes

- **node1**: Input feature
- **node2**: sparsify
- **node3**: aggregate
- **node4**: map
- **node5**: add
- **node6**: query
- **node7**: Point cloud adapter
- **node8**: voxelize
- **node9**: merge
- **node10**: update
- **node11**: previous memory
- **node12**: updated memory
- **node13**: Point cloud memory

### Edges

- Input feature → map
- sparsify → aggregate
- voxelize → merge
- map → add
- Input feature → add
- voxelize → update
- sparsify → map
- previous memory → merge
- voxelize → updated memory
- previous memory → update
- Input feature → sparsify
- aggregate → map
- sparsify → add
- update → updated memory
- previous memory → updated memory
- Input feature → query
- Input feature → aggregate
- aggregate → add
- merge → update
- merge → updated memory

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Voxelize Process | voxelize |
| Merge Operation | merge |
| Previous Data | previous memory |
| Updated Memory Store | updated memory |
| Sparsify Process | sparsify |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| voxelize | updated memory |
| voxelize | merge |
| merge | updated memory |