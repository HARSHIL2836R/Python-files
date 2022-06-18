# Calculator version 5.0 Alpha

# Title
print("\nIn this calculator only one operator separated by a blank space can be used.")

def check_operator(x, i):
    global a
    global b
    a = int(x[i-2])
    b = int(x[i])
    if x[i-1] == "+":
        return a + b
    if x[i-1] == "-":
        return sum(a,b)
    if x[i-1] == "*" or "x":
        return (int(a) * int(b))
    if x[i-1] == "/" or "%":
        return a * 1/b
    else:
        pass
    
def calc():
    ex = '1 + 2'
    if ex.find('+') != -1:
        i = ex.index("+")
        el = ex.split()
        el.insert(i, check_operator(el, i))
        el.pop(i-1)
        el.remove(str(a))
        el.remove(str(b)) 
calc()
