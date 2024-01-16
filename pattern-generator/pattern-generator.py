import sys

n = int(input('Enter value of a natural number: '))
x = ''
m = n

if n <= 0:
   x = 'Invalid number. Given value will not create a pattern'
   sys.exit(x)

while n > 0:
   x+= (n * ' * ') + '\n'
   n -= 1

end = 'Pattern made from entered natural number ({0})'

print(x, end.format(m))


input("Press ENTER to exit")
