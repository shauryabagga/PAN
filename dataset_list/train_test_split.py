base_path = './'
train_test_split = base_path + 'train_test_split.txt'
file_names = base_path + 'cub200_2011_multi.txt'
train_images = base_path + 'cub200_2011_multi_train.txt'
test_images = base_path + 'cub200_2011_multi_test.txt'

def get_file_contents(path):
	f = open(path, 'r')
	arr = f.readlines()
	f.close()
	arr = list(map(lambda x : x.rstrip(), arr))
	return arr

train_test_arr = get_file_contents(train_test_split)

train_test_arr = list(map(lambda x : int(x.split()[-1]), train_test_arr))

# len(train_test_arr)

# train_test_arr[1]

file_names_arr = get_file_contents(file_names)

# len(file_names_arr)
print(file_names_arr[0])


for i, is_train in enumerate(train_test_arr):
	if is_train == 0:
		# the image is a test image, so remove from train dataset
		with open(test_images, 'a') as f:
			f.write(file_names_arr[i]+'\n')
		
	else:
		# the image is a training image, so remove from the test dataset
		with open(train_images, 'a') as f:
			f.write(file_names_arr[i]+'\n')