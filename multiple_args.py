def print_msg(msg, error="No error", *args, **kwargs):
    print("Log:"+error+":" + msg)
    print(args)
    print(kwargs)

print_msg("This will be logged","File not found", "-13", "-1", "0", key1="1", key2="2", key3="25")

# * ==> return tuple
# ** ==> returns dictionary --->define a key while passing arguments


