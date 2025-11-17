# README

This is the Open Science material to accompany the article "Evaluating the layout quality of UML class diagrams using machine learning," written by:

* Gustav BERGSTRÖM
* Fadhl HUJAINAH
* Truong HO-QUANG
* Rodi JOLAK
* Satrio Adi RUKMONO (corresponding author)
* Arif NURWIDYANTORO
* Michel R.V. CHAUDRON

## 1. Study Protocol

For the complete explanation on the methodology of our study, including the formulae for extracting image features and the normalization of feature values, please consult the [manuscript](preprint.pdf).

1. We selected 654 UML class diagrams from [the Lindholmen dataset](http://www.models-db.com/) that satisfies our criteria.
2. We had six experts manually inspecting and labeling the layout quality of the diagrams. Each diagram was rated by two experts in the scale of 1 (very bad) to 5 (very good). The final quality label of a diagram is the average of the two rating points.
3. We extracted features for machine learning from the 654 diagrams using computer vision based on [prior work](https://doi.org/10.1109/APSEC.2014.65) and filtered out diagrams that our image processor could not handle. This leaves a final dataset of 609 images.
4. We fed the dataset (and a normalized version of the dataset) to various machine learning algorithms using the [Weka](https://www.cs.waikato.ac.nz/~ml/weka/) tool, selected the best performing algorithm, and performed grid search on the algorithm's parameters using `python` with the `scikit-learn` module to find a better-performing model.
5. We evaluated the performance of our models.

## 2. Raw data

|Link|Description|
|-|-|
|[zenodo<sup>🡭</sup>](https://zenodo.org/record/5037744#.YO1lUagzaUk)|The 654 diagrams that we selected from the Lindholmen dataset.|
[01-diagrams](01-diagrams/)|A copy of the diagrams from the zenodo link.|
|[02-labeling/instructions.md](02-labeling/instructions.md)|The instruction texts shown to the experts on a Web interface used for the manual labeling process.|
|[03-features-labels/dataset.csv](03-features-labels/dataset.csv)|A table containing the extracted features and quality labels of the final 609 diagrams.|
|[03-features-labels/dataset_scaled.csv](03-features-labels/dataset_scaled.csv)|A version of the dataset with normalized feature values.|
|[04-parameters/weka.md](04-parameters/weka.md)|The parameter values and usage instructions for the selected twelve machine learning algorithms from the Weka tool. These are the default values for the algorithms as of Weka 3.8.5.|
|[04-parameters/grid-search.ipynb](04-parameters/grid-search.ipynb)|A `python` notebook for gird search on the Random Forest algorithm.|
|[05-analysis/confusion-matrix.ipynb](05-analysis/confusion-matrix.ipynb)|A `python` notebook that loads a Weka model and generates a confusion matrix from the predicted labels.|
|[05-analysis/features.ipynb](05-analysis/features.ipynb)|A `python` notebook used in the analysis of features and their relations to the quality labels.|

Note: the python scripts were verified to work on Python 3.9.5 and scikit-learn 1.0.2.

## Contact

This material was first published at [rsatrioadi/OpenScience-UMLLayoutQuality (github.com)](https://github.com/rsatrioadi/OpenScience-UMLLayoutQuality). Questions, problems, and so on can be communicated via the [Issues](https://github.com/rsatrioadi/OpenScience-UMLLayoutQuality/issues) page.