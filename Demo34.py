def func34(par1, par2, *args):
    print(f"fix para1={par1}, para2={par2}")
    for arg in args:
        print(f"*dynamic part={arg}")


func34("zero", "argument")
func34("1", "parameter", "hello world")
func34("multiple", "any number", 500, 3.14, "hi", "welcome")
list1 = [500, 3.14, "hi", "welcome"]
func34("put", 'list', list1)
func34("expand", "list", *list1)