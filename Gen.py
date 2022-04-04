import random
import string

def email_gen():
    chars_after_at = int(input("Enter the chars here :"))
    if(chars_after_at < 4 or chars_after_at > 50): # here yo can only put the chars from 4 to 50 to be generated if less than 4 it would not work
        print("Please enter between 4 and 20 chars maximum !!")
        exit()
    else:
        letters_list = [string.hexdigits, string.ascii_lowercase, string.ascii_uppercase]
        letters_list_to_str = "".join(letters_list)
        email_format = "@gmail.com"
        email_generated = "".join(random.choices(letters_list_to_str, k=chars_after_at)) + email_format
        print(email_generated)
    pass

def pass_gen():
    chars_after_at = int(input("Enter the chars here :"))
    if(chars_after_at < 4 or chars_after_at > 50): # here yo can only put the chars from 4 to 50 to be generated if less than 4 it would not work
        print("Please enter between 4 and 20 chars maximum !!")
        exit()
    else:
        letters_list = [string.hexdigits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.printable,]
        letters_list_to_str = "".join(letters_list)
        pass_format = ""
        pass_generated = "".join(random.choices(letters_list_to_str, k=chars_after_at)) + pass_format
        print(pass_generated)

email_gen()
pass_gen()

