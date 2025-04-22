# Solicita ao usuário que digite um número inteiro e converte o valor para o tipo int
# A função input() retorna uma string, por isso usamos int() para conversão
num = int(input("Digite um número para ver a sua tabuada: "))

# Inicializa a variável contadora i com o valor 1
# Esta variável será usada como multiplicador na tabuada
i = 1

# Inicia um loop while que irá executar enquanto i for menor ou igual a 10
# Isso garante que a tabuada será calculada de 1 até 10
while i <= 10:
    # Usa uma f-string para formatar a saída da tabuada
    # {i:2} formata o número para ocupar 2 dígitos (útil para alinhamento)
    # {num * i:2} calcula o resultado e também formata para 2 dígitos
    print(f'{num} x {i:2} = {num * i:2}')
    
    # Incrementa o contador i em 1 a cada iteração
    # Isso evita loops infinitos e garante que passemos por todos os multiplicadores de 1 a 10
    i += 1
