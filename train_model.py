from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

import yugioh_data
import yugioh_model

train, val, test = yugioh_data.load_data()

train_x, train_y = yugioh_model.preprocess_data(train)
val_x, val_y = yugioh_model.preprocess_data(val)
test_x, test_y = yugioh_model.preprocess_data(test)

model = yugioh_model.get_model()

weights_path = 'model/weights.h5'

history = model.fit(x=train_x, y=train_y, batch_size=32, epochs=80, verbose=1,
        callbacks=[ModelCheckpoint(weights_path)],
        validation_data=(val_x, val_y))

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig('acc.png', bbox_inches='tight')
plt.clf()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig('loss.png', bbox_inches='tight')
plt.clf()

print(model.test_on_batch(test_x, test_y))
