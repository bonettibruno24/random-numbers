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
print(f"algarismo do posterior = {algarism_previus} & ultimo alg= {algarism_later}")

print(f"posição iin array {position_array_index}, numero anterior: : {previous_position}, numero posterior: : {later_position}")

print(f"n1= {last_digit_insert} & n2 = {last_digit_insert1} & n3 = {last_digit_insert2}")

df = pd.DataFrame({
    'Valor 1': [numero],
    'Valor 2': [number1],
    'Valor 3': [number2],
    'Resultado' : [None],
    'Probabilidade': [None]
    })

def veirify_algarism():
    current_set = {numero, number1, number2}
    required_set = {0, 26, 32}
    if  last_digit_insert2 == last_digit_insert and last_digit_insert1:
        print(last_digit_insert2, "OK")
        return True 
    elif last_digit_insert2 == algarism_previus and algarism_later:
        print(f"{numero}, {number1} ,{number2} OK")
        return True
    elif required_set == current_set:
        print(f"{numero}, {number1} ,{number2} OK")
        return True
    else:
        print(f"{numero}, {number1} ,{number2} X")
        return False

print("teste function",veirify_algarism())


from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Alignment
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
    
# print(df)
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
wb.save(path)

green_fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
red_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
for cell in ws[1]:
    if cell.value == 'Resultado':
        col_index = cell.col_idx
        break

for row in ws.iter_rows(min_row=2, min_col=col_index, max_col=col_index):
    for cell in row:
        cell.alignment = Alignment(horizontal='center', vertical='center')
        if cell.value == 'OK':
            cell.fill = green_fill
        elif cell.value == 'X':
            cell.fill = red_fill
wb.save(path)
"""
P(A) = EventosFavoraveis/EventosPossiveis
Probabilidade: verificar na tabela num1 e num2 inseridos 
"""

def calculate_probability(df, inputs):
    numero, number1, number2 = inputs

    total_aparicoes = (
        ((df['Valor 1'] == numero) | (df['Valor 2'] == numero) | (df['Valor 3'] == numero)) &
        ((df['Valor 1'] == number1) | (df['Valor 2'] == number1) | (df['Valor 3'] == number1)) &
        ((df['Valor 1'] == number2) | (df['Valor 2'] == number2) | (df['Valor 3'] == number2))
    ).sum()

    casos_favoraveis = df[
        ((df['Valor 1'] == numero) | (df['Valor 2'] == numero) | (df['Valor 3'] == numero)) &
        ((df['Valor 1'] == number1) | (df['Valor 2'] == number1) | (df['Valor 3'] == number1)) &
        ((df['Valor 1'] == number2) | (df['Valor 2'] == number2) | (df['Valor 3'] == number2)) &
        (df['Resultado'] == "OK")
    ].shape[0]

       # Conta as aparições dos valores nas colunas específicas
    count_valor1 = ((df['Valor 1'] == numero) | (df['Valor 1'] == number1)).sum()
    count_valor2 = ((df['Valor 2'] == numero) | (df['Valor 2'] == number1)).sum()

    # Calcula a probabilidade
    probabilidade = casos_favoraveis / total_aparicoes if total_aparicoes > 0 else 0

    return probabilidade

inputs = (numero, number1, number2)  # Os números inseridos
probabilidade = calculate_probability(df, inputs)
print("teste probabilidade: ",probabilidade)