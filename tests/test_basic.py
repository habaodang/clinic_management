import pytest
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_app_import():
    """Test that the app module can be imported"""
    from app import create_app
    assert create_app is not None

@pytest.fixture
def app():
    """Create application for testing"""
    # Set test environment variables
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_USER'] = 'test_user'
    os.environ['DB_PASSWORD'] = 'test_pass'
    os.environ['DB_NAME'] = 'test_db'
    os.environ['SECRET_KEY'] = 'test_secret'
    
    from app import create_app
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    return app

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'clinic_management'

def test_app_creation(app):
    """Test app creation"""
    assert app is not None
    assert app.config['TESTING'] is True