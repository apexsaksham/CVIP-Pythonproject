import random
import string
print("Welcome to our Random password generator")
def main():

    length=int(input("enter the length of password you want: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine=lowerD+upperD+digitD+symbolsD
    x=random.sample(combine,length)
    password="".join(x)
    print("Your password:",password)
    main()
main()