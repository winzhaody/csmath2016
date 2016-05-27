import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


# show image: the input is a 1024*1 vector
def show_img(vec):
	plt.imshow(vec.reshape(32,32),cmap=cm.gray)
	plt.show()

# load the dataset - optdigits-orig (the head part is removed)
def load_data(file_name, num):
	file_data = open(file_name)
	list_data = []
	while True:
		str_data = ''
		for i in range(32):
			line = file_data.readline()
			if not line:
				break
			str_data += line[:-1] # remove the last char: \n
		line = file_data.readline()
		if not line:
			break
		if int(line) == num:
			# change the string into int array with ascii
			# 45 is the ascii code of '0'
			list_data.append(np.fromstring(str_data, dtype=np.int8)-48)
	file_data.close()
	return np.mat(list_data)

# load the changed dataset 
def load_mat(file_name, num):
	file_data = open(file_name)
	list_data = []
	while True:
		line = file_data.readline()
		if not line:
			break
		sample_data = []
		for item in line[:-1].split(','):
			sample_data.append(int(item))
			
		if sample_data[-1] == num:
			list_data.append(sample_data[:-1])
		
	file_data.close()

	return np.mat(list_data)

	
# input is the data_matrix samples_num*feature_num
# output is the reduced 2-d data
def pca_reduce_2d(x):
	mean_x = np.mean(x,axis=0)
	xnew = x - mean_x
	cov_x = np.cov(xnew, rowvar=0)
	eig_val, eig_vec = np.linalg.eig(cov_x)
	eig_val_ind = np.argsort(eig_val)
	# find the index of the 2 largest eig-value
	ind = [eig_val_ind[-1], eig_val_ind[-2]]
	eig_vec_reduced = eig_vec[:,ind]
	
	return x*eig_vec_reduced

# input is the 2-d data
def grid_data(d, step):
	# built a 2-d vector with 25 elements
	grid = []
	for i in range(-2,3):
		for j in range(-2,3):
			grid.append([i*step,j*step])

	ind_grid = []
	for gd in np.mat(grid):
		ind = np.argmin(np.linalg.norm(d-gd,axis=1))
		ind_grid.append(ind)	
	return ind_grid
#	return d[ind_grid,:]

def get_xy(d):
	x = []
	y = []
	for e in d:
		x.append(e[0,1])
		y.append(e[0,0])
	return x, y

# integrate grid images into a larger image
# input is a 25*1024 matrix
def int_img(mat_img):
	n = 32*5
	img = np.empty((n,n))
	for i in range(5):
		for j in range(5):
			m = mat_img[(j)*5+4-i].reshape(32,32)
			for ii in range(32):
				for jj in range(32):
					ind_x = i*32+ii
					ind_y = j*32+jj
					img[ind_x,ind_y] = m[ii,jj]
	return img

# choose number
def choose_num(n):
	data = load_mat('optdigits-tra-comp.cv',n)
	data_orig = load_data('optdigits-tra-orig.cv',n)
	return data, data_orig



if __name__ == '__main__':
	data, data_orig = choose_num(3)
	pt = pca_reduce_2d(data)
	
	grid_ind = grid_data(pt,7.5)
	remain_pt = pt[np.setdiff1d(np.arange(pt.shape[0]),grid_ind),:]
	grid_pt =pt[grid_ind,:]
	
	x0, y0 = get_xy(remain_pt)
	xg, yg = get_xy(grid_pt)
	
	
	# get the origin data of grid index
	grid_img = data_orig[grid_ind,:]
	#print grid_img.shape
	img = int_img(grid_img)
	
	plt.figure(1)		
	plt.scatter(x0,y0,marker='o',color=[0,0,1])
	plt.scatter(xg,yg,marker='*',color=[1,0,0])
	plt.figure(2)
	plt.imshow(img,cmap=cm.gray)
	plt.show()


















