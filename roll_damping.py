"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}

def predict(lpp):
    """
    This function responds to a request for /api/roll_damping
    To predict the roll damping of a ship.

    :param lpp:   ship perpendicular length m
    :return:      ship roll damping prediction
    """

    damping = {}

    if lpp>0:
        damping['lpp']=lpp

    # otherwise, nope, not found
    else:
        abort(
            404, "Bad value for lpp: {lpp}".format(lpp=lpp)
        )


    return damping



