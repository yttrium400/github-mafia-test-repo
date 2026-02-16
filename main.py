
from utils.logger import log
from utils.math import calculate_percentage
from models.user import User

def main():
    log("Starting application...")
    user = User("Alice", 85, 100)
    print(f"User {user.name} score: {calculate_percentage(user.score, user.total)}%")

if __name__ == "__main__":
    main()
