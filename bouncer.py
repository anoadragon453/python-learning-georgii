def get_rid_of_all_spaces_in_iterable(input_iter):
    """Remove spaces from a given iterable
    
    It does this by iterating through the input variable, checking if any of
    the items is a space, and if it is, preventing it from being copied to a
    new variable which is then returned.
    """  # docstring = documentation string
    # input = "2 1"
    # Remove all the spaces in input
    # ? :D
    # for some_new_variable in the_thing_we're_searching_through:

    # user_input = "2 1"
    # temp = ""
    #
    temp = ""
    for not_space in input_iter:
        if not_space != " ":
            # concatenation: combining two or more things
            # concatenating two strings: temp and not_space
            # temp += not_space ( temp = temp + not_space )
            temp += not_space
    return temp


# We are a bouncer at a club. And we only want to let in people
# who are 18 years or older
print("What's ur gender ('male' or 'female')?!")
gender = input("Gender: ")

if gender == "male":
    print("Your age, nugget!?")
    try:
        user_input = input()
        user_input = get_rid_of_all_spaces_in_iterable(user_input)
        age = int(user_input)
    except ValueError:
        print("That didn't look like a number")
        age = 0
    except:
        print("Something went wrong")
        age = 0

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


# functions can raise exceptions
# see exceptions.py

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
