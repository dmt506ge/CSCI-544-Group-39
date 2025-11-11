# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt4o\3.png`
- **Reference**: `..\ground_png\3.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.765
- **Recall**: 0.765
- **F1 Score**: 0.765

### Path Alignment
- **Precision**: 0.978
- **Recall**: 0.210
- **F1 Score**: 0.345

## Generated Graph

### Nodes

- **node1**: CPU Section
- **node2**: Video Sequences
- **node3**: Patch i Pixel-wide Embeddings
- **node4**: Evenly random select N vectors: S_seed in S_i
- **node5**: Prune & Cluster, get r and l
- **node6**: Obtain Nmin based on Eq. (19)
- **node7**: Decision: N ≤ L × Nmin
- **node8**: Update
- **node9**: Decision: N ≥ H × Nmin
- **node10**: Patch i is last batch
- **node11**: End
- **node12**: N = N ×
- **node13**: i = i + 1
- **node14**: GPU Section
- **node15**: Parallel Mean-shift
- **node16**: Converged > Y
- **node17**: $N_{initial}$ and $H$ influence Impact on computational load

### Edges

- Video Sequences → Patch i is last batch
- Video Sequences → Update
- Video Sequences → Prune & Cluster, get r and l
- Prune & Cluster, get r and l → N = N ×
- Obtain Nmin based on Eq. (19) → End
- Video Sequences → Decision: N ≤ L × Nmin
- Video Sequences → i = i + 1
- Obtain Nmin based on Eq. (19) → Patch i is last batch
- Obtain Nmin based on Eq. (19) → Update
- Obtain Nmin based on Eq. (19) → Decision: N ≤ L × Nmin
- Obtain Nmin based on Eq. (19) → i = i + 1
- Video Sequences → Patch i Pixel-wide Embeddings
- Evenly random select N vectors: S_seed in S_i → End
- Prune & Cluster, get r and l → Obtain Nmin based on Eq. (19)
- Video Sequences → Decision: N ≥ H × Nmin
- Evenly random select N vectors: S_seed in S_i → Update
- Evenly random select N vectors: S_seed in S_i → Prune & Cluster, get r and l
- Patch i Pixel-wide Embeddings → End
- Evenly random select N vectors: S_seed in S_i → Decision: N ≤ L × Nmin
- Video Sequences → N = N ×
- Patch i Pixel-wide Embeddings → Update
- Evenly random select N vectors: S_seed in S_i → Patch i is last batch
- Evenly random select N vectors: S_seed in S_i → i = i + 1
- Patch i Pixel-wide Embeddings → Prune & Cluster, get r and l
- Obtain Nmin based on Eq. (19) → Decision: N ≥ H × Nmin
- Decision: N ≤ L × Nmin → End
- Patch i Pixel-wide Embeddings → Decision: N ≤ L × Nmin
- Patch i Pixel-wide Embeddings → Patch i is last batch
- Patch i Pixel-wide Embeddings → i = i + 1
- Obtain Nmin based on Eq. (19) → N = N ×
- Decision: N ≥ H × Nmin → End
- Decision: N ≥ H × Nmin → Patch i is last batch
- Decision: N ≤ L × Nmin → Patch i is last batch
- Evenly random select N vectors: S_seed in S_i → Decision: N ≥ H × Nmin
- Decision: N ≤ L × Nmin → Update
- GPU Section → Converged > Y
- Video Sequences → Obtain Nmin based on Eq. (19)
- Decision: N ≥ H × Nmin → i = i + 1
- Decision: N ≤ L × Nmin → i = i + 1
- Evenly random select N vectors: S_seed in S_i → N = N ×
- Patch i Pixel-wide Embeddings → Decision: N ≥ H × Nmin
- Patch i is last batch → End
- Decision: N ≤ L × Nmin → Decision: N ≥ H × Nmin
- Patch i Pixel-wide Embeddings → N = N ×
- Patch i is last batch → i = i + 1
- Update → End
- Evenly random select N vectors: S_seed in S_i → Obtain Nmin based on Eq. (19)
- GPU Section → Parallel Mean-shift
- Decision: N ≥ H × Nmin → N = N ×
- Decision: N ≤ L × Nmin → N = N ×
- Update → Patch i is last batch
- Video Sequences → Evenly random select N vectors: S_seed in S_i
- Patch i Pixel-wide Embeddings → Obtain Nmin based on Eq. (19)
- Update → i = i + 1
- Patch i is last batch → N = N ×
- Prune & Cluster, get r and l → End
- Prune & Cluster, get r and l → Update
- Prune & Cluster, get r and l → Decision: N ≤ L × Nmin
- Prune & Cluster, get r and l → Patch i is last batch
- Prune & Cluster, get r and l → i = i + 1
- Update → N = N ×
- Parallel Mean-shift → Converged > Y
- Prune & Cluster, get r and l → Decision: N ≥ H × Nmin
- Video Sequences → End
- Patch i Pixel-wide Embeddings → Evenly random select N vectors: S_seed in S_i

## Reference Graph

### Nodes

- **node1**: CPU
- **node2**: Video Sequences
- **node3**: Patch i
Pixel-wide
Embeddings S_i
- **node4**: Evenly random select
N vectors: S_seed ∈ S_i
- **node5**: Prune & Cluster,
get r and I
- **node6**: Obtain N_min
based on Eq. (19)
- **node7**: N ≤ L × N_min
- **node8**: N = N * 2
- **node9**: Update N
- **node10**: i = i + 1
- **node11**: Patch i
is last batch
- **node12**: End
- **node13**: N ≥ H × N_min
- **node14**: N = N − N_min
- **node15**: GPU
- **node16**: Parallel Mean-shift
- **node17**: Converged
>γ

### Edges

- Patch i
is last batch → N = N − N_min
- N ≤ L × N_min → Evenly random select
N vectors: S_seed ∈ S_i
- Patch i
is last batch → i = i + 1
- Patch i
is last batch → Prune & Cluster,
get r and I
- Video Sequences → Parallel Mean-shift
- Obtain N_min
based on Eq. (19) → Parallel Mean-shift
- Converged
>γ → N = N − N_min
- N = N − N_min → N = N * 2
- Converged
>γ → i = i + 1
- Evenly random select
N vectors: S_seed ∈ S_i → Parallel Mean-shift
- N = N − N_min → N ≥ H × N_min
- Parallel Mean-shift → N ≥ H × N_min
- Update N → Patch i
is last batch
- N = N − N_min → Parallel Mean-shift
- Parallel Mean-shift → Parallel Mean-shift
- Update N → i = i + 1
- N ≤ L × N_min → N ≤ L × N_min
- Converged
>γ → Prune & Cluster,
get r and I
- Update N → Prune & Cluster,
get r and I
- Patch i
Pixel-wide
Embeddings S_i → Parallel Mean-shift
- N = N − N_min → Patch i
Pixel-wide
Embeddings S_i
- Parallel Mean-shift → Patch i
Pixel-wide
Embeddings S_i
- Patch i
Pixel-wide
Embeddings S_i → Patch i
Pixel-wide
Embeddings S_i
- i = i + 1 → Patch i
is last batch
- N ≥ H × N_min → Evenly random select
N vectors: S_seed ∈ S_i
- i = i + 1 → i = i + 1
- N ≤ L × N_min → Parallel Mean-shift
- Prune & Cluster,
get r and I → Evenly random select
N vectors: S_seed ∈ S_i
- N ≤ L × N_min → Update N
- i = i + 1 → Prune & Cluster,
get r and I
- N = N * 2 → Patch i
is last batch
- End → N = N − N_min
- Update N → End
- End → Patch i
is last batch
- Patch i
is last batch → Converged
>γ
- End → i = i + 1
- End → Prune & Cluster,
get r and I
- i = i + 1 → End
- Update N → Obtain N_min
based on Eq. (19)
- N ≥ H × N_min → N ≤ L × N_min
- Prune & Cluster,
get r and I → N ≤ L × N_min
- N = N * 2 → End
- i = i + 1 → Obtain N_min
based on Eq. (19)
- Converged
>γ → Converged
>γ
- Evenly random select
N vectors: S_seed ∈ S_i → Evenly random select
N vectors: S_seed ∈ S_i
- End → End
- N ≥ H × N_min → Parallel Mean-shift
- N ≥ H × N_min → Update N
- N = N − N_min → Evenly random select
N vectors: S_seed ∈ S_i
- Update N → Converged
>γ
- Prune & Cluster,
get r and I → Update N
- Parallel Mean-shift → Evenly random select
N vectors: S_seed ∈ S_i
- Patch i
Pixel-wide
Embeddings S_i → Evenly random select
N vectors: S_seed ∈ S_i
- N = N * 2 → Obtain N_min
based on Eq. (19)
- Video Sequences → N ≤ L × N_min
- Patch i
is last batch → N = N * 2
- i = i + 1 → Converged
>γ
- End → Obtain N_min
based on Eq. (19)
- Obtain N_min
based on Eq. (19) → N ≤ L × N_min
- Patch i
is last batch → N ≥ H × N_min
- Video Sequences → Update N
- Patch i
is last batch → Patch i
Pixel-wide
Embeddings S_i
- Evenly random select
N vectors: S_seed ∈ S_i → N ≤ L × N_min
- Obtain N_min
based on Eq. (19) → Update N
- End → Converged
>γ
- N = N − N_min → N ≤ L × N_min
- Parallel Mean-shift → N ≤ L × N_min
- N ≤ L × N_min → Patch i
is last batch
- Converged
>γ → N = N * 2
- Patch i
Pixel-wide
Embeddings S_i → N ≤ L × N_min
- Converged
>γ → N ≥ H × N_min
- Update N → N = N − N_min
- Update N → N = N * 2
- Evenly random select
N vectors: S_seed ∈ S_i → Update N
- Converged
>γ → Parallel Mean-shift
- N = N − N_min → Update N
- Parallel Mean-shift → Update N
- Update N → N ≥ H × N_min
- Converged
>γ → Patch i
Pixel-wide
Embeddings S_i
- Patch i
Pixel-wide
Embeddings S_i → Update N
- i = i + 1 → N = N − N_min
- Update N → Patch i
Pixel-wide
Embeddings S_i
- i = i + 1 → N = N * 2
- i = i + 1 → N ≥ H × N_min
- N = N * 2 → N = N − N_min
- i = i + 1 → Patch i
Pixel-wide
Embeddings S_i
- N = N * 2 → i = i + 1
- End → N = N * 2
- N = N * 2 → Prune & Cluster,
get r and I
- N ≤ L × N_min → Obtain N_min
based on Eq. (19)
- End → N ≥ H × N_min
- N ≥ H × N_min → Patch i
is last batch
- Patch i
is last batch → Evenly random select
N vectors: S_seed ∈ S_i
- Prune & Cluster,
get r and I → Patch i
is last batch
- Prune & Cluster,
get r and I → Prune & Cluster,
get r and I
- End → Patch i
Pixel-wide
Embeddings S_i
- Converged
>γ → Evenly random select
N vectors: S_seed ∈ S_i
- Video Sequences → Patch i
is last batch
- Video Sequences → i = i + 1
- N ≥ H × N_min → End
- Video Sequences → Prune & Cluster,
get r and I
- Prune & Cluster,
get r and I → End
- Obtain N_min
based on Eq. (19) → Patch i
is last batch
- Update N → Evenly random select
N vectors: S_seed ∈ S_i
- Obtain N_min
based on Eq. (19) → i = i + 1
- Patch i
is last batch → N ≤ L × N_min
- Obtain N_min
based on Eq. (19) → Prune & Cluster,
get r and I
- N ≥ H × N_min → Obtain N_min
based on Eq. (19)
- i = i + 1 → Evenly random select
N vectors: S_seed ∈ S_i
- Evenly random select
N vectors: S_seed ∈ S_i → Patch i
is last batch
- Prune & Cluster,
get r and I → Obtain N_min
based on Eq. (19)
- N = N − N_min → Patch i
is last batch
- Patch i
is last batch → Parallel Mean-shift
- Patch i
is last batch → Update N
- Evenly random select
N vectors: S_seed ∈ S_i → Prune & Cluster,
get r and I
- Parallel Mean-shift → Patch i
is last batch
- Patch i
Pixel-wide
Embeddings S_i → Patch i
is last batch
- N = N * 2 → Converged
>γ
- Video Sequences → End
- Patch i
Pixel-wide
Embeddings S_i → Prune & Cluster,
get r and I
- Converged
>γ → N ≤ L × N_min
- N ≤ L × N_min → N = N − N_min
- Obtain N_min
based on Eq. (19) → End
- End → Evenly random select
N vectors: S_seed ∈ S_i
- Prune & Cluster,
get r and I → Converged
>γ
- N ≤ L × N_min → i = i + 1
- N ≤ L × N_min → Prune & Cluster,
get r and I
- Video Sequences → Obtain N_min
based on Eq. (19)
- Converged
>γ → Update N
- Evenly random select
N vectors: S_seed ∈ S_i → End
- Obtain N_min
based on Eq. (19) → Obtain N_min
based on Eq. (19)
- N = N − N_min → End
- Update N → Parallel Mean-shift
- Parallel Mean-shift → End
- Patch i
Pixel-wide
Embeddings S_i → End
- Video Sequences → Converged
>γ
- Evenly random select
N vectors: S_seed ∈ S_i → Obtain N_min
based on Eq. (19)
- i = i + 1 → Parallel Mean-shift
- N = N − N_min → Obtain N_min
based on Eq. (19)
- N ≤ L × N_min → End
- Parallel Mean-shift → Obtain N_min
based on Eq. (19)
- Obtain N_min
based on Eq. (19) → Converged
>γ
- N = N * 2 → N = N * 2
- Patch i
Pixel-wide
Embeddings S_i → Obtain N_min
based on Eq. (19)
- N = N * 2 → N ≥ H × N_min
- N ≥ H × N_min → N = N − N_min
- Prune & Cluster,
get r and I → N = N − N_min
- Evenly random select
N vectors: S_seed ∈ S_i → Converged
>γ
- Prune & Cluster,
get r and I → N = N * 2
- N = N * 2 → Patch i
Pixel-wide
Embeddings S_i
- End → Parallel Mean-shift
- End → Update N
- N ≥ H × N_min → i = i + 1
- Prune & Cluster,
get r and I → N ≥ H × N_min
- Prune & Cluster,
get r and I → i = i + 1
- N ≥ H × N_min → Prune & Cluster,
get r and I
- Patch i
Pixel-wide
Embeddings S_i → Converged
>γ
- N ≤ L × N_min → Converged
>γ
- Patch i
is last batch → Patch i
is last batch
- Video Sequences → N = N − N_min
- Video Sequences → N = N * 2
- Video Sequences → N ≥ H × N_min
- Obtain N_min
based on Eq. (19) → N = N − N_min
- Obtain N_min
based on Eq. (19) → N = N * 2
- Obtain N_min
based on Eq. (19) → N ≥ H × N_min
- Video Sequences → Patch i
Pixel-wide
Embeddings S_i
- Evenly random select
N vectors: S_seed ∈ S_i → N = N − N_min
- Evenly random select
N vectors: S_seed ∈ S_i → N = N * 2
- Obtain N_min
based on Eq. (19) → Patch i
Pixel-wide
Embeddings S_i
- N = N − N_min → N = N − N_min
- Parallel Mean-shift → N = N − N_min
- Parallel Mean-shift → N = N * 2
- Converged
>γ → Patch i
is last batch
- Evenly random select
N vectors: S_seed ∈ S_i → N ≥ H × N_min
- Evenly random select
N vectors: S_seed ∈ S_i → i = i + 1
- Patch i
Pixel-wide
Embeddings S_i → N = N − N_min
- Patch i
Pixel-wide
Embeddings S_i → N = N * 2
- Patch i
is last batch → End
- N = N − N_min → Prune & Cluster,
get r and I
- N = N − N_min → i = i + 1
- Parallel Mean-shift → Prune & Cluster,
get r and I
- Parallel Mean-shift → i = i + 1
- Patch i
Pixel-wide
Embeddings S_i → N ≥ H × N_min
- Patch i
Pixel-wide
Embeddings S_i → i = i + 1
- Evenly random select
N vectors: S_seed ∈ S_i → Patch i
Pixel-wide
Embeddings S_i
- N = N * 2 → Evenly random select
N vectors: S_seed ∈ S_i
- N ≤ L × N_min → N = N * 2
- N ≥ H × N_min → Converged
>γ
- Update N → N ≤ L × N_min
- N ≤ L × N_min → N ≥ H × N_min
- Patch i
is last batch → Obtain N_min
based on Eq. (19)
- N ≤ L × N_min → Patch i
Pixel-wide
Embeddings S_i
- Converged
>γ → End
- i = i + 1 → N ≤ L × N_min
- Update N → Update N
- Converged
>γ → Obtain N_min
based on Eq. (19)
- N = N * 2 → N ≤ L × N_min
- Video Sequences → Evenly random select
N vectors: S_seed ∈ S_i
- i = i + 1 → Update N
- End → N ≤ L × N_min
- Obtain N_min
based on Eq. (19) → Evenly random select
N vectors: S_seed ∈ S_i
- N = N * 2 → Parallel Mean-shift
- N = N * 2 → Update N
- N ≥ H × N_min → N = N * 2
- N ≥ H × N_min → N ≥ H × N_min
- N = N − N_min → Converged
>γ
- Parallel Mean-shift → Converged
>γ
- Prune & Cluster,
get r and I → Parallel Mean-shift
- N ≥ H × N_min → Patch i
Pixel-wide
Embeddings S_i
- Prune & Cluster,
get r and I → Patch i
Pixel-wide
Embeddings S_i

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| CPU Section | CPU |
| Video Sequences | Video Sequences |
| Patch i Pixel-wide Embeddings | Patch i
Pixel-wide
Embeddings S_i |
| Evenly random select N vectors: S_seed in S_i | Evenly random select
N vectors: S_seed ∈ S_i |
| Prune & Cluster, get r and l | Prune & Cluster,
get r and I |
| Obtain Nmin based on Eq. (19) | Obtain N_min
based on Eq. (19) |
| Decision: N ≤ L × Nmin | N ≤ L × N_min |
| Update | Update N |
| Patch i is last batch | Patch i
is last batch |
| End | End |
| i = i + 1 | i = i + 1 |
| GPU Section | GPU |
| Parallel Mean-shift | Parallel Mean-shift |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| Patch i
is last batch | i = i + 1 |
| Patch i
is last batch | End |
| Video Sequences | i = i + 1 |
| Video Sequences | Patch i
is last batch |
| Video Sequences | End |
| Video Sequences | Patch i
Pixel-wide
Embeddings S_i |
| Video Sequences | Evenly random select
N vectors: S_seed ∈ S_i |
| Video Sequences | Prune & Cluster,
get r and I |
| Video Sequences | Obtain N_min
based on Eq. (19) |
| Video Sequences | N ≤ L × N_min |
| Video Sequences | Update N |
| Patch i
Pixel-wide
Embeddings S_i | i = i + 1 |
| Patch i
Pixel-wide
Embeddings S_i | Patch i
is last batch |
| Patch i
Pixel-wide
Embeddings S_i | End |
| Patch i
Pixel-wide
Embeddings S_i | Evenly random select
N vectors: S_seed ∈ S_i |
| Patch i
Pixel-wide
Embeddings S_i | Prune & Cluster,
get r and I |
| Patch i
Pixel-wide
Embeddings S_i | Obtain N_min
based on Eq. (19) |
| Patch i
Pixel-wide
Embeddings S_i | N ≤ L × N_min |
| Patch i
Pixel-wide
Embeddings S_i | Update N |
| Evenly random select
N vectors: S_seed ∈ S_i | i = i + 1 |
| Evenly random select
N vectors: S_seed ∈ S_i | Patch i
is last batch |
| Evenly random select
N vectors: S_seed ∈ S_i | End |
| Evenly random select
N vectors: S_seed ∈ S_i | Prune & Cluster,
get r and I |
| Evenly random select
N vectors: S_seed ∈ S_i | Obtain N_min
based on Eq. (19) |
| Evenly random select
N vectors: S_seed ∈ S_i | N ≤ L × N_min |
| Evenly random select
N vectors: S_seed ∈ S_i | Update N |
| Prune & Cluster,
get r and I | i = i + 1 |
| Prune & Cluster,
get r and I | Patch i
is last batch |
| Prune & Cluster,
get r and I | End |
| Prune & Cluster,
get r and I | Obtain N_min
based on Eq. (19) |
| Prune & Cluster,
get r and I | N ≤ L × N_min |
| Prune & Cluster,
get r and I | Update N |
| Obtain N_min
based on Eq. (19) | i = i + 1 |
| Obtain N_min
based on Eq. (19) | Patch i
is last batch |
| Obtain N_min
based on Eq. (19) | End |
| Obtain N_min
based on Eq. (19) | N ≤ L × N_min |
| Obtain N_min
based on Eq. (19) | Update N |
| N ≤ L × N_min | i = i + 1 |
| N ≤ L × N_min | Patch i
is last batch |
| N ≤ L × N_min | End |
| N ≤ L × N_min | Update N |
| Update N | i = i + 1 |
| Update N | Patch i
is last batch |
| Update N | End |