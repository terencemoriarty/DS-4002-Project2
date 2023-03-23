from tensorflow.python import train
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import Model
import os
import matplotlib.pyplot as plt
import PIL.Image as img
from tensorflow.keras.preprocessing import image
from tensorflow.keras.callbacks import EarlyStopping

train_data = 'Covid19-dataset/train'
test_data = 'Covid19-dataset/test'

# Function to Extract features from the images
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from tqdm import tqdm
from os import listdir
import shutil
def image_feature(direc):
    model = InceptionV3(weights='imagenet', include_top=False)
    features = [];
    img_name = [];
    for i in listdir(direc):
        fname=direc+'/'+i
        if i != '.DS_Store':
            img = image.load_img(fname,target_size=(224,224))
            x = img_to_array(img)
            x = np.expand_dims(x,axis=0)
            x = preprocess_input(x)
            feat = model.predict(x)
            feat = feat.flatten()
            features.append(feat)
            img_name.append(i)
    return features,img_name

# append train
t1img_features,t1img_name=image_feature('/Users/terencemoriarty/Desktop/Covid19-dataset/train/Covid')
t2img_features,t2img_name=image_feature('/Users/terencemoriarty/Desktop/Covid19-dataset/train/Normal')
t3img_features,t3img_name=image_feature('/Users/terencemoriarty/Desktop/Covid19-dataset/train/Viral Pneumonia')
trimg_features = t1img_features + t2img_features +  t3img_features
trimg_name = t1img_name + t2img_name +  t3img_name

'''
#append test
t1img_features,t1img_name=image_feature('/Users/terencemoriarty/Desktop/Covid19-dataset/test/Covid')
t2img_features,t2img_name=image_feature('/Users/terencemoriarty/Desktop/Covid19-dataset/test/Normal')
t3img_features,t3img_name=image_feature('/Users/terencemoriarty/Desktop/Covid19-dataset/test/Viral Pneumonia')
teimg_features = t1img_features + t2img_features +  t3img_features
teimg_name = t1img_name + t2img_name +  t3img_name
'''

#Creating Clusters
k = 3 # normal, covid, and pneumonia
clusters = KMeans(k, random_state = 40)
clusters.fit(trimg_features)
image_cluster = pd.DataFrame(trimg_name,columns=['image'])
image_cluster["clusterid"] = clusters.labels_
pd.set_option('display.max_rows', None)
print(image_cluster)