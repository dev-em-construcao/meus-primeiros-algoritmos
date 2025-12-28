# Esse programa pergunta o nome e calcula a idade em 2030

print("----BEM VINDO AOS MEUS PROGRAMAS---")

nome = input(" Qual seu nome por favor? ")
nascimento = input(" Em que ano nasceu? ")

idade_em_2030 = 2030 - int(nascimento)
print(f"ola {nome}!Obrigado por colaborar, em 2030 voce tera {idade_em_2030} anos. ")
