"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).

def process_file(filename):
    words_dict = {}

    with open(filename) as file:
        words = file.read().lower().split()

        for word in words:
            if word in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    return words_dict

def sort_by_word(my_dict):
    return {k: v for k, v in sorted(my_dict.items(), key=lambda i: i[0])}

def sort_by_occurrences_top_20(my_dict):
    return {k: v for k, v in sorted(my_dict.items(), key=lambda i: i[1], reverse=True)[:20]}

def print_formatted_dict(my_dict):
    for k, v in my_dict.items():
        print(f'{k} {v}')

def print_words(words_dict):
    words_dict = sort_by_word(words_dict)
    print_formatted_dict(words_dict)

def print_top(words_dict):
    words_dict = sort_by_occurrences_top_20(words_dict)
    print_formatted_dict(words_dict)

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    words_dict = process_file(filename)

    if option == '--count':
        print_words(words_dict)
    elif option == '--topcount':
        print_top(words_dict)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
