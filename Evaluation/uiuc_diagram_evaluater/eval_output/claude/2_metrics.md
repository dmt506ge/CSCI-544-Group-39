# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\2.png`
- **Reference**: `..\ground_png\2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.444
- **Recall**: 0.471
- **F1 Score**: 0.457

### Path Alignment
- **Precision**: 0.300
- **Recall**: 0.070
- **F1 Score**: 0.113

## Generated Graph

### Nodes

- **node1**: Holistic Instance Segmentation and Tracking Framework
- **node2**: Video Frame
t=0
H x W x 3
- **node3**: Video Frame
t=1
H x W x 3
- **node4**: Video Frame
t=N
H x W x 3
- **node5**: Deep Recurrent Network (RSHN)
Output: H x W x C
- **node6**: Deep Recurrent Network (RSHN)
Output: H x W x C
- **node7**: Deep Recurrent Network (RSHN)
Output: H x W x C
- **node8**: Pixel-wise Embedding
H x W x D space
Unified representation
- **node9**: Pixel-wise Embedding
H x W x D space
Unified representation
- **node10**: Pixel-wise Embedding
H x W x D space
Unified representation
- **node11**: Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- **node12**: Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- **node13**: Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- **node14**: Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- **node15**: Segmentation and Tracking
Output t=1
H x W masks
Instance masks with tracking IDs
- **node16**: Segmentation and Tracking
Output t=N
H x W masks
Instance masks with tracking IDs
- **node17**: Real-time processing enabled
- **node18**: Vertical flow: data processing pipeline | Horizontal flow: temporal continuity
GPU acceleration enables real-time performance

### Edges

- Video Frame
t=N
H x W x 3 → Pixel-wise Embedding
H x W x D space
Unified representation
- Deep Recurrent Network (RSHN)
Output: H x W x C → Pixel-wise Embedding
H x W x D space
Unified representation
- Video Frame
t=N
H x W x 3 → Pixel-wise Embedding
H x W x D space
Unified representation
- Video Frame
t=1
H x W x 3 → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Video Frame
t=N
H x W x 3 → Deep Recurrent Network (RSHN)
Output: H x W x C
- Deep Recurrent Network (RSHN)
Output: H x W x C → Pixel-wise Embedding
H x W x D space
Unified representation
- Deep Recurrent Network (RSHN)
Output: H x W x C → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Deep Recurrent Network (RSHN)
Output: H x W x C → Segmentation and Tracking
Output t=1
H x W masks
Instance masks with tracking IDs
- Video Frame
t=0
H x W x 3 → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Video Frame
t=1
H x W x 3 → Pixel-wise Embedding
H x W x D space
Unified representation
- Video Frame
t=1
H x W x 3 → Deep Recurrent Network (RSHN)
Output: H x W x C
- Video Frame
t=N
H x W x 3 → Deep Recurrent Network (RSHN)
Output: H x W x C
- Video Frame
t=N
H x W x 3 → Segmentation and Tracking
Output t=N
H x W masks
Instance masks with tracking IDs
- Video Frame
t=N
H x W x 3 → Deep Recurrent Network (RSHN)
Output: H x W x C
- Pixel-wise Embedding
H x W x D space
Unified representation → Segmentation and Tracking
Output t=N
H x W masks
Instance masks with tracking IDs
- Video Frame
t=N
H x W x 3 → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Video Frame
t=N
H x W x 3 → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Deep Recurrent Network (RSHN)
Output: H x W x C → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Deep Recurrent Network (RSHN)
Output: H x W x C → Segmentation and Tracking
Output t=1
H x W masks
Instance masks with tracking IDs
- Video Frame
t=1
H x W x 3 → Deep Recurrent Network (RSHN)
Output: H x W x C
- Pixel-wise Embedding
H x W x D space
Unified representation → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Pixel-wise Embedding
H x W x D space
Unified representation → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Deep Recurrent Network (RSHN)
Output: H x W x C → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Video Frame
t=0
H x W x 3 → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Video Frame
t=1
H x W x 3 → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Video Frame
t=N
H x W x 3 → Pixel-wise Embedding
H x W x D space
Unified representation
- Deep Recurrent Network (RSHN)
Output: H x W x C → Deep Recurrent Network (RSHN)
Output: H x W x C
- Deep Recurrent Network (RSHN)
Output: H x W x C → Deep Recurrent Network (RSHN)
Output: H x W x C
- Deep Recurrent Network (RSHN)
Output: H x W x C → Pixel-wise Embedding
H x W x D space
Unified representation
- Deep Recurrent Network (RSHN)
Output: H x W x C → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Deep Recurrent Network (RSHN)
Output: H x W x C → Pixel-wise Embedding
H x W x D space
Unified representation
- Pixel-wise Embedding
H x W x D space
Unified representation → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Video Frame
t=0
H x W x 3 → Pixel-wise Embedding
H x W x D space
Unified representation
- Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Video Frame
t=1
H x W x 3 → Pixel-wise Embedding
H x W x D space
Unified representation
- Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup → Segmentation and Tracking
Output t=N
H x W masks
Instance masks with tracking IDs
- Deep Recurrent Network (RSHN)
Output: H x W x C → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Video Frame
t=N
H x W x 3 → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Deep Recurrent Network (RSHN)
Output: H x W x C → Pixel-wise Embedding
H x W x D space
Unified representation
- Deep Recurrent Network (RSHN)
Output: H x W x C → Deep Recurrent Network (RSHN)
Output: H x W x C
- Deep Recurrent Network (RSHN)
Output: H x W x C → Segmentation and Tracking
Output t=N
H x W masks
Instance masks with tracking IDs
- Video Frame
t=N
H x W x 3 → Segmentation and Tracking
Output t=1
H x W masks
Instance masks with tracking IDs
- Deep Recurrent Network (RSHN)
Output: H x W x C → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Video Frame
t=0
H x W x 3 → Deep Recurrent Network (RSHN)
Output: H x W x C
- Deep Recurrent Network (RSHN)
Output: H x W x C → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Pixel-wise Embedding
H x W x D space
Unified representation → Segmentation and Tracking
Output t=1
H x W masks
Instance masks with tracking IDs
- Video Frame
t=1
H x W x 3 → Segmentation and Tracking
Output t=1
H x W masks
Instance masks with tracking IDs
- Video Frame
t=1
H x W x 3 → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup → Segmentation and Tracking
Output t=1
H x W masks
Instance masks with tracking IDs
- Deep Recurrent Network (RSHN)
Output: H x W x C → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Video Frame
t=N
H x W x 3 → Segmentation and Tracking
Output t=0
H x W masks
Instance masks with tracking IDs
- Deep Recurrent Network (RSHN)
Output: H x W x C → Pixel-wise Embedding
H x W x D space
Unified representation
- Pixel-wise Embedding
H x W x D space
Unified representation → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup
- Deep Recurrent Network (RSHN)
Output: H x W x C → Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup

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
- **node10**: [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- **node11**: [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- **node12**: [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- **node13**: Mean-shift Clustering
- **node14**: Faster Mean-shift
- **node15**: Faster Mean-shift
- **node16**: Faster Mean-shift
- **node17**: Output

### Edges

- RSHN → Faster Mean-shift
- RSHN → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- t=N → RSHN
- t=1 → Output
- [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn] → Output
- Faster Mean-shift → Output
- RSHN → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- RSHN → Faster Mean-shift
- Video Frames → Faster Mean-shift
- Video Frames → Output
- t=N → Faster Mean-shift
- Video Frames → RSHN
- Video Frames → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- t=N → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- Video Frames → RSHN
- Faster Mean-shift → Output
- [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn] → Faster Mean-shift
- t=1 → RSHN
- RSHN → Output
- [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn] → Faster Mean-shift
- t=0 → Faster Mean-shift
- Video Frames → t=N
- t=0 → Output
- Faster Mean-shift → Output
- Video Frames → Faster Mean-shift
- Video Frames → RSHN
- RSHN → Faster Mean-shift
- RSHN → Output
- t=0 → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- Video Frames → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn] → Faster Mean-shift
- [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn] → Output
- RSHN → Output
- t=0 → RSHN
- [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn] → Output
- Video Frames → t=0
- RSHN → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- Video Frames → t=1
- t=1 → Faster Mean-shift
- t=1 → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- Video Frames → [a_11  a_12  …  a_1n
 a_21  a_22  …  a_2n
 …
 a_m1  a_m2  …  a_mn]
- t=N → Output
- Video Frames → Faster Mean-shift

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Holistic Instance Segmentation and Tracking Framework | Output |
| Video Frame
t=0
H x W x 3 | t=0 |
| Video Frame
t=1
H x W x 3 | t=1 |
| Video Frame
t=N
H x W x 3 | t=N |
| Pixel-wise Embedding
H x W x D space
Unified representation | Pixel-wise Embedding |
| Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup | Faster Mean-shift |
| Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup | Faster Mean-shift |
| Faster Mean-shift Clustering
GPU
Plug-and-play replacement
7-10x speedup | Faster Mean-shift |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| t=0 | Faster Mean-shift |
| t=1 | Faster Mean-shift |
| t=N | Faster Mean-shift |