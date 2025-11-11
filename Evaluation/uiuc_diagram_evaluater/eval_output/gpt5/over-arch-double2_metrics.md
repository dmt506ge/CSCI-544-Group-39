# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\over-arch-double2.png`
- **Reference**: `..\ground_png\over-arch-double2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.667
- **Recall**: 0.667
- **F1 Score**: 0.667

### Path Alignment
- **Precision**: 0.545
- **Recall**: 0.100
- **F1 Score**: 0.169

## Generated Graph

### Nodes

- **node1**: frame image t
temporal input
- **node2**: frame image t plus 1
temporal input
- **node3**: rgb t and t plus 1
- **node4**: image backbone
resnet fpn unet
- **node5**: 3d to 2d adapter
inter modal temporal
- **node6**: point clouds t and t plus 1
- **node7**: pointcloud backbone
mink unet
cat3d td3d
- **node8**: fusion and aggregation
inter frame and inter modal
- **node9**: multi task head
seg det inst
- **node10**: image memory
temporal cache
- **node11**: image adapter
temporal aggregate
- **node12**: 2d predictions y
- **node13**: point memory
scene cache roi
- **node14**: point adapter
temporal aggregate
- **node15**: 3d predictions o
3d nms for instance

### Edges

- frame image t plus 1
temporal input → 3d to 2d adapter
inter modal temporal
- image backbone
resnet fpn unet → fusion and aggregation
inter frame and inter modal
- frame image t
temporal input → 3d to 2d adapter
inter modal temporal
- frame image t plus 1
temporal input → multi task head
seg det inst
- frame image t
temporal input → multi task head
seg det inst
- point clouds t and t plus 1 → pointcloud backbone
mink unet
cat3d td3d
- frame image t plus 1
temporal input → fusion and aggregation
inter frame and inter modal
- frame image t
temporal input → fusion and aggregation
inter frame and inter modal
- rgb t and t plus 1 → image backbone
resnet fpn unet
- point clouds t and t plus 1 → multi task head
seg det inst
- point memory
scene cache roi → 3d predictions o
3d nms for instance
- rgb t and t plus 1 → 3d to 2d adapter
inter modal temporal
- point clouds t and t plus 1 → fusion and aggregation
inter frame and inter modal
- point adapter
temporal aggregate → 3d predictions o
3d nms for instance
- image memory
temporal cache → image adapter
temporal aggregate
- rgb t and t plus 1 → multi task head
seg det inst
- 3d to 2d adapter
inter modal temporal → multi task head
seg det inst
- rgb t and t plus 1 → fusion and aggregation
inter frame and inter modal
- point memory
scene cache roi → point adapter
temporal aggregate
- 3d to 2d adapter
inter modal temporal → fusion and aggregation
inter frame and inter modal
- frame image t plus 1
temporal input → rgb t and t plus 1
- image memory
temporal cache → 2d predictions y
- fusion and aggregation
inter frame and inter modal → multi task head
seg det inst
- image backbone
resnet fpn unet → multi task head
seg det inst
- frame image t plus 1
temporal input → image backbone
resnet fpn unet
- pointcloud backbone
mink unet
cat3d td3d → multi task head
seg det inst
- frame image t
temporal input → rgb t and t plus 1
- frame image t
temporal input → image backbone
resnet fpn unet
- image adapter
temporal aggregate → 2d predictions y
- pointcloud backbone
mink unet
cat3d td3d → fusion and aggregation
inter frame and inter modal

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
- **node12**: P-memory
- **node13**: P-adapter
- **node14**: result t
- **node15**: 3D-2D-adapter

### Edges

- Image Backbone → I-memory
- 3D-2D-adapter → Fusion
- P-adapter → Task Head
- Image Backbone → Task Head
- input t-1 → I-memory
- input t-1 → I-adapter
- I-adapter → result t
- input t-1 → Task Head
- input t → P-adapter
- Pointcloud Backbone → P-adapter
- 3D-2D-adapter → P-memory
- result t-1 → result t
- 3D-2D-adapter → Fusion
- P-memory → Fusion
- Detailed → result t
- P-adapter → Fusion
- I-adapter → Task Head
- Image Backbone → Fusion
- I-memory → result t
- input t-1 → Fusion
- Pointcloud Backbone → P-memory
- Detailed → 3D-2D-adapter
- input t → result t
- Detailed → I-adapter
- P-memory → P-adapter
- I-memory → I-adapter
- 3D-2D-adapter → P-adapter
- Pointcloud Backbone → result t
- Detailed → I-memory
- Detailed → Task Head
- Fusion → result t
- 3D-2D-adapter → result t
- I-memory → Task Head
- I-adapter → Fusion
- Task Head → result t
- Pointcloud Backbone → Fusion
- input t → Pointcloud Backbone
- input t → Task Head
- Pointcloud Backbone → Task Head
- result t-1 → Fusion
- 3D-2D-adapter → I-memory
- 3D-2D-adapter → I-adapter
- 3D-2D-adapter → result t
- P-memory → result t
- Detailed → P-memory
- Detailed → Fusion
- 3D-2D-adapter → Task Head
- P-adapter → result t
- I-memory → Fusion
- Image Backbone → result t
- input t-1 → Image Backbone
- input t-1 → result t
- input t → P-memory
- input t → Fusion
- Detailed → 3D-2D-adapter
- Image Backbone → I-adapter
- Task Head → Fusion
- Detailed → P-adapter
- P-memory → Task Head
- 3D-2D-adapter → Task Head

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| image backbone
resnet fpn unet | Image Backbone |
| 3d to 2d adapter
inter modal temporal | 3D-2D-adapter |
| fusion and aggregation
inter frame and inter modal | Fusion |
| multi task head
seg det inst | Task Head |
| image memory
temporal cache | I-memory |
| image adapter
temporal aggregate | I-adapter |
| 2d predictions y | result t-1 |
| point memory
scene cache roi | P-memory |
| point adapter
temporal aggregate | P-adapter |
| 3d predictions o
3d nms for instance | 3D-2D-adapter |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| P-memory | P-adapter |
| Image Backbone | Task Head |
| Image Backbone | Fusion |
| 3D-2D-adapter | Task Head |
| 3D-2D-adapter | Fusion |
| I-memory | I-adapter |