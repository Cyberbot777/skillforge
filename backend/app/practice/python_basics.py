# app/practice/python_basics.py

def get_home():
    return {
        "message": "Welcome to SkillForge backend!",
        "status": 200
    }

if __name__ == "__main__":
    response = get_home()
    print(response)
