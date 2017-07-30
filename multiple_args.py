def print_msg(msg, error="No error", *kwargs):
    print("Log:"+error+":" + msg)
    print(kwargs)

print_msg("This will be logged","File not found", "1", "2", "12", "213", "252")

# * ==> return tuple
# ** ==> returns dictionary --->define a key while passing arguments


