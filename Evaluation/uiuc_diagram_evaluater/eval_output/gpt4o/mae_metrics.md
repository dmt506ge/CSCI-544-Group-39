# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\mae.png`
- **Reference**: `..\ground_png\mae.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.333
- **Recall**: 1.000
- **F1 Score**: 0.500

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Input
- **node2**: Image Grid
- **node3**: Encoder
- **node4**: Masked Input
Self-Attention
Semantic Regions
- **node5**: Decoder
- **node6**: Reconstruction
Holistic View
Concept Learning
- **node7**: Target
- **node8**: Image Grid
- **node9**: Initial input is masked into a grid for processing
- **node10**: Uses self-attention to identify semantic regions
- **node11**: Reconstructs holistic view from semantic regions
- **node12**: Final output after reconstruction and learning

### Edges

- Masked Input
Self-Attention
Semantic Regions → Image Grid
- Image Grid → Masked Input
Self-Attention
Semantic Regions
- Image Grid → Image Grid
- Masked Input
Self-Attention
Semantic Regions → Decoder
- Decoder → Image Grid
- Image Grid → Decoder

## Reference Graph

### Nodes

- **node1**: input
- **node2**: encoder
- **node3**: decoder
- **node4**: target

### Edges

- encoder → target
- input → encoder
- decoder → target
- input → decoder
- input → target
- encoder → decoder

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Input | input |
| Encoder | encoder |
| Decoder | decoder |
| Target | target |

## Path Alignment Matches

*(No matched paths)*