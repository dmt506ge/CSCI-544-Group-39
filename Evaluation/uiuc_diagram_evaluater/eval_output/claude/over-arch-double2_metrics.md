# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\over-arch-double2.png`
- **Reference**: `..\ground_png\over-arch-double2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.400
- **Recall**: 0.500
- **F1 Score**: 0.444

### Path Alignment
- **Precision**: 0.786
- **Recall**: 0.147
- **F1 Score**: 0.247

## Generated Graph

### Nodes

- **node1**: Memory-Based Adapter Architecture for Online 3D Perception
- **node2**: RGB Image
Time t
(Current Frame)
- **node3**: RGB Image
Time t+1
(Next Frame)
- **node4**: Image Backbone
ResNet/U-Net
(Time t)
- **node5**: Image Backbone
ResNet/U-Net
(Time t+1)
- **node6**: Image Memory Adapter
Temporal Feature Aggregation
- **node7**: Point Cloud
Time t
(Current Frame)
- **node8**: Point Cloud
Time t+1
(Next Frame)
- **node9**: Point Cloud Backbone
Minkowski-UNet
(Time t)
- **node10**: Point Cloud Backbone
Minkowski-UNet
(Time t+1)
- **node11**: Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context
- **node12**: 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- **node13**: Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- **node14**: Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- **node15**: Output
3D Scene Understanding
- **node16**: Image Feature Memory Bank
(Cached Image Features)
- **node17**: Point Cloud Memory Bank
(Cached 3D Features)
- **node18**: Image Processing Pathway
- **node19**: Point Cloud Processing Pathway
- **node20**: Solid lines: Single-frame operations
Dashed lines: Temporal operations across frames (feature caching and temporal context sharing)

### Edges

- Point Cloud
Time t
(Current Frame) → Point Cloud Backbone
Minkowski-UNet
(Time t)
- Point Cloud Backbone
Minkowski-UNet
(Time t) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- RGB Image
Time t+1
(Next Frame) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- Point Cloud
Time t+1
(Next Frame) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Image Backbone
ResNet/U-Net
(Time t+1) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Image Memory Adapter
Temporal Feature Aggregation → Output
3D Scene Understanding
- RGB Image
Time t+1
(Next Frame) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Point Cloud Backbone
Minkowski-UNet
(Time t) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Point Cloud Backbone
Minkowski-UNet
(Time t+1) → Output
3D Scene Understanding
- RGB Image
Time t
(Current Frame) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Point Cloud
Time t
(Current Frame) → Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context
- Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Image Backbone
ResNet/U-Net
(Time t) → Output
3D Scene Understanding
- RGB Image
Time t+1
(Next Frame) → Image Backbone
ResNet/U-Net
(Time t+1)
- Point Cloud
Time t
(Current Frame) → Output
3D Scene Understanding
- Image Backbone
ResNet/U-Net
(Time t) → Image Memory Adapter
Temporal Feature Aggregation
- Point Cloud Backbone
Minkowski-UNet
(Time t+1) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Image Memory Adapter
Temporal Feature Aggregation → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context → Output
3D Scene Understanding
- Point Cloud
Time t+1
(Next Frame) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- Point Cloud
Time t+1
(Next Frame) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Image Backbone
ResNet/U-Net
(Time t+1) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud → Output
3D Scene Understanding
- Image Backbone
ResNet/U-Net
(Time t+1) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- RGB Image
Time t
(Current Frame) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Image Backbone
ResNet/U-Net
(Time t) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- RGB Image
Time t
(Current Frame) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- Point Cloud
Time t+1
(Next Frame) → Point Cloud Backbone
Minkowski-UNet
(Time t+1)
- Point Cloud Backbone
Minkowski-UNet
(Time t) → Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context
- Point Cloud
Time t
(Current Frame) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Point Cloud Backbone
Minkowski-UNet
(Time t+1) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Point Cloud Backbone
Minkowski-UNet
(Time t) → Output
3D Scene Understanding
- Image Memory Adapter
Temporal Feature Aggregation → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Point Cloud Backbone
Minkowski-UNet
(Time t+1) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- RGB Image
Time t+1
(Next Frame) → Output
3D Scene Understanding
- Image Memory Adapter
Temporal Feature Aggregation → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- RGB Image
Time t+1
(Next Frame) → Image Memory Adapter
Temporal Feature Aggregation
- Image Backbone
ResNet/U-Net
(Time t) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- Image Backbone
ResNet/U-Net
(Time t) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- Point Cloud
Time t
(Current Frame) → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- Point Cloud
Time t+1
(Next Frame) → Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context
- Point Cloud
Time t
(Current Frame) → 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud
- RGB Image
Time t+1
(Next Frame) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- Point Cloud Backbone
Minkowski-UNet
(Time t) → Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context
- Point Cloud
Time t+1
(Next Frame) → Output
3D Scene Understanding
- 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud → Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation
- RGB Image
Time t
(Current Frame) → Image Backbone
ResNet/U-Net
(Time t)
- Image Backbone
ResNet/U-Net
(Time t+1) → Output
3D Scene Understanding
- RGB Image
Time t
(Current Frame) → Output
3D Scene Understanding
- Point Cloud Backbone
Minkowski-UNet
(Time t+1) → Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context
- Point Cloud Memory/Adapter
Temporal Feature Aggregation
Temporal context → Output
3D Scene Understanding
- Image Backbone
ResNet/U-Net
(Time t+1) → Image Memory Adapter
Temporal Feature Aggregation
- RGB Image
Time t
(Current Frame) → Image Memory Adapter
Temporal Feature Aggregation
- Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation → Output
3D Scene Understanding

## Reference Graph

### Nodes

- **node1**: input t-1
- **node2**: Image Backbone
- **node3**: Detailed
- **node4**: 3D-2D-adapter
- **node5**: I-memory
- **node6**: I-adapter
- **node7**: Task Head
- **node8**: Fusion
- **node9**: result t-1
- **node10**: input t
- **node11**: Pointcloud Backbone
- **node12**: Detailed
- **node13**: P-memory
- **node14**: P-adapter
- **node15**: 3D-2D-adapter
- **node16**: result t

### Edges

- Fusion → result t
- Task Head → result t-1
- Detailed → P-adapter
- Task Head → Fusion
- P-memory → Task Head
- I-memory → result t
- P-memory → Fusion
- P-memory → result t-1
- Image Backbone → result t
- Pointcloud Backbone → P-memory
- input t-1 → Task Head
- input t-1 → Fusion
- input t-1 → result t-1
- Detailed → I-memory
- Pointcloud Backbone → result t
- Detailed → Task Head
- Detailed → Fusion
- input t-1 → Image Backbone
- Detailed → result t-1
- P-adapter → result t
- 3D-2D-adapter → I-adapter
- input t → P-memory
- input t → result t
- I-adapter → result t
- Detailed → 3D-2D-adapter
- Detailed → Task Head
- 3D-2D-adapter → result t
- Detailed → result t-1
- 3D-2D-adapter → P-memory
- Detailed → Fusion
- Task Head → result t
- input t-1 → I-adapter
- Pointcloud Backbone → P-adapter
- Detailed → I-memory
- Detailed → I-adapter
- P-memory → result t
- Detailed → 3D-2D-adapter
- Image Backbone → I-memory
- Detailed → P-memory
- input t → P-adapter
- input t-1 → result t
- Detailed → result t
- Fusion → result t-1
- Detailed → I-adapter
- 3D-2D-adapter → P-adapter
- I-memory → Task Head
- 3D-2D-adapter → result t-1
- I-memory → Fusion
- I-memory → result t-1
- Image Backbone → Task Head
- Image Backbone → result t-1
- Pointcloud Backbone → Task Head
- Pointcloud Backbone → Fusion
- Pointcloud Backbone → result t-1
- 3D-2D-adapter → I-memory
- Image Backbone → Fusion
- Detailed → P-memory
- Detailed → result t
- P-memory → P-adapter
- P-adapter → Task Head
- P-adapter → result t-1
- Detailed → P-adapter
- input t → Task Head
- P-adapter → Fusion
- I-adapter → Task Head
- input t → result t-1
- I-adapter → result t-1
- input t → Fusion
- I-adapter → Fusion
- input t → Pointcloud Backbone
- 3D-2D-adapter → Task Head
- I-memory → I-adapter
- input t-1 → I-memory
- Image Backbone → I-adapter
- 3D-2D-adapter → Fusion

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Image Backbone
ResNet/U-Net
(Time t) | Image Backbone |
| Point Cloud Backbone
Minkowski-UNet
(Time t) | Pointcloud Backbone |
| 3D-to-2D Adapter
Inter-Modal Temporal Learning
(Cross-Modal Fusion)
Image + Point Cloud | 3D-2D-adapter |
| Task Head
3D Semantic Segmentation
3D Object Detection
3D Instance Segmentation | Task Head |
| Multi-Modal Fusion
Combined Image +
Point Cloud Features
with Temporal Context | Fusion |
| Image Feature Memory Bank
(Cached Image Features) | I-memory |
| Point Cloud Memory Bank
(Cached 3D Features) | P-memory |
| Output
3D Scene Understanding | result t |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Pointcloud Backbone | result t |
| Pointcloud Backbone | Task Head |
| Pointcloud Backbone | Fusion |
| Image Backbone | result t |
| Image Backbone | Task Head |
| Image Backbone | Fusion |
| 3D-2D-adapter | result t |
| 3D-2D-adapter | Task Head |
| 3D-2D-adapter | Fusion |
| Task Head | result t |
| Fusion | result t |