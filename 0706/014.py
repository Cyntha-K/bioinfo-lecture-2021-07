word = input('word?')

if word.isdigit(): 
    result = 'digit'
elif word.isalpha():
    result = 'alphabet'
else:
    result = 'none'

print(result)

