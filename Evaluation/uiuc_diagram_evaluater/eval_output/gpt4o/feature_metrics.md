# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\feature.png`
- **Reference**: `..\ground_png\feature.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.917
- **Recall**: 1.000
- **F1 Score**: 0.957

### Path Alignment
- **Precision**: 0.864
- **Recall**: 0.442
- **F1 Score**: 0.585

## Generated Graph

### Nodes

- **node1**: Labelled Source Domain
- **node2**: Unlabelled Target Domain
- **node3**: CNN
- **node4**: CNN
- **node5**: Feature Map
- **node6**: Feature Map
- **node7**: ID-FC
- **node8**: Attr-FC
- **node9**: Person IDs
- **node10**: Attr IDs
- **node11**: L_attr
- **node12**: Cotraining

### Edges

- Labelled Source Domain → Attr-FC
- Labelled Source Domain → Feature Map
- Unlabelled Target Domain → Cotraining
- Feature Map → Attr IDs
- CNN → Attr IDs
- Feature Map → Person IDs
- Feature Map → Cotraining
- CNN → Person IDs
- Labelled Source Domain → ID-FC
- ID-FC → Person IDs
- Unlabelled Target Domain → CNN
- Cotraining → Cotraining
- CNN → Cotraining
- Attr-FC → Attr IDs
- Unlabelled Target Domain → Feature Map
- Feature Map → Attr-FC
- CNN → Feature Map
- CNN → Attr-FC
- Feature Map → Feature Map
- CNN → ID-FC
- Labelled Source Domain → CNN
- Feature Map → ID-FC
- L_attr → Attr IDs
- Cotraining → Feature Map
- Labelled Source Domain → Attr IDs
- CNN → Feature Map
- Labelled Source Domain → Person IDs

## Reference Graph

### Nodes

- **node1**: Labelled source domain
- **node2**: Unlabelled target domain
- **node3**: CNN
- **node4**: CNN
- **node5**: Feature map
- **node6**: Feature map
- **node7**: ID-FC
- **node8**: Person IDs
- **node9**: Attr IDs
- **node10**: Attr-FC
- **node11**: L_attr

### Edges

- Feature map → Attr-FC
- Unlabelled target domain → Attr IDs
- Feature map → L_attr
- Feature map → Attr IDs
- CNN → L_attr
- ID-FC → L_attr
- Attr IDs → Attr-FC
- Labelled source domain → Person IDs
- Labelled source domain → Feature map
- Unlabelled target domain → Person IDs
- CNN → Attr IDs
- CNN → Attr-FC
- Feature map → Attr-FC
- CNN → Attr-FC
- Feature map → Attr IDs
- Feature map → Person IDs
- CNN → Attr IDs
- Labelled source domain → ID-FC
- ID-FC → Attr-FC
- Unlabelled target domain → ID-FC
- ID-FC → Attr IDs
- Feature map → ID-FC
- Unlabelled target domain → CNN
- CNN → Person IDs
- Unlabelled target domain → Feature map
- Feature map → Person IDs
- CNN → Feature map
- Labelled source domain → L_attr
- CNN → Person IDs
- Unlabelled target domain → L_attr
- ID-FC → Person IDs
- CNN → ID-FC
- Feature map → L_attr
- CNN → ID-FC
- Labelled source domain → CNN
- Feature map → ID-FC
- Attr-FC → L_attr
- Attr IDs → L_attr
- Labelled source domain → Attr-FC
- CNN → Feature map
- Labelled source domain → Attr IDs
- CNN → L_attr
- Unlabelled target domain → Attr-FC

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Labelled Source Domain | Labelled source domain |
| Unlabelled Target Domain | Unlabelled target domain |
| CNN | CNN |
| CNN | CNN |
| Feature Map | Feature map |
| Feature Map | Feature map |
| ID-FC | ID-FC |
| Attr-FC | Attr-FC |
| Person IDs | Person IDs |
| Attr IDs | Attr IDs |
| L_attr | L_attr |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Labelled source domain | Attr-FC |
| Labelled source domain | CNN |
| Labelled source domain | Feature map |
| Labelled source domain | ID-FC |
| Labelled source domain | Person IDs |
| Labelled source domain | Attr IDs |
| Unlabelled target domain | CNN |
| Unlabelled target domain | Feature map |
| CNN | Attr-FC |
| CNN | Feature map |
| CNN | ID-FC |
| CNN | Person IDs |
| CNN | Attr IDs |
| CNN | Feature map |
| Feature map | Attr-FC |
| Feature map | ID-FC |
| Feature map | Person IDs |
| Feature map | Attr IDs |
| ID-FC | Person IDs |