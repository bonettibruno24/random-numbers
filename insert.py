import pandas as pd
import os 

 

numbers = [33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26, 0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10,  5, 24, 16]


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

"""
 Busca o último dígito de um número inteiro inserido, com valores e posição incluidos nas variavéis.
    Nos ternários eu verifico para pegar previus_position e later_position do numero.

"""            

def get_last_digit(valor):
    return int(str(valor)[-1])

numero = get_valid_numbers("Digite um número: ")
number1 = get_valid_numbers("Digite o segundo numero: ")
number2 = get_valid_numbers("Digite o terceiro numero: ")
    

last_digit_insert = get_last_digit(numero)
last_digit_insert1 = get_last_digit(number1)
last_digit_insert2= get_last_digit(number2)

position_array_index = numbers.index(number2)

previous_position = numbers[position_array_index - 1] if position_array_index > 0 else numbers[-1]
later_position = numbers[position_array_index + 1] if position_array_index < len(numbers) -1 else numbers[0]
algarism_previus = get_last_digit(previous_position)
algarism_later = get_last_digit(later_position)
# print(f"posterior algarismo = {algarism_previus} & ultimo alg= {algarism_later}")

# print(f"posição iin array {position_array_index}, numero anterior: : {previous_position}, numero posterior: : {later_position}")

# print(f"n1= {last_digit_insert} & n2 = {last_digit_insert1} & n3 = {last_digit_insert2}")

def veirify_algarism():
    if last_digit_insert & last_digit_insert1 == last_digit_insert2:
        print(last_digit_insert2, "OK")
        return True 
    elif algarism_previus & algarism_later == last_digit_insert2 & last_digit_insert1 & last_digit_insert:
        print(f"{numero}, {number1} ,{number2} Ok")
        return True
    else:
        print(f"{numero}, {number1} ,{number2} X")
        return False


df = pd.DataFrame({
    'Valor 1': [numero],
    'Valor 2': [number1],
    'Valor 3': [number2],
    'Resultado' : [None],
    'Probabilidade': [None]
    })

from openpyxl import load_workbook, Workbook
from openpyxl.styles import PatternFill
path = '/home/twobe/Documentos/projeto1/final.xlsx'



# green = PatternFill("solid", fgColor="DDDDDD")
# blue = PatternFill(fill_type='solid', start_color='00FF00', end_color='00FF00')

# if veirify_algarism():
#     WS['D2'] = "Ok"

# else:
#     WS['D2'] = "X"




result_verify_algarism = veirify_algarism()

if result_verify_algarism == True:
    df['Resultado'] = "OK"
    df['Resultado'].fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
else:
    df['Resultado'].fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    df['Resultado'] = "X"
    


def highligh_cells(value):
    if value == "OK":
        return ['background-color: yellow']
    else:
        return 'red'



# if last_digit_insert & last_digit_insert1 == last_digit_insert2:
#     print(f"{last_digit_insert2} Ok")  
   
# elif algarism_previus & algarism_later == last_digit_insert2 & last_digit_insert1 & last_digit_insert:
#     print(f"{numero}, {number1} ,{number2} Ok") 
# else:
#     print(f"{numero}, {number1} ,{number2} X") 

# print(chack_algarism())

# print(df)


"""
P(A) = EventosFavoraveis/EventosPossiveis
Probabilidade: verificar na tabela num1 e num2 inseridos 
"""

# print(veirify_algarism())
    

def calculate_probability(num, num1, num2):
    filter = df_ler[(df_ler['Valor 1'])]
    print("teste", filter)

# print(df_ler.columns)
# print("col 1 ", df_ler['Valor 1'])
# print("col 2 ",df_ler['Valor 2'])
# print("col 3 ",df_ler['Valor 3'])
if os.path.exists(path):
    df_existente = pd.read_excel(path, sheet_name='Sheet1')
    df_atualizado = pd.concat([df_existente, df], ignore_index=True)

    with pd.ExcelWriter(path, engine='openpyxl', mode= 'a', if_sheet_exists='replace') as writer:
        df_atualizado.to_excel(writer, sheet_name='Sheet1', index=False)
        print(f"Dados inseridos com sucesso! {path}")
else:
    df.to_excel(path, index=False)
    print(f"Dados inseridos com sucesso! {path}")

wb = load_workbook(path)
ws = wb.active

for cell in ws[1]:
    if cell.internal_value == 'Resultado':
        col_index = cell.col_idx
        break
for cells_in_row in ws.iter_rows(min_row=0,
                                min_col=col_index,
                                max_col=col_index):
    print(cells_in_row)
    if cells_in_row[0].internal_value == 'Resultado':
        cells_in_row[0].fill = PatternFill(patternType='solid', fgColor='000f00')

wb.save(path)
