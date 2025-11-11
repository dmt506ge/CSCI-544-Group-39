# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\supp.png`
- **Reference**: `..\ground_png\supp.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.240
- **Recall**: 0.500
- **F1 Score**: 0.324

### Path Alignment
- **Precision**: 0.556
- **Recall**: 0.053
- **F1 Score**: 0.097

## Generated Graph

### Nodes

- **node1**: Architecture Integration with Adapters
- **node2**: (A) TD3D - Point Cloud Instance Segmentation
- **node3**: Input
- **node4**: DownConv
- **node5**: Adapter
Point Cloud Memory
- **node6**: DownConv
- **node7**: ROI Extractor
- **node8**: Seg head
- **node9**: Det head
- **node10**: Conv
3D NMS
- **node11**: Output
- **node12**: (B) FCAF3D - Point Cloud Object Detection
- **node13**: Input
- **node14**: DownConv
- **node15**: Adapter
Point Cloud Memory
- **node16**: DownConv
- **node17**: Det head
- **node18**: UpConv
- **node19**: Conv
- **node20**: Output
- **node21**: (C) MinkUnet - Point Cloud Semantic Segmentation
- **node22**: Input
- **node23**: DownConv
- **node24**: Adapter
Point Cloud Memory
- **node25**: DownConv
- **node26**: Adapter
Point Cloud Memory
- **node27**: Seg head
- **node28**: Conv
- **node29**: Output
- **node30**: (D) Unet - Image Semantic Segmentation
- **node31**: Input
- **node32**: DownConv
- **node33**: Adapter
Image-to-3D Memory
- **node34**: DownConv
- **node35**: Adapter
Image-to-3D Memory
- **node36**: UpConv
- **node37**: UpConv
- **node38**: Feature
- **node39**: Output
- **node40**: (E) ResNet+FPN - Image Object Detection
- **node41**: Input
- **node42**: DownConv
- **node43**: Adapter
Image-to-3D Memory
- **node44**: DownConv
- **node45**: Adapter
Image-to-3D Memory
- **node46**: Conv
FPN
- **node47**: Det head
- **node48**: Feature
Multi-scale
- **node49**: Output
- **node50**: Memory-Based Adapter Mechanism:
Point Cloud Memory: Caches high-resolution scene representations for temporal context in 3D tasks (Sections A, B, C)
Image-to-3D Memory: Projects 2D image features to 3D memory for multi-view integration (Sections D, E)

### Edges

- Input → DownConv
- Conv → Output
- DownConv → Adapter
Image-to-3D Memory
- Adapter
Image-to-3D Memory → Feature
Multi-scale
- Input → Seg head
- Adapter
Image-to-3D Memory → Output
- Adapter
Point Cloud Memory → Conv
- Input → DownConv
- Input → Output
- DownConv → Adapter
Point Cloud Memory
- Input → Adapter
Point Cloud Memory
- Det head → Conv
- DownConv → Adapter
Image-to-3D Memory
- DownConv → Output
- UpConv → Output
- DownConv → DownConv
- Adapter
Point Cloud Memory → DownConv
- Adapter
Image-to-3D Memory → Conv
FPN
- UpConv → Output
- Input → UpConv
- DownConv → Adapter
Image-to-3D Memory
- Conv
FPN → Det head
- Det head → Output
- DownConv → Adapter
Point Cloud Memory
- Input → Conv
3D NMS
- Input → DownConv
- Input → Adapter
Image-to-3D Memory
- Adapter
Image-to-3D Memory → Output
- DownConv → UpConv
- Input → DownConv
- UpConv → Feature
- DownConv → ROI Extractor
- Conv
FPN → Output
- Input → Adapter
Point Cloud Memory
- UpConv → UpConv
- Feature → Output
- DownConv → DownConv
- Input → Conv
- DownConv → Det head
- DownConv → Output
- Adapter
Point Cloud Memory → Output
- ROI Extractor → Output
- Seg head → Conv
3D NMS
- DownConv → Conv
- Adapter
Point Cloud Memory → Conv
3D NMS
- Adapter
Image-to-3D Memory → UpConv
- DownConv → Seg head
- Det head → Output
- DownConv → Conv
- DownConv → Det head
- Adapter
Image-to-3D Memory → Det head
- DownConv → Det head
- Det head → UpConv
- Conv → Output
- DownConv → Seg head
- Adapter
Point Cloud Memory → Seg head
- Adapter
Image-to-3D Memory → Feature
Multi-scale
- Input → Adapter
Image-to-3D Memory
- DownConv → Output
- Adapter
Point Cloud Memory → Output
- Adapter
Image-to-3D Memory → Output
- DownConv → Output
- DownConv → DownConv
- DownConv → Output
- Input → Det head
- Adapter
Point Cloud Memory → Conv
- DownConv → Adapter
Point Cloud Memory
- Adapter
Point Cloud Memory → DownConv
- DownConv → Output
- Input → Adapter
Point Cloud Memory
- Adapter
Image-to-3D Memory → UpConv
- Adapter
Point Cloud Memory → Det head
- Input → DownConv
- Input → Adapter
Image-to-3D Memory
- DownConv → Feature
- DownConv → Feature
Multi-scale
- UpConv → Conv
- Input → Output
- Input → Output
- Det head → Conv
3D NMS
- UpConv → Feature
- Adapter
Point Cloud Memory → Output
- Input → DownConv
- Input → Output
- DownConv → UpConv
- Adapter
Point Cloud Memory → DownConv
- DownConv → Conv
3D NMS
- Conv
3D NMS → Output
- Input → Det head
- DownConv → Conv
FPN
- Seg head → Output
- Adapter
Point Cloud Memory → Seg head
- UpConv → Output
- Adapter
Point Cloud Memory → Output
- Adapter
Image-to-3D Memory → Output
- Adapter
Image-to-3D Memory → Adapter
Image-to-3D Memory
- Adapter
Image-to-3D Memory → Feature
- DownConv → Conv
- Input → DownConv
- Adapter
Point Cloud Memory → Conv
- DownConv → Feature
Multi-scale
- DownConv → ROI Extractor
- Seg head → Output
- Input → Output
- DownConv → UpConv
- Input → UpConv
- DownConv → Det head
- DownConv → UpConv
- Adapter
Point Cloud Memory → ROI Extractor
- DownConv → UpConv
- DownConv → Conv
FPN
- Adapter
Image-to-3D Memory → Feature
- Adapter
Point Cloud Memory → Det head
- ROI Extractor → Det head
- DownConv → Seg head
- DownConv → Adapter
Image-to-3D Memory
- DownConv → Adapter
Image-to-3D Memory
- Adapter
Image-to-3D Memory → Conv
FPN
- DownConv → Adapter
Point Cloud Memory
- Adapter
Point Cloud Memory → UpConv
- DownConv → UpConv
- DownConv → Seg head
- Seg head → Conv
- DownConv → Output
- Input → DownConv
- DownConv → Det head
- Input → DownConv
- Adapter
Point Cloud Memory → Seg head
- ROI Extractor → Seg head
- Input → Conv
- Adapter
Point Cloud Memory → Adapter
Point Cloud Memory
- Adapter
Image-to-3D Memory → UpConv
- Det head → Output
- Input → DownConv
- DownConv → Feature
- DownConv → Adapter
Image-to-3D Memory
- Input → ROI Extractor
- Input → UpConv
- DownConv → Output
- Conv
FPN → Feature
Multi-scale
- Input → Feature
Multi-scale
- Adapter
Image-to-3D Memory → Adapter
Image-to-3D Memory
- DownConv → Output
- Input → Adapter
Image-to-3D Memory
- Adapter
Image-to-3D Memory → DownConv
- Input → Det head
- DownConv → DownConv
- DownConv → Det head
- Adapter
Image-to-3D Memory → UpConv
- Input → Feature
- Input → Conv
FPN
- Input → Adapter
Point Cloud Memory
- DownConv → Conv
3D NMS
- DownConv → Adapter
Point Cloud Memory
- Input → Seg head
- Det head → Feature
Multi-scale
- DownConv → Conv
- Adapter
Image-to-3D Memory → DownConv
- Adapter
Image-to-3D Memory → Det head
- DownConv → Output
- Feature
Multi-scale → Output
- DownConv → DownConv
- ROI Extractor → Conv
3D NMS

## Reference Graph

### Nodes

- **node1**: (A)
- **node2**: TD3D
- **node3**: (B)
- **node4**: FCAF3D
- **node5**: (C)
- **node6**: MinkUnet
- **node7**: (D)
- **node8**: Unet
- **node9**: (E)
- **node10**: ResNet+FPN
- **node11**: Input
- **node12**: Prediction
- **node13**: Feature
- **node14**: Seg head
- **node15**: Det head
- **node16**: Memory
- **node17**: Adapter
- **node18**: DownConv
- **node19**: Conv
- **node20**: UpConv
- **node21**: Interpolate
- **node22**: ROI extracter
- **node23**: ⊕ Add
- **node24**: ⊙ Concatenate

### Edges

- Det head → Prediction
- UpConv → Feature
- ⊕ Add → Prediction
- Input → Memory
- ⊙ Concatenate → Interpolate
- ROI extracter → ⊕ Add
- DownConv → ⊕ Add
- Interpolate → Prediction
- UpConv → Seg head
- DownConv → Memory
- Conv → Prediction
- Memory → Prediction
- UpConv → ⊕ Add
- Seg head → Prediction
- ⊕ Add → Adapter
- ROI extracter → Seg head
- ⊙ Concatenate → Det head
- ⊙ Concatenate → Feature
- Interpolate → Adapter
- Input → ROI extracter
- ⊙ Concatenate → Seg head
- ROI extracter → Prediction
- Conv → Adapter
- DownConv → Prediction
- Memory → Adapter
- Input → Interpolate
- ⊕ Add → ROI extracter
- Input → Conv
- ROI extracter → Memory
- Feature → Prediction
- Conv → UpConv
- Input → Adapter
- ⊙ Concatenate → ⊕ Add
- ⊕ Add → Interpolate
- Conv → Det head
- UpConv → Prediction
- Conv → Feature
- Adapter → Det head
- Conv → ROI extracter
- Input → UpConv
- DownConv → Conv
- ROI extracter → Adapter
- DownConv → Adapter
- Memory → ROI extracter
- Input → Det head
- Conv → Interpolate
- UpConv → Memory
- Input → Feature
- Memory → Interpolate
- Adapter → Seg head
- DownConv → UpConv
- ⊕ Add → Det head
- ⊕ Add → Feature
- DownConv → Det head
- UpConv → Adapter
- Interpolate → Det head
- ROI extracter → ROI extracter
- DownConv → Feature
- DownConv → ROI extracter
- ⊙ Concatenate → Prediction
- ⊕ Add → Seg head
- ROI extracter → Interpolate
- Input → DownConv
- DownConv → Interpolate
- Input → ⊕ Add
- Interpolate → Seg head
- Memory → Det head
- ⊙ Concatenate → Memory
- Seg head → Det head
- Memory → Feature
- ⊕ Add → ⊕ Add
- Conv → Seg head
- UpConv → ROI extracter
- Conv → ⊙ Concatenate
- Memory → Seg head
- UpConv → Interpolate
- ⊙ Concatenate → Adapter
- ⊕ Add → Memory
- ROI extracter → Det head
- Input → Seg head
- Conv → ⊕ Add
- ROI extracter → Feature
- Input → ⊙ Concatenate
- ⊙ Concatenate → UpConv
- Memory → ⊕ Add
- Adapter → Prediction
- Feature → Det head
- Conv → Memory
- DownConv → Seg head
- Input → Prediction
- Memory → Memory
- DownConv → ⊙ Concatenate
- ⊙ Concatenate → ROI extracter
- UpConv → Det head

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Architecture Integration with Adapters | Adapter |
| (A) TD3D - Point Cloud Instance Segmentation | TD3D |
| Adapter
Point Cloud Memory | Memory |
| ROI Extractor | ROI extracter |
| Seg head | Seg head |
| Det head | Det head |
| Conv
3D NMS | Conv |
| (B) FCAF3D - Point Cloud Object Detection | FCAF3D |
| UpConv | UpConv |
| (C) MinkUnet - Point Cloud Semantic Segmentation | MinkUnet |
| (D) Unet - Image Semantic Segmentation | Unet |
| (E) ResNet+FPN - Image Object Detection | ResNet+FPN |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Memory | Seg head |
| Memory | Det head |
| Memory | ROI extracter |
| ROI extracter | Seg head |
| ROI extracter | Det head |