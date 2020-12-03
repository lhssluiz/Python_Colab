# -*- coding: utf-8 -*-
"""1_Introdução.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HUhAxO8kLn7KtuRauK3e7_tiMgLCRGHm
"""

print("Hello world!")

"""**Regras e boas práticas com variáveis em python**
1. Nome de variáveis, preferencialmente contém apenas letras, números e underscores (evitar que se inicie com números)
2. Não utilizar espaços, usar underscore no lugar
3. Não usar palavras reservadas para nomes
"""

mensagem = "Atruibuindo valor"
print(mensagem)

var1 = "mensagem inicial"
print(var1)
var1 = "mensagem de troca"
print(var1)

name = "luiZ henrique"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "Luiz"
second_name = "Henrique"
full_name = first_name + " " + second_name
print(full_name)

mensagem1 = "Hello, " + full_name.title() + "\nWelcome to my program"
print(mensagem1)

mensagem2 = "Comecei na linha 1 \n\t Essa é a primeira opção \n\t Essa é a segunda opção \nTodas elas estão organizadas acima \n\n Mc'Donald só para testar a apóstrofe"
print(mensagem2)

einstein = " python teste"

print(einstein)
print(einstein.strip())

"""**Strings**

Python usa a adição para combinar strings

`title() ` neste caso é um método. Para chamar métodos dentro de funções, basta colocar o "." e o nome do método e os parênteses da chamada depois.
"""

2+3**2

age = 20
message3 = "Happy " + str(age) + "th birthday"
print(message3)

3/2

"""**Números**
Para elevar a alguma potência se coloca '**' dois asteriscos (multiplicação)
"""
