from keras.callbacks import ModelCheckpoint

import yugioh_data
import yugioh_model

train, val, test = yugioh_data.load_data()

train_x, train_y = yugioh_model.preprocess_data(train)
val_x, val_y = yugioh_model.preprocess_data(val)
test_x, test_y = yugioh_model.preprocess_data(test)

model = yugioh_model.get_model()

weights_path = 'model/weights.h5'

model.fit(x=train_x, y=train_y, batch_size=32, epochs=10, verbose=1,
        callbacks=[ModelCheckpoint(weights_path)],
        validation_data=(val_x, val_y))
