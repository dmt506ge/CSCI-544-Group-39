# Diagram Evaluation Report

## Input Files
- **Generated**: `..\evaluate_png\gpt5\3.png`
- **Reference**: `..\ground_png\3.png`

## Evaluation Scores

### Node Alignment
- **Precision**: 0.636
- **Recall**: 0.824
- **F1 Score**: 0.718

### Path Alignment
- **Precision**: 1.000
- **Recall**: 0.739
- **F1 Score**: 0.850

## Generated Graph

### Nodes

- **node1**: Start
- **node2**: Video Sequences
- **node3**: Patch i pixel wide embeddings S i
- **node4**: Evenly random select N vectors
Return to seed selection S seed in S i
- **node5**: Prune and cluster to get centers r and assignments l
- **node6**: Obtain N min based on Eq. 19
- **node7**: N = N x 2
- **node8**: Update N
- **node9**: N = N / 2
- **node10**: N <= L x N min
- **node11**: N >= H x N min
- **node12**: Patch i is last batch
- **node13**: End
- **node14**: Check GPU memory and batch
- **node15**: Fits in memory
- **node16**: Split batches adjust B
- **node17**: S sent to GPU
Bandwidth H
- **node18**: Parallel mean shift
- **node19**: Not converged
- **node20**: Converged
delta less than eps or max iters
- **node21**: Yes r and t to CPU
- **node22**: i = i + 1

### Edges

- Prune and cluster to get centers r and assignments l → Converged
delta less than eps or max iters
- Obtain N min based on Eq. 19 → S sent to GPU
Bandwidth H
- Parallel mean shift → Update N
- Patch i pixel wide embeddings S i → End
- Not converged → N = N / 2
- Yes r and t to CPU → End
- S sent to GPU
Bandwidth H → End
- Evenly random select N vectors
Return to seed selection S seed in S i → S sent to GPU
Bandwidth H
- Update N → Split batches adjust B
- Evenly random select N vectors
Return to seed selection S seed in S i → N = N x 2
- Patch i is last batch → Prune and cluster to get centers r and assignments l
- Prune and cluster to get centers r and assignments l → Parallel mean shift
- Patch i pixel wide embeddings S i → S sent to GPU
Bandwidth H
- Update N → Obtain N min based on Eq. 19
- Start → i = i + 1
- Update N → Fits in memory
- Video Sequences → Evenly random select N vectors
Return to seed selection S seed in S i
- Patch i pixel wide embeddings S i → N = N x 2
- Yes r and t to CPU → N = N x 2
- S sent to GPU
Bandwidth H → N = N x 2
- Not converged → Parallel mean shift
- Update N → Converged
delta less than eps or max iters
- i = i + 1 → N <= L x N min
- Patch i is last batch → N <= L x N min
- Start → Yes r and t to CPU
- Parallel mean shift → N = N / 2
- Update N → Not converged
- N >= H x N min → Evenly random select N vectors
Return to seed selection S seed in S i
- Converged
delta less than eps or max iters → Yes r and t to CPU
- Video Sequences → i = i + 1
- Start → Split batches adjust B
- Video Sequences → Update N
- Yes r and t to CPU → Check GPU memory and batch
- Start → Obtain N min based on Eq. 19
- Update N → N >= H x N min
- S sent to GPU
Bandwidth H → Check GPU memory and batch
- i = i + 1 → Patch i pixel wide embeddings S i
- Obtain N min based on Eq. 19 → Evenly random select N vectors
Return to seed selection S seed in S i
- N = N / 2 → Prune and cluster to get centers r and assignments l
- Converged
delta less than eps or max iters → Split batches adjust B
- Update N → End
- Start → Converged
delta less than eps or max iters
- Evenly random select N vectors
Return to seed selection S seed in S i → Evenly random select N vectors
Return to seed selection S seed in S i
- Converged
delta less than eps or max iters → Obtain N min based on Eq. 19
- Video Sequences → Yes r and t to CPU
- Converged
delta less than eps or max iters → Fits in memory
- N >= H x N min → i = i + 1
- Patch i pixel wide embeddings S i → Evenly random select N vectors
Return to seed selection S seed in S i
- Converged
delta less than eps or max iters → Converged
delta less than eps or max iters
- N >= H x N min → Update N
- Start → Parallel mean shift
- N = N / 2 → N <= L x N min
- Update N → N = N x 2
- Start → Not converged
- Prune and cluster to get centers r and assignments l → Patch i is last batch
- Prune and cluster to get centers r and assignments l → Check GPU memory and batch
- Obtain N min based on Eq. 19 → i = i + 1
- Video Sequences → N = N / 2
- N >= H x N min → Yes r and t to CPU
- Obtain N min based on Eq. 19 → Update N
- Not converged → Patch i is last batch
- Converged
delta less than eps or max iters → Not converged
- Video Sequences → Converged
delta less than eps or max iters
- Evenly random select N vectors
Return to seed selection S seed in S i → i = i + 1
- Evenly random select N vectors
Return to seed selection S seed in S i → Update N
- Start → End
- Patch i pixel wide embeddings S i → i = i + 1
- Obtain N min based on Eq. 19 → Yes r and t to CPU
- Converged
delta less than eps or max iters → N >= H x N min
- Patch i pixel wide embeddings S i → Update N
- Video Sequences → Parallel mean shift
- Yes r and t to CPU → Update N
- S sent to GPU
Bandwidth H → Update N
- Not converged → Prune and cluster to get centers r and assignments l
- Update N → Check GPU memory and batch
- Evenly random select N vectors
Return to seed selection S seed in S i → Yes r and t to CPU
- Patch i is last batch → Split batches adjust B
- N >= H x N min → N = N / 2
- Video Sequences → Not converged
- Converged
delta less than eps or max iters → End
- Start → N = N x 2
- N >= H x N min → Converged
delta less than eps or max iters
- Patch i is last batch → Obtain N min based on Eq. 19
- Patch i is last batch → Fits in memory
- Patch i pixel wide embeddings S i → Yes r and t to CPU
- Parallel mean shift → Patch i is last batch
- Not converged → N <= L x N min
- Obtain N min based on Eq. 19 → N = N / 2
- Converged
delta less than eps or max iters → N = N x 2
- N >= H x N min → Parallel mean shift
- Update N → Evenly random select N vectors
Return to seed selection S seed in S i
- N <= L x N min → Prune and cluster to get centers r and assignments l
- Obtain N min based on Eq. 19 → Converged
delta less than eps or max iters
- Evenly random select N vectors
Return to seed selection S seed in S i → N = N / 2
- Evenly random select N vectors
Return to seed selection S seed in S i → Converged
delta less than eps or max iters
- Parallel mean shift → Prune and cluster to get centers r and assignments l
- Patch i pixel wide embeddings S i → N = N / 2
- Yes r and t to CPU → N = N / 2
- Prune and cluster to get centers r and assignments l → Patch i pixel wide embeddings S i
- S sent to GPU
Bandwidth H → N = N / 2
- Obtain N min based on Eq. 19 → Parallel mean shift
- Video Sequences → N = N x 2
- Patch i pixel wide embeddings S i → Converged
delta less than eps or max iters
- Start → Check GPU memory and batch
- N <= L x N min → N <= L x N min
- Obtain N min based on Eq. 19 → Not converged
- Evenly random select N vectors
Return to seed selection S seed in S i → Parallel mean shift
- Not converged → Patch i pixel wide embeddings S i
- Patch i is last batch → N >= H x N min
- N = N / 2 → Split batches adjust B
- Update N → i = i + 1
- Patch i pixel wide embeddings S i → Parallel mean shift
- Parallel mean shift → N <= L x N min
- Converged
delta less than eps or max iters → Check GPU memory and batch
- Patch i is last batch → End
- Update N → Update N
- N = N / 2 → Obtain N min based on Eq. 19
- N = N / 2 → Fits in memory
- Check GPU memory and batch → Split batches adjust B
- i = i + 1 → S sent to GPU
Bandwidth H
- Video Sequences → Patch i is last batch
- Patch i is last batch → S sent to GPU
Bandwidth H
- Check GPU memory and batch → Fits in memory
- Video Sequences → Check GPU memory and batch
- Converged
delta less than eps or max iters → Evenly random select N vectors
Return to seed selection S seed in S i
- Obtain N min based on Eq. 19 → N = N x 2
- Parallel mean shift → Patch i pixel wide embeddings S i
- N = N / 2 → Not converged
- i = i + 1 → Prune and cluster to get centers r and assignments l
- N >= H x N min → Patch i is last batch
- Update N → N = N / 2
- Start → Update N
- N = N / 2 → N >= H x N min
- N >= H x N min → Check GPU memory and batch
- N = N / 2 → End
- Converged
delta less than eps or max iters → i = i + 1
- Converged
delta less than eps or max iters → Update N
- Obtain N min based on Eq. 19 → Patch i is last batch
- N <= L x N min → Yes r and t to CPU
- Update N → Parallel mean shift
- Obtain N min based on Eq. 19 → Check GPU memory and batch
- Evenly random select N vectors
Return to seed selection S seed in S i → Patch i is last batch
- N = N / 2 → S sent to GPU
Bandwidth H
- Evenly random select N vectors
Return to seed selection S seed in S i → Check GPU memory and batch
- Patch i pixel wide embeddings S i → Patch i is last batch
- Yes r and t to CPU → Patch i is last batch
- N <= L x N min → Split batches adjust B
- S sent to GPU
Bandwidth H → Patch i is last batch
- Patch i is last batch → Evenly random select N vectors
Return to seed selection S seed in S i
- Patch i pixel wide embeddings S i → Check GPU memory and batch
- Start → Video Sequences
- N <= L x N min → Obtain N min based on Eq. 19
- Video Sequences → Patch i pixel wide embeddings S i
- Start → N = N / 2
- N <= L x N min → Fits in memory
- Yes r and t to CPU → Prune and cluster to get centers r and assignments l
- Parallel mean shift → Obtain N min based on Eq. 19
- S sent to GPU
Bandwidth H → Prune and cluster to get centers r and assignments l
- Parallel mean shift → Fits in memory
- Converged
delta less than eps or max iters → N = N / 2
- Not converged → N >= H x N min
- N >= H x N min → Patch i pixel wide embeddings S i
- Patch i is last batch → i = i + 1
- N <= L x N min → Not converged
- Yes r and t to CPU → N <= L x N min
- S sent to GPU
Bandwidth H → N <= L x N min
- Converged
delta less than eps or max iters → Parallel mean shift
- Not converged → S sent to GPU
Bandwidth H
- N <= L x N min → N >= H x N min
- Obtain N min based on Eq. 19 → Patch i pixel wide embeddings S i
- i = i + 1 → Yes r and t to CPU
- N = N / 2 → Evenly random select N vectors
Return to seed selection S seed in S i
- Patch i is last batch → Yes r and t to CPU
- Prune and cluster to get centers r and assignments l → Prune and cluster to get centers r and assignments l
- Evenly random select N vectors
Return to seed selection S seed in S i → Patch i pixel wide embeddings S i
- N <= L x N min → End
- Update N → Patch i is last batch
- Parallel mean shift → N >= H x N min
- i = i + 1 → Split batches adjust B
- Patch i pixel wide embeddings S i → Patch i pixel wide embeddings S i
- Yes r and t to CPU → Patch i pixel wide embeddings S i
- S sent to GPU
Bandwidth H → Patch i pixel wide embeddings S i
- N <= L x N min → S sent to GPU
Bandwidth H
- i = i + 1 → Obtain N min based on Eq. 19
- Prune and cluster to get centers r and assignments l → N <= L x N min
- N <= L x N min → N = N x 2
- i = i + 1 → Fits in memory
- i = i + 1 → Converged
delta less than eps or max iters
- Parallel mean shift → S sent to GPU
Bandwidth H
- Patch i is last batch → Converged
delta less than eps or max iters
- N = N / 2 → i = i + 1
- N = N / 2 → Update N
- Patch i is last batch → Parallel mean shift
- Update N → N <= L x N min
- i = i + 1 → Not converged
- Patch i is last batch → Not converged
- Start → Patch i is last batch
- N = N / 2 → Yes r and t to CPU
- Converged
delta less than eps or max iters → Patch i is last batch
- i = i + 1 → N >= H x N min
- Start → Prune and cluster to get centers r and assignments l
- i = i + 1 → End
- N = N / 2 → N = N / 2
- Update N → Patch i pixel wide embeddings S i
- N <= L x N min → Evenly random select N vectors
Return to seed selection S seed in S i
- N = N / 2 → Converged
delta less than eps or max iters
- Yes r and t to CPU → Obtain N min based on Eq. 19
- Converged
delta less than eps or max iters → Prune and cluster to get centers r and assignments l
- S sent to GPU
Bandwidth H → Obtain N min based on Eq. 19
- Yes r and t to CPU → Fits in memory
- S sent to GPU
Bandwidth H → Fits in memory
- i = i + 1 → N = N x 2
- Patch i is last batch → N = N x 2
- Start → N <= L x N min
- Parallel mean shift → Evenly random select N vectors
Return to seed selection S seed in S i
- N = N / 2 → Parallel mean shift
- Converged
delta less than eps or max iters → N <= L x N min
- Video Sequences → Prune and cluster to get centers r and assignments l
- Not converged → Yes r and t to CPU
- Prune and cluster to get centers r and assignments l → Split batches adjust B
- N <= L x N min → i = i + 1
- N <= L x N min → Update N
- Prune and cluster to get centers r and assignments l → Obtain N min based on Eq. 19
- Patch i is last batch → Patch i is last batch
- Prune and cluster to get centers r and assignments l → Fits in memory
- Start → Patch i pixel wide embeddings S i
- Not converged → Split batches adjust B
- i = i + 1 → Check GPU memory and batch
- Video Sequences → N <= L x N min
- Parallel mean shift → i = i + 1
- Yes r and t to CPU → N >= H x N min
- Patch i is last batch → Check GPU memory and batch
- S sent to GPU
Bandwidth H → N >= H x N min
- Not converged → Obtain N min based on Eq. 19
- N >= H x N min → Prune and cluster to get centers r and assignments l
- Not converged → Fits in memory
- Converged
delta less than eps or max iters → Patch i pixel wide embeddings S i
- Not converged → Converged
delta less than eps or max iters
- N = N / 2 → N = N x 2
- Parallel mean shift → Yes r and t to CPU
- Yes r and t to CPU → S sent to GPU
Bandwidth H
- Prune and cluster to get centers r and assignments l → Not converged
- S sent to GPU
Bandwidth H → S sent to GPU
Bandwidth H
- i = i + 1 → Evenly random select N vectors
Return to seed selection S seed in S i
- Obtain N min based on Eq. 19 → Prune and cluster to get centers r and assignments l
- N >= H x N min → N <= L x N min
- Evenly random select N vectors
Return to seed selection S seed in S i → Prune and cluster to get centers r and assignments l
- N <= L x N min → N = N / 2
- Not converged → Not converged
- Parallel mean shift → Split batches adjust B
- Prune and cluster to get centers r and assignments l → N >= H x N min
- N <= L x N min → Converged
delta less than eps or max iters
- Patch i pixel wide embeddings S i → Prune and cluster to get centers r and assignments l
- Obtain N min based on Eq. 19 → N <= L x N min
- Prune and cluster to get centers r and assignments l → End
- N = N / 2 → Patch i is last batch
- Parallel mean shift → Converged
delta less than eps or max iters
- Evenly random select N vectors
Return to seed selection S seed in S i → N <= L x N min
- N <= L x N min → Parallel mean shift
- N = N / 2 → Check GPU memory and batch
- i = i + 1 → i = i + 1
- Not converged → End
- Prune and cluster to get centers r and assignments l → S sent to GPU
Bandwidth H
- i = i + 1 → Update N
- Patch i pixel wide embeddings S i → N <= L x N min
- Patch i is last batch → Update N
- Prune and cluster to get centers r and assignments l → N = N x 2
- Parallel mean shift → Parallel mean shift
- Start → Fits in memory
- Patch i is last batch → Patch i pixel wide embeddings S i
- Parallel mean shift → Not converged
- Not converged → N = N x 2
- Update N → S sent to GPU
Bandwidth H
- Yes r and t to CPU → Evenly random select N vectors
Return to seed selection S seed in S i
- S sent to GPU
Bandwidth H → Evenly random select N vectors
Return to seed selection S seed in S i
- Video Sequences → Split batches adjust B
- Parallel mean shift → End
- Video Sequences → Obtain N min based on Eq. 19
- i = i + 1 → N = N / 2
- Video Sequences → Fits in memory
- Patch i is last batch → N = N / 2
- Update N → Prune and cluster to get centers r and assignments l
- Start → N >= H x N min
- Not converged → Check GPU memory and batch
- Parallel mean shift → N = N x 2
- N >= H x N min → Split batches adjust B
- N = N / 2 → Patch i pixel wide embeddings S i
- Yes r and t to CPU → i = i + 1
- S sent to GPU
Bandwidth H → i = i + 1
- i = i + 1 → Parallel mean shift
- Prune and cluster to get centers r and assignments l → Evenly random select N vectors
Return to seed selection S seed in S i
- N >= H x N min → Obtain N min based on Eq. 19
- N >= H x N min → Fits in memory
- Start → S sent to GPU
Bandwidth H
- N <= L x N min → Patch i is last batch
- Not converged → Evenly random select N vectors
Return to seed selection S seed in S i
- Obtain N min based on Eq. 19 → Split batches adjust B
- N <= L x N min → Check GPU memory and batch
- Yes r and t to CPU → Yes r and t to CPU
- S sent to GPU
Bandwidth H → Yes r and t to CPU
- Converged
delta less than eps or max iters → S sent to GPU
Bandwidth H
- Obtain N min based on Eq. 19 → Obtain N min based on Eq. 19
- Video Sequences → N >= H x N min
- Evenly random select N vectors
Return to seed selection S seed in S i → Split batches adjust B
- Obtain N min based on Eq. 19 → Fits in memory
- Parallel mean shift → Check GPU memory and batch
- Evenly random select N vectors
Return to seed selection S seed in S i → Obtain N min based on Eq. 19
- Video Sequences → End
- Evenly random select N vectors
Return to seed selection S seed in S i → Fits in memory
- Patch i pixel wide embeddings S i → Split batches adjust B
- N >= H x N min → Not converged
- Yes r and t to CPU → Split batches adjust B
- Prune and cluster to get centers r and assignments l → i = i + 1
- S sent to GPU
Bandwidth H → Split batches adjust B
- Prune and cluster to get centers r and assignments l → Update N
- Patch i pixel wide embeddings S i → Obtain N min based on Eq. 19
- Patch i pixel wide embeddings S i → Fits in memory
- Video Sequences → S sent to GPU
Bandwidth H
- Not converged → i = i + 1
- N >= H x N min → N >= H x N min
- Yes r and t to CPU → Converged
delta less than eps or max iters
- Not converged → Update N
- S sent to GPU
Bandwidth H → Converged
delta less than eps or max iters
- Prune and cluster to get centers r and assignments l → Yes r and t to CPU
- N >= H x N min → End
- Evenly random select N vectors
Return to seed selection S seed in S i → Not converged
- Yes r and t to CPU → Parallel mean shift
- S sent to GPU
Bandwidth H → Parallel mean shift
- Obtain N min based on Eq. 19 → N >= H x N min
- Patch i pixel wide embeddings S i → Not converged
- N >= H x N min → S sent to GPU
Bandwidth H
- Yes r and t to CPU → Not converged
- S sent to GPU
Bandwidth H → Not converged
- Start → Evenly random select N vectors
Return to seed selection S seed in S i
- Evenly random select N vectors
Return to seed selection S seed in S i → N >= H x N min
- Obtain N min based on Eq. 19 → End
- N >= H x N min → N = N x 2
- i = i + 1 → Patch i is last batch
- Prune and cluster to get centers r and assignments l → N = N / 2
- Evenly random select N vectors
Return to seed selection S seed in S i → End
- N <= L x N min → Patch i pixel wide embeddings S i
- Update N → Yes r and t to CPU
- Patch i pixel wide embeddings S i → N >= H x N min

## Reference Graph

### Nodes

- **node1**: CPU
- **node2**: Video Sequences
- **node3**: Patch i Pixel-wide Embeddings S_i
- **node4**: Evenly random select N vectors: S_seed ∈ S_i
- **node5**: Prune & Cluster, get r and I
- **node6**: Obtain N_min based on Eq. (19)
- **node7**: N ≤ L × N_min
- **node8**: N = N * 2
- **node9**: N ≥ H × N_min
- **node10**: N = N - N_min
- **node11**: Patch i is last batch
- **node12**: End
- **node13**: i = i + 1
- **node14**: Update N
- **node15**: GPU
- **node16**: Parallel Mean-shift
- **node17**: Converged >γ

### Edges

- Parallel Mean-shift → N ≥ H × N_min
- Prune & Cluster, get r and I → i = i + 1
- Prune & Cluster, get r and I → Patch i Pixel-wide Embeddings S_i
- Obtain N_min based on Eq. (19) → Converged >γ
- Converged >γ → N ≥ H × N_min
- N ≥ H × N_min → End
- Video Sequences → N ≤ L × N_min
- Patch i Pixel-wide Embeddings S_i → i = i + 1
- Patch i Pixel-wide Embeddings S_i → Patch i Pixel-wide Embeddings S_i
- Update N → Evenly random select N vectors: S_seed ∈ S_i
- CPU → Update N
- Evenly random select N vectors: S_seed ∈ S_i → N = N - N_min
- N = N - N_min → N = N - N_min
- i = i + 1 → Prune & Cluster, get r and I
- Parallel Mean-shift → i = i + 1
- i = i + 1 → Patch i is last batch
- Evenly random select N vectors: S_seed ∈ S_i → Converged >γ
- N = N - N_min → Converged >γ
- Parallel Mean-shift → Patch i Pixel-wide Embeddings S_i
- i = i + 1 → N ≥ H × N_min
- N ≥ H × N_min → Update N
- Converged >γ → i = i + 1
- Converged >γ → Patch i Pixel-wide Embeddings S_i
- N = N * 2 → Parallel Mean-shift
- Prune & Cluster, get r and I → N = N - N_min
- Evenly random select N vectors: S_seed ∈ S_i → N ≤ L × N_min
- N = N - N_min → N ≤ L × N_min
- Prune & Cluster, get r and I → Converged >γ
- N ≥ H × N_min → Parallel Mean-shift
- i = i + 1 → Patch i Pixel-wide Embeddings S_i
- i = i + 1 → i = i + 1
- Patch i Pixel-wide Embeddings S_i → N = N - N_min
- Prune & Cluster, get r and I → N ≤ L × N_min
- Patch i Pixel-wide Embeddings S_i → Converged >γ
- N ≤ L × N_min → Prune & Cluster, get r and I
- N = N * 2 → Obtain N_min based on Eq. (19)
- N ≤ L × N_min → Patch i is last batch
- Update N → End
- N ≤ L × N_min → N ≥ H × N_min
- Video Sequences → Evenly random select N vectors: S_seed ∈ S_i
- Patch i Pixel-wide Embeddings S_i → N ≤ L × N_min
- N = N * 2 → N = N * 2
- N ≥ H × N_min → Obtain N_min based on Eq. (19)
- Parallel Mean-shift → N ≤ L × N_min
- Converged >γ → N ≤ L × N_min
- Update N → Update N
- N ≥ H × N_min → N = N * 2
- N ≤ L × N_min → i = i + 1
- N ≤ L × N_min → Patch i Pixel-wide Embeddings S_i
- i = i + 1 → N = N - N_min
- i = i + 1 → Converged >γ
- Update N → Parallel Mean-shift
- i = i + 1 → N ≤ L × N_min
- Video Sequences → End
- N ≤ L × N_min → N = N - N_min
- N = N * 2 → N = N - N_min
- Update N → Obtain N_min based on Eq. (19)
- N ≤ L × N_min → Converged >γ
- N = N * 2 → Converged >γ
- Parallel Mean-shift → Evenly random select N vectors: S_seed ∈ S_i
- Video Sequences → Update N
- CPU → End
- Update N → N = N * 2
- Converged >γ → Evenly random select N vectors: S_seed ∈ S_i
- Video Sequences → Parallel Mean-shift
- Obtain N_min based on Eq. (19) → N ≤ L × N_min
- Patch i is last batch → Evenly random select N vectors: S_seed ∈ S_i
- Video Sequences → Obtain N_min based on Eq. (19)
- CPU → Parallel Mean-shift
- Video Sequences → N = N * 2
- Parallel Mean-shift → Update N
- N = N * 2 → Prune & Cluster, get r and I
- Patch i is last batch → End
- CPU → Obtain N_min based on Eq. (19)
- CPU → Prune & Cluster, get r and I
- N = N * 2 → Patch i is last batch
- Converged >γ → Update N
- CPU → Patch i is last batch
- N = N * 2 → N ≥ H × N_min
- Obtain N_min based on Eq. (19) → Evenly random select N vectors: S_seed ∈ S_i
- N ≥ H × N_min → Prune & Cluster, get r and I
- CPU → N = N * 2
- N ≥ H × N_min → Patch i is last batch
- N ≥ H × N_min → N ≥ H × N_min
- Patch i is last batch → Update N
- N = N * 2 → i = i + 1
- N = N * 2 → Patch i Pixel-wide Embeddings S_i
- Evenly random select N vectors: S_seed ∈ S_i → Evenly random select N vectors: S_seed ∈ S_i
- N = N - N_min → Evenly random select N vectors: S_seed ∈ S_i
- Parallel Mean-shift → Obtain N_min based on Eq. (19)
- Patch i is last batch → Parallel Mean-shift
- N ≥ H × N_min → i = i + 1
- N ≥ H × N_min → Patch i Pixel-wide Embeddings S_i
- Converged >γ → Obtain N_min based on Eq. (19)
- Prune & Cluster, get r and I → Evenly random select N vectors: S_seed ∈ S_i
- Obtain N_min based on Eq. (19) → End
- Patch i is last batch → Obtain N_min based on Eq. (19)
- Update N → Prune & Cluster, get r and I
- Patch i Pixel-wide Embeddings S_i → Evenly random select N vectors: S_seed ∈ S_i
- CPU → N = N - N_min
- Update N → Patch i is last batch
- CPU → Converged >γ
- Patch i is last batch → N = N * 2
- Update N → N ≥ H × N_min
- Obtain N_min based on Eq. (19) → Update N
- Evenly random select N vectors: S_seed ∈ S_i → End
- N ≥ H × N_min → N = N - N_min
- N = N - N_min → End
- N ≤ L × N_min → N ≤ L × N_min
- N = N * 2 → N ≤ L × N_min
- N ≥ H × N_min → Converged >γ
- Update N → Patch i Pixel-wide Embeddings S_i
- Update N → i = i + 1
- Prune & Cluster, get r and I → End
- Obtain N_min based on Eq. (19) → Parallel Mean-shift
- Evenly random select N vectors: S_seed ∈ S_i → Update N
- N = N - N_min → Update N
- i = i + 1 → Evenly random select N vectors: S_seed ∈ S_i
- Patch i Pixel-wide Embeddings S_i → End
- Parallel Mean-shift → End
- Video Sequences → Prune & Cluster, get r and I
- Prune & Cluster, get r and I → Update N
- Obtain N_min based on Eq. (19) → Obtain N_min based on Eq. (19)
- Video Sequences → Patch i is last batch
- Evenly random select N vectors: S_seed ∈ S_i → Parallel Mean-shift
- N = N - N_min → Parallel Mean-shift
- Converged >γ → End
- Video Sequences → N ≥ H × N_min
- Obtain N_min based on Eq. (19) → N = N * 2
- Patch i Pixel-wide Embeddings S_i → Update N
- Update N → N = N - N_min
- Prune & Cluster, get r and I → Parallel Mean-shift
- Update N → Converged >γ
- CPU → Video Sequences
- N ≤ L × N_min → Evenly random select N vectors: S_seed ∈ S_i
- Evenly random select N vectors: S_seed ∈ S_i → Obtain N_min based on Eq. (19)
- N = N - N_min → Obtain N_min based on Eq. (19)
- Video Sequences → Patch i Pixel-wide Embeddings S_i
- Video Sequences → i = i + 1
- i = i + 1 → End
- CPU → N ≥ H × N_min
- Update N → N ≤ L × N_min
- Patch i Pixel-wide Embeddings S_i → Parallel Mean-shift
- Evenly random select N vectors: S_seed ∈ S_i → N = N * 2
- N = N - N_min → N = N * 2
- Parallel Mean-shift → Parallel Mean-shift
- Prune & Cluster, get r and I → Obtain N_min based on Eq. (19)
- Converged >γ → Parallel Mean-shift
- i = i + 1 → Update N
- CPU → Patch i Pixel-wide Embeddings S_i
- CPU → i = i + 1
- Prune & Cluster, get r and I → N = N * 2
- Patch i Pixel-wide Embeddings S_i → Obtain N_min based on Eq. (19)
- Parallel Mean-shift → Prune & Cluster, get r and I
- Video Sequences → N = N - N_min
- N ≤ L × N_min → End
- Parallel Mean-shift → Patch i is last batch
- Converged >γ → Prune & Cluster, get r and I
- Patch i Pixel-wide Embeddings S_i → N = N * 2
- Video Sequences → Converged >γ
- i = i + 1 → Parallel Mean-shift
- Converged >γ → Patch i is last batch
- Parallel Mean-shift → N = N * 2
- Converged >γ → N = N * 2
- Patch i is last batch → Prune & Cluster, get r and I
- N ≤ L × N_min → Update N
- N = N * 2 → Update N
- Patch i is last batch → Patch i is last batch
- i = i + 1 → Obtain N_min based on Eq. (19)
- Patch i is last batch → N ≥ H × N_min
- i = i + 1 → N = N * 2
- N ≤ L × N_min → Parallel Mean-shift
- CPU → N ≤ L × N_min
- Patch i is last batch → i = i + 1
- Patch i is last batch → Patch i Pixel-wide Embeddings S_i
- N ≥ H × N_min → N ≤ L × N_min
- N ≤ L × N_min → Obtain N_min based on Eq. (19)
- Parallel Mean-shift → N = N - N_min
- Parallel Mean-shift → Converged >γ
- Converged >γ → N = N - N_min
- Converged >γ → Converged >γ
- Obtain N_min based on Eq. (19) → Prune & Cluster, get r and I
- N ≤ L × N_min → N = N * 2
- Obtain N_min based on Eq. (19) → Patch i is last batch
- Obtain N_min based on Eq. (19) → N ≥ H × N_min
- Patch i is last batch → N = N - N_min
- Patch i is last batch → Converged >γ
- N = N * 2 → Evenly random select N vectors: S_seed ∈ S_i
- Evenly random select N vectors: S_seed ∈ S_i → Prune & Cluster, get r and I
- CPU → Evenly random select N vectors: S_seed ∈ S_i
- N = N - N_min → Prune & Cluster, get r and I
- Evenly random select N vectors: S_seed ∈ S_i → Patch i is last batch
- Obtain N_min based on Eq. (19) → i = i + 1
- Obtain N_min based on Eq. (19) → Patch i Pixel-wide Embeddings S_i
- N = N - N_min → Patch i is last batch
- Evenly random select N vectors: S_seed ∈ S_i → N ≥ H × N_min
- N = N - N_min → N ≥ H × N_min
- Patch i is last batch → N ≤ L × N_min
- N ≥ H × N_min → Evenly random select N vectors: S_seed ∈ S_i
- Prune & Cluster, get r and I → Prune & Cluster, get r and I
- Prune & Cluster, get r and I → Patch i is last batch
- Prune & Cluster, get r and I → N ≥ H × N_min
- Evenly random select N vectors: S_seed ∈ S_i → i = i + 1
- Evenly random select N vectors: S_seed ∈ S_i → Patch i Pixel-wide Embeddings S_i
- N = N - N_min → i = i + 1
- Patch i Pixel-wide Embeddings S_i → Prune & Cluster, get r and I
- N = N - N_min → Patch i Pixel-wide Embeddings S_i
- Patch i Pixel-wide Embeddings S_i → Patch i is last batch
- Patch i Pixel-wide Embeddings S_i → N ≥ H × N_min
- N = N * 2 → End
- Obtain N_min based on Eq. (19) → N = N - N_min

## Node Alignment Matches

| Generated Node | Reference Node |
|----------------|----------------|
| Video Sequences | Video Sequences |
| Patch i pixel wide embeddings S i | Patch i Pixel-wide Embeddings S_i |
| Evenly random select N vectors
Return to seed selection S seed in S i | Evenly random select N vectors: S_seed ∈ S_i |
| Prune and cluster to get centers r and assignments l | Prune & Cluster, get r and I |
| Obtain N min based on Eq. 19 | Obtain N_min based on Eq. (19) |
| N = N x 2 | N = N * 2 |
| Update N | Update N |
| N = N / 2 | N = N - N_min |
| N <= L x N min | N ≤ L × N_min |
| N >= H x N min | N ≥ H × N_min |
| Patch i is last batch | Patch i is last batch |
| End | End |
| Parallel mean shift | Parallel Mean-shift |
| i = i + 1 | i = i + 1 |

## Path Alignment Matches

| Source | Target |
|--------|--------|
| N = N - N_min | N = N - N_min |
| N = N - N_min | Patch i is last batch |
| N = N - N_min | End |
| N = N - N_min | i = i + 1 |
| N = N - N_min | Update N |
| N = N - N_min | Parallel Mean-shift |
| N = N - N_min | Patch i Pixel-wide Embeddings S_i |
| N = N - N_min | Evenly random select N vectors: S_seed ∈ S_i |
| N = N - N_min | Prune & Cluster, get r and I |
| N = N - N_min | Obtain N_min based on Eq. (19) |
| N = N - N_min | N ≤ L × N_min |
| N = N - N_min | N = N * 2 |
| N = N - N_min | N ≥ H × N_min |
| Patch i is last batch | N = N - N_min |
| Patch i is last batch | Patch i is last batch |
| Patch i is last batch | End |
| Patch i is last batch | i = i + 1 |
| Patch i is last batch | Update N |
| Patch i is last batch | Parallel Mean-shift |
| Patch i is last batch | Patch i Pixel-wide Embeddings S_i |
| Patch i is last batch | Evenly random select N vectors: S_seed ∈ S_i |
| Patch i is last batch | Prune & Cluster, get r and I |
| Patch i is last batch | Obtain N_min based on Eq. (19) |
| Patch i is last batch | N ≤ L × N_min |
| Patch i is last batch | N = N * 2 |
| Patch i is last batch | N ≥ H × N_min |
| i = i + 1 | N = N - N_min |
| i = i + 1 | Patch i is last batch |
| i = i + 1 | End |
| i = i + 1 | i = i + 1 |
| i = i + 1 | Update N |
| i = i + 1 | Parallel Mean-shift |
| i = i + 1 | Patch i Pixel-wide Embeddings S_i |
| i = i + 1 | Evenly random select N vectors: S_seed ∈ S_i |
| i = i + 1 | Prune & Cluster, get r and I |
| i = i + 1 | Obtain N_min based on Eq. (19) |
| i = i + 1 | N ≤ L × N_min |
| i = i + 1 | N = N * 2 |
| i = i + 1 | N ≥ H × N_min |
| Update N | N = N - N_min |
| Update N | Patch i is last batch |
| Update N | End |
| Update N | i = i + 1 |
| Update N | Update N |
| Update N | Parallel Mean-shift |
| Update N | Patch i Pixel-wide Embeddings S_i |
| Update N | Evenly random select N vectors: S_seed ∈ S_i |
| Update N | Prune & Cluster, get r and I |
| Update N | Obtain N_min based on Eq. (19) |
| Update N | N ≤ L × N_min |
| Update N | N = N * 2 |
| Update N | N ≥ H × N_min |
| Parallel Mean-shift | N = N - N_min |
| Parallel Mean-shift | Patch i is last batch |
| Parallel Mean-shift | End |
| Parallel Mean-shift | i = i + 1 |
| Parallel Mean-shift | Update N |
| Parallel Mean-shift | Parallel Mean-shift |
| Parallel Mean-shift | Patch i Pixel-wide Embeddings S_i |
| Parallel Mean-shift | Evenly random select N vectors: S_seed ∈ S_i |
| Parallel Mean-shift | Prune & Cluster, get r and I |
| Parallel Mean-shift | Obtain N_min based on Eq. (19) |
| Parallel Mean-shift | N ≤ L × N_min |
| Parallel Mean-shift | N = N * 2 |
| Parallel Mean-shift | N ≥ H × N_min |
| Video Sequences | N = N - N_min |
| Video Sequences | Patch i is last batch |
| Video Sequences | End |
| Video Sequences | i = i + 1 |
| Video Sequences | Update N |
| Video Sequences | Parallel Mean-shift |
| Video Sequences | Patch i Pixel-wide Embeddings S_i |
| Video Sequences | Evenly random select N vectors: S_seed ∈ S_i |
| Video Sequences | Prune & Cluster, get r and I |
| Video Sequences | Obtain N_min based on Eq. (19) |
| Video Sequences | N ≤ L × N_min |
| Video Sequences | N = N * 2 |
| Video Sequences | N ≥ H × N_min |
| Patch i Pixel-wide Embeddings S_i | N = N - N_min |
| Patch i Pixel-wide Embeddings S_i | Patch i is last batch |
| Patch i Pixel-wide Embeddings S_i | End |
| Patch i Pixel-wide Embeddings S_i | i = i + 1 |
| Patch i Pixel-wide Embeddings S_i | Update N |
| Patch i Pixel-wide Embeddings S_i | Parallel Mean-shift |
| Patch i Pixel-wide Embeddings S_i | Patch i Pixel-wide Embeddings S_i |
| Patch i Pixel-wide Embeddings S_i | Evenly random select N vectors: S_seed ∈ S_i |
| Patch i Pixel-wide Embeddings S_i | Prune & Cluster, get r and I |
| Patch i Pixel-wide Embeddings S_i | Obtain N_min based on Eq. (19) |
| Patch i Pixel-wide Embeddings S_i | N ≤ L × N_min |
| Patch i Pixel-wide Embeddings S_i | N = N * 2 |
| Patch i Pixel-wide Embeddings S_i | N ≥ H × N_min |
| Evenly random select N vectors: S_seed ∈ S_i | N = N - N_min |
| Evenly random select N vectors: S_seed ∈ S_i | Patch i is last batch |
| Evenly random select N vectors: S_seed ∈ S_i | End |
| Evenly random select N vectors: S_seed ∈ S_i | i = i + 1 |
| Evenly random select N vectors: S_seed ∈ S_i | Update N |
| Evenly random select N vectors: S_seed ∈ S_i | Parallel Mean-shift |
| Evenly random select N vectors: S_seed ∈ S_i | Patch i Pixel-wide Embeddings S_i |
| Evenly random select N vectors: S_seed ∈ S_i | Evenly random select N vectors: S_seed ∈ S_i |
| Evenly random select N vectors: S_seed ∈ S_i | Prune & Cluster, get r and I |
| Evenly random select N vectors: S_seed ∈ S_i | Obtain N_min based on Eq. (19) |
| Evenly random select N vectors: S_seed ∈ S_i | N ≤ L × N_min |
| Evenly random select N vectors: S_seed ∈ S_i | N = N * 2 |
| Evenly random select N vectors: S_seed ∈ S_i | N ≥ H × N_min |
| Prune & Cluster, get r and I | N = N - N_min |
| Prune & Cluster, get r and I | Patch i is last batch |
| Prune & Cluster, get r and I | End |
| Prune & Cluster, get r and I | i = i + 1 |
| Prune & Cluster, get r and I | Update N |
| Prune & Cluster, get r and I | Parallel Mean-shift |
| Prune & Cluster, get r and I | Patch i Pixel-wide Embeddings S_i |
| Prune & Cluster, get r and I | Evenly random select N vectors: S_seed ∈ S_i |
| Prune & Cluster, get r and I | Prune & Cluster, get r and I |
| Prune & Cluster, get r and I | Obtain N_min based on Eq. (19) |
| Prune & Cluster, get r and I | N ≤ L × N_min |
| Prune & Cluster, get r and I | N = N * 2 |
| Prune & Cluster, get r and I | N ≥ H × N_min |
| Obtain N_min based on Eq. (19) | N = N - N_min |
| Obtain N_min based on Eq. (19) | Patch i is last batch |
| Obtain N_min based on Eq. (19) | End |
| Obtain N_min based on Eq. (19) | i = i + 1 |
| Obtain N_min based on Eq. (19) | Update N |
| Obtain N_min based on Eq. (19) | Parallel Mean-shift |
| Obtain N_min based on Eq. (19) | Patch i Pixel-wide Embeddings S_i |
| Obtain N_min based on Eq. (19) | Evenly random select N vectors: S_seed ∈ S_i |
| Obtain N_min based on Eq. (19) | Prune & Cluster, get r and I |
| Obtain N_min based on Eq. (19) | Obtain N_min based on Eq. (19) |
| Obtain N_min based on Eq. (19) | N ≤ L × N_min |
| Obtain N_min based on Eq. (19) | N = N * 2 |
| Obtain N_min based on Eq. (19) | N ≥ H × N_min |
| N ≤ L × N_min | N = N - N_min |
| N ≤ L × N_min | Patch i is last batch |
| N ≤ L × N_min | End |
| N ≤ L × N_min | i = i + 1 |
| N ≤ L × N_min | Update N |
| N ≤ L × N_min | Parallel Mean-shift |
| N ≤ L × N_min | Patch i Pixel-wide Embeddings S_i |
| N ≤ L × N_min | Evenly random select N vectors: S_seed ∈ S_i |
| N ≤ L × N_min | Prune & Cluster, get r and I |
| N ≤ L × N_min | Obtain N_min based on Eq. (19) |
| N ≤ L × N_min | N ≤ L × N_min |
| N ≤ L × N_min | N = N * 2 |
| N ≤ L × N_min | N ≥ H × N_min |
| N ≥ H × N_min | N = N - N_min |
| N ≥ H × N_min | Patch i is last batch |
| N ≥ H × N_min | End |
| N ≥ H × N_min | i = i + 1 |
| N ≥ H × N_min | Update N |
| N ≥ H × N_min | Parallel Mean-shift |
| N ≥ H × N_min | Patch i Pixel-wide Embeddings S_i |
| N ≥ H × N_min | Evenly random select N vectors: S_seed ∈ S_i |
| N ≥ H × N_min | Prune & Cluster, get r and I |
| N ≥ H × N_min | Obtain N_min based on Eq. (19) |
| N ≥ H × N_min | N ≤ L × N_min |
| N ≥ H × N_min | N = N * 2 |
| N ≥ H × N_min | N ≥ H × N_min |