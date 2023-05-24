from tests.conftest import client


def test_register():
    """Test that user was registered"""
    response = client.post('/auth/register', json={
            "email": "email@gmail.com",
            "password": "password",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "John"
    })

    assert response.status_code == 201
