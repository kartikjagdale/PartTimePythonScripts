#In this tuto we will see that local variables and functiona variables are differnet despite of their name being same they dont collide each other

# Filename: func_local.py
x = 50
def func(x):
    #print('x is', x)
    x = 2
    print('Function X is ', x)
#End of Function 'func'
func(x)
print('Local X is', x)
