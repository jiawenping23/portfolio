# o365_tools.py
# 模拟 Office 365 管理脚本

def create_user(username):
    print(f"Creating user {username}...")
    # 模拟创建用户
    return True

def check_mailbox(username):
    print(f"Checking mailbox for {username}...")
    # 模拟检查
    return True

def main():
    user = "testuser"
    if create_user(user):
        print(f"User {user} created successfully")
    if check_mailbox(user):
        print(f"Mailbox for {user} is OK")

if __name__ == "__main__":
    main()
