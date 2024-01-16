
def mult(a,b):
    return a*b
print(mult(3,3))

def addition(a,b):
    return a+b

def mult_par_add(a,b):
    res=0
    for i in range(b):
        res=addition(a,res)
    return res
print(mult_par_add(6,2))