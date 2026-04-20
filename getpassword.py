import json
import os
import random
import string 
from getpass import getpass

FILE = "passwords.json"

def load_data():
    if not os.path.exists(FILE):
         return {}
    try: 
       with open(FILE) as f:
          return json.load(f)

    except: 
       return {} 

   def save_data(data):
       with open(FILE, "w") as f:
          json.dump(data,f,indent=4)

  def generate_password(length=12):
       chars= string.ascii_letters + \
           string.digits + "!@#$%^&*"
       return ''.join(random.choice(chars)
           for _ in range(length))

   def add_password():
       data = load_data()
       site = input("Website/App name: ").strip()
       username = input("Username/Email: ").strip() 
       choice = input("1. Enter password " \ "\n2. Generate strong password: ")

       if choice == "2":
            pwd = generate_password()
           print(f"Generated Password: {pwd}")
       else:

