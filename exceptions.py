# Raises a ValueError
try:
    int("hjkasd%%77")
except:
    print("The above code did not work!")

print("This code ran!")

"""
Somewhere in int(input):

process_input(input)
if cant_process:
    raise ValueError("invalid literal for int() with base 10", input)

"""
