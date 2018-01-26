Title: Locally Weighted Regression
author: Olamilekan Wahab
Slug: locally-weighted-regression
categories: python maths machine-learning
Date: 2017-11-01
Tags: Maths,Python,Fourier
image: locally-weighted-regression.png 
Status: draft


Locally weighted regression is estimates a regression surface through a multivariate smoothing. 

A couple of weeks back, I started a review of the linear models I have used over the years and it hit me that I never really understood how this algorithm works. This inspired me to do an investigation into their working principles of the algorithm.In this post, I would attempt to provide an overview of the algorithm using statistical inferences,a possible sklearn/numpy powered implementation and a benchmark of different implementations. 

This article would follow the trend below:

* Regression 
    * Regression Function
    * Regression Algorithms
* Locally Weight Regression
    * Mathematical Proof
    * Python Implementation
    * Benchmark
* Conclusion
* Resources