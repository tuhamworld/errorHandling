#  Using Try Except to handle error in Python

x = 50
y = 0
try:
    result = x/y
    print(result)

except:
    print('This is exactly where an issue occurs')
