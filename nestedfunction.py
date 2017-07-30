#scope of function
"""
def hello_world():
    def hello_world2():
      print("inside hello world2")
print("inside hello world")
 hello_world2()


hello_world()

"""

def print_msg(msg, error="No Error"):
    print("Log :"+error+":" + msg)

print_msg("File not found", "this will be logged")
