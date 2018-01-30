Title: Locally Weighted Regression
author: Olamilekan Wahab
Slug: locally-weighted-regression
categories: python maths machine-learning
Date: 2017-11-01
Tags: Maths,Python,regression, lwr, 
image: locally-weighted-regression.png 
Status: draft


A couple of weeks back, I started a review of the linear models I've used over the years and it hit me that I never really understood how the locally weight regression algorithm works. This and the fact that sklearn had no support for it, encouraged me to do an investigation into the working principles of the algorithm.In this post, I would attempt to provide an overview of the algorithm using mathematical inference and introduce a possible Python implementation for it. 

The rest of this article will be organised as follows:

* Regression 
    * Regression Function
    * Regression Assumptions
    * The Linear Regression Algorithm
* Locally Weight Regression
    * Python Implementation
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
| $$ X_i, y_i $$  |<sup>ith</sup> index of X and y |
| $$ m $$         |Number of training examples|



## Regression
Regression is the estimation of a continuous response variable based on the values of some other variable. The variable to be estimated is dependent on the other variable(s) in the function space. It is parametric in nature because it makes certain assumptions on the available data. If the data follows these [assumptions](#regression-assumptions), regression gives incredible results. Otherwise, it struggles to provide convincing accuracy. 

###Regression Assumptions

As was mentioned above, regression works best when the assumptions made about the available data are true. 
Some of these assumptions are:

* There exists a linear relationship between $X$ and $y$. 

    This assumes that a change in $X$ would lead to a corresponding change in $y$.
    This assumptions is particularly important in linear regression of which locally weighted regression is a form.

* There must be no correlation in the set of data in $X$. 

    The presence of correlation in $y$ leads to a concept known as [multicollinearity](https://en.wikipedia.org/wiki/Multicollinearity). 
    If variables are correlated, it becomes extremely difficult for the model to determine the true effect of $X$ on $Y$.

* Independence of errors

     This assumes that the errors of the response variables are uncorrelated with each other i.e the error at $ h(x)_i $ should not indicate the error at any other point.

* $y$ must have a normal distribution to the error term


###Regression Function
The regession function is a parametric function used for estimating the target variable. This function can either be linear or non-linear. Now, since this article's main focus is the locally weighted regression which is a form of the linear regression, there would be a focus on linear regression.

Linear regression is an approach for modelling the linear relationship between a scalar $y$ and a set of variables $X$.

![Unfitted scatter plot.](/images/scatter.png) Figure 1


Given a function whose scatter plot is above, a linear regression can be modeled to it by finding the line of best fit. Finding the **line of best fit** in simpler terms is really just getting the best function to represent the relationship between the $X$ and $y$ variables. This function, mostly called the `linear regression function` or more generally the `hypothesis` is a linear function which includes a dependent variable(target), a set of independent variables(features) and an unknown parameter. It's represented as:

$$ h_{\theta}(x) = \theta_{0} + \theta_{1} X_{1} + \theta_{2} X_{2}+ ... + \theta_{n} X_{n} \label{a}\tag{1}$$

When evaluated, $h_{\theta}(x)$ in $\ref{a}$ above becomes $h(x)$. The regression function is called `simple linear regression` when only one independent variable $(X)$ is involved. In such cases, it becomes $$ h(x) = \theta_{0} + \theta_{1} X_{1} + \epsilon_{1} \label{b}\tag{2}$$ It's called `multivariate linear regression` when there is more than a single value for $X$.

Additionally, the equation above is the equation of a line, more formally represented as $y = mx + c$ . Given this, to simplify the function, the intercept $X_{0}$ at $\theta_{0}$,is assumed to be $1$ so that it becomes a summation equation expressed as:
 
$$ h(x) = \sum_{i=0}^{n} \theta_{i} X_{i} + \epsilon_{i} \label{c}\tag{3}$$ 


An alternative representation of $\ref{c}$ when expressed in vector form is given as:

$$ h(x) = θ^{{T}} x_{i} \label{d}\tag{4}$$ 


###The Linear Regression Algorithm
The linear regression algorithm applies the regression function in one form or another in predicting values using `real` data.
Since this prediction can never really be totally accurate, an error (represented as $\epsilon$ in $\ref{b}$ above) is generated.
This error, formulated as $\epsilon = |y - h(x)|$ is the vertical distance from the actual $y$ value to our prediction ($h(x)$) for the same $x$.  The error has a direct relationship with the accuracy of the algorithm. This means the smaller the error, the higher the model accuracy and vice versa. As such, the algorithm attempts to minimize this error.     

The process of minimizing the error involves selecting the most appropriate features($\theta$) to include in fitting the algorithm. 
A popular approach for selecting $\theta$'s is making $h(x)$ as close to to $y$ as possible for each item in $(X, y)$. To do this, a function caled the `cost function` is used. The `cost function` measures the closeness of each $h(x)$ to its corresponding $y$.

> The cost function calculates the `cost` of your regression algorithm.


It's represented mathematically as:

$$ J(\theta) = (\frac{1}{2}) \sum_{i=1}^{m} \left| \left(h(x)_i - y_i \right)^2\right|  \label{e}\tag{5}$$


So, essentially, the linear regression algorithm tries to choose the best $\theta$ to minimize $J(\theta)$ which would in turn reduce the measure of error.
To do this, the algorithm starts by :

1. Choosing a base value for $\theta$. 
2. Updating this value to make $J(\theta)$ smaller. 

This goes on for many iterations until the value of $J(\theta)$ converges to it's local minima. An implementation of the above steps is called the `gradient descent` algorithm. 

The working principles of the gradient descent are beyond the scope of this article and would be covered in a different article in the near future. Alternatively, a very good resource on how they work is available in Sebastian Ruder's paper [here](http://ruder.io/optimizing-gradient-descent/index.html).

In summary, to evaluate $h(x)$, i.e make a prediction, the linear regression algorithm:

1. Fits $\theta$ to minimize $\sum_{i}(y_i - \theta^T x_i)^2 \label{f}\tag{6}$. 

    Upon successful fitting, the graph of the function above becomes
    ![Fitted scatter plot.](/images/fitted_scatter.png)

2. Ouputs $\theta^T x$.



##Locally Weighted Regression


![Unfitted LWR.](/images/unfitted_lwr.png) Figure 3
![Unfitted LWR.](/images/fitted_lwr.png)   Figure 4

In Figure 3 above, there's a relatively higher number of mountains in the input/output relationship. Attempting to fit this with linear regression would result in getting a very high error and a line of best fit that does not optimally fit the data as shown in Figure 4. This error results from the fact that linear regression generally struggles in fitting functions with non-linear relationships. These difficulties introduce a new approach for fitting non-linear multivariate regression functions called "locally weighted regression".

Locally weighted regression is a non-parametric variant of the linear regression for fitting data using multivariate smoothing. Often called **LOWESS** (locally weighted scatterplot smoothing), this algorithm is a mix of multiple local regression models on a meta **k-nearest-neighor**.
It's mostly used in cases where linear regression does not perform well i.e finds it very hard to find a line of best fit. 

It works by fitting simple models to localized subsets ,say $x$, of the data to build up a function that describes the deterministic part of the variation in the data. The points covered by each point (i.e neighorhood) $x$ is calculated using k-nearest-neighors.

> For each selected $X_i$, LWR selects a point $x$ that acts as a neighorhood within which a local linear model is fitted.

LOWESS while fitting the data, gives more weight to points within the neighorhood of $x$ and less weight to points further away from it. A user dependent value, called the **bandwidth** determines the size of the data to fit each local subset. 
The given weight $w$ at each point $i$ is calculated using:
$$w_i = \exp(- \frac{(x_i - x ) ^ 2}{2 \tau ^ 2}) \label{g}\tag{7}$$

$w_i$ depends on the point $x_i$ at which $x$ is being calculated. Since, a small $|x_i − x|$ yields a $w(i)$ close to 1 and a large  $|x_i − x|$ yields a very small $w(i)$, the parameter ($\theta$) is calculated for the LOWESS by giving more weight to the points within the neighorhood of $x$ than the points outside it.

Essentially, this algorithm makes a prediction by:

1. Fitting $\theta$ to minimize $\sum_{i}w_i(y_i - \theta^T x_i)^2  \tag{8}$.       

    The fitting is done using either **weighted linear least squares** or the **weighted quadratic least squares**. The algorithm is called the LOESS when it's fitted using the **weighted quadratic least square** regression.

2. Ouputs $\theta^T x$.



###Python Implementation 


The support for LOWESS in Python is rather poor. This is primarily because the algorithm is computationally intensive given that it has to fit $j$ number of lines at every point $x_i$ within the neighorhood of $x_i$.

Regardless of this challenge, there are currently 2 implementations of the LOWESS algorithm in Python that I have come across. These are:

1.  Statsmodel Implementation
[http://www.statsmodels.org/devel/generated/statsmodels.nonparametric.smoothers_lowess.lowess.html](http://www.statsmodels.org/devel/generated/statsmodels.nonparametric.smoothers_lowess.lowess.html)

    Statsmodel is a python package that provides a range of tools for carrying out statistical computation in Python.

    It provides support for LOWESS in it's `statsmodel.nonparametric` module. Statsmodel supports

    >A lowess function that outs smoothed estimates of endog at the given exog values from points (exog, endog)

    The *exog* and *endog* expressions in the quote above represent 1-D numpy arrays.These arrays denote $x_i$ and $y_i$ from the equation

    This function takes input $y$ and $x$ and estimates each smooth $y_i$ closest to $(x_i, y_i)$ based on their values of $x$. It essentially uses a **weighted linear least square** approach to fitting the data. 
    A downside of this is that statsmodels combines fit and predict methods into one, and so doesn't allow prediction on new data.
    
    *Practice Case Scenario*:

    Let $x$ be a set of 1000 random float between $-\tau$ and $\tau$.

    Let $y$ be a function of the sine of x.

    A scatter plot of the relationship between $x$ and $y$ is shown below:

   ![Unfitted LWR.](/images/statsmodel_case.png) Figure 3

   Now, to fit this scatter plot using statsmodel implementation of model, let's write a simple python function:

``` python
import numpy as np
import statsmodels.api as sm
lowess = sm.nonparametric.lowess
x = np.random.uniform(low = -2*np.pi, high = 2*np.pi, size=1000)
y = np.sin(x) + np.random.normal(size=len(x))
```


