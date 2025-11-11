# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\img-module-single.png`
- **Reference**: `..\ground_png\img-module-single.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.529
- **Recall**: 0.692
- **F1 Score**: 0.600

### Path Alignment
- **Precision**: 0.667
- **Recall**: 0.200
- **F1 Score**: 0.308

## Generated Graph

### Nodes

- **node1**: 2D Image Feature Processing Path
- **node2**: Input feature
(C channels, H x W)
- **node3**: Image Memory
(Temporal Information Storage)
- **node4**: Reorganize
- **node5**: Memory Buffer
(temporal storage)
- **node6**: Shift Out
(channels at t)
- **node7**: Aggregate
(Temporal Fusion)
- **node8**: Shift In
(memory at t-1)
- **node9**: Image Adapter
(2D Convolution)
(dilated/recurrent layers)
- **node10**: Temporal Aggregation
- **node11**: Output features
(with temporal context)
- **node12**: Context Fusion
(3D + 2D Integration)
- **node13**: 3D Context Management Path
- **node14**: 3D Memory
(Global Context)
(spatial + temporal)
- **node15**: Project
- **node16**: Aggregate / Densify
(3D processing grid)
- **node17**: 3D to 2D Adapter
(dimensional transformation)

### Edges

- Aggregate / Densify
(3D processing grid) → 3D to 2D Adapter
(dimensional transformation)
- Reorganize → Memory Buffer
(temporal storage)
- 3D to 2D Adapter
(dimensional transformation) → Temporal Aggregation
- Project → Aggregate / Densify
(3D processing grid)
- Project → Context Fusion
(3D + 2D Integration)
- 3D Memory
(Global Context)
(spatial + temporal) → Project
- Input feature
(C channels, H x W) → Image Memory
(Temporal Information Storage)
- Context Fusion
(3D + 2D Integration) → Temporal Aggregation
- 3D Memory
(Global Context)
(spatial + temporal) → Context Fusion
(3D + 2D Integration)
- 3D Memory
(Global Context)
(spatial + temporal) → Aggregate / Densify
(3D processing grid)
- Shift In
(memory at t-1) → Aggregate
(Temporal Fusion)
- Aggregate / Densify
(3D processing grid) → Context Fusion
(3D + 2D Integration)
- Image Memory
(Temporal Information Storage) → Image Adapter
(2D Convolution)
(dilated/recurrent layers)
- Image Memory
(Temporal Information Storage) → Output features
(with temporal context)
- Project → Temporal Aggregation
- Input feature
(C channels, H x W) → Image Adapter
(2D Convolution)
(dilated/recurrent layers)
- Shift Out
(channels at t) → Memory Buffer
(temporal storage)
- 3D Memory
(Global Context)
(spatial + temporal) → Temporal Aggregation
- Input feature
(C channels, H x W) → Output features
(with temporal context)
- 3D to 2D Adapter
(dimensional transformation) → Context Fusion
(3D + 2D Integration)
- Aggregate / Densify
(3D processing grid) → Temporal Aggregation
- Project → 3D to 2D Adapter
(dimensional transformation)
- Reorganize → Shift Out
(channels at t)
- Image Adapter
(2D Convolution)
(dilated/recurrent layers) → Output features
(with temporal context)
- 3D Memory
(Global Context)
(spatial + temporal) → 3D to 2D Adapter
(dimensional transformation)

## Reference Graph

### Nodes

- **node1**: Input feature
- **node2**: Image memory
- **node3**: Image adapter
- **node4**: 3D memory
- **node5**: 3D to 2D adapter
- **node6**: reorganize
- **node7**: shift
- **node8**: shift in
from memory
- **node9**: shift out
to memory
- **node10**: add
- **node11**: add
- **node12**: project
- **node13**: aggregate
densify

### Edges

- Input feature → shift out
to memory
- shift in
from memory → add
- Input feature → add
- 3D memory → 3D to 2D adapter
- Input feature → shift in
from memory
- shift → Image adapter
- Image memory → shift
- reorganize → shift
- project → 3D to 2D adapter
- Image memory → Image adapter
- reorganize → Image adapter
- Image memory → reorganize
- 3D memory → aggregate
densify
- shift in
from memory → Image adapter
- Input feature → shift
- Input feature → Image adapter
- shift → add
- project → aggregate
densify
- Image memory → shift out
to memory
- Image adapter → add
- shift → shift in
from memory
- 3D memory → project
- Input feature → reorganize
- Image memory → add
- reorganize → add
- Image memory → shift in
from memory
- 3D to 2D adapter → aggregate
densify
- reorganize → shift in
from memory
- Input feature → Image memory
- shift out
to memory → add

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Input feature
(C channels, H x W) | Input feature |
| Image Memory
(Temporal Information Storage) | Image memory |
| Shift Out
(channels at t) | shift out
to memory |
| Shift In
(memory at t-1) | shift in
from memory |
| Image Adapter
(2D Convolution)
(dilated/recurrent layers) | Image adapter |
| Context Fusion
(3D + 2D Integration) | add |
| 3D Memory
(Global Context)
(spatial + temporal) | 3D memory |
| Project | project |
| 3D to 2D Adapter
(dimensional transformation) | 3D to 2D adapter |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Input feature | Image memory |
| Input feature | Image adapter |
| project | 3D to 2D adapter |
| Image memory | Image adapter |
| 3D memory | project |
| 3D memory | 3D to 2D adapter |