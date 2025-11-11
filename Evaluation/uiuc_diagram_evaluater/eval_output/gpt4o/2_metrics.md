# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\2.png`
- **Reference**: `..\ground_png\2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.444
- **Recall**: 0.471
- **F1 Score**: 0.457

### Path Alignment
- **Precision**: 1.000
- **Recall**: 0.179
- **F1 Score**: 0.304

## Generated Graph

### Nodes

- **node1**: Video Frame t=0
- **node2**: Input Flow
- **node3**: RSHN t=0
- **node4**: Embedding t=0
- **node5**: Clustering
- **node6**: Faster Mean-shift t=0
- **node7**: Output
- **node8**: Output t=0
- **node9**: Video Frame t=1
- **node10**: RSHN t=1
- **node11**: Embedding t=1
- **node12**: Faster Mean-shift t=1
- **node13**: Output t=1
- **node14**: Video Frame t=N
- **node15**: RSHN t=N
- **node16**: Embedding t=N
- **node17**: Faster Mean-shift t=N
- **node18**: Output t=N

### Edges

- RSHN t=0 → Faster Mean-shift t=0
- Video Frame t=1 → RSHN t=N
- Video Frame t=0 → Embedding t=N
- Video Frame t=1 → Output t=0
- Embedding t=N → Output t=N
- RSHN t=1 → Embedding t=1
- RSHN t=1 → Faster Mean-shift t=1
- Video Frame t=0 → Faster Mean-shift t=0
- Faster Mean-shift t=0 → Output t=0
- Video Frame t=0 → RSHN t=0
- Input Flow → RSHN t=N
- Video Frame t=N → Embedding t=0
- Input Flow → Output t=0
- RSHN t=N → Output t=N
- Video Frame t=1 → Embedding t=1
- Video Frame t=0 → Faster Mean-shift t=N
- Video Frame t=1 → Faster Mean-shift t=1
- Video Frame t=N → RSHN t=1
- Video Frame t=0 → Input Flow
- Video Frame t=1 → Output t=N
- Video Frame t=N → Output t=1
- Input Flow → Embedding t=1
- Faster Mean-shift t=N → Output t=N
- RSHN t=0 → Output t=0
- Input Flow → Faster Mean-shift t=1
- Input Flow → Output t=N
- Video Frame t=1 → RSHN t=1
- Video Frame t=1 → Embedding t=0
- Video Frame t=0 → RSHN t=N
- Video Frame t=N → Embedding t=N
- Video Frame t=0 → Output t=0
- RSHN t=1 → Output t=1
- Video Frame t=N → Faster Mean-shift t=0
- Video Frame t=0 → Embedding t=1
- Video Frame t=N → RSHN t=0
- Embedding t=0 → Faster Mean-shift t=0
- Video Frame t=1 → Output t=1
- Embedding t=1 → Faster Mean-shift t=1
- Video Frame t=0 → Faster Mean-shift t=1
- Input Flow → RSHN t=1
- Input Flow → Embedding t=0
- Video Frame t=N → Faster Mean-shift t=N
- RSHN t=N → Embedding t=N
- Video Frame t=0 → Output t=N
- Video Frame t=N → Input Flow
- Video Frame t=1 → Embedding t=N
- Embedding t=N → Faster Mean-shift t=N
- Input Flow → Output t=1
- RSHN t=0 → Embedding t=0
- RSHN t=N → Faster Mean-shift t=N
- Video Frame t=1 → Faster Mean-shift t=0
- Faster Mean-shift t=1 → Output t=1
- Video Frame t=1 → RSHN t=0
- Video Frame t=0 → RSHN t=1
- Video Frame t=N → RSHN t=N
- Video Frame t=0 → Embedding t=0
- Video Frame t=N → Output t=0
- Video Frame t=1 → Faster Mean-shift t=N
- Input Flow → Embedding t=N
- Video Frame t=1 → Input Flow
- Embedding t=0 → Output t=0
- Video Frame t=0 → Output t=1
- Input Flow → RSHN t=0
- Input Flow → Faster Mean-shift t=0
- Embedding t=1 → Output t=1
- Input Flow → Faster Mean-shift t=N
- Video Frame t=N → Embedding t=1
- Video Frame t=N → Faster Mean-shift t=1
- Video Frame t=N → Output t=N

## Reference Graph

### Nodes

- **node1**: Video Frames
- **node2**: t=0
- **node3**: t=1
- **node4**: t=N
- **node5**: Deep Recurrent Network
- **node6**: RSHN
- **node7**: RSHN
- **node8**: RSHN
- **node9**: Pixel-wise Embedding
- **node10**: [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- **node11**: [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- **node12**: [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- **node13**: Mean-shift Clustering
- **node14**: Faster Mean-shift
- **node15**: Faster Mean-shift
- **node16**: Faster Mean-shift
- **node17**: Output

### Edges

- [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn] → Output
- Video Frames → Faster Mean-shift
- RSHN → Faster Mean-shift
- RSHN → t=N
- Video Frames → RSHN
- t=1 → Output
- RSHN → RSHN
- Video Frames → t=1
- t=0 → Faster Mean-shift
- t=0 → RSHN
- [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn] → Output
- Video Frames → Output
- RSHN → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- Video Frames → t=0
- RSHN → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn] → Faster Mean-shift
- RSHN → RSHN
- t=0 → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- RSHN → Faster Mean-shift
- t=1 → Faster Mean-shift
- t=1 → RSHN
- t=0 → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- RSHN → Output
- Video Frames → Faster Mean-shift
- t=0 → RSHN
- Video Frames → RSHN
- [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn] → Faster Mean-shift
- RSHN → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- RSHN → Faster Mean-shift
- RSHN → t=N
- t=N → Faster Mean-shift
- t=1 → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- t=1 → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- RSHN → Faster Mean-shift
- Video Frames → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- t=1 → RSHN
- Faster Mean-shift → Output
- Video Frames → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- t=0 → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- t=0 → Faster Mean-shift
- t=0 → t=N
- RSHN → Output
- Video Frames → RSHN
- RSHN → Faster Mean-shift
- t=N → Output
- RSHN → RSHN
- Faster Mean-shift → Output
- [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn] → Output
- t=1 → t=N
- Faster Mean-shift → Output
- RSHN → Faster Mean-shift
- Video Frames → Faster Mean-shift
- Video Frames → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- Video Frames → t=N
- RSHN → t=1
- RSHN → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- RSHN → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- t=0 → Faster Mean-shift
- t=N → RSHN
- RSHN → Output
- t=0 → t=1
- [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn] → Faster Mean-shift
- t=0 → RSHN
- t=0 → Output
- t=1 → Faster Mean-shift
- RSHN → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]
- t=N → [a11 a12 ... a1n
 a21 a22 ... a2n
 ...  ...  ...
 am1 am2 ... amn]

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Video Frame t=0 | Video Frames |
| RSHN t=0 | RSHN |
| RSHN t=1 | RSHN |
| RSHN t=N | RSHN |
| Faster Mean-shift t=0 | Faster Mean-shift |
| Faster Mean-shift t=1 | Faster Mean-shift |
| Faster Mean-shift t=N | Faster Mean-shift |
| Output t=0 | Output |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Video Frames | Faster Mean-shift |
| Video Frames | Faster Mean-shift |
| Video Frames | Faster Mean-shift |
| Video Frames | Output |
| Video Frames | RSHN |
| Video Frames | RSHN |
| Video Frames | RSHN |
| Faster Mean-shift | Output |
| RSHN | Faster Mean-shift |
| RSHN | Output |
| RSHN | Faster Mean-shift |
| RSHN | Faster Mean-shift |