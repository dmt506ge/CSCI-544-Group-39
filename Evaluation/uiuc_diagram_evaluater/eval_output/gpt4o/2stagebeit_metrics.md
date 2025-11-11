# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\2stagebeit.png`
- **Reference**: `..\ground_png\2stagebeit.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.615
- **Recall**: 0.500
- **F1 Score**: 0.552

### Path Alignment
- **Precision**: 0.538
- **Recall**: 0.143
- **F1 Score**: 0.226

## Generated Graph

### Nodes

- **node1**: Original Image
- **node2**: Tokenizer
- **node3**: Token Representation
- **node4**: Decoder
- **node5**: Reconstructed Image
- **node6**: Image Input
- **node7**: Token Output
- **node8**: Masked Image Modeling Head
- **node9**: BEiT Encoder
- Self-attention maps
- Semantic region distinction
- **node10**: Patch Embedding
- **node11**: Position Embedding
- **node12**: Image Patches
- **node13**: Connection: Stage 1 to Stage 2

### Edges

- Image Input → Tokenizer
- Image Input → Decoder
- Original Image → Token Output
- Image Input → Masked Image Modeling Head
- Image Input → BEiT Encoder
- Self-attention maps
- Semantic region distinction
- Image Input → Connection: Stage 1 to Stage 2
- BEiT Encoder
- Self-attention maps
- Semantic region distinction → Connection: Stage 1 to Stage 2
- Original Image → Reconstructed Image
- Original Image → Token Representation
- Image Input → Reconstructed Image
- Masked Image Modeling Head → Connection: Stage 1 to Stage 2
- Image Patches → Patch Embedding
- Tokenizer → Decoder
- Decoder → Reconstructed Image
- Tokenizer → Masked Image Modeling Head
- Tokenizer → BEiT Encoder
- Self-attention maps
- Semantic region distinction
- Tokenizer → Connection: Stage 1 to Stage 2
- Image Input → Token Output
- Masked Image Modeling Head → BEiT Encoder
- Self-attention maps
- Semantic region distinction
- Tokenizer → Reconstructed Image
- Original Image → Tokenizer
- Image Input → Token Representation
- Image Patches → Connection: Stage 1 to Stage 2
- Image Patches → BEiT Encoder
- Self-attention maps
- Semantic region distinction
- Original Image → Decoder
- Tokenizer → Token Output
- Original Image → Masked Image Modeling Head
- Original Image → Connection: Stage 1 to Stage 2
- Original Image → BEiT Encoder
- Self-attention maps
- Semantic region distinction
- Token Representation → Decoder
- Patch Embedding → Connection: Stage 1 to Stage 2
- Patch Embedding → BEiT Encoder
- Self-attention maps
- Semantic region distinction
- Position Embedding → Connection: Stage 1 to Stage 2
- Position Embedding → BEiT Encoder
- Self-attention maps
- Semantic region distinction
- Tokenizer → Token Representation
- Token Representation → Reconstructed Image

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
- **node9**: 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544
- **node10**: Masked Image Modeling Head
- **node11**: BEiT Encoder
- **node12**: Flatten
- **node13**: [S]
- **node14**: [M]
- **node15**: Position
Embedding
- **node16**: Patch
Embedding

### Edges

- Stage2 → BEiT Encoder
- Flatten → Patch
Embedding
- Tokenizer → Position
Embedding
- Masked Image Modeling Head → [M]
- Tokenizer → BEiT Encoder
- 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544 → [S]
- Masked Image Modeling Head → Patch
Embedding
- BEiT Encoder → [M]
- Flatten → Position
Embedding
- 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544 → BEiT Encoder
- Stage2 → Tokenizer
- Stage2 → 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544
- Stage2 → [S]
- BEiT Encoder → Patch
Embedding
- Tokenizer → [S]
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → Reconstructed Image
- Original Image → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → Decoder
- Tokenizer → 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544
- Masked Image Modeling Head → Position
Embedding
- Masked Image Modeling Head → Flatten
- 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544 → [M]
- BEiT Encoder → Flatten
- BEiT Encoder → Position
Embedding
- 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544 → Patch
Embedding
- Masked Image Modeling Head → BEiT Encoder
- Original Image → Reconstructed Image
- Stage2 → [M]
- Original Image → Decoder
- Stage2 → Patch
Embedding
- Flatten → [S]
- Tokenizer → [M]
- 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544 → Position
Embedding
- Decoder → Reconstructed Image
- Tokenizer → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- Tokenizer → Patch
Embedding
- 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544 → Flatten
- Masked Image Modeling Head → [S]
- 123 234 □□□ 567
987 □□□ 765 □□□
112 □□□ 334 □□□
211 □□□ 433 544 → Masked Image Modeling Head
- Stage2 → Position
Embedding
- BEiT Encoder → [S]
- Stage2 → Flatten
- Stage2 → Masked Image Modeling Head
- Original Image → Tokenizer
- Tokenizer → Reconstructed Image
- Flatten → [M]
- Tokenizer → Masked Image Modeling Head
- Tokenizer → Decoder
- Tokenizer → Flatten

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Original Image | Original Image |
| Tokenizer | Tokenizer |
| Reconstructed Image | Reconstructed Image |
| Patch Embedding | Patch
Embedding |
| Position Embedding | Position
Embedding |
| Masked Image Modeling Head | Masked Image Modeling Head |
| BEiT Encoder
- Self-attention maps
- Semantic region distinction | BEiT Encoder |
| Decoder | Decoder |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Masked Image Modeling Head | BEiT Encoder |
| Original Image | Tokenizer |
| Original Image | Decoder |
| Original Image | Reconstructed Image |
| Tokenizer | Decoder |
| Tokenizer | Reconstructed Image |
| Decoder | Reconstructed Image |