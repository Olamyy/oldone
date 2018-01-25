Title: Beyond Linearity
author: Olamilekan Wahab
Slug: beyond-linearity
categories: python machine-learning non-linear algorithms
Date: 2017-11-01
Tags: Maths,Python,Fourier
image: linearity.png 
Status: draft



### Beyond Linearity

Before going any deep, let’s note the following:

1.  Two possible estimations can be carried out using the equation below. These are
**Prediction** and **Inference**

![](https://cdn-images-1.medium.com/max/640/1*bpXEdJYFCHe8I-ml8Vlfqw.png)
<span class="figcaption_hack">Model function with Y representing prediction, X representing input and E , a
measure of error.</span>

2.  In **prediction**, the above function resolves to

![](https://cdn-images-1.medium.com/max/640/1*JHpzzUWlm17T0u8mABbWlw.png)
<span class="figcaption_hack">In prediction, error term gets averaged to 0 so E=0</span>

Prediction is often carried in situations where sets of input variables, **X**,
exist and the output **Y** cannot be easily deciphered. In this sense, **Y
**is** **predicted using a **function** of **X** which can be either linear or
non-linear.

3. **Inference** is much more interested in relationships. It’s carried out when
an understanding of the way **Y **is affected as values in **X **change is
required**. **More formally, in inference we attempt to understand the
relationship between **Y** and **X** as **X **takes on different values, say,*
***X.1,…, X.n .**

<br> 

Now, In machine learning, there’s a constant tussle between model **accuracy**,
**flexibility** and **interpretability**. This tussle exists because highly
accurate models are hard to interpret and easily interpretable models generally
have low accuracy. The same logic applies to model flexibility and
interpretability. Generally flexible methods are not very interpretable and vice
versa. Choosing a side in this tussle happens to be one of the most important
decision to make while building Machine Learning models. *Should we focus on
making our predictions more accurate/flexible or more interpretable*?* How does
our choice directly or indirectly affect our performance?*

![](https://cdn-images-1.medium.com/max/640/1*UfNy09IS0djZqA69jsaLng.png)
<span class="figcaption_hack">A table showing the trade-off between model flexibility and interpretability for
various methods.</span>

From the table above, it can be inferred that linear models are easily
interpretable. This gives them an advantage over approaches with less
interpretability. Linear regression for example is quite easy to interpret since
it's a representation of linear functions. Also, when the task at hand is
*inference, *linear models are a good choice since they make it easy to
understand the relationship between** Y** and **X.1** , . . . , **X.n**

However, they’re **inflexible **thereby very **restrictive.**
