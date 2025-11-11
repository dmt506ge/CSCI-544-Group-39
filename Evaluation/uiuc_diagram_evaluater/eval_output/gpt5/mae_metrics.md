# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\mae.png`
- **Reference**: `..\ground_png\mae.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.158
- **Recall**: 0.750
- **F1 Score**: 0.261

### Path Alignment
- **Precision**: 1.000
- **Recall**: 0.500
- **F1 Score**: 0.667

## Generated Graph

### Nodes

- **node1**: input image
- **node2**: zoom in
- **node3**: uniform
- **node4**: local
- **node5**: frequency
- **node6**: encoder
- **node7**: patch embed
conv or linear
- **node8**: mask sampler
mask ratio 75 percent
- **node9**: encoder layers
visible tokens only
- **node10**: image b
- **node11**: decoder
- **node12**: mask tokens
- **node13**: add mask tokens
- **node14**: add pos embed
positional embeddings
- **node15**: decoder layers
- **node16**: reconstruction head
- **node17**: target reconstruction
- **node18**: loss
L2
- **node19**: masked pixel loss

### Edges

- reconstruction head → loss
L2
- mask tokens → add pos embed
positional embeddings
- mask tokens → add mask tokens
- add pos embed
positional embeddings → loss
L2
- loss
L2 → masked pixel loss
- patch embed
conv or linear → mask sampler
mask ratio 75 percent
- add mask tokens → decoder layers
- zoom in → decoder
- frequency → encoder
- mask tokens → decoder layers
- uniform → decoder
- input image → decoder
- encoder layers
visible tokens only → decoder
- patch embed
conv or linear → encoder layers
visible tokens only
- zoom in → image b
- local → mask sampler
mask ratio 75 percent
- zoom in → encoder
- uniform → patch embed
conv or linear
- uniform → image b
- uniform → encoder
- mask tokens → loss
L2
- zoom in → patch embed
conv or linear
- mask tokens → masked pixel loss
- add mask tokens → target reconstruction
- add pos embed
positional embeddings → decoder layers
- input image → patch embed
conv or linear
- input image → image b
- input image → encoder
- mask tokens → target reconstruction
- local → encoder layers
visible tokens only
- encoder layers
visible tokens only → image b
- add mask tokens → add pos embed
positional embeddings
- reconstruction head → masked pixel loss
- target reconstruction → loss
L2
- encoder → mask sampler
mask ratio 75 percent
- frequency → mask sampler
mask ratio 75 percent
- reconstruction head → target reconstruction
- patch embed
conv or linear → decoder
- mask sampler
mask ratio 75 percent → encoder layers
visible tokens only
- add pos embed
positional embeddings → masked pixel loss
- image b → decoder
- decoder layers → reconstruction head
- encoder → encoder layers
visible tokens only
- frequency → encoder layers
visible tokens only
- add mask tokens → reconstruction head
- mask tokens → reconstruction head
- zoom in → uniform
- encoder → image b
- add pos embed
positional embeddings → target reconstruction
- decoder layers → target reconstruction
- input image → zoom in
- local → decoder
- decoder layers → masked pixel loss
- patch embed
conv or linear → image b
- input image → uniform
- frequency → image b
- mask sampler
mask ratio 75 percent → decoder
- add pos embed
positional embeddings → reconstruction head
- target reconstruction → masked pixel loss
- local → patch embed
conv or linear
- zoom in → mask sampler
mask ratio 75 percent
- local → encoder
- local → image b
- uniform → mask sampler
mask ratio 75 percent
- frequency → decoder
- encoder → decoder
- add mask tokens → masked pixel loss
- mask sampler
mask ratio 75 percent → image b
- input image → mask sampler
mask ratio 75 percent
- add mask tokens → loss
L2
- decoder layers → loss
L2
- uniform → encoder layers
visible tokens only
- encoder → patch embed
conv or linear
- frequency → patch embed
conv or linear
- zoom in → encoder layers
visible tokens only
- input image → encoder layers
visible tokens only

## Reference Graph

### Nodes

- **node1**: input
- **node2**: encoder
- **node3**: decoder
- **node4**: target

### Edges

- decoder → target
- encoder → target
- input → target
- encoder → decoder
- input → encoder
- input → decoder

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| input image | input |
| encoder | encoder |
| decoder | decoder |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| input | encoder |
| input | decoder |
| encoder | decoder |