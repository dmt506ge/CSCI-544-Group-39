# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\2.png`
- **Reference**: `..\ground_png\2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.357
- **Recall**: 0.250
- **F1 Score**: 0.294

### Path Alignment
- **Precision**: 0.500
- **Recall**: 0.071
- **F1 Score**: 0.125

## Generated Graph

### Nodes

- **node1**: fig2 holistic instance segmentation and tracking with pixel embeddings and faster mean shift gpu
- **node2**: video frame
- **node3**: rshn module
recurrent stacked hourglass network
- **node4**: pixel embeddings
- **node5**: faster mean shift
gpu accelerated
- **node6**: gpu
- **node7**: id association linking
embedding matching and temporal cues
- **node8**: instances and tracks
- **node9**: inset embedding space mean shift
- **node10**: mode
- **node11**: inset plug and play replacement
- **node12**: cpu mean shift
- **node13**: faster mean shift gpu
- **node14**: overall framework with pixel embeddings and plug and play faster mean shift gpu clustering for real time cell tracking adapted from payer et al and achieving 7 to 10x speedup on gpu

### Edges

- faster mean shift
gpu accelerated → id association linking
embedding matching and temporal cues
- pixel embeddings → id association linking
embedding matching and temporal cues
- rshn module
recurrent stacked hourglass network → pixel embeddings
- faster mean shift
gpu accelerated → instances and tracks
- pixel embeddings → instances and tracks
- video frame → pixel embeddings
- pixel embeddings → faster mean shift
gpu accelerated
- rshn module
recurrent stacked hourglass network → instances and tracks
- video frame → id association linking
embedding matching and temporal cues
- rshn module
recurrent stacked hourglass network → id association linking
embedding matching and temporal cues
- id association linking
embedding matching and temporal cues → instances and tracks
- video frame → instances and tracks
- video frame → faster mean shift
gpu accelerated
- rshn module
recurrent stacked hourglass network → faster mean shift
gpu accelerated
- video frame → rshn module
recurrent stacked hourglass network

## Reference Graph

### Nodes

- **node1**: t=0
- **node2**: Video Frames
- **node3**: Deep Recurrent Network
- **node4**: RSHN
- **node5**: Pixel-wise Embedding
- **node6**: [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- **node7**: Mean-shift Clustering
- **node8**: Faster Mean-shift
- **node9**: Output
- **node10**: t=1
- **node11**: RSHN
- **node12**: [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- **node13**: Faster Mean-shift
- **node14**: Output
- **node15**: t=N
- **node16**: RSHN
- **node17**: [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- **node18**: Faster Mean-shift
- **node19**: Output
- **node20**: ...

### Edges

- RSHN → Faster Mean-shift
- RSHN → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- Video Frames → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- RSHN → Output
- RSHN → Output
- RSHN → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- RSHN → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- Faster Mean-shift → Output
- [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn] → Output
- Video Frames → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- Video Frames → RSHN
- Video Frames → Faster Mean-shift
- RSHN → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- RSHN → RSHN
- Video Frames → Faster Mean-shift
- Video Frames → Faster Mean-shift
- Video Frames → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- RSHN → Faster Mean-shift
- [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn] → Faster Mean-shift
- [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn] → Faster Mean-shift
- RSHN → Faster Mean-shift
- RSHN → Faster Mean-shift
- RSHN → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- RSHN → Faster Mean-shift
- Video Frames → RSHN
- Video Frames → Output
- RSHN → [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn]
- [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn] → Output
- Faster Mean-shift → Output
- Video Frames → Output
- RSHN → RSHN
- Video Frames → Output
- RSHN → Output
- Faster Mean-shift → Output
- RSHN → Output
- Video Frames → RSHN
- [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn] → Output
- RSHN → RSHN
- RSHN → Faster Mean-shift
- RSHN → Output
- RSHN → Output
- [a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn] → Faster Mean-shift

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| video frame | Video Frames |
| rshn module
recurrent stacked hourglass network | RSHN |
| pixel embeddings | Pixel-wise Embedding |
| faster mean shift
gpu accelerated | Faster Mean-shift |
| faster mean shift gpu | Faster Mean-shift |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Video Frames | RSHN |
| Video Frames | Faster Mean-shift |
| RSHN | Faster Mean-shift |