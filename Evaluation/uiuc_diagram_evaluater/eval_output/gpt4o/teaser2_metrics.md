# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\teaser2.png`
- **Reference**: `..\ground_png\teaser2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.143
- **Recall**: 0.130
- **F1 Score**: 0.136

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Online Semantic Segmentation
- **node2**: Image Set 1
- **node3**: Image Set 2
- **node4**: Image Set 3
- **node5**: Processes dynamic scene data into labeled segments
- **node6**: Memory-Based Adapter
- **node7**: Integrates temporal memory for enhanced accuracy
- **node8**: Online Object Detection
- **node9**: Detected Objects 1
- **node10**: Detected Objects 2
- **node11**: Detected Objects 3
- **node12**: Identifies objects in the scene over time
- **node13**: Memory-Based Adapter
- **node14**: Enhances detection with temporal memory
- **node15**: Online Instance Segmentation
- **node16**: Segmented Instances 1
- **node17**: Segmented Instances 2
- **node18**: Segmented Instances 3
- **node19**: Segments individual object instances in real-time
- **node20**: Memory-Based Adapter
- **node21**: Utilizes memory for accurate instance segmentation

### Edges

- Identifies objects in the scene over time → Memory-Based Adapter
- Online Semantic Segmentation → Image Set 1
- Online Semantic Segmentation → Processes dynamic scene data into labeled segments
- Segmented Instances 3 → Segments individual object instances in real-time
- Segmented Instances 1 → Segmented Instances 3
- Segmented Instances 3 → Memory-Based Adapter
- Online Object Detection → Detected Objects 3
- Processes dynamic scene data into labeled segments → Integrates temporal memory for enhanced accuracy
- Detected Objects 2 → Identifies objects in the scene over time
- Image Set 3 → Processes dynamic scene data into labeled segments
- Detected Objects 1 → Detected Objects 2
- Image Set 1 → Processes dynamic scene data into labeled segments
- Online Instance Segmentation → Segmented Instances 1
- Segmented Instances 2 → Utilizes memory for accurate instance segmentation
- Online Semantic Segmentation → Integrates temporal memory for enhanced accuracy
- Detected Objects 1 → Identifies objects in the scene over time
- Memory-Based Adapter → Enhances detection with temporal memory
- Online Instance Segmentation → Utilizes memory for accurate instance segmentation
- Processes dynamic scene data into labeled segments → Memory-Based Adapter
- Memory-Based Adapter → Utilizes memory for accurate instance segmentation
- Image Set 2 → Processes dynamic scene data into labeled segments
- Detected Objects 2 → Memory-Based Adapter
- Online Semantic Segmentation → Image Set 3
- Segments individual object instances in real-time → Utilizes memory for accurate instance segmentation
- Identifies objects in the scene over time → Enhances detection with temporal memory
- Segmented Instances 2 → Segments individual object instances in real-time
- Online Semantic Segmentation → Memory-Based Adapter
- Detected Objects 3 → Enhances detection with temporal memory
- Online Object Detection → Enhances detection with temporal memory
- Detected Objects 1 → Memory-Based Adapter
- Online Instance Segmentation → Segments individual object instances in real-time
- Online Object Detection → Detected Objects 1
- Online Instance Segmentation → Segmented Instances 2
- Online Semantic Segmentation → Image Set 2
- Online Instance Segmentation → Memory-Based Adapter
- Segmented Instances 2 → Memory-Based Adapter
- Image Set 3 → Integrates temporal memory for enhanced accuracy
- Image Set 1 → Integrates temporal memory for enhanced accuracy
- Detected Objects 2 → Detected Objects 3
- Image Set 2 → Integrates temporal memory for enhanced accuracy
- Segments individual object instances in real-time → Memory-Based Adapter
- Image Set 1 → Image Set 3
- Segmented Instances 1 → Utilizes memory for accurate instance segmentation
- Online Object Detection → Detected Objects 2
- Image Set 2 → Image Set 3
- Detected Objects 1 → Detected Objects 3
- Image Set 3 → Memory-Based Adapter
- Segmented Instances 2 → Segmented Instances 3
- Image Set 1 → Memory-Based Adapter
- Online Instance Segmentation → Segmented Instances 3
- Memory-Based Adapter → Integrates temporal memory for enhanced accuracy
- Image Set 1 → Image Set 2
- Online Object Detection → Identifies objects in the scene over time
- Detected Objects 3 → Identifies objects in the scene over time
- Image Set 2 → Memory-Based Adapter
- Detected Objects 2 → Enhances detection with temporal memory
- Segmented Instances 1 → Segments individual object instances in real-time
- Segmented Instances 3 → Utilizes memory for accurate instance segmentation
- Segmented Instances 1 → Segmented Instances 2
- Segmented Instances 1 → Memory-Based Adapter
- Detected Objects 3 → Memory-Based Adapter
- Online Object Detection → Memory-Based Adapter
- Detected Objects 1 → Enhances detection with temporal memory

## Reference Graph

### Nodes

- **node1**: Online Semantic Segmentation
- **node2**: Online Object Detection
- **node3**: Online Instance Segmentation
- **node4**: wall
- **node5**: floor
- **node6**: cabinet
- **node7**: bed
- **node8**: chair
- **node9**: sofa
- **node10**: table
- **node11**: door
- **node12**: window
- **node13**: bookshelf
- **node14**: picture
- **node15**: counter
- **node16**: desk
- **node17**: curtain
- **node18**: refrigerator
- **node19**: shower curtain
- **node20**: toilet
- **node21**: sink
- **node22**: bathtub
- **node23**: other furniture

### Edges

- Online Semantic Segmentation → Online Object Detection
- Online Semantic Segmentation → Online Instance Segmentation
- Online Object Detection → Online Instance Segmentation

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Online Semantic Segmentation | Online Semantic Segmentation |
| Online Object Detection | Online Object Detection |
| Online Instance Segmentation | Online Instance Segmentation |

## Path Alignment Matches

*(No matched paths)*