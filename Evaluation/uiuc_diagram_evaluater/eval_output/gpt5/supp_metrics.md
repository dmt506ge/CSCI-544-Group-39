# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\supp.png`
- **Reference**: `..\ground_png\supp.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.255
- **Recall**: 0.542
- **F1 Score**: 0.347

### Path Alignment
- **Precision**: 0.500
- **Recall**: 0.086
- **F1 Score**: 0.147

## Generated Graph

### Nodes

- **node1**: (A) TD3D
- **node2**: Input
- **node3**: DownConv
- **node4**: Adapter
- **node5**: Seg head
- **node6**: ROI extractor
- **node7**: Det head
- **node8**: 3D NMS
- **node9**: Point memory
- **node10**: (B) FCAF3D
- **node11**: Input
- **node12**: DownConv1
- **node13**: DownConv2
- **node14**: Adapter
- **node15**: Det head
- **node16**: UpConv
- **node17**: Conv
- **node18**: Det output
- **node19**: Point memory
- **node20**: (C) MinkUnet
- **node21**: Input
- **node22**: DownConv1
- **node23**: Adapter1
- **node24**: DownConv2
- **node25**: Adapter2
- **node26**: Seg head
- **node27**: Conv
- **node28**: Output
- **node29**: Point memory
- **node30**: (D) Unet
- **node31**: Input
- **node32**: DownConv1
- **node33**: Adapter1
- **node34**: DownConv2
- **node35**: Adapter2
- **node36**: UpConv1
- **node37**: UpConv2
- **node38**: Seg head
- **node39**: Conv
- **node40**: Output
- **node41**: 3D to 2D memory
- **node42**: (E) ResNet plus FPN
- **node43**: Input
- **node44**: DownConv
- **node45**: Adapter
- **node46**: Det head
- **node47**: Conv
- **node48**: Feature P3
- **node49**: Feature P4
- **node50**: Feature P5
- **node51**: 3D to 2D memory

### Edges

- DownConv1 → DownConv2
- Adapter → 3D NMS
- Conv → Feature P5
- Adapter2 → Output
- DownConv → Adapter
- Adapter1 → UpConv2
- DownConv2 → Adapter
- Adapter → Seg head
- Adapter → Conv
- Adapter → Det head
- Adapter1 → UpConv1
- DownConv2 → Point memory
- Input → Conv
- Input → DownConv1
- Input → Conv
- Seg head → Output
- Seg head → Det head
- DownConv1 → UpConv
- Adapter2 → Conv
- DownConv → 3D NMS
- DownConv → ROI extractor
- Input → Adapter
- DownConv1 → Output
- Conv → Feature P4
- Det head → Feature P5
- Seg head → Output
- Input → Det output
- Det head → Feature P3
- DownConv → Conv
- DownConv2 → Seg head
- Adapter → UpConv
- UpConv2 → Conv
- Adapter1 → Point memory
- Seg head → ROI extractor
- Adapter → Feature P5
- Input → Seg head
- DownConv1 → Point memory
- Input → Det head
- Input → DownConv
- Det head → Feature P4
- Input → Det head
- Adapter → Feature P3
- DownConv2 → Conv
- ROI extractor → 3D NMS
- DownConv2 → Output
- DownConv1 → Adapter
- UpConv1 → Seg head
- DownConv2 → UpConv2
- Conv → Feature P3
- Adapter1 → Seg head
- Adapter2 → Seg head
- DownConv1 → 3D to 2D memory
- Input → Conv
- DownConv2 → Adapter2
- DownConv2 → Det output
- DownConv2 → UpConv1
- DownConv → Feature P5
- Adapter → Feature P4
- Input → UpConv2
- Conv → Output
- Adapter → Det head
- Input → Adapter1
- DownConv → Feature P3
- DownConv1 → Conv
- Input → Adapter1
- Input → UpConv1
- Adapter1 → Output
- Input → DownConv1
- Adapter1 → 3D to 2D memory
- UpConv1 → UpConv2
- DownConv → Seg head
- DownConv2 → 3D to 2D memory
- DownConv1 → DownConv2
- Input → DownConv2
- DownConv2 → Det head
- UpConv2 → Output
- Det head → UpConv
- Adapter2 → UpConv2
- Input → Point memory
- Input → Seg head
- Adapter1 → Adapter2
- Adapter2 → Seg head
- DownConv → 3D to 2D memory
- UpConv → Det output
- DownConv → Adapter
- DownConv → Feature P4
- Input → 3D to 2D memory
- Seg head → 3D NMS
- Adapter2 → UpConv1
- DownConv → Det head
- Input → DownConv
- Adapter1 → DownConv2
- Input → Feature P5
- DownConv1 → Conv
- DownConv1 → Conv
- Adapter1 → DownConv2
- Input → Feature P3
- Det head → 3D NMS
- Input → Adapter
- Adapter2 → Output
- Input → DownConv2
- Adapter1 → Output
- DownConv1 → Det output
- Adapter → Det head
- DownConv1 → DownConv2
- Adapter1 → Conv
- Input → Adapter2
- Input → Point memory
- DownConv2 → Conv
- Input → 3D to 2D memory
- Input → Adapter
- Input → Feature P4
- Input → ROI extractor
- Input → 3D NMS
- Input → UpConv
- UpConv → Conv
- Input → Det head
- Conv → Det output
- Seg head → Conv
- Input → Conv
- DownConv1 → Adapter1
- Input → DownConv2
- DownConv1 → Det head
- Adapter → Det output
- DownConv2 → Point memory
- DownConv → Det head
- Adapter → ROI extractor
- UpConv1 → Conv
- UpConv2 → Seg head
- DownConv1 → Adapter2
- DownConv1 → Seg head
- Adapter2 → Conv
- DownConv1 → Output
- Input → Point memory
- Input → DownConv1
- Conv → Output
- Adapter → Point memory
- DownConv2 → Conv
- DownConv1 → Seg head
- Input → Output
- Adapter1 → Adapter2
- DownConv2 → UpConv
- DownConv2 → Adapter2
- Seg head → Conv
- DownConv2 → Output
- Det head → Conv
- ROI extractor → Det head
- Adapter → Conv
- Input → Adapter2
- Adapter1 → Seg head
- DownConv1 → Adapter2
- DownConv → Point memory
- Input → Output
- DownConv1 → Point memory
- DownConv2 → Seg head
- Adapter1 → Conv
- DownConv1 → UpConv2
- Det head → Det output
- Det head → Conv
- Input → Seg head
- DownConv1 → Adapter1
- UpConv1 → Output
- DownConv1 → UpConv1

## Reference Graph

### Nodes

- **node1**: Input
- **node2**: Prediction
- **node3**: Feature
- **node4**: Seg head
- **node5**: Det head
- **node6**: Memory
- **node7**: Adapter
- **node8**: DownConv
- **node9**: Conv
- **node10**: UpConv
- **node11**: Interpolate
- **node12**: ROI extracter
- **node13**: Add
- **node14**: Concatenate
- **node15**: (A)
- **node16**: TD3D
- **node17**: (B)
- **node18**: FCAF3D
- **node19**: (C)
- **node20**: MinkUnet
- **node21**: (D)
- **node22**: Unet
- **node23**: (E)
- **node24**: ResNet+FPN

### Edges

- Interpolate → Conv
- DownConv → UpConv
- DownConv → Feature
- UpConv → Prediction
- ROI extracter → Prediction
- Feature → Seg head
- Interpolate → UpConv
- Interpolate → Feature
- Concatenate → Det head
- Seg head → Det head
- DownConv → Seg head
- Input → UpConv
- Interpolate → ROI extracter
- Interpolate → Seg head
- Concatenate → Prediction
- Interpolate → Concatenate
- Conv → Prediction
- DownConv → Add
- Add → Conv
- DownConv → Det head
- Add → Feature
- Input → DownConv
- Interpolate → Det head
- Add → Seg head
- ROI extracter → Concatenate
- Det head → Conv
- Input → Conv
- Conv → UpConv
- Det head → UpConv
- Det head → Feature
- Input → Feature
- Add → Add
- Feature → Add
- Seg head → Prediction
- Det head → Seg head
- Input → Seg head
- Add → Det head
- Feature → Det head
- Interpolate → Add
- UpConv → Conv
- ROI extracter → Conv
- Det head → Add
- UpConv → UpConv
- ROI extracter → UpConv
- UpConv → Feature
- ROI extracter → Feature
- Input → Add
- Feature → Prediction
- DownConv → Prediction
- Det head → Det head
- Concatenate → Conv
- Input → Det head
- UpConv → Seg head
- ROI extracter → Seg head
- Conv → Conv
- Interpolate → Prediction
- Concatenate → UpConv
- Concatenate → Feature
- Conv → Feature
- Input → Prediction
- UpConv → Add
- ROI extracter → Add
- Concatenate → Seg head
- Conv → Seg head
- UpConv → Det head
- ROI extracter → Det head
- Conv → Add
- Add → Prediction
- Conv → Det head
- Seg head → Conv
- Seg head → UpConv
- Seg head → Feature
- Det head → Prediction
- Seg head → Seg head
- Feature → Conv
- Add → UpConv
- Feature → UpConv
- DownConv → Conv
- Feature → Feature
- Concatenate → Add
- Seg head → Add

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Input | Input |
| DownConv | DownConv |
| Adapter | Adapter |
| Seg head | Seg head |
| Det head | Det head |
| Point memory | Memory |
| (B) FCAF3D | FCAF3D |
| UpConv | UpConv |
| Conv | Conv |
| (C) MinkUnet | MinkUnet |
| (D) Unet | Unet |
| Output | Prediction |
| (E) ResNet plus FPN | ResNet+FPN |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Input | Seg head |
| Input | Det head |
| Input | DownConv |
| UpConv | Conv |
| Seg head | Det head |
| DownConv | Seg head |
| DownConv | Det head |