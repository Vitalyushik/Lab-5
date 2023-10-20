a = ord('а')
alphabet = ''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] +[chr(i) for i in range(a+6,a+32)])
upper_alphabet = alphabet.upper()
output = ''
x  = 1
while x > 0:
    phrase = input('Введите текст кириллицей: ')
    if phrase in ' ':
        print('Введено пустое поле, попробуйте снова')
    else:
        x -= 1
        y = 1
        while y > 0:
            type = int(input('Введите 1 для шифровки или -1 для расшифровки: '))
            if type != 1 and type != (-1):
                print('Введено неправльное значение, попробуйте 1 или -1')
            else:
                y -= 1
                while True:
                    try:
                        step = int(input('Введите шаг шифроки: '))
                        break
                    except ValueError:
                        print('Введено неправильное значение, введите число')
                for i in range(len(phrase)):
                    try:
                        index = alphabet.index(phrase[i])
                        output += alphabet[(index+step*type)%33]
                    except ValueError:
                        try:
                            index = upper_alphabet.index(phrase[i])
                            output += upper_alphabet[(index+step*type)%33]
                        except ValueError:
                            output += phrase[i]
                
print(output)

   