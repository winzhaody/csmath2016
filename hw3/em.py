import numpy as np
import matplotlib.pyplot as plt

# define a class of gaussian distribution
class Gauss_model(object):
	def __init__(self, mu, sigma):
		# mu: D*1
		# sigma: D*D
		self.mu = mu
		self.sigma = sigma
		self.D = mu.shape[0]

	# sigle sample x: D*1
	def cal_gauss(self, x):	
		tmp = -0.5 * (x-self.mu).T * self.sigma.I * (x-self.mu)
		return 1.0 / ((2*np.pi)**(self.D/2)) / (np.linalg.det(self.sigma)**0.5) * np.exp(tmp)

def Init_data(mean, cov, num):
# input: (data dimension -> D, model number -> K)
# 	 mean: D*K
#	 cov : D*D*K
#	 num : 1*K
	D = len(mean[0])
	K = len(num)
	N = sum(num)
	x = np.empty([N,D])
	index = 0
	for i in range(K):
		x[index:index+num[i],:] = np.random.multivariate_normal(mean[i], cov[i], num[i])
		index = index+num[i]
	return x

		
		
def init_gmm(x, K):	# K: number of gaussian model
	N, D = x.shape
	ind_k = x[0:N:N/K]
	gmm = []
	cov0 = np.mat([[1, 0], [0, 1]])
	for i in range(K):
		gmm.append(Gauss_model(np.mat(ind_k[i]).T,cov0))
	
	pw = np.ones([K,1]) / K

	return pw, gmm



def EM(x, K, lmd=0):
##### Initialize
	N, D = x.shape
	ind_k = x[0:N:N/K]
	gmm = []
	cov0 = np.mat(np.eye(D))
	for i in range(K):
		gmm.append(Gauss_model(np.mat(ind_k[i]).T,cov0))
	
	pw = np.ones([K,1]) / K

	Lprev = -float('Inf')
	threshold = 1e-15

	
	while True:
	##### E step
		gamma = np.empty([N,K])
		for n in range(N):
			for k in range(K):
				gamma[n,k] = pw[k,] * gmm[k].cal_gauss(np.mat(x[n]).T)
		tmp = np.sum(gamma, axis=1)

		for n in range(N):
			for k in range(K):
				gamma[n,k] = gamma[n,k] / tmp[n]

	##### M step
		sum_gamma = np.sum(gamma, axis=0)

		# update mu
		for k in range(K):
			for d in range(D):
				gmm[k].mu[d,0] = np.sum(gamma[:,k] * x[:,d]) / sum_gamma[k]

		# update sigma
		for k in range(K):
			tmp = np.zeros([D,D])
			for n in range(N):			
				xx= np.mat(x[n]).T	
				tmp = tmp + gamma[n,k] * (xx - gmm[k].mu) * (xx - gmm[k].mu).T
			gmm[k].sigma = tmp / sum_gamma[k] + lmd*np.eye(D)

		# update pw
		pw = sum_gamma / N

	##### check for convergence
		L_tmp = np.empty([N,K])
		for n in range(N):
			for k in range(K):
				L_tmp[n,k] = pw[k,] * gmm[k].cal_gauss(np.mat(x[n]).T)
		L = np.sum(np.log(np.sum(L_tmp, axis=1)))
		if L-Lprev < threshold:
			break
		Lprev = L

	# calc the result of clustering
	prob = np.empty([N,K])
	for n in range(N):
		for k in range(K):
			prob[n,k] = gmm[k].cal_gauss(np.mat(x[n]).T)
	cluster_res = np.argmax(prob, axis=1)

	return gmm, pw, cluster_res
	

def cal_accuracy(num, cluster_res):
	wrong = 0
	ind = 0
	for i in range(len(num)):
		for xx in cluster_res[ind:ind+num[i]]:
			if xx != i:
				wrong = wrong + 1
		ind = ind+num[i]
	return 1 - float(wrong) / len(cluster_res)
				
def plot_2d_data(x, cluster_res):
	K = np.max(cluster_res) + 1
	N = x.shape[0]
	for i in range(K):
		xx = []
		yy = []
		for j in range(N):
			if cluster_res[j] == i:
				xx.append(x[j,0])
				yy.append(x[j,1])

		plt.plot(xx, yy, '.')
				
		

	plt.show()
	


if __name__ == '__main__':
##### 2d MOG #####
	mean = [[5,1], [-5,-4], [4,3]]
	cov  = [[[1, 2], [2, -4]], [[5, 0], [0, 5]], [[5, 0], [0, 1]]]
	num  = [100, 100, 200]
	
	K = len(num)

	x = Init_data(mean, cov, num)

	gmm,pw, res = EM(x,K)

	print '---------- 2-d MOG ----------'
	print pw
	for i in range(K):
		print gmm[i].mu
		print gmm[i].sigma
		
	rate = cal_accuracy(num, res)

	print rate

	## regulized
	gmm_r,pw_r, res_r = EM(x,K,1e-2)
	print '---------- 2-d regulized MOG ----------'
	print pw_r
	for i in range(K):
		print gmm_r[i].mu
		print gmm_r[i].sigma
		
	rate_r = cal_accuracy(num, res_r)

	print rate_r

##### 3d MOG #####
	mean3 = [[-5,1,1], [-5,-4,2]]
	cov3  = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[2, 0, 0], [0, 1, 0],[0, 0, 2]]]
	num3  = [100, 200]

	x3 = Init_data(mean3, cov3, num3)
	K3 = len(num3)
	gmm3,pw3, res3 = EM(x3,K3,1e-3)

	print '---------- 3-d MOG ----------'
	print pw3
	for i in range(K3):
		print gmm3[i].mu
		print gmm3[i].sigma
		
	
	rate3 = cal_accuracy(num3, res3)
	print rate3

##### plot 2-d clustering result
	plot_2d_data(x, res)










