
senha = 'AAA'
x = 32

while x <= 126:
    y = 32
    
    while y <= 126:
        z = 32
        
        while z <= 126:

            print(f'{chr(x)}  {chr(y)}  {chr(z)}')
            if (x + y + z) == senha:
                print(f'A senha é {senha}')
                break
            z += 1

        print(f'{chr(x)}  {chr(y)}  {chr(z)}')
        y += 1

    print(f'{chr(x)}  {chr(y)}  {chr(z)}')
    x += 1

print('fim')