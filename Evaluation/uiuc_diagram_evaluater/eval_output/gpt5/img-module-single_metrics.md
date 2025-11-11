# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\img-module-single.png`
- **Reference**: `..\ground_png\img-module-single.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.533
- **Recall**: 0.571
- **F1 Score**: 0.552

### Path Alignment
- **Precision**: 0.800
- **Recall**: 0.080
- **F1 Score**: 0.145

## Generated Graph

### Nodes

- **node1**: Memory based adapter for image features
- **node2**: Reorganize input shift channels to memory fuse with previous memory by 2d convolution add global context from 3d memory
- **node3**: Input feature from image backbone shape C x H x W
- **node4**: Reorganize channels
- **node5**: Split channels p between 0.25 and 0.5 to mem
- **node6**: Write memory write to mem t plus 1 shift out t plus 1
- **node7**: Current frame kept channels t
- **node8**: Read memory read mem t minus 1 shift in from t minus 1
- **node9**: Temporal conv 2d shape Q x H x W
- **node10**: Context fusion concat then 1 x 1 conv or attention or add
- **node11**: Adapter output to next backbone layer
- **node12**: Backbone layer k plus 1
- **node13**: 3d memory maintain context maintained over time
- **node14**: Project to view from 3d memory to temporal grid
- **node15**: Aggregate densify temporal pooling or attention plus upsampling per

### Edges

- Input feature from image backbone shape C x H x W → Split channels p between 0.25 and 0.5 to mem
- 3d memory maintain context maintained over time → Project to view from 3d memory to temporal grid
- Read memory read mem t minus 1 shift in from t minus 1 → Split channels p between 0.25 and 0.5 to mem
- Read memory read mem t minus 1 shift in from t minus 1 → Adapter output to next backbone layer
- Reorganize channels → Write memory write to mem t plus 1 shift out t plus 1
- Reorganize channels → Temporal conv 2d shape Q x H x W
- Split channels p between 0.25 and 0.5 to mem → Current frame kept channels t
- Input feature from image backbone shape C x H x W → Reorganize channels
- Input feature from image backbone shape C x H x W → Write memory write to mem t plus 1 shift out t plus 1
- Temporal conv 2d shape Q x H x W → Adapter output to next backbone layer
- Current frame kept channels t → Context fusion concat then 1 x 1 conv or attention or add
- Context fusion concat then 1 x 1 conv or attention or add → Adapter output to next backbone layer
- 3d memory maintain context maintained over time → Aggregate densify temporal pooling or attention plus upsampling per
- Read memory read mem t minus 1 shift in from t minus 1 → Write memory write to mem t plus 1 shift out t plus 1
- Input feature from image backbone shape C x H x W → Temporal conv 2d shape Q x H x W
- Current frame kept channels t → Backbone layer k plus 1
- Read memory read mem t minus 1 shift in from t minus 1 → Temporal conv 2d shape Q x H x W
- Split channels p between 0.25 and 0.5 to mem → Adapter output to next backbone layer
- Reorganize channels → Context fusion concat then 1 x 1 conv or attention or add
- Reorganize channels → Backbone layer k plus 1
- Input feature from image backbone shape C x H x W → Context fusion concat then 1 x 1 conv or attention or add
- Split channels p between 0.25 and 0.5 to mem → Write memory write to mem t plus 1 shift out t plus 1
- Read memory read mem t minus 1 shift in from t minus 1 → Context fusion concat then 1 x 1 conv or attention or add
- Split channels p between 0.25 and 0.5 to mem → Temporal conv 2d shape Q x H x W
- Reorganize channels → Current frame kept channels t
- Input feature from image backbone shape C x H x W → Backbone layer k plus 1
- Read memory read mem t minus 1 shift in from t minus 1 → Backbone layer k plus 1
- Current frame kept channels t → Adapter output to next backbone layer
- Temporal conv 2d shape Q x H x W → Context fusion concat then 1 x 1 conv or attention or add
- Input feature from image backbone shape C x H x W → Current frame kept channels t
- Project to view from 3d memory to temporal grid → Aggregate densify temporal pooling or attention plus upsampling per
- Temporal conv 2d shape Q x H x W → Backbone layer k plus 1
- Context fusion concat then 1 x 1 conv or attention or add → Backbone layer k plus 1
- Read memory read mem t minus 1 shift in from t minus 1 → Current frame kept channels t
- Adapter output to next backbone layer → Backbone layer k plus 1
- Reorganize channels → Split channels p between 0.25 and 0.5 to mem
- Reorganize channels → Adapter output to next backbone layer
- Split channels p between 0.25 and 0.5 to mem → Context fusion concat then 1 x 1 conv or attention or add
- Current frame kept channels t → Temporal conv 2d shape Q x H x W
- Split channels p between 0.25 and 0.5 to mem → Backbone layer k plus 1
- Input feature from image backbone shape C x H x W → Adapter output to next backbone layer

## Reference Graph

### Nodes

- **node1**: Input feature
- **node2**: Image memory
- **node3**: Image adapter
- **node4**: 3D memory
- **node5**: 3D to 2D adapter
- **node6**: reorganize
- **node7**: shift
- **node8**: shift in
from memory
- **node9**: shift out
to memory
- **node10**: add
- **node11**: add
- **node12**: project
- **node13**: aggregate
- **node14**: densify

### Edges

- aggregate → densify
- reorganize → Image memory
- reorganize → add
- reorganize → Image adapter
- Input feature → reorganize
- Image memory → shift in
from memory
- shift → Image memory
- shift → Image adapter
- shift → add
- Input feature → shift out
to memory
- shift in
from memory → shift out
to memory
- reorganize → shift
- reorganize → shift in
from memory
- aggregate → 3D to 2D adapter
- 3D to 2D adapter → 3D to 2D adapter
- 3D to 2D adapter → aggregate
- Input feature → Image memory
- shift out
to memory → shift out
to memory
- aggregate → aggregate
- shift → shift in
from memory
- Input feature → add
- Input feature → Image adapter
- 3D memory → project
- 3D memory → densify
- shift in
from memory → Image memory
- shift in
from memory → Image adapter
- densify → densify
- project → densify
- shift in
from memory → add
- Image memory → shift out
to memory
- shift out
to memory → Image memory
- Input feature → shift
- Input feature → shift in
from memory
- shift out
to memory → add
- shift out
to memory → Image adapter
- add → Image adapter
- Image memory → Image memory
- shift in
from memory → shift in
from memory
- reorganize → shift out
to memory
- 3D memory → 3D to 2D adapter
- 3D memory → aggregate
- Image memory → add
- Image memory → Image adapter
- shift → shift out
to memory
- densify → 3D to 2D adapter
- densify → aggregate
- project → 3D to 2D adapter
- project → aggregate
- shift out
to memory → shift in
from memory
- 3D to 2D adapter → densify

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Memory based adapter for image features | Image adapter |
| Reorganize input shift channels to memory fuse with previous memory by 2d convolution add global context from 3d memory | reorganize |
| Write memory write to mem t plus 1 shift out t plus 1 | shift out
to memory |
| Read memory read mem t minus 1 shift in from t minus 1 | shift in
from memory |
| Temporal conv 2d shape Q x H x W | 3D to 2D adapter |
| 3d memory maintain context maintained over time | 3D memory |
| Project to view from 3d memory to temporal grid | project |
| Aggregate densify temporal pooling or attention plus upsampling per | aggregate |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| project | aggregate |
| 3D memory | project |
| 3D memory | aggregate |
| shift in
from memory | shift out
to memory |