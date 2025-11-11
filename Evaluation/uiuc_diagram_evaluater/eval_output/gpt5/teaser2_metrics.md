# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\teaser2.png`
- **Reference**: `..\ground_png\teaser2.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.053
- **Recall**: 0.130
- **F1 Score**: 0.075

### Path Alignment
- **Precision**: 0.000
- **Recall**: 0.000
- **F1 Score**: 0.000

## Generated Graph

### Nodes

- **node1**: Online Semantic Segmentation
- **node2**: frame t1
- **node3**: frame t2
- **node4**: frame t3
- **node5**: write update
- **node6**: write update
- **node7**: write update
- **node8**: Memory Adapters
- **node9**: Offline Model
- **node10**: U-Net Minkowski-UNet
- **node11**: FCAF3D TD3D
- **node12**: Encoder Decoder
- **node13**: read from memory
- **node14**: Real-time Memory
- **node15**: Key Value Cache
- **node16**: enqueue
- **node17**: decay
- **node18**: top k
- **node19**: 3D-2D Adapter
- **node20**: write update
- **node21**: Online Object Detection
- **node22**: frame t1
- **node23**: frame t2
- **node24**: frame t3
- **node25**: write update
- **node26**: write update
- **node27**: write update
- **node28**: Memory Adapters
- **node29**: Offline Model
- **node30**: Detector Head
- **node31**: FCAF3D TD3D
- **node32**: read from memory
- **node33**: Real-time Memory
- **node34**: Box Feature Bank
- **node35**: enqueue
- **node36**: decay
- **node37**: top k
- **node38**: 3D-2D Adapter
- **node39**: write update
- **node40**: Online Instance Segmentation
- **node41**: frame t1
- **node42**: frame t2
- **node43**: frame t3
- **node44**: write update
- **node45**: write update
- **node46**: write update
- **node47**: Memory Adapters
- **node48**: Offline Model
- **node49**: Mask Head
- **node50**: read from memory
- **node51**: Real-time Memory
- **node52**: Instance Bank
- **node53**: enqueue
- **node54**: decay
- **node55**: top k
- **node56**: 3D NMS
- **node57**: write update

### Edges

- read from memory → 3D NMS
- frame t2 → read from memory
- write update → 3D-2D Adapter
- read from memory → Real-time Memory
- Offline Model → 3D-2D Adapter
- frame t1 → Instance Bank
- write update → Real-time Memory
- Real-time Memory → Box Feature Bank
- top k → 3D-2D Adapter
- enqueue → Box Feature Bank
- frame t1 → Real-time Memory
- decay → 3D-2D Adapter
- frame t2 → write update
- write update → Offline Model
- frame t1 → 3D-2D Adapter
- write update → Box Feature Bank
- read from memory → Key Value Cache
- Real-time Memory → Instance Bank
- write update → 3D-2D Adapter
- frame t3 → write update
- write update → Box Feature Bank
- read from memory → 3D-2D Adapter
- Key Value Cache → 3D-2D Adapter
- frame t1 → Offline Model
- decay → Instance Bank
- write update → 3D NMS
- frame t2 → 3D-2D Adapter
- decay → 3D-2D Adapter
- frame t1 → Key Value Cache
- Real-time Memory → Key Value Cache
- Box Feature Bank → 3D-2D Adapter
- frame t1 → 3D-2D Adapter
- Real-time Memory → 3D-2D Adapter
- frame t2 → write update
- frame t3 → write update
- top k → Instance Bank
- write update → Offline Model
- frame t2 → read from memory
- Offline Model → Box Feature Bank
- write update → write update
- Real-time Memory → 3D-2D Adapter
- frame t2 → 3D NMS
- frame t3 → write update
- write update → Real-time Memory
- Offline Model → 3D-2D Adapter
- enqueue → 3D-2D Adapter
- read from memory → Instance Bank
- enqueue → Key Value Cache
- frame t1 → Offline Model
- enqueue → 3D-2D Adapter
- write update → Offline Model
- read from memory → Real-time Memory
- write update → 3D-2D Adapter
- frame t1 → write update
- frame t2 → Offline Model
- frame t3 → write update
- write update → read from memory
- frame t2 → Offline Model
- read from memory → Box Feature Bank
- write update → write update
- frame t1 → write update
- frame t2 → Real-time Memory
- Real-time Memory → 3D NMS
- Instance Bank → 3D NMS
- frame t2 → read from memory
- read from memory → Offline Model
- write update → Offline Model
- Offline Model → Instance Bank
- enqueue → 3D NMS
- write update → Real-time Memory
- write update → Instance Bank
- write update → read from memory
- Offline Model → Real-time Memory
- write update → 3D NMS
- Offline Model → Real-time Memory
- top k → Key Value Cache
- write update → Real-time Memory
- frame t3 → write update
- top k → 3D-2D Adapter
- frame t1 → 3D NMS
- frame t1 → Real-time Memory
- write update → Offline Model
- write update → Real-time Memory
- frame t2 → Instance Bank
- read from memory → Offline Model
- read from memory → Offline Model
- write update → Key Value Cache
- Offline Model → Key Value Cache
- write update → Key Value Cache
- read from memory → Real-time Memory
- frame t2 → Real-time Memory
- read from memory → 3D-2D Adapter
- frame t2 → Real-time Memory
- write update → Offline Model
- write update → 3D-2D Adapter
- top k → Box Feature Bank
- frame t1 → Offline Model
- write update → read from memory
- frame t1 → write update
- decay → Box Feature Bank
- decay → 3D NMS
- frame t1 → Real-time Memory
- Offline Model → Real-time Memory
- frame t2 → Offline Model
- frame t1 → Box Feature Bank
- frame t3 → write update
- top k → 3D NMS
- Offline Model → 3D NMS
- frame t2 → Key Value Cache
- frame t2 → write update
- frame t2 → 3D-2D Adapter
- write update → write update
- enqueue → Instance Bank
- frame t2 → Box Feature Bank
- write update → Real-time Memory
- decay → Key Value Cache
- write update → Instance Bank

## Reference Graph

### Nodes

- **node1**: Online Semantic Segmentation
- **node2**: Online Object Detection
- **node3**: Online Instance Segmentation
- **node4**: wall
- **node5**: floor
- **node6**: cabinet
- **node7**: bed
- **node8**: chair
- **node9**: picture
- **node10**: counter
- **node11**: desk
- **node12**: curtain
- **node13**: refrigerator
- **node14**: sofa
- **node15**: table
- **node16**: door
- **node17**: window
- **node18**: bookshelf
- **node19**: shower curtain
- **node20**: toilet
- **node21**: sink
- **node22**: bathtub
- **node23**: other furniture

### Edges

- Online Object Detection → Online Instance Segmentation

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Online Semantic Segmentation | Online Semantic Segmentation |
| Online Object Detection | Online Object Detection |
| Online Instance Segmentation | Online Instance Segmentation |

## Path Alignment Matches

*(No matched paths)*