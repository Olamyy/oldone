Title: Locally Weighted Regression
author: Olamilekan Wahab
Slug: locally-weighted-regression
categories: python maths machine-learning
Date: 2017-11-01
Tags: Maths,Python,regression, lwr, 
image: locally-weighted-regression.png 
Status: draft


Locally weighted regression is estimates a regression surface through a multivariate smoothing. 

A couple of weeks back, I started a review of the linear models I have used over the years and it hit me that I never really understood how the locally weight regression algorithm works. This encouraged me to do an investigation into the working principles of the algorithm.In this post, I would attempt to provide an overview of the algorithm using statistical inferences,a possible sklearn/numpy powered implementation and a benchmark of different implementations. 

This article would follow the trend below:

* Regression 
    * Regression Function
    * Regression Algorithms 
    * Regression Assumptions
* Locally Weight Regression
    * Mathematical Proof
    * Python Implementation
    * Benchmark
    * Differences between LWR and Linear Regression
* Conclusion
* Resources


##Notations


The following notations would be used throughout this article

| Symbol          | Meaning       |
| -------------   |:-------------:| 
| $$ y $$         |Target Variable|
| $$ X $$         |Features         |  
| $$ (X, y)   $$  |Training set  |
| $$ n $$         |Number of features|
| $$ X^i, y^i $$  |<sup>ith</sup> index of X and y |
| $$ m $$         |Number of training examples|



## Regression
Regression is the estimation of a continuous response variable based on the values of some other variable. The variable to be estimated is dependent on some other variable(s) in the function space. It is parametric in nature because it makes certain assumptions based on the available data. If the data follows those assumptions, regression gives incredible results. Otherwise, it struggles to provide convincing accuracy. 

###Regression Function
The regession function is a linear function used for estimating the target variable. It includes a dependent variable(target), a set of independent variables(features) and an unknown parameter. It's represented as:

    
$$ h_{\theta}(x) = \theta_{0} + \theta_{1} X_{1} + \theta_{2} X_{2}+ ... + \theta_{n} X_{n} \label{a}\tag{1}$$

When evaluated, $h_{\theta}(x)$ in $\ref{a}$ above becomes $h(x)$. The regression function is called `linear regression` when only one independent variable $(X)$ is involved. In such cases, it becomes $ h_{\theta}(x) = \theta_{0} + \theta_{1} X_{1} + \epsilon_{1}$. It's called `multiple regression` when there are more than a single value for $X$.

Also, when carefully looked at, the equation above is the equation of a line, more formally represented as $y = mx + c$ .Given this, to simplify the function, the intercept x_{0},is assumed to be $1$ so that the equation becomes:
 
$$ h_{\theta}(x) = \sum_{a}^{b} \theta_{i} X_{i} + \epsilon_{i} \label{b}\tag{2}$$ 


An alternative representation of $\ref{b}$ when expressed in vector form is given as:

$$ h_{\theta}(x) = θ^{{T}} x_{i} \label{c}\tag{3}$$ 


###Regression Algorithms


###Regression Assumptions
While doing regress

As we discussed above, regression is a parametric technique, so it makes assumptions. Let's look at the assumptions it makes:

* There exists a linear and additive relationship between dependent (DV) and independent variables (IV). 
By linear, it means that the change in DV by 1 unit change in IV is constant. By additive, it refers to the effect of X on Y is independent of other variables.

* There must be no correlation among independent variables. Presence of correlation in independent variables lead to Multicollinearity. If variables are correlated, it becomes extremely difficult for the model to determine the true effect of IVs on DV.

* The error terms must possess constant variance. Absence of constant variance leads to heteroskedestacity.

* The error terms must be uncorrelated i.e. error at ∈t must not indicate the at error at ∈t+1. Presence of correlation in error terms is known as Autocorrelation. It drastically affects the regression coefficients and standard error values since they are based on the assumption of uncorrelated error terms.

* The dependent variable and the error terms must possess a normal distribution.
Presence of these assumptions make regression quite restrictive. By restrictive I meant, the performance of a regression model is conditioned on fulfillment of these assumptions.
