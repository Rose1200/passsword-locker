#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import random  

def cr_user(user_name, password):
    """
    Function to create a new user
    """
    new_user = User(user_name, password)
    return new_user



