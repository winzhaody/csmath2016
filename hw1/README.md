# Curve fitting

## Theory

### 1. Polynomial Curve Fitting to Linear Regression
![img](../imgs/hw1_t1.png)

![img](../imgs/hw1_t2.png)

### 2. Minimum-Squared Error 

![img](../imgs/hw1_t3.png)

Using matrix notation for convenience

![img](../imgs/hw1_t4.png)

### 3. Optimizing the MSE Criterion
Computing the gradient gives

![img](../imgs/hw1_t5.png)

Setting the gradient to zero

![img](../imgs/hw1_t6.png)
### 4. Regulization
The solution for *a* can be obtained uniquely if *XX<sup>T</sup>* is non-singular. We can use ridge regression.

![img](../imgs/hw1_t7.png)

The unique solution:

![img](../imgs/hw1_t8.png)

## Program results

Sample the function curve of y=sin(x) with Gaussian noise. The blue curve is the origin curve and the green one is the polynomial fitting curve.

* fit degree 3 curves in 10 samples

![img](../imgs/hw1_10s_3d.png)

* fit degree 9 curves in 10 samples

![img](../imgs/hw1_10s_9d.png)

* fit degree 9 curves in 15 samples

![img](../imgs/hw1_15s_9d.png)

* fit degree 9 curves in 100 samples

![img](../imgs/hw1_100s_9d.png)

* fit degree 9 curves in 10 samples with regularization

![img](../imgs/hw1_10s_9d_r.png)

