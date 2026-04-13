# user_registration_service.py

from dataclasses import dataclass
from typing import Optional, Dict
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---- Domain Model ---- #
@dataclass
class User:
    username: str
    email: str


# ---- Exceptions ---- #
class ValidationError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


# ---- Repository (In-memory for this example) ---- #
class UserRepository:
    def __init__(self):
        self._users: Dict[str, User] = {}

    def find_by_username(self, username: str) -> Optional[User]:
        return self._users.get(username)

    def save(self, user: User) -> None:
        if self.find_by_username(user.username):
            raise UserAlreadyExistsError(f"User '{user.username}' already exists.")
        self._users[user.username] = user
        logger.info(f"User '{user.username}' saved successfully.")


# ---- Service Layer ---- #
class UserService:
    EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, username: str, email: str) -> User:
        self._validate(username, email)
        user = User(username=username, email=email)
        self.repository.save(user)
        return user

    def _validate(self, username: str, email: str):
        if not username or len(username) < 3:
            raise ValidationError("Username must be at least 3 characters long.")
        if not re.match(self.EMAIL_REGEX, email):
            raise ValidationError("Invalid email format.")


# ---- Entry Point (like controller) ---- #
def main():
    repo = UserRepository()
    service = UserService(repo)

    try:
        user1 = service.register_user("brianbett", "brian@example.com")
        print(f"Registered user: {user1}")
        
        user2 = service.register_user("brianbett", "duplicate@example.com")  # This should raise an error
    except ValidationError as ve:
        logger.error(f"Validation failed: {ve}")
    except UserAlreadyExistsError as uae:
        logger.error(f"Registration failed: {uae}")
    except Exception as e:
        logger.exception("Unexpected error occurred")


if __name__ == "__main__":
    main()

