
"""
Task 1
String manipulation
Write a Python program to get a string made of the first 2 and the
last 2 chars from a given string. If the string length
 is less than 2, return instead of the empty string.
"""
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('helloworld'))

#Sample String: 'my'

def sample_string(str):
  if len(str) > 2:
    return ''
  return 'mmymy'
print(sample_string('my'))


# Ssmple String: 'x'

def string(str):
  if len(str) < 3:
    return ''
print(string('x'))

# Task 2 The valid phone number program.
print('Enter your phone number:')
print('The number should be no larger and no less than 10 digits.')
phone = input()
if phone == str or len(phone)<10 or len(phone)>10:
  print("Wrong entry, enter numbers.")
else:
  print("Thanks for your number:" + phone)



#Task 3
"""
name = 'volodymyr'
print('Enter your name:')
input()
if name != str:
  print('please use leters.')
elif name == 'uppercase':
  print('Try agen.')
else:
  print('Hello' + name + 'we happy to see you.')
"""


