n = int(input('Enter value of a natural number: '))
x = ''
#Saving the natural number in different variable
m = n 
end = 'Pattern made from entered natural number ({0})'

if n <= 0:
    x = 'Invalid number. Given value will not create a pattern'
    print(x)
else:
    while n > 0:
        x+= (n * ' * ') + '\n'
        n -= 1
    print(x, end.format(m))

input("Press ENTER to exit")
