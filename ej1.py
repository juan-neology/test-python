__author__ = 'juan'

print('HW', '2')
condition = 1
while condition < 10:
    print(condition)
    # condition = condition +1
    '''
    comentarios multiples
    '''
    condition += 1

cuadrados = [1, 4, 5, 10]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print cuadrados
#print cuadrados[1]
#print letras
#print cuadrados[:]
letras[2:5] = ['C', 'D', 'E']
#x = int(input)
end = ''


def fib(n):
    """

    :param n:
    """
    a, b = 0, 1
    while a < n:
        print (a)
        a, b = b, a + b


print()

fib(2000)

print('end')