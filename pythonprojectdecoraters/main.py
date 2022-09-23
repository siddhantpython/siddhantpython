#decoraters :using decoraters we can add the extra features in existing function.
def div(a,b):
    print(a/b)

def smart_div(func):  #here func smart_div() is decorater
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(3,6)