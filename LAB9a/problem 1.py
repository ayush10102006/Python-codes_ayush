def fun():
    print("This is function fun()")

def disp():
    print("This is function disp()")

def msg():
    print("This is function msg()")
function_list = [fun, disp, msg]
for f in function_list:
    f()
