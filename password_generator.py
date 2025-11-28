import random
import string 

print(" ------ PASSWORD GENERATOR ------")

length= int(input("Enter the password length: "))

Characters= string.ascii_letters+string.digits+string.punctuation

password="".join(random.choice(Characters) for i in range(length))

print("Your password is:", password)
                                                          