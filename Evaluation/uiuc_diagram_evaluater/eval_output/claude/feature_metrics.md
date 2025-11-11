# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\feature.png`
- **Reference**: `..\ground_png\feature.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.550
- **Recall**: 0.917
- **F1 Score**: 0.687

### Path Alignment
- **Precision**: 0.750
- **Recall**: 0.724
- **F1 Score**: 0.737

## Generated Graph

### Nodes

- **node1**: Labelled Source Domain
- **node2**: Unlabelled Target Domain
- **node3**: Temporal Consistency
- **node4**: CNN (trained)
- **node5**: CNN (shared)
- **node6**: Feature Map (Source)
fs
- **node7**: Feature Map (Target)
ft
- **node8**: Alignment
Statistical Matching
Cross-Domain Mixup
- **node9**: Clustering
Pseudo-Labels (iterative)
- **node10**: Memory Bank (OIM)
lookup table
- **node11**: ID-FC (Identity)
Triplet Loss
OIM Loss
- **node12**: Attr-FC (Attributes)
Mid-level features
- **node13**: Camera-Aware
Intra-camera probability
Inter-camera
- **node14**: Person IDs
- **node15**: Attr IDs
- **node16**: Training Phase: Joint Learning
- **node17**: Alignment: Iterative Updates
- **node18**: Triplet Loss (Hard-Batch)
L_htri: margin-based
- **node19**: OIM Loss
Online Instance Mining
- **node20**: Attribute Loss (L_attr)
Mid-level alignment

### Edges

- Camera-Aware
Intra-camera probability
Inter-camera → ID-FC (Identity)
Triplet Loss
OIM Loss
- Feature Map (Source)
fs → Memory Bank (OIM)
lookup table
- Feature Map (Source)
fs → Alignment
Statistical Matching
Cross-Domain Mixup
- Labelled Source Domain → Memory Bank (OIM)
lookup table
- Unlabelled Target Domain → Memory Bank (OIM)
lookup table
- Alignment: Iterative Updates → Alignment: Iterative Updates
- Alignment
Statistical Matching
Cross-Domain Mixup → Memory Bank (OIM)
lookup table
- Unlabelled Target Domain → Alignment
Statistical Matching
Cross-Domain Mixup
- Alignment
Statistical Matching
Cross-Domain Mixup → Alignment
Statistical Matching
Cross-Domain Mixup
- Alignment: Iterative Updates → Clustering
Pseudo-Labels (iterative)
- CNN (trained) → Person IDs
- Unlabelled Target Domain → Attr IDs
- Clustering
Pseudo-Labels (iterative) → Memory Bank (OIM)
lookup table
- Camera-Aware
Intra-camera probability
Inter-camera → Person IDs
- Temporal Consistency → ID-FC (Identity)
Triplet Loss
OIM Loss
- Alignment: Iterative Updates → Memory Bank (OIM)
lookup table
- Alignment: Iterative Updates → Alignment
Statistical Matching
Cross-Domain Mixup
- Labelled Source Domain → Feature Map (Source)
fs
- Temporal Consistency → Feature Map (Target)
ft
- Unlabelled Target Domain → CNN (shared)
- Unlabelled Target Domain → Alignment: Iterative Updates
- Temporal Consistency → Person IDs
- Feature Map (Target)
ft → Person IDs
- Temporal Consistency → Attr-FC (Attributes)
Mid-level features
- CNN (trained) → ID-FC (Identity)
Triplet Loss
OIM Loss
- Feature Map (Target)
ft → Attr-FC (Attributes)
Mid-level features
- CNN (shared) → Feature Map (Target)
ft
- ID-FC (Identity)
Triplet Loss
OIM Loss → Person IDs
- CNN (shared) → Person IDs
- Feature Map (Target)
ft → ID-FC (Identity)
Triplet Loss
OIM Loss
- Feature Map (Source)
fs → Person IDs
- Labelled Source Domain → Person IDs
- Alignment
Statistical Matching
Cross-Domain Mixup → Person IDs
- Temporal Consistency → Clustering
Pseudo-Labels (iterative)
- CNN (shared) → ID-FC (Identity)
Triplet Loss
OIM Loss
- Attr-FC (Attributes)
Mid-level features → Attr IDs
- Temporal Consistency → Memory Bank (OIM)
lookup table
- Temporal Consistency → Alignment
Statistical Matching
Cross-Domain Mixup
- Alignment: Iterative Updates → Person IDs
- Labelled Source Domain → CNN (trained)
- CNN (trained) → Alignment: Iterative Updates
- Feature Map (Source)
fs → ID-FC (Identity)
Triplet Loss
OIM Loss
- Temporal Consistency → Attr IDs
- Labelled Source Domain → ID-FC (Identity)
Triplet Loss
OIM Loss
- Unlabelled Target Domain → ID-FC (Identity)
Triplet Loss
OIM Loss
- Feature Map (Target)
ft → Attr IDs
- CNN (trained) → Clustering
Pseudo-Labels (iterative)
- Alignment
Statistical Matching
Cross-Domain Mixup → ID-FC (Identity)
Triplet Loss
OIM Loss
- CNN (shared) → Attr-FC (Attributes)
Mid-level features
- Unlabelled Target Domain → Feature Map (Target)
ft
- CNN (trained) → Memory Bank (OIM)
lookup table
- Clustering
Pseudo-Labels (iterative) → ID-FC (Identity)
Triplet Loss
OIM Loss
- CNN (trained) → Alignment
Statistical Matching
Cross-Domain Mixup
- Temporal Consistency → CNN (shared)
- Temporal Consistency → Alignment: Iterative Updates
- Alignment: Iterative Updates → ID-FC (Identity)
Triplet Loss
OIM Loss
- Unlabelled Target Domain → Person IDs
- Feature Map (Target)
ft → Alignment: Iterative Updates
- CNN (shared) → Attr IDs
- Unlabelled Target Domain → Attr-FC (Attributes)
Mid-level features
- Feature Map (Target)
ft → Clustering
Pseudo-Labels (iterative)
- Labelled Source Domain → Alignment
Statistical Matching
Cross-Domain Mixup
- Clustering
Pseudo-Labels (iterative) → Person IDs
- Memory Bank (OIM)
lookup table → Person IDs
- CNN (trained) → Feature Map (Source)
fs
- Feature Map (Target)
ft → Memory Bank (OIM)
lookup table
- Feature Map (Target)
ft → Alignment
Statistical Matching
Cross-Domain Mixup
- CNN (shared) → Alignment: Iterative Updates
- Temporal Consistency → Camera-Aware
Intra-camera probability
Inter-camera
- CNN (shared) → Clustering
Pseudo-Labels (iterative)
- Feature Map (Source)
fs → Alignment: Iterative Updates
- CNN (shared) → Memory Bank (OIM)
lookup table
- Labelled Source Domain → Alignment: Iterative Updates
- CNN (shared) → Alignment
Statistical Matching
Cross-Domain Mixup
- Alignment
Statistical Matching
Cross-Domain Mixup → Alignment: Iterative Updates
- Feature Map (Source)
fs → Clustering
Pseudo-Labels (iterative)
- Memory Bank (OIM)
lookup table → ID-FC (Identity)
Triplet Loss
OIM Loss
- Labelled Source Domain → Clustering
Pseudo-Labels (iterative)
- Unlabelled Target Domain → Clustering
Pseudo-Labels (iterative)
- Alignment
Statistical Matching
Cross-Domain Mixup → Clustering
Pseudo-Labels (iterative)

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
- **node12**: ID-FC

### Edges

- ID-FC → Attr IDs
- Feature map → Person IDs
- Labelled source domain → Person IDs
- Unlabelled target domain → Person IDs
- CNN → ID-FC
- CNN → Person IDs
- ID-FC → L_attr
- Feature map → ID-FC
- CNN → Feature map
- ID-FC → Person IDs
- Unlabelled target domain → CNN
- CNN → Attr IDs
- Feature map → ID-FC
- Feature map → Attr IDs
- Labelled source domain → CNN
- Labelled source domain → ID-FC
- Unlabelled target domain → ID-FC
- Unlabelled target domain → Feature map
- CNN → ID-FC
- Labelled source domain → Feature map
- CNN → Person IDs
- Feature map → Person IDs
- CNN → Feature map
- Attr-FC → L_attr
- Feature map → Attr IDs
- ID-FC → Attr-FC
- Labelled source domain → Attr IDs
- Unlabelled target domain → Attr IDs
- CNN → Attr IDs

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Labelled Source Domain | Labelled source domain |
| Unlabelled Target Domain | Unlabelled target domain |
| Temporal Consistency | CNN |
| CNN (shared) | CNN |
| Feature Map (Source)
fs | Feature map |
| Feature Map (Target)
ft | Feature map |
| ID-FC (Identity)
Triplet Loss
OIM Loss | ID-FC |
| Attr-FC (Attributes)
Mid-level features | Attr-FC |
| Person IDs | Person IDs |
| Attr IDs | Attr IDs |
| Attribute Loss (L_attr)
Mid-level alignment | L_attr |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Labelled source domain | Feature map |
| Labelled source domain | ID-FC |
| Labelled source domain | Person IDs |
| Unlabelled target domain | CNN |
| Unlabelled target domain | Feature map |
| Unlabelled target domain | ID-FC |
| Unlabelled target domain | Person IDs |
| Unlabelled target domain | Attr IDs |
| CNN | ID-FC |
| CNN | Person IDs |
| CNN | Attr IDs |
| CNN | Feature map |
| CNN | ID-FC |
| CNN | Person IDs |
| CNN | Attr IDs |
| Feature map | ID-FC |
| Feature map | Person IDs |
| Feature map | ID-FC |
| Feature map | Person IDs |
| Feature map | Attr IDs |
| ID-FC | Person IDs |