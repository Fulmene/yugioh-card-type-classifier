import tkinter
import numpy as np

import yugioh_model
import yugioh_data

def output_result(model, entry, message):
    result = yugioh_model.predict(model, [entry.get()])
    card_type = yugioh_data.card_types[np.argmax(result)]
    message.configure(text='Monster: {:f}\nSpell: {:f}\nTrap: {:f}\nType: {:s}'.format(result[0][0], result[0][1], result[0][2], card_type))

model = yugioh_model.get_model()

weights_path = 'model/weights.h5'
model.load_weights(weights_path)

top = tkinter.Tk(className='yugioh card type classifier')

label = tkinter.Label(top, text='Card Name')
label.pack(side='top')

entry = tkinter.Entry(top, width=20)
entry.pack(side='top')

message = tkinter.Message(top, width=300, text='\n\n\n')
message.pack(side='top')

button = tkinter.Button(top, text='Predict', command=lambda: output_result(model, entry, message))
button.pack(side='top')

top.mainloop()
