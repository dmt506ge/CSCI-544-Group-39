# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\2stagebeit.png`
- **Reference**: `..\ground_png\2stagebeit.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.524
- **Recall**: 0.579
- **F1 Score**: 0.550

### Path Alignment
- **Precision**: 0.545
- **Recall**: 0.130
- **F1 Score**: 0.211

## Generated Graph

### Nodes

- **node1**: Stage 1: Tokenization and Reconstruction (Creates Discrete Token Vocabulary)
- **node2**: Original Image
- **node3**: Tokenizer (Denoising)
- **node4**: Discrete Token Vocabulary [9, 1, 4, 8...]
- **node5**: Decoder (Reconstruction)
- **node6**: Reconstructed Image
- **node7**: Token vocabulary from Stage 1 used as prediction targets in Stage 2
- **node8**: Stage 2: BEIT Pre-training (Masked Image Modeling)
- **node9**: Image Input
- **node10**: Image Patches (16x16)
- **node11**: V=Visible, M=Masked (~75% masked)
- **node12**: Target Visual Tokens (from frozen tokenizer) [3, 7, 2, 5 
 9, 7, 4...] 
 ? = masked positions
- **node13**: Patch Embedding {E0, E1, ..., En}
- **node14**: Position Embedding {P0, P1, ..., Pn}
- **node15**: Tokenzier FROZEN 
 from Stage 1 
 (Denoising)
- **node16**: BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation
- **node17**: Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets
- **node18**: Loss Cross-Entropy
- **node19**: After Pre-training: 
 Pre-trained BEIT encoder transfers to downstream tasks 
 (classification, segmentation, detection) via fine-tuning
- **node20**: Note: MAE can infer complex reconstructions even with 95% masking, 
 suggesting learned semantics via rich hidden representations
- **node21**: Self-attention learns to distinguish semantic regions 
 without task-specific supervision

### Edges

- Patch Embedding {E0, E1, ..., En} → Loss Cross-Entropy
- Image Input → Patch Embedding {E0, E1, ..., En}
- Image Input → Loss Cross-Entropy
- Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets → Loss Cross-Entropy
- Position Embedding {P0, P1, ..., Pn} → BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation
- Patch Embedding {E0, E1, ..., En} → Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets
- Image Input → Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets
- Patch Embedding {E0, E1, ..., En} → BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation
- Image Input → BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation
- Original Image → Tokenizer (Denoising)
- Tokenizer (Denoising) → Reconstructed Image
- Original Image → Discrete Token Vocabulary [9, 1, 4, 8...]
- V=Visible, M=Masked (~75% masked) → Patch Embedding {E0, E1, ..., En}
- V=Visible, M=Masked (~75% masked) → Loss Cross-Entropy
- Decoder (Reconstruction) → Reconstructed Image
- Tokenizer (Denoising) → Decoder (Reconstruction)
- V=Visible, M=Masked (~75% masked) → Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets
- V=Visible, M=Masked (~75% masked) → BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation
- Image Patches (16x16) → Patch Embedding {E0, E1, ..., En}
- Image Patches (16x16) → Loss Cross-Entropy
- Image Patches (16x16) → Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets
- Original Image → Reconstructed Image
- Target Visual Tokens (from frozen tokenizer) [3, 7, 2, 5 
 9, 7, 4...] 
 ? = masked positions → Loss Cross-Entropy
- Image Patches (16x16) → BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation
- Image Input → Image Patches (16x16)
- Discrete Token Vocabulary [9, 1, 4, 8...] → Reconstructed Image
- Target Visual Tokens (from frozen tokenizer) [3, 7, 2, 5 
 9, 7, 4...] 
 ? = masked positions → Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets
- Position Embedding {P0, P1, ..., Pn} → Loss Cross-Entropy
- Tokenizer (Denoising) → Discrete Token Vocabulary [9, 1, 4, 8...]
- Original Image → Decoder (Reconstruction)
- BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation → Loss Cross-Entropy
- Position Embedding {P0, P1, ..., Pn} → Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets
- Discrete Token Vocabulary [9, 1, 4, 8...] → Decoder (Reconstruction)
- BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation → Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets

## Reference Graph

### Nodes

- **node1**: Stage1
- **node2**: Original Image
- **node3**: Tokenizer
- **node4**: 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- **node5**: Decoder
- **node6**: Reconstructed Image
- **node7**: Stage2
- **node8**: Tokenizer
- **node9**: Masked Image Modeling Head
- **node10**: BEiT Encoder
- **node11**: h2
- **node12**: h3
- **node13**: h6
- **node14**: h14
- **node15**: Flatten
- **node16**: [S]
- **node17**: [M]
- **node18**: Position Embedding
- **node19**: Patch Embedding

### Edges

- h2 → Masked Image Modeling Head
- [M] → Position Embedding
- h2 → BEiT Encoder
- Flatten → Position Embedding
- Tokenizer → Reconstructed Image
- Flatten → [M]
- Original Image → Tokenizer
- Tokenizer → Masked Image Modeling Head
- Patch Embedding → Position Embedding
- Flatten → [S]
- h3 → Masked Image Modeling Head
- Stage2 → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- Tokenizer → Reconstructed Image
- Tokenizer → BEiT Encoder
- Original Image → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- h3 → BEiT Encoder
- Stage2 → Tokenizer
- [S] → Patch Embedding
- Tokenizer → Masked Image Modeling Head
- Tokenizer → BEiT Encoder
- Tokenizer → Decoder
- h14 → Masked Image Modeling Head
- Decoder → Reconstructed Image
- Tokenizer → Decoder
- [M] → Patch Embedding
- h14 → BEiT Encoder
- Flatten → Patch Embedding
- h6 → Masked Image Modeling Head
- Stage2 → Reconstructed Image
- Original Image → Reconstructed Image
- h6 → BEiT Encoder
- Masked Image Modeling Head → BEiT Encoder
- Stage2 → Masked Image Modeling Head
- Stage2 → BEiT Encoder
- Tokenizer → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → Reconstructed Image
- Original Image → Masked Image Modeling Head
- Original Image → BEiT Encoder
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → Masked Image Modeling Head
- Tokenizer → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- Stage2 → Decoder
- Original Image → Decoder
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → BEiT Encoder
- [S] → Position Embedding
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → Decoder
- [S] → [M]

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Stage 1: Tokenization and Reconstruction (Creates Discrete Token Vocabulary) | Stage1 |
| Original Image | Original Image |
| Tokenizer (Denoising) | Tokenizer |
| Decoder (Reconstruction) | Decoder |
| Reconstructed Image | Reconstructed Image |
| Stage 2: BEIT Pre-training (Masked Image Modeling) | Stage2 |
| Patch Embedding {E0, E1, ..., En} | Patch Embedding |
| Position Embedding {P0, P1, ..., Pn} | Position Embedding |
| Tokenzier FROZEN 
 from Stage 1 
 (Denoising) | Tokenizer |
| BEiT Encoder 
 Transformer Layers 
 with Self-Attention 
 Input: Visible patches only 
 Output: {H0, H1, ..., Hn} 
 Rich hidden representation | BEiT Encoder |
| Masked Image Modeling Head 
 Predicts token IDs for masked positions 
 Output: [T3, T6, T12] (predicted tokens) 
 Loss: Cross-Entropy vs frozen tokenizer targets | Masked Image Modeling Head |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Original Image | Tokenizer |
| Original Image | Decoder |
| Original Image | Reconstructed Image |
| Tokenizer | Decoder |
| Tokenizer | Reconstructed Image |
| Decoder | Reconstructed Image |