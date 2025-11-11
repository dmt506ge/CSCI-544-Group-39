# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\feature.png`
- **Reference**: `..\ground_png\feature.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.500
- **Recall**: 0.778
- **F1 Score**: 0.609

### Path Alignment
- **Precision**: 1.000
- **Recall**: 0.500
- **F1 Score**: 0.667

## Generated Graph

### Nodes

- **node1**: Labelled source domain
- **node2**: Unlabelled target domain
- **node3**: CNN
- **node4**: CNN
- **node5**: Feature map
- **node6**: Feature map
- **node7**: ID FC
- **node8**: Attr FC
- **node9**: Person IDs
- **node10**: IDs
- **node11**: L align
- **node12**: L ID
- **node13**: L attr
- **node14**: L attr cls

### Edges

- Feature map → Attr FC
- Unlabelled target domain → Attr FC
- CNN → L ID
- CNN → L attr cls
- Feature map → L attr cls
- Feature map → Person IDs
- Attr FC → L attr
- Labelled source domain → Feature map
- Unlabelled target domain → CNN
- CNN → L attr
- Attr FC → L attr cls
- Labelled source domain → IDs
- CNN → Feature map
- CNN → L attr cls
- ID FC → Person IDs
- Labelled source domain → Attr FC
- CNN → Feature map
- Feature map → IDs
- Labelled source domain → Person IDs
- CNN → IDs
- Feature map → Attr FC
- Feature map → L attr
- Feature map → L align
- Attr FC → IDs
- CNN → Person IDs
- CNN → Attr FC
- Feature map → ID FC
- Feature map → L attr
- Unlabelled target domain → L attr
- CNN → IDs
- Labelled source domain → L attr cls
- CNN → Attr FC
- Feature map → L ID
- Unlabelled target domain → Feature map
- Labelled source domain → CNN
- Labelled source domain → L align
- Unlabelled target domain → L attr cls
- Feature map → L attr cls
- Labelled source domain → ID FC
- CNN → L align
- Labelled source domain → L attr
- ID FC → L ID
- Labelled source domain → L ID
- CNN → ID FC
- CNN → L attr
- Feature map → IDs
- Unlabelled target domain → IDs

## Reference Graph

### Nodes

- **node1**: Labelled source domain
- **node2**: Unlabelled target domain
- **node3**: CNN
- **node4**: Feature map
- **node5**: ID-FC
- **node6**: Person IDs
- **node7**: Attr IDs
- **node8**: Attr-FC
- **node9**: L_attr

### Edges

- Unlabelled target domain → Attr-FC
- CNN → Person IDs
- Unlabelled target domain → L_attr
- Feature map → Attr IDs
- Labelled source domain → ID-FC
- Unlabelled target domain → Feature map
- Feature map → Person IDs
- Labelled source domain → Attr-FC
- CNN → ID-FC
- Labelled source domain → L_attr
- Unlabelled target domain → CNN
- Labelled source domain → Feature map
- CNN → Attr-FC
- CNN → L_attr
- Feature map → ID-FC
- ID-FC → Attr IDs
- Unlabelled target domain → Attr IDs
- CNN → Feature map
- Attr-FC → L_attr
- Feature map → Attr-FC
- ID-FC → Person IDs
- Unlabelled target domain → Person IDs
- Labelled source domain → CNN
- Feature map → L_attr
- Labelled source domain → Attr IDs
- Labelled source domain → Person IDs
- Unlabelled target domain → ID-FC
- CNN → Attr IDs

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Labelled source domain | Labelled source domain |
| Unlabelled target domain | Unlabelled target domain |
| CNN | CNN |
| Feature map | Feature map |
| ID FC | ID-FC |
| Person IDs | Person IDs |
| Attr FC | Attr-FC |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Labelled source domain | CNN |
| Labelled source domain | Feature map |
| Labelled source domain | ID-FC |
| Labelled source domain | Person IDs |
| Labelled source domain | Attr-FC |
| Unlabelled target domain | Attr-FC |
| CNN | Feature map |
| CNN | ID-FC |
| CNN | Person IDs |
| CNN | Attr-FC |
| Feature map | ID-FC |
| Feature map | Person IDs |
| Feature map | Attr-FC |
| ID-FC | Person IDs |