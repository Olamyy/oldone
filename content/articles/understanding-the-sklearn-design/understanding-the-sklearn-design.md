Title: The Sklearn API Design
author: Olamilekan Wahab
Slug: understanding-the-sklearn-design
categories: python sklearn machine-learning
Date: 2017-11-01
Tags: machine-learning,sklearn, python
image: scikit.png 
Status: draft


Some weeks back, I decided to start contributing to the open source scikit-learn library. This decision led me to read a whole lot of sklearn's code, documentation , contribution and 
online guides.

This article is an attempt to document everything I learnt about the design principles behind the library.

The rest of the article will be organised as follows:

* What is a scikit in python? 
    * Examples of scikits
* Scikit-learn
    * What is scikit-learn?
    * A little history
    * Data representation
    * API Design Principles
        * Consistency
            * Estimators
            * Predictors
            * Transformers
            * Meta-estimators
            * Pipelines
            * Feature Unions
            * Models and Model Selection
        * Inspection
        * Composition
        * Defaults
    * Extending scikit-learn
    * Reading the scikit-learn code 
    * Contributing to scikit-learn
* Conclusion
* Resources  



## What is a scikit in python?
A scikit, short for SciPy Toolkit(or the more expressive, Scientifica Python Toolkit) is a any open sourced software for Python written to supplement Scipy. Scikits are essentially add on packages 
that are related to either science, engineering or research in one field or another. They're usually BSD licensed and are built upon existing libraries like scipy and numpy. A package can be called
a scikit when :

1. It is too specialized on a field or topic to part of SciPy.
2. It is GPL licensed (This makes it incompatible with SciPy’s BSD license).
3. It's meant to be part of Scipy but is still actively being developed.

### Example of scikits
Some of the most widly used example scikit packages are:

1. Machine Learning Specific
    * [Scikit-learn](http://scikit-learn.org/)
    * [Scikit-neuralnetwork](http://scikits.appspot.com/scikit-neuralnetwork)
    * [scikit-splearn](http://scikits.appspot.com/scikit-splearn)
    * [scikit-metrics](http://scikits.appspot.com/scikit-metrics)
    * [scikit-tensor](http://scikits.appspot.com/scikit-tensor)
    * [scikit-surprise](http://scikits.appspot.com/scikit-surprise)
    * [scikit-stack](http://scikits.appspot.com/scikit-stack)
    * [scikit-graph](http://scikits.appspot.com/scikit-graph)
    * [scikit-keras](http://scikits.appspot.com/scikit-keras)
2. Media Specific Scikits
    * [Scikit-image](http://scikits.appspot.com/scikit-image)
    * [Scikit-sound](http://scikits.appspot.com/scikit-sound)
    * [Scikit-video](http://scikits.appspot.com/scikit-video)
    * [Scikit-xray](http://scikits.appspot.com/scikit-xray)
3. Data Specific
    * [Scikit-dataacces](http://scikits.appspot.com/scikit-dataaccess)
    * [Pandas](http://github.com/pandas/pandas-dev)
    * [Scikit-data](http://scikits.appspot.com/scikit-data)
    * [Scikit-datasets](http://scikits.appspot.com/scikit-datasets)
    * [Scikit-discovery](http://scikits.appspot.com/scikit-discovery)
4. Visualization Specific Scikits
    * [Matplotlib]()
    * [Scikit-visualizations](http://scikits.appspot.com/scikit-visualizations)
    * [Scikit-vi](http://scikits.appspot.com/scikit-vi)
    * [Scikit-vis](http://scikits.appspot.com/scikit-vis)	
    * [Scikit-viz](http://scikits.appspot.com/scikit-viz)
    * [Scikit-plot](http://scikits.appspot.com/scikit-plot)
    
While the list above covers some popular scikits, the official [scikit appspot website](http://scikits.appspot.com/scikits) links to a whole lot of other scikits.


## Scikit-learn
### What is scikit-learn?
Scikit-learn(shortened as sklearn) is an open source library that provides a consistent API for using traditional state of the art Machine Learning algorithms/methods in Python.

Majorly written in Python, some of sklearn's internal algorithms are written in Cython using third party bindings like LIBSVM and 
LIBLINEAR. Sklearn's major python dependencies are scipy, numpy and matplotlib. 


![sklearn dependency tree.](/images/sklearn.png) 

Figure 1 : This shows a dependency tree for the sklearn library.


## A little history
During the Google Summer of Code in 2007, David Cournapeau decided to put together a number of algorithms he has been using over time into a python module. A while after this, Matthieu Brucher joined
the project and decided to use it for computational work in his thesis. This gave sklearn more light and in no time(2010 to be specific), [INRA]() got involved in it and the first major release was 
published in the same year.
 


## Data Representation
Machine learning data in different fields, languages, etc. is generally represented as a pair of matrices with numerical values, say $X$ and $y$. The $X$ variables often represent the input values and
the $y$ variables represent the output values. Each row of these matrices  to one sample of the dataset and each column to one variable of the problem.
Sklearn as expected also follows the same form for representing data internally. To represent data, it classifies all data under 3 types of data:

####1. Sparse Data

A sparse data is any dataset that mostly contains more zeros that non-zero entries. To be a bit technical, a vector is $k$-sparse if it contains at most $k$ nonzero entries. 
    
![sparse matrix.](/images/sparse_matrix.png) 

Figure 2 : An example of a sparse matrix.

Sklearn represents sparse data as scipy sparse matrices. It does this because:

* Storing all zero values in a sparse matrix is a computational waste.
* It is much more efficient to operate only on elements that will return nonzero values.

To avoid these, sklearn uses a scipy algorithm called Compressed Sparse Row (CSR). This essentially compresses the memory footprint of the matrix object and speeds up insert and retrieval processes
 to optimize the operation of many sklearn's algorithms. 
 
 
 >>> Sklearn has a number of algorithms that support sparse matrix operations. If you ever need to check if an algorithm supports sparse data, check the documentation of the  `fit` method of it's 
 class. If it has an `X: {array-like, sparse matrix}` entry, then it supports sparse data entry.

 For a much more thorough understanding of how scipy sparse matrices work, you can check out [David Ziganto's](https://github.com/dziganto/Data_Science_Fundamentals) article [here](https://dziganto.github.io/Sparse-Matrices-For-Efficient-Machine-Learning/)
  

####2. Dense Data

   A dense data contains mostly non-zero entries. 
    
   ![dense matrix.](/images/dense.jpg) 
   
   Figure 3 : An example of a dense matrix.
   
   Sklearn represents dense data as  multidimensional numpy arrays.
   [X's]() notes has a very thorough explanation of how this works.
  
  
####3. Non standard textual data
For situations where models are to be built using text files or semi-stuctured python objects, sklearn attempts to `vectorize` these files/objects into the more efficient numpy and scipy data types.


## API Design Principles
 In this section, I would discuss some of the design desicions that were made during the creation of the library, why they were made and how these decisions have influenced the way the library is 
 used now.
 
### Consistency
The sklearn API was majorly designed to be consistent. This means object that do the same things were given a simple and consistent interface. Having a consistent API meant objects(sklearn objects)
 had to be grouped based on a number of conditions.
 The available types of sklearn objects are:
 
     1. Estimators and Meta-estimators
     2. Transformers
     3. Predictors
     4. Pipelines
     5. Feature Unions

1. Estimators and meta-estimators:

    Estimator objects like you would expect are sklearn classes that estimate parameters in data. Both supervised and unsupervised sklearn algorithms provide support for estimators. Since estimator
    objects do some form of `learning`, the initialization and learning phase of estimators are separated.
    If  `hyperparameter` values are set during the initialization of estimators, the set values are used during learning. If not, the default values are used while learning.
    
    Once initialized, estimators expose a ``fit`` method where the estimation learning happens. The `fit` method is called with one parameter(or two if the task being handled is a 
    supervised learning task. This parameter is the `label` datasets.)  The `fit` method when called learns by determining model-specific parameters from the training data and set these as attributes
     on the estimator object. Once learning is complete, this model sets its parameters(the learned parameters) gets exposed as class attributes with trailing underscore in their names(An example 
     is the `statistics_` attribute of the `Imputer` estimator.).
     
     In situations were a user needs to implement his own meta-estimator, the `BaseEstimator` 
       class and it's(the required classifier) 
       corresponding 
       `mixin` can be 
       subclassed as shown below.
       
        from sklearn.base import BaseEstimator, RegressorMixin
        
        ## A regressor mixin is being used here because 
        ## the example is for a regressor Estimator.  
    
        class ExampleClassifierEstimator(BaseEstimator, RegressorMixin):  
        """An example of an regressor estimator. 
        Take a good look at docstring of the constructor, fit and predict methods. """
    
        def __init__(self, **kwargs):
            """
            Called when initializing the classifier.
             Set default hyperparameter values here.
            """
            
    
    
        def fit(self, X, y=None):
            """
            This should fit classifier. All the "work" should be done here.
    
            Note: assert is not a good choice here and you should rather
            use try/except blog with exceptions. This is just for short syntax.
             The y parameter must be set if the task is supervised learning.
            """
    
            return self
    
        def predict(self, X, y=None):
            """Prediction Logic goes here. 
            Remember to always check if the 
            threshold attribute of your estimator is set. """
    
        def score(self, X, y=None):
            """ This is only needed if the estimator is to be used with a GridSearchCV """
            
        def get_params(self, deep=True):
            pass

        def set_params(self, **parameters):
            pass
            
           
   
       Meta estimators are a higher order estimators that are made from other(base) estimators. They require base estimators to be provided in their constructor. The most used example of 
       meta-estimators are ensemble methods available via `sklearn.ensemble` 
       In sklearn, each instance of a classifier (estimator) implements a corresponding meta-estimator.  An alternative approach to creating meta-estimators is to use the multiclass sklearn module and implementing any of the algorithms below:
   
    * one-vs-all
    * one-vs-one
    * error correcting output codes
    
    
     In conclusion, always keep the following at the back of your mind when writing or working with estimators and meta-estimators:
     
     * Constructor parameters should have default values.
     * Constructor shouldn't implement any form of logic(whether complex or not). Logic is best suited for the fit method.
     * The `fit` method should handle all logic and return an instance of the class.
     
    
2. Transformers

    Transformer objects are somewhat `transmutational` in nature. They exist to provide an interface for data modification or filtering within sklearn. Transformer objects mostly exists 
    along sides estimator objects. This means some objects have both estimator and transformation features availble to them.
    
    Like estimators, transformers do not carry out any major logic in their constructor. Instead, they  expose a `transform` method where the transformation happens. This method takes a dataset as 
    a parameter. Transformers also have a `fit_transform` or `fit_predict`(fit_predict for clustering transformers) method that both `fits` and `transforms` data in one go. Preprocessing, feature 
    selection, feature extraction and 
    dimensionality 
    reduction 
    algorithms are all provided as transformers within the sklearn.
    
     
    `from sklearn.preprocessing import Imputer`
    
    ```imputer = Imputer()```
    
    ```imputer.fit(X train)```
    
    ```X_train = imputer.transform(X_train)```
    
    The above block can be made better as shown below:
    
    `X_train = Imputer().fit(X_train).transform(X_train)`
    
    The above line can even made more better as shown below:
    
    `X_train = Imputer().fit_transform(X_train)`


3. Predictors

    Predictor objects are able to make predictions. They're basically estimators with a `predict` method. Predictors returns the predicted label as output. 
    Asides prediction, some predictors expose methods to benchmark various aspects of the prediction. These methods can be any of:
    
    1. `decision_function` for linear models to measure the distance between samples
    2. `score` to  measure the quality of the prediction. This method computes the coefficient of determination  in regression and the accuracy in classification.
    3. `predict_proba` to measure class probabilities.