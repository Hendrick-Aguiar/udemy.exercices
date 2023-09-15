# conversor fahrenheit to celsius



f = int(input('insira a temperatura em fahrenheit: '))

c = (f-32)*5/9

if c < 48:
    print('aguarde mais um pouco')
elif c in range(49, 53):
    print('mal passada')




#print('a temperatura em celsius:' , c)

#input()
