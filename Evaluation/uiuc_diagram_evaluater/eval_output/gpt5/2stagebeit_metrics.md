# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\2stagebeit.png`
- **Reference**: `..\ground_png\2stagebeit.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.176
- **Recall**: 0.429
- **F1 Score**: 0.250

### Path Alignment
- **Precision**: 0.667
- **Recall**: 0.051
- **F1 Score**: 0.095

## Generated Graph

### Nodes

- **node1**: Stage 1
- **node2**: Original Image
- **node3**: dVAE Tokenizer
- **node4**: discrete tokens
- **node5**: 11
- **node6**: 45
- **node7**: 87
- **node8**: 23
- **node9**: 64
- **node10**: dVAE Decoder
- **node11**: Reconstructed Image
- **node12**: Stage 2
- **node13**: Image
- **node14**: frozen
- **node15**: reuse
- **node16**: 12
- **node17**: 58
- **node18**: 91
- **node19**: 37
- **node20**: 49
- **node21**: 75
- **node22**: token targets
- **node23**: discrete codes
- **node24**: targets
- **node25**: Masked Image Modeling Head
- **node26**: CE loss over tokenizer codes
- **node27**: BEiT Encoder
- **node28**: self attention map
- **node29**: image patches
- **node30**: masked tokens use MASK placeholder
- **node31**: unmasked use patch embedding
- **node32**: patch embedding
- **node33**: MASK
- **node34**: p1
- **node35**: p2
- **node36**: p3
- **node37**: p4
- **node38**: p5
- **node39**: p6
- **node40**: p7
- **node41**: position embedding
- **node42**: pos0
- **node43**: pos1
- **node44**: pos2
- **node45**: pos3
- **node46**: pos4
- **node47**: pos5
- **node48**: pos6
- **node49**: pos7
- **node50**: same image
- **node51**: Figure fig beit Overview of BEiT pre training

### Edges

- dVAE Decoder → Reconstructed Image
- Original Image → CE loss over tokenizer codes
- Original Image → dVAE Tokenizer
- token targets → CE loss over tokenizer codes
- masked tokens use MASK placeholder → self attention map
- unmasked use patch embedding → self attention map
- Image → CE loss over tokenizer codes
- Image → dVAE Tokenizer
- dVAE Tokenizer → CE loss over tokenizer codes
- dVAE Tokenizer → discrete tokens
- Original Image → token targets
- image patches → self attention map
- BEiT Encoder → self attention map
- unmasked use patch embedding → BEiT Encoder
- masked tokens use MASK placeholder → BEiT Encoder
- Original Image → Masked Image Modeling Head
- Image → token targets
- position embedding → self attention map
- Original Image → Reconstructed Image
- token targets → Masked Image Modeling Head
- Image → Masked Image Modeling Head
- dVAE Tokenizer → token targets
- Original Image → dVAE Decoder
- Image → Reconstructed Image
- image patches → BEiT Encoder
- dVAE Tokenizer → Reconstructed Image
- dVAE Tokenizer → Masked Image Modeling Head
- Image → dVAE Decoder
- dVAE Tokenizer → dVAE Decoder
- Masked Image Modeling Head → CE loss over tokenizer codes
- Original Image → discrete tokens
- position embedding → BEiT Encoder
- discrete tokens → Reconstructed Image
- Image → discrete tokens
- discrete tokens → dVAE Decoder

## Reference Graph

### Nodes

- **node1**: Stage 1
- **node2**: Original Image
- **node3**: Tokenizer
- **node4**: Decoder
- **node5**: Reconstructed Image
- **node6**: 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- **node7**: Stage 2
- **node8**: 123 234 567
- **node9**: 987 543
- **node10**: 122 223 334 445
- **node11**: 211 433 544
- **node12**: Masked Image Modeling Head
- **node13**: h3
- **node14**: h6
- **node15**: h12
- **node16**: h14
- **node17**: BEiT Encoder
- **node18**: Flatten
[S] [M] [M] [M] [M]
- **node19**: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
- **node20**: Position Embedding
- **node21**: Patch Embedding

### Edges

- Position Embedding → BEiT Encoder
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → Reconstructed Image
- Patch Embedding → h6
- Flatten
[S] [M] [M] [M] [M] → h6
- Original Image → Reconstructed Image
- Original Image → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 → Position Embedding
- Original Image → Tokenizer
- Tokenizer → Reconstructed Image
- Tokenizer → 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544
- 987 543 → Masked Image Modeling Head
- Patch Embedding → h3
- Flatten
[S] [M] [M] [M] [M] → h3
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 → h6
- Patch Embedding → h14
- BEiT Encoder → h6
- Flatten
[S] [M] [M] [M] [M] → h14
- Decoder → Reconstructed Image
- Patch Embedding → h12
- Flatten
[S] [M] [M] [M] [M] → h12
- 123 234 567 → Masked Image Modeling Head
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 → h3
- BEiT Encoder → h3
- Patch Embedding → BEiT Encoder
- Flatten
[S] [M] [M] [M] [M] → BEiT Encoder
- Position Embedding → h6
- 122 223 334 445 → Masked Image Modeling Head
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 → h14
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 → h12
- BEiT Encoder → h14
- 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 → Decoder
- BEiT Encoder → h12
- 211 433 544 → Masked Image Modeling Head
- Position Embedding → h3
- Original Image → Decoder
- Position Embedding → h14
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 → BEiT Encoder
- Position Embedding → h12
- Tokenizer → Decoder

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Stage 1 | Stage 1 |
| Original Image | Original Image |
| 11 | 123 234 456 567
987 876 765 543
112 223 334 445
211 322 433 544 |
| Stage 2 | Stage 2 |
| Reconstructed Image | Reconstructed Image |
| Masked Image Modeling Head | Masked Image Modeling Head |
| BEiT Encoder | BEiT Encoder |
| position embedding | Position Embedding |
| patch embedding | Patch Embedding |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Original Image | Reconstructed Image |
| Position Embedding | BEiT Encoder |