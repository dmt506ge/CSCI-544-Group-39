# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\mae.png`
- **Reference**: `..\ground_png\mae.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.174
- **Recall**: 1.000
- **F1 Score**: 0.296

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Masked Autoencoder (MAE) Architecture
- **node2**: Input Image
- **node3**: Reconstruction Target
- **node4**: Processes 25% of patches
3x faster than full image
- **node5**: Processes all tokens
Reconstructs complete image
- **node6**: Encoder
(Lightweight)
- **node7**: Patch Embedding
+ Pos. Encoding
- **node8**: Transformer Blocks
Cross-Attention
Self-Attention
- **node9**: Deep Blocks
(fewer layers)
- **node10**: Latent
Representations
- **node11**: Learned Features
from visible patches
- **node12**: Decoder
(Heavier - more layers)
- **node13**: Token Fusion
+ Pos. Encoding
- **node14**: Transformer
Multi-Head
Self-Attention
- **node15**: Reconstruction Blocks
(deeper processing)
(more layers)
- **node16**: Pixel Predictor
for all patches
- **node17**: Full Image Output
- **node18**: Complete Reconstruction
(visible + masked patches)
- **node19**: Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- **node20**: latent representations
combined with
mask tokens
(learned embeddings)
- **node21**: predicted pixels
for all patches
- **node22**: Random masking: 75% ratio
Only 25% visible patches processed
- **node23**: visible patches
with positional
embeddings

### Edges

- Full Image Output → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Token Fusion
+ Pos. Encoding → Reconstruction Blocks
(deeper processing)
(more layers)
- latent representations
combined with
mask tokens
(learned embeddings) → Transformer Blocks
Cross-Attention
Self-Attention
- Reconstruction Blocks
(deeper processing)
(more layers) → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Transformer
Multi-Head
Self-Attention → Reconstruction Blocks
(deeper processing)
(more layers)
- Transformer
Multi-Head
Self-Attention → Pixel Predictor
for all patches
- visible patches
with positional
embeddings → Reconstruction Blocks
(deeper processing)
(more layers)
- Full Image Output → Complete Reconstruction
(visible + masked patches)
- Token Fusion
+ Pos. Encoding → Full Image Output
- Input Image → Transformer Blocks
Cross-Attention
Self-Attention
- Complete Reconstruction
(visible + masked patches) → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Patch Embedding
+ Pos. Encoding → Deep Blocks
(fewer layers)
- Patch Embedding
+ Pos. Encoding → Pixel Predictor
for all patches
- Token Fusion
+ Pos. Encoding → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- visible patches
with positional
embeddings → Full Image Output
- Input Image → Latent
Representations
- Transformer
Multi-Head
Self-Attention → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- latent representations
combined with
mask tokens
(learned embeddings) → Pixel Predictor
for all patches
- Latent
Representations → Pixel Predictor
for all patches
- visible patches
with positional
embeddings → latent representations
combined with
mask tokens
(learned embeddings)
- Transformer Blocks
Cross-Attention
Self-Attention → Reconstruction Blocks
(deeper processing)
(more layers)
- Reconstruction Blocks
(deeper processing)
(more layers) → Full Image Output
- visible patches
with positional
embeddings → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Token Fusion
+ Pos. Encoding → Complete Reconstruction
(visible + masked patches)
- Input Image → Patch Embedding
+ Pos. Encoding
- Transformer
Multi-Head
Self-Attention → Complete Reconstruction
(visible + masked patches)
- Patch Embedding
+ Pos. Encoding → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Input Image → Deep Blocks
(fewer layers)
- Transformer Blocks
Cross-Attention
Self-Attention → Full Image Output
- visible patches
with positional
embeddings → Complete Reconstruction
(visible + masked patches)
- Token Fusion
+ Pos. Encoding → Transformer Blocks
Cross-Attention
Self-Attention
- Deep Blocks
(fewer layers) → Pixel Predictor
for all patches
- Latent
Representations → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Transformer Blocks
Cross-Attention
Self-Attention → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Reconstruction Blocks
(deeper processing)
(more layers) → Complete Reconstruction
(visible + masked patches)
- visible patches
with positional
embeddings → Transformer Blocks
Cross-Attention
Self-Attention
- Patch Embedding
+ Pos. Encoding → Reconstruction Blocks
(deeper processing)
(more layers)
- Transformer
Multi-Head
Self-Attention → Full Image Output
- Transformer
Multi-Head
Self-Attention → latent representations
combined with
mask tokens
(learned embeddings)
- Transformer Blocks
Cross-Attention
Self-Attention → Complete Reconstruction
(visible + masked patches)
- latent representations
combined with
mask tokens
(learned embeddings) → Reconstruction Blocks
(deeper processing)
(more layers)
- Latent
Representations → Reconstruction Blocks
(deeper processing)
(more layers)
- visible patches
with positional
embeddings → Latent
Representations
- Pixel Predictor
for all patches → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Deep Blocks
(fewer layers) → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- visible patches
with positional
embeddings → Token Fusion
+ Pos. Encoding
- Patch Embedding
+ Pos. Encoding → Full Image Output
- visible patches
with positional
embeddings → Transformer
Multi-Head
Self-Attention
- Patch Embedding
+ Pos. Encoding → latent representations
combined with
mask tokens
(learned embeddings)
- visible patches
with positional
embeddings → Patch Embedding
+ Pos. Encoding
- Input Image → Reconstruction Blocks
(deeper processing)
(more layers)
- Latent
Representations → Full Image Output
- Input Image → Pixel Predictor
for all patches
- Latent
Representations → latent representations
combined with
mask tokens
(learned embeddings)
- Deep Blocks
(fewer layers) → Reconstruction Blocks
(deeper processing)
(more layers)
- latent representations
combined with
mask tokens
(learned embeddings) → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Transformer
Multi-Head
Self-Attention → Transformer Blocks
Cross-Attention
Self-Attention
- Patch Embedding
+ Pos. Encoding → Complete Reconstruction
(visible + masked patches)
- Input Image → latent representations
combined with
mask tokens
(learned embeddings)
- Pixel Predictor
for all patches → Full Image Output
- Deep Blocks
(fewer layers) → Full Image Output
- latent representations
combined with
mask tokens
(learned embeddings) → Complete Reconstruction
(visible + masked patches)
- Transformer
Multi-Head
Self-Attention → Latent
Representations
- Input Image → Loss Computation
MSE on masked patches only
Self-supervised learning objective
Learns holistic semantic representations
- Latent
Representations → Complete Reconstruction
(visible + masked patches)
- Transformer
Multi-Head
Self-Attention → Token Fusion
+ Pos. Encoding
- Patch Embedding
+ Pos. Encoding → Transformer Blocks
Cross-Attention
Self-Attention
- Deep Blocks
(fewer layers) → latent representations
combined with
mask tokens
(learned embeddings)
- Latent
Representations → Transformer Blocks
Cross-Attention
Self-Attention
- Input Image → Complete Reconstruction
(visible + masked patches)
- Patch Embedding
+ Pos. Encoding → Latent
Representations
- Token Fusion
+ Pos. Encoding → Pixel Predictor
for all patches
- Patch Embedding
+ Pos. Encoding → Token Fusion
+ Pos. Encoding
- Transformer
Multi-Head
Self-Attention → Deep Blocks
(fewer layers)
- latent representations
combined with
mask tokens
(learned embeddings) → Full Image Output
- Pixel Predictor
for all patches → Complete Reconstruction
(visible + masked patches)
- Deep Blocks
(fewer layers) → Complete Reconstruction
(visible + masked patches)
- Patch Embedding
+ Pos. Encoding → Transformer
Multi-Head
Self-Attention
- visible patches
with positional
embeddings → Deep Blocks
(fewer layers)
- visible patches
with positional
embeddings → Pixel Predictor
for all patches
- latent representations
combined with
mask tokens
(learned embeddings) → Token Fusion
+ Pos. Encoding
- Latent
Representations → Token Fusion
+ Pos. Encoding
- Input Image → Full Image Output
- Reconstruction Blocks
(deeper processing)
(more layers) → Pixel Predictor
for all patches
- Deep Blocks
(fewer layers) → Transformer Blocks
Cross-Attention
Self-Attention
- Input Image → Token Fusion
+ Pos. Encoding
- Input Image → visible patches
with positional
embeddings
- Transformer Blocks
Cross-Attention
Self-Attention → Pixel Predictor
for all patches
- Deep Blocks
(fewer layers) → Latent
Representations
- Input Image → Transformer
Multi-Head
Self-Attention
- Deep Blocks
(fewer layers) → Token Fusion
+ Pos. Encoding

## Reference Graph

### Nodes

- **node1**: input
- **node2**: encoder
- **node3**: decoder
- **node4**: target

### Edges

- input → decoder
- decoder → target
- input → encoder
- encoder → target
- encoder → decoder
- input → target

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Input Image | input |
| Encoder
(Lightweight) | encoder |
| Decoder
(Heavier - more layers) | decoder |
| Reconstruction Target | target |

## Path Alignment Matches

*(No matched paths)*