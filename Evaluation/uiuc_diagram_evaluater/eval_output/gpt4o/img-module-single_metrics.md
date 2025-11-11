# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\img-module-single.png`
- **Reference**: `..\ground_png\img-module-single.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.833
- **Recall**: 0.385
- **F1 Score**: 0.526

### Path Alignment
- **Precision**: 0.667
- **Recall**: 0.093
- **F1 Score**: 0.163

## Generated Graph

### Nodes

- **node1**: Input Feature
- **node2**: Image Memory
Reorganize
Add & Shift
Temporal Agg.
- **node3**: Image Adapter
Integrate
- **node4**: 3D Memory
Stores Temporal Context
- **node5**: Processing Grid
Project
Aggregate
Enhance
- **node6**: 3D to 2D Adapter
Adapt 3D to 2D

### Edges

- Input Feature → Image Adapter
Integrate
- 3D Memory
Stores Temporal Context → Processing Grid
Project
Aggregate
Enhance
- Image Memory
Reorganize
Add & Shift
Temporal Agg. → Processing Grid
Project
Aggregate
Enhance
- 3D Memory
Stores Temporal Context → 3D to 2D Adapter
Adapt 3D to 2D
- Image Memory
Reorganize
Add & Shift
Temporal Agg. → 3D to 2D Adapter
Adapt 3D to 2D
- Input Feature → Processing Grid
Project
Aggregate
Enhance
- Input Feature → 3D to 2D Adapter
Adapt 3D to 2D
- Processing Grid
Project
Aggregate
Enhance → 3D to 2D Adapter
Adapt 3D to 2D
- Input Feature → Image Memory
Reorganize
Add & Shift
Temporal Agg.
- Image Memory
Reorganize
Add & Shift
Temporal Agg. → Image Adapter
Integrate

## Reference Graph

### Nodes

- **node1**: Input feature
- **node2**: Image memory
- **node3**: Image adapter
- **node4**: 3D memory
- **node5**: 3D to 2D adapter
- **node6**: shift in from memory
- **node7**: reorganize
- **node8**: shift
- **node9**: shift out to memory
- **node10**: add
- **node11**: project
- **node12**: aggregate
- **node13**: densify

### Edges

- aggregate → 3D to 2D adapter
- shift → shift out to memory
- Input feature → shift out to memory
- densify → densify
- 3D to 2D adapter → aggregate
- shift in from memory → Image adapter
- Image memory → shift in from memory
- project → aggregate
- shift in from memory → shift in from memory
- 3D memory → densify
- Image memory → shift
- reorganize → add
- aggregate → aggregate
- Image memory → shift out to memory
- 3D memory → project
- shift in from memory → shift out to memory
- shift in from memory → shift
- shift → add
- Input feature → add
- densify → 3D to 2D adapter
- Input feature → reorganize
- shift out to memory → add
- Image memory → add
- 3D to 2D adapter → densify
- project → densify
- Image memory → reorganize
- 3D memory → 3D to 2D adapter
- shift in from memory → add
- densify → aggregate
- aggregate → densify
- shift in from memory → reorganize
- Input feature → Image memory
- 3D memory → aggregate
- Input feature → Image adapter
- shift in from memory → Image memory
- Image memory → Image memory
- 3D to 2D adapter → 3D to 2D adapter
- reorganize → shift out to memory
- Input feature → shift in from memory
- reorganize → shift
- project → 3D to 2D adapter
- Image memory → Image adapter
- Input feature → shift

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Input Feature | Input feature |
| Image Memory
Reorganize
Add & Shift
Temporal Agg. | Image memory |
| Image Adapter
Integrate | Image adapter |
| 3D Memory
Stores Temporal Context | 3D memory |
| 3D to 2D Adapter
Adapt 3D to 2D | 3D to 2D adapter |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Input feature | Image memory |
| Input feature | Image adapter |
| Image memory | Image adapter |
| 3D memory | 3D to 2D adapter |