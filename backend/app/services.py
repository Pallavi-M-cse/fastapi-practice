from database import fake_users_db

def add_user(user_data:dict):
    fake_users_db.append(user_data)
    return user_data

def get_all_users():
    return fake_users_db