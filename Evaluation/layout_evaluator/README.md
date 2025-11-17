## Methodology, Evaluation, and Limitations

This work builds on the dataset fields provided in **Bergström et al., 2022**, but the original feature extraction logic was not available.  
To address this, we implemented our own feature extraction pipeline, focusing on geometric layout features (rectangles, lines, polylines, crossings, angles, etc.).  

### Differences from **Bergström et al., 2022**
- **Feature definitions**: Our features may not match it exactly, which introduces bias when comparing results.  
- **GroundTruth encoding**: The GroundTruth diagrams are stored as SVGs that rely heavily on `<clipPath>` and `<path>` instead of `<rect>` or `<line>`.  
  - This leads to systematically lower scores for GroundTruth, since rectangle features are weighted but absent.  
- **Generated diagrams**: LLM‑generated diagrams use `<rect>` and `<line>` more directly, so their feature vectors are richer and score higher under our model.

### Evaluation Summary
The trained model provides **quantitative scores based on layout geometry**. While useful for systematic comparison, these scores do not always align with **human perception of diagram clarity**. For example, GPT‑4o diagrams scored higher numerically but appeared visually less clear compared to Claude 4.5 and GPT‑5. This highlights the limitation of relying solely on layout‑based evaluation.

### Limitations
- **Feature bias**: Current features emphasize rectangles and line geometry, which penalizes GroundTruth diagrams that use clip paths.  
- **Perceptual gap**: Human evaluators value clarity, richness, and semantic detail, which are not captured by the current feature set.  
- **Model scope**: The model measures layout geometry only; it does not evaluate semantic correctness or visual readability.

### Future Directions
1. **Dataset consistency**  
   Reuse the PNG files from the original dataset, manually convert them into SVG, and re‑extract features using our method. This would align GroundTruth and generated diagrams more fairly.

2. **Feature expansion**  
   Incorporate additional features beyond geometry, such as:
   - Color usage  
   - Text density and distribution  
   - Label alignment and readability  
   - Symmetry and semantic connectivity  

3. **Hybrid evaluation**  
   Combine automatic layout scores with human evaluation metrics to provide a more balanced assessment of diagram quality.

---

**Takeaway:**  
The current model is valuable for systematic, geometry‑based comparison, but results should be interpreted with caution. To better reflect actual diagram clarity and usefulness, future work should expand feature coverage and integrate human‑informed evaluation.
