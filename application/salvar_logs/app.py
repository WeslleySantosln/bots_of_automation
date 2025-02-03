import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


data = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = data.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  
    keras.layers.Dense(128, activation='relu'),  
    keras.layers.Dense(10, activation='softmax')  
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Acurácia no teste: {test_acc:.4f}')


def predict_sample(index):
    plt.imshow(x_test[index], cmap=plt.cm.binary)
    plt.show()
    prediction = model.predict(np.expand_dims(x_test[index], axis=0))
    print(f'Previsão: {np.argmax(prediction)}')


predict_sample(0)