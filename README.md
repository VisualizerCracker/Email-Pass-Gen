# Email-Pass-Gen
# About.

*This is an Email/Pass Generator to execute the file you need to have python downloaded the latest version and the pip's installed.

# **Example**:

-*This is the Email Generator.*


~~~
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
        
email_gen()
~~~


-*This is the Pass Generator*



~~~
import random
import string

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

pass_gen()
~~~
    



>Installation
### pip install string
### pip install random
