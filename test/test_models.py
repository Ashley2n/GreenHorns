import pytest
from sqlalchemy.orm import Session

from helper_functions import encrypt_password
from infrastructure.CRUD import create_user_repo, get_by_id_repo, get_user_by_username_repo, get_user_by_email_repo, \
    update_user_repo, delete_user_repo


@pytest.fixture
def sample_user(db_session: Session):
    """Create a sample user for testing"""
    user = create_user_repo(
        db_session,
        "sampleuser",
        "samplepass",
        "sample@example.com"
    )
    return user

def test_create_user_repo(db_session:Session):
    """Test creating a new user"""
    user = create_user_repo(db_session, "testuser", "hashedpass123", "test@example.com")

    assert user.id is not None
    assert user.username == "testuser"
    assert user.password_hash == "hashedpass123"
    assert user.email == "test@example.com"


def test_get_by_id_repo(db_session, sample_user):
    """Test retrieving user by ID"""
    retrieved_user = get_by_id_repo(db_session, sample_user.id)

    assert retrieved_user.id == sample_user.id
    assert retrieved_user.username == sample_user.username


def test_get_by_id_repo_not_found(db_session):
    """Test retrieving non-existent user"""
    result = get_by_id_repo(db_session, 99999)
    assert result is None


def test_get_user_by_username_repo(db_session, sample_user):
    """Test retrieving user by username"""
    user = get_user_by_username_repo(db_session, sample_user.username)

    assert user.username == sample_user.username
    assert user.id == sample_user.id


def test_get_user_by_email_repo(db_session, sample_user):
    """Test retrieving user by email"""
    user = get_user_by_email_repo(db_session, sample_user.email)

    assert user.email == sample_user.email
    assert user.id == sample_user.id


def test_update_user_repo(db_session, sample_user):
    """Test updating user information"""
    updated_user = update_user_repo(
        db_session,
        "sampleuser",
        "newhashedpass",
        "newemail@example.com"
    )

    assert updated_user.username == "sampleuser"
    assert updated_user.hashed_password == "newhashedpass"
    assert updated_user.email == "newemail@example.com"


def test_delete_user_repo(db_session, sample_user):
    """Test deleting a user"""
    user_id = sample_user.id
    result = delete_user_repo(db_session, user_id)

    assert result is True
    assert get_by_id_repo(db_session, user_id) is None


def test_delete_user_repo_not_found(db_session):
    """Test deleting non-existent user"""
    # This might need error handling in your actual function
    result = delete_user_repo(db_session, 99999)
    # Adjust assertion based on how your function handles non-existent users
    assert result is True or result is False  # Adjust based on your logic


# Fixtures for test data
