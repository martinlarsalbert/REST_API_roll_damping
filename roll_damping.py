"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules
from datetime import datetime
import os

# 3rd party modules
from flask import make_response, abort
import numpy as np

# My modules
from rolldecayestimators.polynom_estimator import Polynom

file_path = os.path.join(os.path.dirname(__file__),'static','models','polynom_complex.sym')
polynom = Polynom.load(file_path=file_path)
assert isinstance(polynom, Polynom)

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def predict(lpp, beam, T, BK_L, BK_B, OG, omega0_hat, C_b, A_0, V, phi_a):
    """
    This function responds to a request for /api/roll_damping
    To predict the roll damping of a ship.

    :param lpp:   ship perpendicular length m
    :return:      ship roll damping prediction
    """

    inputs = {
        'beam': beam/lpp,
        'T': T/lpp,
        'BK_L': BK_L/lpp,
        'BK_B': BK_B/lpp,
        'OG': OG/lpp,
        'omega0_hat': omega0_hat,
        'C_b': C_b,
        'A_0': A_0,
        'V': V/np.sqrt(lpp),
        'phi_a': phi_a,
    }
    damping = make_prediction(inputs=inputs)

    results = {
        'method':file_path,
        'B_e_hat':damping,
    }

    if lpp>0:
        results['lpp']=lpp

    # otherwise, nope, not found
    else:
        abort(
            404, "Bad value for lpp: {lpp}".format(lpp=lpp)
        )


    return results


def make_prediction(inputs:dict):

    result = polynom.predict(X=inputs)
    return result

