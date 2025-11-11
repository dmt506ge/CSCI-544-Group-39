# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\over-arch-double2.png`
- **Reference**: `..\ground_png\over-arch-double2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.333
- **Recall**: 0.312
- **F1 Score**: 0.323

### Path Alignment
- **Precision**: 1.000
- **Recall**: 0.016
- **F1 Score**: 0.032

## Generated Graph

### Nodes

- **node1**: Image t
- **node2**: RGB-D Backbone
- **node3**: Task Head
- **node4**: Image Backbone
- **node5**: Image t+1
- **node6**: RGB-D Backbone
- **node7**: Task Head
- **node8**: Pointcloud Backbone
- **node9**: Fusion
- **node10**: Memory
- **node11**: Adapter
- **node12**: 3D-to-2D Adapter
- **node13**: Y
- **node14**: O
- **node15**: Temporal Aggregation

### Edges

- RGB-D Backbone → Task Head
- Adapter → 3D-to-2D Adapter
- Image t → Task Head
- RGB-D Backbone → Pointcloud Backbone
- 3D-to-2D Adapter → O
- Y → O
- Image t+1 → Pointcloud Backbone
- Image t+1 → RGB-D Backbone
- RGB-D Backbone → Image Backbone
- Image t → Image Backbone
- Memory → O
- Adapter → Y
- Image t → RGB-D Backbone
- Task Head → Image Backbone
- RGB-D Backbone → Task Head
- Memory → 3D-to-2D Adapter
- Image t+1 → Task Head
- 3D-to-2D Adapter → Y
- Task Head → Pointcloud Backbone
- Memory → Adapter
- Memory → Y
- Adapter → O
- Fusion → Temporal Aggregation

## Reference Graph

### Nodes

- **node1**: input t-1
- **node2**: Image Backbone
- **node3**: Detailed
- **node4**: 3D-2D-adapter
- **node5**: I-memory
- **node6**: I-adapter
- **node7**: input t
- **node8**: Pointcloud Backbone
- **node9**: Detailed
- **node10**: P-memory
- **node11**: P-adapter
- **node12**: 3D-2D-adapter
- **node13**: Task Head
- **node14**: result t-1
- **node15**: Fusion
- **node16**: result t

### Edges

- I-memory → Fusion
- Pointcloud Backbone → P-adapter
- I-adapter → Task Head
- Pointcloud Backbone → Task Head
- input t → result t-1
- 3D-2D-adapter → result t-1
- input t → result t
- 3D-2D-adapter → Task Head
- P-adapter → Fusion
- Task Head → result t-1
- 3D-2D-adapter → I-adapter
- Task Head → result t
- 3D-2D-adapter → result t
- I-memory → Task Head
- Image Backbone → result t-1
- I-memory → I-adapter
- Image Backbone → result t
- input t-1 → result t-1
- P-memory → result t-1
- input t-1 → result t
- P-adapter → Task Head
- input t-1 → Image Backbone
- input t → P-memory
- P-memory → result t
- 3D-2D-adapter → P-memory
- result t-1 → Fusion
- input t → Fusion
- Task Head → Fusion
- 3D-2D-adapter → Fusion
- Image Backbone → I-memory
- I-adapter → result t-1
- I-adapter → result t
- Image Backbone → Fusion
- input t-1 → I-memory
- Pointcloud Backbone → result t-1
- input t-1 → Fusion
- input t → P-adapter
- 3D-2D-adapter → P-adapter
- 3D-2D-adapter → result t-1
- Pointcloud Backbone → result t
- P-memory → Fusion
- input t → Task Head
- I-memory → result t-1
- input t → Pointcloud Backbone
- 3D-2D-adapter → result t
- 3D-2D-adapter → Task Head
- Image Backbone → Task Head
- Image Backbone → I-adapter
- I-memory → result t
- P-memory → P-adapter
- result t → Fusion
- I-adapter → Fusion
- Pointcloud Backbone → P-memory
- input t-1 → Task Head
- P-memory → Task Head
- input t-1 → I-adapter
- P-adapter → result t-1
- P-adapter → result t
- Pointcloud Backbone → Fusion
- 3D-2D-adapter → I-memory
- 3D-2D-adapter → Fusion

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| RGB-D Backbone | Image Backbone |
| Task Head | Task Head |
| Pointcloud Backbone | Pointcloud Backbone |
| Fusion | Fusion |
| 3D-to-2D Adapter | 3D-2D-adapter |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Image Backbone | Task Head |