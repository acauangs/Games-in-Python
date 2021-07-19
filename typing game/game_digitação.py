import requests
import random
import time

#Boa noite
#esse é um jogo simples de digitação
#ao final sera mostrado sua pontuação e o tempo gasto para resolver o desafio.




url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

resposta = requests.get(url)
palavras = resposta.content.splitlines()
palavras = [palavra.decode('utf-8')for palavra in palavras]

random_palavras = random.sample(palavras,10)

pontos = 0

print('-' * 45)
print('       Bem Vindo ao jogo de digitação')
print('-' * 45,'\n')
tic = time.perf_counter()
for palavra in random_palavras:
  print(f'\033[33m{palavra}\033[m')
  entrada = input()
  if entrada == palavra:
     pontos = pontos + 1

toc = time.perf_counter()
if pontos > 5:
  print(f'Sua pontuação foi: \033[32m{pontos}\033[m')
else:
  print(f'Sua pontuação foi: \033[31m{pontos}\033[m')
print(f'E seu tempo foi: {toc-tic}')

