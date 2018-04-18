Title: The Data Splitting Dilemma
author: Olamilekan Wahab
Slug: splitting-dilemma
categories: python sklearn machine-learning
Date: 2017-11-01
Tags: machine-learning,sklearn, python
image: scikit.png 
Status: draft


Splitting data the right way is arguably one of the less discussed topics in Machine Learning. 
0Being less discussed results in either doing it all wrong
or not 
This article is an attempt at explaining the topic, its importance and various ways of effectively splitting data.
The rest of the article would be structured in the format below:

1. What is data splitting?

2. Why should data be split?

3. Methods of splitting data
    1. Random
    
    2. Cross Validation
    
    3. 
    
    

### 1. What is Data Splitting?
One of the first decisions to make when modeling is to decide which samples will be used to evaluate performance. Ideally, the model should be evaluated on samples that were not used to build or fine-tune the model, so that they provide an unbiased sense of model effectiveness. When a large amount of data is at hand, a set of samples can be set aside to evaluate the final model. The “training” data set is the general term for the samples used to create the model, while the “test” or “validation” data set is used to qualify performance.
