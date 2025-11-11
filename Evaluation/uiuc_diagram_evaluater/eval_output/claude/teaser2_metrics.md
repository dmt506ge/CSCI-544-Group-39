# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\teaser2.png`
- **Reference**: `..\ground_png\teaser2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.178
- **Recall**: 0.348
- **F1 Score**: 0.235

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Online 3D Scene Perception Framework
- **node2**: Online Semantic Segmentation
- **node3**: Memory Adapter Injection Layer
- **node4**: Frame t (t=0)
- **node5**: Timestamp: 0ms
- **node6**: Wall
- **node7**: Floor
- **node8**: Objects
- **node9**: Memory
- **node10**: Frame t+1 (t=1)
- **node11**: Timestamp: 33ms
- **node12**: Updated
- **node13**: Refine
- **node14**: Frame t+2 (t=2)
- **node15**: Timestamp: 66ms
- **node16**: Refined
- **node17**: Online Object Detection
- **node18**: Frame t (t=0)
- **node19**: Timestamp: 0ms
- **node20**: Chair
- **node21**: Table
- **node22**: Sofa
- **node23**: 3D Memory
- **node24**: Frame t+1 (t=1)
- **node25**: Timestamp: 33ms
- **node26**: Lamp
- **node27**: Track
- **node28**: Frame t+2 (t=2)
- **node29**: Timestamp: 66ms
- **node30**: Online Instance Segmentation
- **node31**: 3D NMS Adapter Layer
- **node32**: Frame t (t=0)
- **node33**: Timestamp: 0ms
- **node34**: Obj 1
- **node35**: Obj 2
- **node36**: Obj 3
- **node37**: 3D Memory Enhancement
- **node38**: Frame t+1 (t=1)
- **node39**: Timestamp: 33ms
- **node40**: Obj 4
- **node41**: Merge
- **node42**: Frame t+2 (t=2)
- **node43**: Timestamp: 66ms
- **node44**: Memory-based adapters enable seamless transition from offline to online perception
- **node45**: Time-Aware Memory stores spatial-temporal information across frames

### Edges

*(No edges)*

## Reference Graph

### Nodes

- **node1**: Online Semantic Segmentation
- **node2**: wall
- **node3**: floor
- **node4**: cabinet
- **node5**: bed
- **node6**: chair
- **node7**: sofa
- **node8**: table
- **node9**: door
- **node10**: window
- **node11**: bookshelf
- **node12**: shower curtain
- **node13**: toilet
- **node14**: sink
- **node15**: bathtub
- **node16**: other furniture
- **node17**: picture
- **node18**: counter
- **node19**: desk
- **node20**: curtain
- **node21**: refrigerator
- **node22**: Online Object Detection
- **node23**: Online Instance Segmentation

### Edges

- Online Semantic Segmentation → Online Instance Segmentation
- Online Object Detection → Online Instance Segmentation
- Online Semantic Segmentation → Online Object Detection

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Online Semantic Segmentation | Online Semantic Segmentation |
| Wall | wall |
| Floor | floor |
| Chair | chair |
| Table | table |
| Sofa | sofa |
| Online Object Detection | Online Object Detection |
| Online Instance Segmentation | Online Instance Segmentation |

## Path Alignment Matches

*(No matched paths)*