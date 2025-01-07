import pandas as pd
import os 
 

numbers = [33 , 1 , 20 , 14 , 31 , 9 , 22 , 18 , 29 , 7 , 28 , 12 , 35 , 3 , 26 , 0, 32 , 15 , 19 , 4 , 21 , 2 , 25 , 17 , 34 , 6 , 27 , 13 , 36 , 11 , 30 , 18 , 29 , 10 ,  5 , 24 , 16 ]

def get_valid_numbers(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number in numbers:
                return number
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Número inválido. Tente novamente.")

def get_last_algarism(valor):
    return int(str(valor)[-1])

numero = get_valid_numbers("Digite um número: ")
numbero1 = get_valid_numbers("Digite o segundo numero: ")
numero2 = get_valid_numbers("Digite o terceiro numero: ")
    

ultimo_numero = get_last_algarism(numero)
ultimo_numero1 = get_last_algarism(numbero1)
ultimo_numero2 = get_last_algarism(numero2)

position = numbers.index(numero2)

previous_position = numbers[position - 1] if position > 0 else numbers[-1]
later_position = numbers[position + 1] if position < len(numbers) -1 else numbers[0]
algarism_previus = get_last_algarism(previous_position)
algarism_later = get_last_algarism(later_position)
print(f"posterior algarismo = {algarism_previus} & ultimo alg= {algarism_later}")

print(position, later_position, previous_position)
print(f"n1= {ultimo_numero} & n2 = {ultimo_numero1}")

df = pd.DataFrame({'Valor 1': [numero], 'Valor 2': [numbero1], 'Valor 3': [numero2]})
path = '/home/twobe/Documentos/projeto1/final.xlsx'

if os.path.exists(path):
    df_existente = pd.read_excel(path, sheet_name='Sheet1')
    df_atualizado = pd.concat([df_existente, df], ignore_index=True)

    with pd.ExcelWriter(path, engine='openpyxl', mode= 'a', if_sheet_exists='replace') as writer:
        df_atualizado.to_excel(writer, sheet_name='Sheet1', index=False)
        print(f"Dados inseridos com sucesso! {path}")
else:
    df.to_excel(path, index=False)
    print(f"Dados inseridos com sucesso! {path}")

