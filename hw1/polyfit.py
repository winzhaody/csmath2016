# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 09:13:18 2016

@author: Zhao
"""

import numpy as np 
import pylab as pl


def generate_sin(x):
	y0 = np.sin(x)
	y1 = [np.random.normal(0, 0.1) + y for y in y0]
	return y1

def poly_fit(x, y, degree):
	n = x.shape[0]
	Vx = np.ones((n,degree+1))
	# assemble reversed a Vandermonde matrix
	for i in range(0, n):
		for j in range(0, degree):
			Vx[i,j] = x[i]**(degree-j)
	w = np.dot(np.dot(np.linalg.inv(np.dot(Vx.T, Vx)), Vx.T), y)
	return w

def poly_fit_reg(x, y, degree, ln_lmd):
	n = x.shape[0]
	Vx = np.ones((n,degree+1))
	# assemble reversed a Vandermonde matrix
	for i in range(0, n):
		for j in range(0, degree):
			Vx[i,j] = x[i]**(degree-j)
	w = np.dot(np.dot(np.linalg.inv(np.dot(Vx.T, Vx)+np.eye(degree+1)*np.exp(ln_lmd)), Vx.T), y)
	return w

def run_demo(x_data, y_data, degree, is_reg, title):
	if is_reg:
		w = poly_fit_reg(x_data, y_data, degree, -8)

	else:
		w = poly_fit(x_data, y_data, degree)

	ploy_fun = np.poly1d(w)

	x_show = np.linspace(0, 2*np.pi, 1000) 

	pl.title(title)
	pl.plot(x_show, np.sin(x_show))
	pl.plot(x_show, ploy_fun(x_show))
	pl.plot(x_data, y_data, 'o')

	pl.show()




if __name__ == '__main__':

	x_data_1 = np.linspace(0, 2*np.pi, 10)
	y_data_1 = generate_sin(x_data_1)

	x_data_2 = np.linspace(0, 2*np.pi, 15)
	y_data_2 = generate_sin(x_data_2)

	x_data_3 = np.linspace(0, 2*np.pi, 100)
	y_data_3 = generate_sin(x_data_3)

	run_demo(x_data_1,y_data_1,3,0,'10 samples and degree 3')
	run_demo(x_data_1,y_data_1,9,0,'10 samples and degree 9')
	run_demo(x_data_1,y_data_1,9,1,'10 samples and degree 9 with regulization')
	run_demo(x_data_2,y_data_2,9,0,'15 samples and degree 9')
	run_demo(x_data_3,y_data_3,9,0,'100 samples and degree 9')
	















	
