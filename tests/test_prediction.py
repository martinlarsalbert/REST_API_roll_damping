import pytest
import os
import numpy as np
import pandas as pd

import roll_damping
import server
from rolldecayestimators.polynom_estimator import Polynom


def test_make_prediction():

    file_path = r'../static/models/polynom_complex.sym'
    assert os.path.exists(file_path)

    inputs = {
        'beam':1.0,
        'T':0.1,
        'BK_L':0,
        'BK_B':0,
        'OG':0,
        'omega0_hat':0,
        'C_b':0.7,
        'A_0':0.97,
        'V':0,
        'phi_a':np.deg2rad(3)

    }

    result = roll_damping.make_prediction(file_path=file_path,  inputs=inputs)