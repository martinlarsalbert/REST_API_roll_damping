import pytest
import server
import numpy as np
import json
import os



@pytest.fixture
def client():
    #db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    application = server.app.app
    application.config['TESTING'] = True

    with application.test_client() as client:
        #with server.app.app_context():
        #    server.init_db()

        yield client

    #os.close(db_fd)
    #os.unlink(server.app.config['DATABASE'])

def test_api_alive(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_damping(client):
    response = client.get('/api/roll_damping?lpp=100&beam=10&T=2&BK_L=0&BK_B=0&OG=0&omega0_hat=0.1&C_b=0.7&A_0=0.97&V=10&phi_a=0.1')
    assert response.status_code == 200
    assert 'B_e_hat' in response.json

def test_post_damping(client):

    data = {
        'lpp':100,
        'beam': 1.0,
        'T': 0.1,
        'BK_L': 0,
        'BK_B': 0,
        'OG': 0,
        'omega0_hat': 0,
        'C_b': 0.7,
        'A_0': 0.97,
        'V': 0,
        'phi_a': np.deg2rad(3)

    }
    inputs=[data,data]

    response = client.post('/api/roll_damping',
        data = json.dumps(inputs),
        content_type = 'application/json')

    assert response.status_code == 200
    outputs = response.json
    'B_e_hat' in outputs[0]