# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from keras.models import load_model
import numpy as np


class CartpoleRlRemoteAgent(object):

    def __init__(self):
        self.model = load_model('Cartpole-rl-remote.h5')

    def predict(self, state):
        return np.argmax(self.model.predict(state)[0])
