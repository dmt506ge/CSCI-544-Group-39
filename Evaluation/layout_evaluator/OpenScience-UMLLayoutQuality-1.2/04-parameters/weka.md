# Weka Experiments

The following list enumerates the algorithms we use in the experiments and the arguments (parameter values) that we used.

- `weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -num-decimal-places 4`
- `weka.classifiers.functions.SimpleLinearRegression`
- `weka.classifiers.functions.SMOreg -C 1.0 -N 0 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.001 -W 1" -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007"`
- `weka.classifiers.functions.GaussianProcesses -L 1.0 -N 0 -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007" -S 1`
- `weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0 -E 20 -H a`
- `weka.classifiers.rules.DecisionTable -X 1 -S "weka.attributeSelection.BestFirst -D 1 -N 5"`
- `weka.classifiers.rules.M5Rules -M 4.0 -num-decimal-places 4`
- `weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1`
- `weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1`
- `weka.classifiers.trees.REPTree -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0`
- `weka.classifiers.trees.M5P -M 4.0 -num-decimal-places 4`
- `weka.classifiers.trees.DecisionStump`

We performed the experiments using Weka's `Explorer` tool with the following steps for each algorithm above and each dataset from the `03-features-labels` directory:

1. Load the dataset using the `Open file...` button on the `Preprocess` tab.
2. Remove the feature called `name` from the `Attributes` panel.
3. Select the algorithm using the `Choose` button on the `Classify` tab.
4. Select `Cross-validation` with 10 folds in the `Test options`.
5. `Start` the experiment.
6. The performance scores of the experiment is acquired from the `Summary` part of the `Classifier output`. This is what we used to construct *Table 1* in the manuscript.
7. Save the model into an `ARFF` file by selecting `Save model` in the context menu of the experiment result in the `Results list` panel.
