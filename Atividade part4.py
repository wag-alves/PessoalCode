
A = 2.5

B = 9

NOME = 'ANA'

PROFISSAO = 'PROFESSOR'

test = False

print(f'{(A+1 >= ((B)**(1/2))) or (NOME != "ANA")}') 

print(f'{(A+1 >= ((B) ** (1/2))) and (PROFISSAO == "MEDICO")}')

print(f'{(NOME != "ANA") or (PROFISSAO == "MEDICO") and (A+1 >= ((B) ** (1/2)))}')

print(f'{not test and ((A+1) >= ((B) ** (1/2))) or not (PROFISSAO == "MEDICO")}')

print(f'{not ((A+1 >= ((B) ** (1/2))) and test)}')