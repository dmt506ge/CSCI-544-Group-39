# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\claude\3.png`
- **Reference**: `..\ground_png\3.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.812
- **Recall**: 0.765
- **F1 Score**: 0.788

### Path Alignment
- **Precision**: 0.920
- **Recall**: 0.404
- **F1 Score**: 0.561

## Generated Graph

### Nodes

- **node1**: CPU
- **node2**: Video Sequences
- **node3**: Patch i Pixel-wide Embeddings S_i
- **node4**: Evenly random select N vectors: S_seed in S_i
- **node5**: Prune and Cluster, get r (clusters) and l (indices)
- **node6**: Obtain N_min based on Eq. (19)
- **node7**: i = i + 1
- **node8**: Update N (N = N x 2)
- **node9**: N <= L x N_min
- **node10**: N >= H x N_min
- **node11**: Patch i is last batch
- **node12**: End
- **node13**: GPU
- **node14**: Parallel Mean-shift
- **node15**: Converged
- **node16**: Y (clusters)

### Edges

- Update N (N = N x 2) → Obtain N_min based on Eq. (19)
- i = i + 1 → Parallel Mean-shift
- Parallel Mean-shift → Y (clusters)
- i = i + 1 → Patch i is last batch
- Obtain N_min based on Eq. (19) → Evenly random select N vectors: S_seed in S_i
- Obtain N_min based on Eq. (19) → i = i + 1
- Obtain N_min based on Eq. (19) → Y (clusters)
- N >= H x N_min → End
- Prune and Cluster, get r (clusters) and l (indices) → Patch i Pixel-wide Embeddings S_i
- N >= H x N_min → Evenly random select N vectors: S_seed in S_i
- N >= H x N_min → i = i + 1
- Prune and Cluster, get r (clusters) and l (indices) → Prune and Cluster, get r (clusters) and l (indices)
- Patch i Pixel-wide Embeddings S_i → Patch i Pixel-wide Embeddings S_i
- Obtain N_min based on Eq. (19) → Parallel Mean-shift
- Prune and Cluster, get r (clusters) and l (indices) → Update N (N = N x 2)
- Patch i Pixel-wide Embeddings S_i → Prune and Cluster, get r (clusters) and l (indices)
- Converged → Y (clusters)
- N >= H x N_min → Parallel Mean-shift
- N >= H x N_min → Patch i is last batch
- Patch i is last batch → End
- Patch i Pixel-wide Embeddings S_i → Update N (N = N x 2)
- Evenly random select N vectors: S_seed in S_i → Patch i is last batch
- i = i + 1 → N <= L x N_min
- Video Sequences → Prune and Cluster, get r (clusters) and l (indices)
- Update N (N = N x 2) → Patch i Pixel-wide Embeddings S_i
- Prune and Cluster, get r (clusters) and l (indices) → N >= H x N_min
- Video Sequences → Y (clusters)
- Update N (N = N x 2) → Update N (N = N x 2)
- i = i + 1 → Y (clusters)
- Prune and Cluster, get r (clusters) and l (indices) → Converged
- Evenly random select N vectors: S_seed in S_i → N <= L x N_min
- Video Sequences → Obtain N_min based on Eq. (19)
- Obtain N_min based on Eq. (19) → Prune and Cluster, get r (clusters) and l (indices)
- i = i + 1 → Obtain N_min based on Eq. (19)
- Obtain N_min based on Eq. (19) → Update N (N = N x 2)
- N >= H x N_min → Prune and Cluster, get r (clusters) and l (indices)
- Evenly random select N vectors: S_seed in S_i → End
- Update N (N = N x 2) → N >= H x N_min
- N >= H x N_min → Y (clusters)
- Evenly random select N vectors: S_seed in S_i → Evenly random select N vectors: S_seed in S_i
- Evenly random select N vectors: S_seed in S_i → i = i + 1
- Obtain N_min based on Eq. (19) → Obtain N_min based on Eq. (19)
- N <= L x N_min → N >= H x N_min
- N >= H x N_min → Obtain N_min based on Eq. (19)
- Update N (N = N x 2) → Converged
- Evenly random select N vectors: S_seed in S_i → Parallel Mean-shift
- N <= L x N_min → Converged
- Parallel Mean-shift → Converged
- Video Sequences → Patch i Pixel-wide Embeddings S_i
- i = i + 1 → Patch i Pixel-wide Embeddings S_i
- Evenly random select N vectors: S_seed in S_i → Converged
- N <= L x N_min → End
- i = i + 1 → Prune and Cluster, get r (clusters) and l (indices)
- Video Sequences → Update N (N = N x 2)
- N <= L x N_min → Evenly random select N vectors: S_seed in S_i
- Prune and Cluster, get r (clusters) and l (indices) → N <= L x N_min
- Patch i Pixel-wide Embeddings S_i → N >= H x N_min
- i = i + 1 → Update N (N = N x 2)
- Update N (N = N x 2) → Patch i is last batch
- Converged → Converged
- Obtain N_min based on Eq. (19) → Patch i Pixel-wide Embeddings S_i
- N >= H x N_min → Patch i Pixel-wide Embeddings S_i
- Patch i Pixel-wide Embeddings S_i → Converged
- N <= L x N_min → Patch i is last batch
- Prune and Cluster, get r (clusters) and l (indices) → End
- Video Sequences → N >= H x N_min
- Prune and Cluster, get r (clusters) and l (indices) → Evenly random select N vectors: S_seed in S_i
- Prune and Cluster, get r (clusters) and l (indices) → i = i + 1
- Evenly random select N vectors: S_seed in S_i → Prune and Cluster, get r (clusters) and l (indices)
- Patch i Pixel-wide Embeddings S_i → End
- N >= H x N_min → Update N (N = N x 2)
- Patch i Pixel-wide Embeddings S_i → Evenly random select N vectors: S_seed in S_i
- Evenly random select N vectors: S_seed in S_i → Y (clusters)
- Update N (N = N x 2) → N <= L x N_min
- Video Sequences → Converged
- Prune and Cluster, get r (clusters) and l (indices) → Parallel Mean-shift
- Prune and Cluster, get r (clusters) and l (indices) → Patch i is last batch
- Evenly random select N vectors: S_seed in S_i → Obtain N_min based on Eq. (19)
- Obtain N_min based on Eq. (19) → N >= H x N_min
- Patch i Pixel-wide Embeddings S_i → Patch i is last batch
- N <= L x N_min → N <= L x N_min
- N >= H x N_min → N >= H x N_min
- N <= L x N_min → Update N (N = N x 2)
- Update N (N = N x 2) → End
- Obtain N_min based on Eq. (19) → Converged
- Update N (N = N x 2) → Evenly random select N vectors: S_seed in S_i
- Update N (N = N x 2) → i = i + 1
- N >= H x N_min → Converged
- Video Sequences → Patch i is last batch
- N <= L x N_min → i = i + 1
- N <= L x N_min → Y (clusters)
- Update N (N = N x 2) → Parallel Mean-shift
- Patch i Pixel-wide Embeddings S_i → N <= L x N_min
- N <= L x N_min → Obtain N_min based on Eq. (19)
- N <= L x N_min → Parallel Mean-shift
- Parallel Mean-shift → Parallel Mean-shift
- Evenly random select N vectors: S_seed in S_i → Patch i Pixel-wide Embeddings S_i
- Obtain N_min based on Eq. (19) → Patch i is last batch
- Prune and Cluster, get r (clusters) and l (indices) → Y (clusters)
- i = i + 1 → N >= H x N_min
- Video Sequences → N <= L x N_min
- Evenly random select N vectors: S_seed in S_i → Update N (N = N x 2)
- Patch i Pixel-wide Embeddings S_i → i = i + 1
- Patch i Pixel-wide Embeddings S_i → Y (clusters)
- Prune and Cluster, get r (clusters) and l (indices) → Obtain N_min based on Eq. (19)
- Converged → Parallel Mean-shift
- i = i + 1 → Converged
- Patch i Pixel-wide Embeddings S_i → Obtain N_min based on Eq. (19)
- Patch i Pixel-wide Embeddings S_i → Parallel Mean-shift
- Video Sequences → End
- Obtain N_min based on Eq. (19) → N <= L x N_min
- Video Sequences → Evenly random select N vectors: S_seed in S_i
- Update N (N = N x 2) → Prune and Cluster, get r (clusters) and l (indices)
- Video Sequences → i = i + 1
- i = i + 1 → End
- Evenly random select N vectors: S_seed in S_i → N >= H x N_min
- N <= L x N_min → Patch i Pixel-wide Embeddings S_i
- i = i + 1 → Evenly random select N vectors: S_seed in S_i
- N >= H x N_min → N <= L x N_min
- i = i + 1 → i = i + 1
- Update N (N = N x 2) → Y (clusters)
- N <= L x N_min → Prune and Cluster, get r (clusters) and l (indices)
- Video Sequences → Parallel Mean-shift
- Obtain N_min based on Eq. (19) → End

## Reference Graph

### Nodes

- **node1**: CPU
- **node2**: Video Sequences
- **node3**: Patch i
Pixel-wide Embeddings Si
- **node4**: Evenly random select N vectors: Sseed ∈ Si
- **node5**: Prune & Cluster, get r and I
- **node6**: Obtain Nmin based on Eq. (19)
- **node7**: N ≤ L × Nmin
- **node8**: N = N * 2
- **node9**: Update N
- **node10**: i = i + 1
- **node11**: N ≥ H × Nmin
- **node12**: N = N - Nmin
- **node13**: Patch i is last batch
- **node14**: End
- **node15**: GPU
- **node16**: Parallel Mean-shift
- **node17**: Converged >γ

### Edges

- N = N * 2 → Obtain Nmin based on Eq. (19)
- Parallel Mean-shift → Prune & Cluster, get r and I
- N ≤ L × Nmin → End
- Converged >γ → N = N - Nmin
- N ≤ L × Nmin → N ≥ H × Nmin
- Obtain Nmin based on Eq. (19) → Evenly random select N vectors: Sseed ∈ Si
- Obtain Nmin based on Eq. (19) → N ≤ L × Nmin
- Update N → Patch i is last batch
- Converged >γ → Evenly random select N vectors: Sseed ∈ Si
- Obtain Nmin based on Eq. (19) → Parallel Mean-shift
- i = i + 1 → N = N - Nmin
- Parallel Mean-shift → Parallel Mean-shift
- i = i + 1 → Evenly random select N vectors: Sseed ∈ Si
- N ≥ H × Nmin → Update N
- i = i + 1 → N ≤ L × Nmin
- N = N - Nmin → N = N - Nmin
- Prune & Cluster, get r and I → Prune & Cluster, get r and I
- Prune & Cluster, get r and I → Converged >γ
- N = N - Nmin → Evenly random select N vectors: Sseed ∈ Si
- Obtain Nmin based on Eq. (19) → End
- N = N - Nmin → N ≤ L × Nmin
- Parallel Mean-shift → Obtain Nmin based on Eq. (19)
- Converged >γ → N ≥ H × Nmin
- Prune & Cluster, get r and I → N = N * 2
- Patch i
Pixel-wide Embeddings Si → Prune & Cluster, get r and I
- Patch i
Pixel-wide Embeddings Si → Converged >γ
- i = i + 1 → End
- i = i + 1 → N ≥ H × Nmin
- Prune & Cluster, get r and I → Patch i is last batch
- N ≥ H × Nmin → N = N - Nmin
- Patch i
Pixel-wide Embeddings Si → N = N * 2
- Evenly random select N vectors: Sseed ∈ Si → N ≥ H × Nmin
- N = N - Nmin → N ≥ H × Nmin
- N ≥ H × Nmin → Evenly random select N vectors: Sseed ∈ Si
- N ≤ L × Nmin → Update N
- N ≥ H × Nmin → N ≤ L × Nmin
- N ≥ H × Nmin → Parallel Mean-shift
- Patch i
Pixel-wide Embeddings Si → Patch i is last batch
- Video Sequences → Prune & Cluster, get r and I
- Prune & Cluster, get r and I → i = i + 1
- N ≥ H × Nmin → Obtain Nmin based on Eq. (19)
- N ≥ H × Nmin → End
- N = N * 2 → Converged >γ
- Converged >γ → Update N
- Video Sequences → Parallel Mean-shift
- N = N * 2 → N = N * 2
- Video Sequences → Patch i is last batch
- N ≤ L × Nmin → Parallel Mean-shift
- Evenly random select N vectors: Sseed ∈ Si → Update N
- N = N * 2 → Patch i is last batch
- Video Sequences → Obtain Nmin based on Eq. (19)
- N = N - Nmin → Update N
- Obtain Nmin based on Eq. (19) → Prune & Cluster, get r and I
- Obtain Nmin based on Eq. (19) → Converged >γ
- N ≤ L × Nmin → Obtain Nmin based on Eq. (19)
- Parallel Mean-shift → Converged >γ
- Obtain Nmin based on Eq. (19) → N = N * 2
- i = i + 1 → Prune & Cluster, get r and I
- Converged >γ → N ≤ L × Nmin
- Parallel Mean-shift → N = N * 2
- Converged >γ → Parallel Mean-shift
- Obtain Nmin based on Eq. (19) → Patch i is last batch
- Evenly random select N vectors: Sseed ∈ Si → N = N - Nmin
- N = N * 2 → i = i + 1
- i = i + 1 → Parallel Mean-shift
- Parallel Mean-shift → Patch i is last batch
- Evenly random select N vectors: Sseed ∈ Si → Evenly random select N vectors: Sseed ∈ Si
- Evenly random select N vectors: Sseed ∈ Si → N ≤ L × Nmin
- Obtain Nmin based on Eq. (19) → Obtain Nmin based on Eq. (19)
- Converged >γ → Obtain Nmin based on Eq. (19)
- Converged >γ → End
- N = N - Nmin → Parallel Mean-shift
- Update N → i = i + 1
- i = i + 1 → Obtain Nmin based on Eq. (19)
- N ≥ H × Nmin → Prune & Cluster, get r and I
- N ≥ H × Nmin → Converged >γ
- Evenly random select N vectors: Sseed ∈ Si → End
- N = N - Nmin → Obtain Nmin based on Eq. (19)
- N = N - Nmin → End
- Parallel Mean-shift → i = i + 1
- N ≥ H × Nmin → N = N * 2
- Video Sequences → Patch i
Pixel-wide Embeddings Si
- N ≥ H × Nmin → Patch i is last batch
- Video Sequences → Converged >γ
- Update N → N = N - Nmin
- N ≤ L × Nmin → Prune & Cluster, get r and I
- N ≤ L × Nmin → Converged >γ
- Video Sequences → N = N * 2
- Patch i is last batch → End
- Update N → Evenly random select N vectors: Sseed ∈ Si
- Prune & Cluster, get r and I → Update N
- Patch i
Pixel-wide Embeddings Si → i = i + 1
- N ≤ L × Nmin → N = N * 2
- N = N * 2 → N ≥ H × Nmin
- N ≤ L × Nmin → Patch i is last batch
- Update N → N ≥ H × Nmin
- Converged >γ → Prune & Cluster, get r and I
- Converged >γ → Converged >γ
- Prune & Cluster, get r and I → N = N - Nmin
- i = i + 1 → Converged >γ
- Converged >γ → N = N * 2
- Video Sequences → i = i + 1
- Prune & Cluster, get r and I → Evenly random select N vectors: Sseed ∈ Si
- Parallel Mean-shift → N ≥ H × Nmin
- Prune & Cluster, get r and I → N ≤ L × Nmin
- Evenly random select N vectors: Sseed ∈ Si → Prune & Cluster, get r and I
- Patch i
Pixel-wide Embeddings Si → N = N - Nmin
- i = i + 1 → N = N * 2
- N = N - Nmin → Prune & Cluster, get r and I
- N = N - Nmin → Converged >γ
- Converged >γ → Patch i is last batch
- Patch i
Pixel-wide Embeddings Si → Evenly random select N vectors: Sseed ∈ Si
- i = i + 1 → Patch i is last batch
- Evenly random select N vectors: Sseed ∈ Si → Parallel Mean-shift
- N = N - Nmin → N = N * 2
- N = N * 2 → Update N
- Prune & Cluster, get r and I → End
- Evenly random select N vectors: Sseed ∈ Si → Patch i is last batch
- Prune & Cluster, get r and I → N ≥ H × Nmin
- N = N - Nmin → Patch i is last batch
- Evenly random select N vectors: Sseed ∈ Si → Obtain Nmin based on Eq. (19)
- Obtain Nmin based on Eq. (19) → i = i + 1
- Patch i
Pixel-wide Embeddings Si → N ≥ H × Nmin
- Update N → Update N
- i = i + 1 → i = i + 1
- Update N → N = N * 2
- N = N * 2 → N = N - Nmin
- Parallel Mean-shift → Update N
- N = N * 2 → Evenly random select N vectors: Sseed ∈ Si
- N = N * 2 → N ≤ L × Nmin
- Video Sequences → N ≥ H × Nmin
- Update N → N ≤ L × Nmin
- Update N → Parallel Mean-shift
- N = N * 2 → End
- Parallel Mean-shift → N = N - Nmin
- N ≥ H × Nmin → i = i + 1
- Parallel Mean-shift → Evenly random select N vectors: Sseed ∈ Si
- Patch i
Pixel-wide Embeddings Si → Update N
- Parallel Mean-shift → N ≤ L × Nmin
- Update N → Obtain Nmin based on Eq. (19)
- Update N → End
- Obtain Nmin based on Eq. (19) → N ≥ H × Nmin
- Parallel Mean-shift → End
- Evenly random select N vectors: Sseed ∈ Si → Converged >γ
- Prune & Cluster, get r and I → Parallel Mean-shift
- N ≤ L × Nmin → i = i + 1
- Video Sequences → Update N
- Evenly random select N vectors: Sseed ∈ Si → N = N * 2
- Patch i
Pixel-wide Embeddings Si → N ≤ L × Nmin
- Patch i
Pixel-wide Embeddings Si → Parallel Mean-shift
- Prune & Cluster, get r and I → Obtain Nmin based on Eq. (19)
- Patch i
Pixel-wide Embeddings Si → Obtain Nmin based on Eq. (19)
- Patch i
Pixel-wide Embeddings Si → End
- Converged >γ → i = i + 1
- Video Sequences → N = N - Nmin
- N ≥ H × Nmin → N ≥ H × Nmin
- Obtain Nmin based on Eq. (19) → Update N
- Video Sequences → Evenly random select N vectors: Sseed ∈ Si
- N = N * 2 → Prune & Cluster, get r and I
- Video Sequences → N ≤ L × Nmin
- N ≤ L × Nmin → N = N - Nmin
- Evenly random select N vectors: Sseed ∈ Si → i = i + 1
- N ≤ L × Nmin → Evenly random select N vectors: Sseed ∈ Si
- N = N - Nmin → i = i + 1
- i = i + 1 → Update N
- N ≤ L × Nmin → N ≤ L × Nmin
- N = N * 2 → Parallel Mean-shift
- Update N → Prune & Cluster, get r and I
- Update N → Converged >γ
- Video Sequences → End
- Obtain Nmin based on Eq. (19) → N = N - Nmin

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| CPU | CPU |
| Video Sequences | Video Sequences |
| Patch i Pixel-wide Embeddings S_i | Patch i
Pixel-wide Embeddings Si |
| Evenly random select N vectors: S_seed in S_i | Evenly random select N vectors: Sseed ∈ Si |
| Prune and Cluster, get r (clusters) and l (indices) | Prune & Cluster, get r and I |
| Obtain N_min based on Eq. (19) | Obtain Nmin based on Eq. (19) |
| Update N (N = N x 2) | Update N |
| N >= H x N_min | N ≥ H × Nmin |
| Patch i is last batch | Patch i is last batch |
| End | End |
| GPU | GPU |
| Parallel Mean-shift | Parallel Mean-shift |
| Converged | Converged >γ |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| N ≥ H × Nmin | N ≥ H × Nmin |
| N ≥ H × Nmin | Patch i is last batch |
| N ≥ H × Nmin | End |
| N ≥ H × Nmin | Parallel Mean-shift |
| N ≥ H × Nmin | Converged >γ |
| N ≥ H × Nmin | Evenly random select N vectors: Sseed ∈ Si |
| N ≥ H × Nmin | Prune & Cluster, get r and I |
| N ≥ H × Nmin | Obtain Nmin based on Eq. (19) |
| N ≥ H × Nmin | Update N |
| Patch i is last batch | End |
| Parallel Mean-shift | Parallel Mean-shift |
| Parallel Mean-shift | Converged >γ |
| Converged >γ | Parallel Mean-shift |
| Converged >γ | Converged >γ |
| Video Sequences | N ≥ H × Nmin |
| Video Sequences | Patch i is last batch |
| Video Sequences | End |
| Video Sequences | Parallel Mean-shift |
| Video Sequences | Converged >γ |
| Video Sequences | Patch i
Pixel-wide Embeddings Si |
| Video Sequences | Evenly random select N vectors: Sseed ∈ Si |
| Video Sequences | Prune & Cluster, get r and I |
| Video Sequences | Obtain Nmin based on Eq. (19) |
| Video Sequences | Update N |
| Patch i
Pixel-wide Embeddings Si | N ≥ H × Nmin |
| Patch i
Pixel-wide Embeddings Si | Patch i is last batch |
| Patch i
Pixel-wide Embeddings Si | End |
| Patch i
Pixel-wide Embeddings Si | Parallel Mean-shift |
| Patch i
Pixel-wide Embeddings Si | Converged >γ |
| Patch i
Pixel-wide Embeddings Si | Evenly random select N vectors: Sseed ∈ Si |
| Patch i
Pixel-wide Embeddings Si | Prune & Cluster, get r and I |
| Patch i
Pixel-wide Embeddings Si | Obtain Nmin based on Eq. (19) |
| Patch i
Pixel-wide Embeddings Si | Update N |
| Evenly random select N vectors: Sseed ∈ Si | N ≥ H × Nmin |
| Evenly random select N vectors: Sseed ∈ Si | Patch i is last batch |
| Evenly random select N vectors: Sseed ∈ Si | End |
| Evenly random select N vectors: Sseed ∈ Si | Parallel Mean-shift |
| Evenly random select N vectors: Sseed ∈ Si | Converged >γ |
| Evenly random select N vectors: Sseed ∈ Si | Evenly random select N vectors: Sseed ∈ Si |
| Evenly random select N vectors: Sseed ∈ Si | Prune & Cluster, get r and I |
| Evenly random select N vectors: Sseed ∈ Si | Obtain Nmin based on Eq. (19) |
| Evenly random select N vectors: Sseed ∈ Si | Update N |
| Prune & Cluster, get r and I | N ≥ H × Nmin |
| Prune & Cluster, get r and I | Patch i is last batch |
| Prune & Cluster, get r and I | End |
| Prune & Cluster, get r and I | Parallel Mean-shift |
| Prune & Cluster, get r and I | Converged >γ |
| Prune & Cluster, get r and I | Evenly random select N vectors: Sseed ∈ Si |
| Prune & Cluster, get r and I | Prune & Cluster, get r and I |
| Prune & Cluster, get r and I | Obtain Nmin based on Eq. (19) |
| Prune & Cluster, get r and I | Update N |
| Obtain Nmin based on Eq. (19) | N ≥ H × Nmin |
| Obtain Nmin based on Eq. (19) | Patch i is last batch |
| Obtain Nmin based on Eq. (19) | End |
| Obtain Nmin based on Eq. (19) | Parallel Mean-shift |
| Obtain Nmin based on Eq. (19) | Converged >γ |
| Obtain Nmin based on Eq. (19) | Evenly random select N vectors: Sseed ∈ Si |
| Obtain Nmin based on Eq. (19) | Prune & Cluster, get r and I |
| Obtain Nmin based on Eq. (19) | Obtain Nmin based on Eq. (19) |
| Obtain Nmin based on Eq. (19) | Update N |
| Update N | N ≥ H × Nmin |
| Update N | Patch i is last batch |
| Update N | End |
| Update N | Parallel Mean-shift |
| Update N | Converged >γ |
| Update N | Evenly random select N vectors: Sseed ∈ Si |
| Update N | Prune & Cluster, get r and I |
| Update N | Obtain Nmin based on Eq. (19) |
| Update N | Update N |