import pytest
import server

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

def test_empty_db(client):
    """Start with a blank database."""

    response = client.get('/')
    assert response.status_code == 200
