# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\supp.png`
- **Reference**: `..\ground_png\supp.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.875
- **Recall**: 0.583
- **F1 Score**: 0.700

### Path Alignment
- **Precision**: 0.381
- **Recall**: 0.184
- **F1 Score**: 0.248

## Generated Graph

### Nodes

- **node1**: TD3D
- **node2**: Input
- **node3**: DownConv
- **node4**: Adapter
- **node5**: Seg head
- **node6**: ROI extractor
- **node7**: Det head
- **node8**: FCAF3D
- **node9**: MinkUnet
- **node10**: Unet
- **node11**: ResNet+FPN
- **node12**: Det head
- **node13**: UpConv
- **node14**: Conv
- **node15**: Feature
- **node16**: Output

### Edges

- Conv → Output
- Det head → Conv
- Input → UpConv
- ROI extractor → Conv
- Adapter → UpConv
- Seg head → Conv
- Det head → Output
- Input → ROI extractor
- Adapter → ROI extractor
- ROI extractor → Output
- DownConv → Conv
- Input → Adapter
- Det head → Det head
- Seg head → Output
- ROI extractor → Det head
- Seg head → Det head
- DownConv → Output
- DownConv → Det head
- Adapter → Feature
- Conv → Feature
- Input → Conv
- ROI extractor → Seg head
- Det head → Seg head
- Seg head → Seg head
- Adapter → Conv
- ROI extractor → Feature
- Det head → Feature
- UpConv → Conv
- Input → Output
- Adapter → Output
- Input → DownConv
- DownConv → Seg head
- Seg head → Feature
- Feature → Output
- Input → Det head
- DownConv → Feature
- Adapter → Det head
- UpConv → Output
- UpConv → Feature
- Det head → UpConv
- ROI extractor → UpConv
- Seg head → UpConv
- Det head → ROI extractor
- ROI extractor → ROI extractor
- DownConv → UpConv
- Input → Feature
- Input → Seg head
- Adapter → Seg head
- Seg head → ROI extractor
- DownConv → Adapter
- DownConv → ROI extractor

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

- ⊕ Add → Memory
- Input → Adapter
- DownConv → UpConv
- Seg head → Prediction
- Input → UpConv
- ⊙ Concatenate → Prediction
- UpConv → Conv
- UpConv → Prediction
- Memory → Adapter
- Feature → ⊕ Add
- ROI extracter → Memory
- ⊙ Concatenate → ⊙ Concatenate
- Input → Prediction
- Conv → Adapter
- Feature → DownConv
- ⊙ Concatenate → Interpolate
- UpConv → ⊙ Concatenate
- DownConv → Det head
- Interpolate → Det head
- UpConv → Interpolate
- Input → ⊙ Concatenate
- DownConv → Adapter
- Feature → Det head
- Adapter → Det head
- ⊙ Concatenate → ROI extracter
- Interpolate → Adapter
- Input → Interpolate
- Conv → Conv
- Memory → Prediction
- UpConv → ROI extracter
- Conv → Prediction
- ⊙ Concatenate → Memory
- ⊙ Concatenate → Conv
- Feature → UpConv
- ⊕ Add → Det head
- Input → ROI extracter
- UpConv → Memory
- DownConv → Prediction
- Conv → ⊙ Concatenate
- Input → Memory
- Input → Conv
- Feature → Seg head
- ROI extracter → ⊕ Add
- Conv → Interpolate
- Adapter → Prediction
- DownConv → ⊙ Concatenate
- ROI extracter → Det head
- Conv → ROI extracter
- DownConv → Interpolate
- Feature → Interpolate
- Conv → Memory
- Feature → Adapter
- ⊙ Concatenate → ⊕ Add
- DownConv → ROI extracter
- UpConv → ⊕ Add
- Interpolate → ROI extracter
- Feature → ROI extracter
- DownConv → Memory
- DownConv → Conv
- Input → ⊕ Add
- ⊕ Add → Adapter
- Input → DownConv
- Feature → Conv
- Interpolate → Prediction
- Det head → Prediction
- UpConv → Det head
- Feature → Prediction
- Feature → ⊙ Concatenate
- UpConv → UpConv
- Input → Feature
- ⊕ Add → Prediction
- Conv → ⊕ Add
- ROI extracter → Adapter
- Memory → Det head
- DownConv → ⊕ Add
- Input → Seg head
- Conv → Det head
- Interpolate → ⊕ Add
- ⊙ Concatenate → Det head
- Interpolate → Memory
- Feature → Memory
- ROI extracter → Prediction
- ⊙ Concatenate → Adapter
- Conv → UpConv
- UpConv → Adapter
- Input → Det head
- ⊙ Concatenate → UpConv

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| TD3D | TD3D |
| Input | Input |
| DownConv | DownConv |
| Adapter | Adapter |
| Seg head | Seg head |
| ROI extractor | ROI extracter |
| Det head | Det head |
| FCAF3D | FCAF3D |
| MinkUnet | MinkUnet |
| Unet | Unet |
| ResNet+FPN | ResNet+FPN |
| UpConv | UpConv |
| Conv | Conv |
| Feature | Feature |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Input | Feature |
| Input | Seg head |
| Input | Det head |
| Input | Adapter |
| Input | DownConv |
| Input | Conv |
| Input | UpConv |
| Input | ROI extracter |
| Adapter | Det head |
| DownConv | Det head |
| DownConv | Adapter |
| DownConv | Conv |
| DownConv | UpConv |
| DownConv | ROI extracter |
| UpConv | Conv |
| ROI extracter | Det head |