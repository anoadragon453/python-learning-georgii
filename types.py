# String
"Andrew \"Eden\" Morgan"
    is the same as
'Andrew "Eden" Morgan'

# int
32

# float (has a decimal)
32.5

# Lists (Arrays)
my_list = [1, 2, 3, "a", "b", "c", [4, 5, 6]]

my_list[0] # 1
my_list[3] # "a"
my_list[100] # error
my_list[-1] # the last thing in the list!
my_list[-2] # the second last thing in the list!

# Variables
bla = 5

agesList <-- C++

thisIsMyVariable
thisismyvariable

classthatdoessomethingveryimportant <- hard to read
class_that_does_something_very_important <- easier to read # Python
    ^-- Called "snake case"
classThatDoesSomethingVeryImportant <- easier to read # C++


# Dictionary
ages_dictionary = {
    "Andrew Morgan": 22,
    "Georgii Logashenko": 23,
    "Bob": 40,
}

some_other_dictionary = {
    [1,2,3]: "bla",
    22: "Andrew Morgan",
    23: "Georgii Logashenko",
    22: "Andrew Morgan2", # error
}

some_other_dictionary[22] # Which one to pull out???

# Nice!
ages_dictionary["Andrew Morgan"] # 22

ages_list = [
    "Georgii Logashenko", 23, # 0, 1
    "Georgii Logashenko", 23, # 2, 3
    "Georgii Logashenko", 23, # 4, 5
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Andrew Morgan", 22,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
    "Georgii Logashenko", 23,
]

# Horrible!
ages_list[17] = 22

# Searching through a list. Slow!
# for `some_new_variable` in `the_thing_were_searching_through`:
for thing in ages_list:
    if thing == "Andrew Morgan":
        return thing + 1

# Tuples
var_one, var_two, var_three = (1, 2, 3)
var_one # 1
var_two # 2
var_three # 3


ages_list <--

# default argument values example

def create_user(
    username, # required
    password, # required
    avatar="", # optional
    bio="", # optional
    relationship_status="", # optional, default ""
    religion="christianity", # optional, default "christianity"
):
    return

create_user("bob", "ilikecheetos", bio="I REAAAAALLY LIKE CHEETOS DON'T HACK ME!")