# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\pc-module-single.png`
- **Reference**: `..\ground_png\pc-module-single.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.375
- **Recall**: 0.692
- **F1 Score**: 0.486

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Memory-Based Adapter Architecture
- **node2**: Point cloud adapter
- **node3**: Input Voxels (t)
- **node4**: cur
- **node5**: upd
- **node6**: prv
- **node7**: sparsify
- **node8**: Sparse
- **node9**: aggregate
- **node10**: (Attention fusion)
- **node11**: Aggregated
- **node12**: map
- **node13**: 3D NMS
- **node14**: Point Features (instance masks)
- **node15**: query (ROI-level)
- **node16**: add
- **node17**: current frame
- **node18**: Point cloud memory
- **node19**: voxelize (t) current frame
- **node20**: merge
- **node21**: Queue (t-1) temporal cache
- **node22**: update
- **node23**: Queue (t) updated memory
- **node24**: feedback

### Edges

*(No edges)*

## Reference Graph

### Nodes

- **node1**: Input feature
- **node2**: query
- **node3**: sparsify
- **node4**: aggregate
- **node5**: map
- **node6**: add
- **node7**: Point cloud adapter
- **node8**: voxelize
- **node9**: merge
- **node10**: update
- **node11**: previous memory
- **node12**: updated memory
- **node13**: Point cloud memory

### Edges

- voxelize → updated memory
- update → updated memory
- merge → updated memory
- Input feature → sparsify
- sparsify → map
- query → sparsify
- sparsify → add
- Input feature → previous memory
- Input feature → update
- merge → previous memory
- Input feature → map
- merge → update
- voxelize → previous memory
- Input feature → add
- voxelize → update
- query → map
- sparsify → aggregate
- previous memory → updated memory
- query → add
- aggregate → map
- Input feature → aggregate
- Input feature → voxelize
- aggregate → add
- Input feature → merge
- query → aggregate
- voxelize → merge
- previous memory → update
- map → add
- Input feature → updated memory
- Input feature → query

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Point cloud adapter | Point cloud adapter |
| Input Voxels (t) | Input feature |
| sparsify | sparsify |
| aggregate | aggregate |
| map | map |
| add | add |
| Point cloud memory | Point cloud memory |
| update | update |
| Queue (t) updated memory | updated memory |

## Path Alignment Matches

*(No matched paths)*