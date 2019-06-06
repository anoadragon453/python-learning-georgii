# We are a bouncer at a club. And we only want to let in people
# who are 18 years or older
print("What's ur gender ('male' or 'female')?!")
gender = input("Gender: ")

if gender == "male":
    print("Your age, nugget!?")
    age = int(input())
    if age >= 18:
        print("Welcome Sir, you may proceed")
    elif age >= 16:
        print("I'm not supposed to do this, " "but you look cool. Come in!")
    else:
        print("Get the HELL OUT'A 'ERE!!!")
elif gender == "female":
    print("What is your age, Miss?")
    age = int(input())
    if age > 14:
        print("Welcome in, Miss!")
    else:
        print("Where are your parents, kid?")
else:
    print("Never heard of that...")


"""
if a == b:
    pass
elif a == c:
    pass
elif a == d:
    pass
elif a == e:
    pass
else:
    pass
"""
