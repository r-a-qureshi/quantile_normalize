# Scikit-Learn Compatible Quantile Normalization
## Introduction
Quantile Normalization is used in gene expression experiments to ensure that all samples in the experiment follow the same distribution of values. This can help reduce technical variation between samples so that true biological variation can be studied. Quantile normalization is an important preprocessing step in the analysis of transcriptomic data. However, using quantile normalization as a part of a machine learning pipeline poses challenges. Since quantile normalization uses all samples in an experiment to generate a distribution, information can leak from test samples to training samples.

The goal of this package is to provide a an extension to scikit-learn for quantile normalization. The class ```QuantileNormalize``` is a sklearn compatible transformer that learns the distribution of samples based on training data and can then quantile normalize the test samples to the same distribution as the training samples. It will preserve the separation between training and testing sets.

## Installation
```
pip install https://github.com/r-a-qureshi/quantile_normalize/archive/master.zip
```

## Demo
QuantileNormalize inherits from ```sklearn.base``` to create a custom transformer. It can be used just like any other sklearn transformer.
```python
from quantile_normalize import QuantileNormalize
qnorm = QuantileNormalize()
qnorm.fit(train_data)
norm_test_data = qnorm.transform(test_data)
# QuantileNormalize inherits fit_transform from sklearn
norm_data = qnorm.fit_transform(all_data)
```

In this example I will show how to use the ```QuantileNormalize``` class as part of a sklearn pipeline to classify gene expression data. We will assume ```exp``` and ```labels``` are a pandas dataframe of gene expression data and binary class labels, respectively. 
```python
from quantile_normalize import QuantileNormalize
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

# split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    exp,
    labels,
    test_size=0.25,
    random_state=0
)

# Create a sklearn pipeline that performs, normalization, scaling
# and classification
pipe = Pipeline(
    [
        ('quantilenorm',QuantileNormalize()),
        ('scaler',StandardScaler()),
        ('classifier',LinearSVC()),
    ]
)

# Train the model
pipe.fit(X_train,y_train)
# Make predictions for the test samples
pred_labels = pipe.predict(X_test)
```

Alternatively, ```QuantileNormalize``` can be used outside a machine learning context to perform quantile normalization on an entire dataset.
```python
from quantile_normalize import QuantileNormalize
norm_data = QuantileNormalize().fit_transform(raw_data)
```