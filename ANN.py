import numpy as np
import os
from PIL import Image
import pickle as pk
from load_images import extract_labels, extract_images
import random
from binascii import hexlify
#=====hyperparameters========
inp_dim = 

inp_hid1 = np.random.random(,dtype=float64)
#=============================
class neuron:
	def __init__(self):
		# define the hyperparameters
class ANN:
 
 def __init__(self, ):
 	#define hyper parameters

 def forward_pass(self):
 	#TODO
 def backprop(self):
 	#TODO
 def loss(self):
 	#TODO

class Process_data:
	
	def __init__(self, data_folder):
		data = []
		self.data_folder = data_folder
		label_file = open('/'.join([data_folder,"labels.txt"]), "r")
		labels = map(int, (map(hexlify, label_file.read().split('\n')[:-1])))
		#print(labels)
		for img_file in os.listdir(data_folder):
			if(not(img_file.endswith(".png") or img_file.endswith(".jpg"))):
				continue
			img_array = self.process_image(Image.open('/'.join([data_folder,img_file])))
			img_array = img_array.flatten()
			#print(img_file)
			try:
				data.append((img_array,labels[eval(img_file.split(".")[0])-1]))
			except:
				pass
		with open("/".join([data_folder, "data.pickle"]), 'wb') as handle:
			pk.dump(data, handle)

	def process_image(self, img_obj):
		img_array = np.array(img_obj)
		#print(img_array.shape)
		return img_array

	def check_pickle(self):
		with open('/'.join([self.data_folder,"data.pickle"])) as handle:
			data = pk.load(handle)
			print("Number of Samples: {}".format(len(data)))
			print("A sample data point")
			for i in range(1,4):
				print(data[random.randint(1,len(data))])


def main():
	global layers  # TODO
	data = []
	#epochs = int(input("Enter the number of epochs:"))
	#model = ANN() #initialise the initial model with random hyperparameters
	
	extract_images("./train-images.idx3-ubyte", "./data/train")
	extract_labels("./train-labels.idx1-ubyte", "./data/train/labels.txt")
	extract_images("./t10k-images.idx3-ubyte", "./data/test")
	extract_labels("./t10k-labels.idx1-ubyte", "./data/test/labels.txt")

	train_handle = Process_data("./data/train")
	test_handle = Process_data("./data/test")
	train_handle.check_pickle()
	test_handle.check_pickle()

if __name__ == '__main__':
	main()