import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.utils import np_utils
from keras.layers import add,Flatten,Input,Dense,Conv1D,GlobalAveragePooling1D,Activation,MaxPool1D,Dropout,LSTM,BatchNormalization,GRU
from keras.models import Sequential,Model
import pickle
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint,LearningRateScheduler,ReduceLROnPlateau

from zipfile import ZipFile
import urllib.request
import os
import json
from pandas._libs.period import extract_ordinals
from io import open

LING10_TRAIN_LARGE = "Ling10-trainlarge"
LING10_TRAIN_MEDIUM = "Ling10-trainmedium"
LING10_TRAIN_SMALL = "Ling10-trainsmall"

DATA_DIR = os.path.join(os.getcwd(),"data_dir")

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

DATA_FILE = os.path.join(DATA_DIR,LING10_TRAIN_LARGE+".zip")

#DONWLOAD THE DATA IF IT DOESN'T EXIST
if not os.path.exists(DATA_FILE):
    urllib.request.urlretrieve("https://github.com/johnolafenwa/Ling10/releases/download/1.0.0/{}.zip".format(LING10_TRAIN_LARGE),DATA_FILE)


train_file = os.path.join(DATA_DIR,LING10_TRAIN_LARGE,"train_set.txt")
test_file = os.path.join(DATA_DIR,LING10_TRAIN_LARGE,"test_set.txt")
chars_map_file = os.path.join(DATA_DIR,LING10_TRAIN_LARGE,"chars.json")

#If any of the content doesn't exist, extract the zip file
if not os.path.exists(train_file) or not os.path.exists(test_file) or not os.path.exists(chars_map_file):
    extractor = ZipFile(DATA_FILE)
    extractor.extractall(DATA_DIR)
    extractor.close()

#READ THE DATA FILES

train_data = open(train_file,encoding="utf-8").read()
test_data = open(test_file,encoding="utf-8").read()
char_map_data = open(chars_map_file)

#Load the char map
char_map = json.load(char_map_data)
char_to_idx = char_map["char_to_idx"]


#Split the train and test into lines
train_data = train_data.splitlines()
test_data = test_data.splitlines()

#Create arrays to store the integer version of the data
train_sentences = []
train_classes = []

test_sentences = []
test_classes = []

for _, line in enumerate(train_data):
    sen, lang_class = line.split("\t")
    sen = [char_to_idx[c] for c in sen]
    train_sentences.append(sen)
    train_classes.append(lang_class)

for _, line in enumerate(test_data):
    sen, lang_class = line.split("\t")
    sen = [char_to_idx[c] for c in sen]
    test_sentences.append(sen)
    test_classes.append(lang_class)


#Pad the sequences to have a fixed length of 100
train_data = pad_sequences(train_sentences,maxlen=100)
train_data = np.array(train_data)

test_data = pad_sequences(test_sentences,maxlen=100)
test_data = np.array(test_data)


#Convert the integer language classes to one-hot encoding
train_y = np_utils.to_categorical(train_classes,10)
test_y = np_utils.to_categorical(test_classes,10)

#Reshape the sequences to have shape (num_of_sequence, sequence_length, 1)
train_x = np.reshape(train_data,(train_data.shape[0],train_data.shape[1],1))
test_x = np.reshape(test_data,(test_data.shape[0],test_data.shape[1],1))

print(train_x.shape)
print(test_x.shape)

print(train_y.shape)
print(test_y.shape)


#DEFINE THE MODEL
model = Sequential()
model.add(GRU(256,activation="relu",input_shape=train_x.shape[1:],return_sequences=True))
model.add(GRU(256,activation="relu"))
model.add(Dense(10,activation="softmax"))

#Compile the model
model.compile(optimizer=Adam(0.001),loss="categorical_crossentropy",metrics=["mse","accuracy"])

#Print full summary of the model
model.summary()

#Create Directory to Store Model for later inference
save_direc = os.path.join(os.getcwd(), 'lang_saved_modelsbest')

model_name = 'model.{epoch:02d}-{val_loss:.2f}-{val_acc:.2f}.hdf5'
if not os.path.isdir(save_direc):
    os.makedirs(save_direc)
filepath = os.path.join(save_direc, model_name)

checkpoint = ModelCheckpoint(filepath=filepath,monitor="val_acc",save_best_only=True)

model.fit(x=train_x,y=train_y,batch_size=128,epochs=200,validation_data=[test_x,test_y],callbacks=[checkpoint])
print("Training Completed")





