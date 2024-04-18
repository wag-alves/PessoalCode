#Tabela
 
A = 3

B = 16

test = False 

NOME = 'MIRIAM'

PROFISSAO = 'ADVOGADA'

a1 = f'{(A+1 >= ((B)**(1/2))) or (NOME != "ANA")}'

b1 = f'{(A+1 >= ((B) ** (1/2))) and (PROFISSAO == "MEDICO")}'

c1 = f'{(NOME != "ANA") or (PROFISSAO == "MEDICO") and (A+1 >= ((B) ** (1/2)))}'

d1 = f'{not test and ((A+1) >= ((B) ** (1/2))) or not (PROFISSAO == "MEDICO")}'

e1 = f'{not ((A+1 >= ((B) ** (1/2))) and test)}'

#----------------------------------------------------------------------------------------------------------------------

A = 5

B = 64

NOME = 'PEDRO'

PROFISSAO = 'MEDICO'

test = False 

a2 = f'{(A+1 >= ((B)**(1/2))) or (NOME != "ANA")}'

b2 = f'{(A+1 >= ((B) ** (1/2))) and (PROFISSAO == "MEDICO")}'

c2 = f'{(NOME != "ANA") or (PROFISSAO == "MEDICO") and (A+1 >= ((B) ** (1/2)))}'

d2 = f'{not test and ((A+1) >= ((B) ** (1/2))) or not (PROFISSAO == "MEDICO")}'

e2 = f'{not ((A+1 >= ((B) ** (1/2))) and test)}'
#----------------------------------------------------------------------------------------------------------------------

A = 2.5

B = 9

NOME = 'ANA'

PROFISSAO = 'PROFESSOR'

test = False

a3 = f'{(A+1 >= ((B)**(1/2))) or (NOME != "ANA")}'

b3 = f'{(A+1 >= ((B) ** (1/2))) and (PROFISSAO == "MEDICO")}'

c3 = f'{(NOME != "ANA") or (PROFISSAO == "MEDICO") and (A+1 >= ((B) ** (1/2)))}'

d3 = f'{not test and ((A+1) >= ((B) ** (1/2))) or not (PROFISSAO == "MEDICO")}'

e3 = f'{not ((A+1 >= ((B) ** (1/2))) and test)}'

print(f'1) {a1} - {b1} - {c1} - {d1} - {e1}')
print(f'2) {a2} - {b2} - {c2} - {d2} - {e2}')
print(f'3) {a3} - {b3} - {c3} - {d3} - {e3}')