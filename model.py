import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

model = Sequential() # 레이어를 선형으로 연결
model.add(SimpleRNN(units=32, input_shape=(1, 5), activation='relu'))
model.add(Dense(8, activation='relu')) 
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam', metrics=['acc'])
