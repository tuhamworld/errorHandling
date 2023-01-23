#  Using Try Else

# import os

# try:
#     os.remove('demofile.pdf')

# except FileNotFoundError as error:
#     # print(error)
#     print('unaccessible file')
# else:
#     print('You do not have access to this file')

######################################### -----------------########################################


import os

try:
    os.remove('demofile.pdf')
except FileNotFoundError as error:
    # print(error)
    print('unaccessible file')
else:
    print('You do not have access to this file')
finally:
    print('As you wishes')
