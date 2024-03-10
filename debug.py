import os
path = os.path.join(os.getcwd(), "Dataset_Converted")
print(path)

dataset_in = "C://Users/navin/OneDrive/Documents/Project_Work/api_development/Dataset_Converted/Dataset_Converted"

import glob
for directory_path in glob.glob(dataset_in + "/*"):
    print(directory_path)
    for img_path in glob.glob(directory_path + "/*.jpg"):
        print(img_path)