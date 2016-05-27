# PCA

## Theory

Consider a data set of observations *{x<sub>n</sub>}* where *n = 1, ..., N*, and *x<sub>n</sub>* is a
Euclidean variable with dimensionality *D*. Our goal is to project the data onto a space having dimensionality *M &lt; D* while maximizing the variance of the projected data.

To begin with, consider the projection onto a one-dimensional space (*M = 1*). We can define the direction of this space using a *D*-dimensional vector *u<sub>1</sub>*, which for convenience (and without loss of generality) we shall choose to be a unit vector so that *u<sub>1</sub><sup>T<sup>**u<sub>1</sub> = 1*(note that we are only interested in the direction defined by *u<sub>1</sub>*, not in the magnitude of *u<sub>1</sub>* itself). Each data point *x<sub>n</sub>* is then projected onto a scalar value *u<sub>1</sub><sup>T<sup>**x<sub>n</sub>*. The sample set mean given by

![img](../imgs/hw2_t1.png)

and the variance of the projected data is given by

![img](../imgs/hw2_t2.png)

where ***S*** is the data covariance matrix defined by

![img](../imgs/hw2_t3.png)

We now maximize the projected variance *u<sub>1</sub><sup>T<sup>**Su<sub>1</sub>* with respect to *u<sub>1</sub>*. The appropriate constraint comes from the normalization condition *u<sub>1</sub><sup>T<sup>**u<sub>1</sub> = 1*. To enforce this constraint, we introduce a Lagrange multiplier, and then make an unconstrained maximization of

![img](../imgs/hw2_t4.png)

By setting the derivative with respect to *u<sub>1</sub>* equal to zero, we see that this quantity will have a stationary point when

![img](../imgs/hw2_t5.png)

and so the variance will be a maximum when we set *u<sub>1</sub>* equal to the eigenvector having the largest eigenvalue. This eigenvector is known as the first principal component.

We can define additional principal components in an incremental fashion by choosing each new direction to be that which maximizes the projected variance amongst all possible directions orthogonal to those already considered. If we consider the general case of an *M*-dimensional projection space, the optimal linear projection for which the variance of the projected data is maximized is now defined by the *M* eigenvectors of the data covariance matrix **S** corresponding to the *M* largest eigenvalues
## Test data

The original data set is from [Optical Recognition of Handwritten Digits Data Set](http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits).
 
I changed the data a little bit for convience and use two files -- *optdigits-tra-comp.cv* and *optdigits-tra-orig.cv*.

**optidgits-tra-comp.cv**: It is the data set for training  which contains 3823 samples with compression. It is optdigits.tra removing its head information.

**optdigits-tra-orig.cv**: It is the data set for generating images. The full data is consisited of these data set and all head information are removed.

 * line 1-1934: optdigit-orig.tra
 * line 1935-2880: optdigit-orig.cv
 * line 2881-3823: optdigit-orig.wedp




## Program results

The digit can be chosen in function *choose_num*

* perform PCA over all digit '3' with 2 components

![img](../imgs/hw2_3_p.png)

![img](../imgs/hw2_3_i.png)


* perform PCA over all digit '6' with 2 components

![img](../imgs/hw2_6_p.png)

![img](../imgs/hw2_6_i.png)


## Reference

Bishop C M. Pattern Recognition and Machine Learning (Information Science and Statistics)[M]. Springer-Verlag New York, Inc. 2006.