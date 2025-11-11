# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\pc-module-single.png`
- **Reference**: `..\ground_png\pc-module-single.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.500
- **Recall**: 0.385
- **F1 Score**: 0.435

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Point cloud adapter
- **node2**: Point cloud memory
- **node3**: current
- **node4**: query input
- **node5**: Aggregated = Attention(Queue_t, Current Features_t)
- **node6**: 3D NMS
- **node7**: previous
- **node8**: Queue_t = Queue_{t-1} ⨁ Current Features_t
- **node9**: updated
- **node10**: instance masks

### Edges

- query input → 3D NMS
- current → Point cloud memory
- current → 3D NMS
- query input → instance masks
- current → instance masks
- 3D NMS → instance masks
- Point cloud adapter → Aggregated = Attention(Queue_t, Current Features_t)
- Point cloud adapter → query input
- Queue_t = Queue_{t-1} ⨁ Current Features_t → updated
- Aggregated = Attention(Queue_t, Current Features_t) → 3D NMS
- Point cloud adapter → Point cloud memory
- previous → Queue_t = Queue_{t-1} ⨁ Current Features_t
- Point cloud adapter → 3D NMS
- Aggregated = Attention(Queue_t, Current Features_t) → instance masks
- previous → updated
- Point cloud adapter → instance masks
- Point cloud adapter → current
- query input → Aggregated = Attention(Queue_t, Current Features_t)
- current → query input
- current → Aggregated = Attention(Queue_t, Current Features_t)

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

- query → updated memory
- query → aggregate
- query → map
- aggregate → add
- voxelize → previous memory
- sparsify → add
- voxelize → updated memory
- merge → update
- query → voxelize
- query → add
- Input feature → previous memory
- Input feature → updated memory
- Input feature → aggregate
- Input feature → map
- query → merge
- query → update
- update → updated memory
- query → sparsify
- voxelize → merge
- map → add
- voxelize → update
- Input feature → query
- Input feature → voxelize
- Input feature → add
- Input feature → update
- Input feature → merge
- Input feature → sparsify
- merge → previous memory
- merge → updated memory
- aggregate → map
- sparsify → aggregate
- query → previous memory
- sparsify → map

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Point cloud adapter | Point cloud adapter |
| Point cloud memory | Point cloud memory |
| query input | query |
| previous | previous memory |
| updated | update |

## Path Alignment Matches

*(No matched paths)*