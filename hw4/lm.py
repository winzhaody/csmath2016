import numpy as np
import pylab as pl

def load_data(datafile):
	x = []
	y = []
	data = open(datafile)
	for line in data.readlines():
		lineArr = line.strip().split('\t')
		x.append(float(lineArr[0]))
		y.append(float(lineArr[1]))
	return x, y

# f = a * exp(-b*x)
def fun_res(a, b, x, y):
	dy = []
	for i in range(len(x)):
		dy.append(y[i] - a * np.exp(-b * x[i]))
	return np.mat(dy).T
    

# x: n*1 matrix
def Jacobi(a, b, x):
	n = len(x)
	J = np.zeros([n,2])
	for i in range(n):
		J[i,:] = np.mat([np.exp(-b * x[i]), -a*x[i]*np.exp(-b * x[i])])
	return J


def LM(x, y):
	a = 1
	b = 1

	n_data = len(x)
	n_para = 2
	n_iter = 50

	lmd = 0.01

	updataJ = 1
    
	for i in range(n_iter):
		if updataJ == 1:
			J = Jacobi(a, b, x)
			dy = fun_res(a,b,x, y)
			# compute the Hessian matrix
			H = np.dot(J.T, J)

			if i == 0:
				e = np.dot(dy.T,dy)
            
		H_lm = H + np.eye(n_para)*lmd
		dp = np.dot(np.dot(np.linalg.inv(H_lm), J.T), dy)
		
		g = np.dot(J.T,dy)
		
		a_lm = a + dp[0,0]
		b_lm = b + dp[1,0]
		
		dy_lm = fun_res(a_lm,b_lm, x, y)
		e_lm = np.dot(dy_lm.T,dy_lm)
		
		if e_lm < e:
			lmd = lmd / 10
			a = a_lm
			b = b_lm
			e = e_lm
			updataJ = 1
		else:
			updataJ = 0
			lmd = lmd * 10
		
		if e < 1e-2 * n_data:
			break
	    
	return a, b
           
def show_res(x_data, y_data, a, b):
	

	x_show = np.linspace(0, 8, 1000) 

	y_show = []
	for xx in x_show:
		y_show.append(a * np.exp(-b * xx))




	pl.plot(x_show, y_show)
	pl.plot(x_data, y_data, 'o')

	pl.show()
        
        
if __name__ == '__main__':
	x,y = load_data('testData.txt')

	a,b = LM(x, y)
	print "a = %.3f" %a
	print "b = %.3f" %b

	show_res(x, y, a, b)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
