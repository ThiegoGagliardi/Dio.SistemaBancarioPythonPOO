
# Simulador de Caixa Eletrônico em Python

Este é um programa em Python que simula um caixa eletrônico básico, permitindo ao usuário realizar operações como depósito, saque, exibição de extrato e sair do programa.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

- **Criar cliente**: Cadastrar cliente.
- **Criar conta**: Cadastra conta e atriui a um cliente
- **Depositar**: Permite ao usuário fazer um depósito na conta.
- **Sacar**: Permite ao usuário sacar dinheiro da conta, desde que haja saldo disponível e o valor do saque esteja dentro do limite diário e do limite total.
- **Extrato**: Exibe o histórico de transações da conta.
- **Sair**: Encerra a execução do programa.

## Como usar

Para executar o programa, basta rodar o script Python `caixa_eletronico.py`. O programa mostrará um menu com as opções disponíveis. O usuário pode escolher uma opção digitando a letra correspondente seguida da tecla Enter.

## Detalhes de Implementação

O programa utiliza as seguintes variáveis globais para rastrear informações da conta:

- `saldo`: Saldo atual na conta.
- `limit`: Limite máximo de saque por transação.
- `extrato`: Histórico de transações da conta.
- `numero_saques`: Número de saques realizados no dia.
- `LIMITE_SAQUES_DIARIOS`: Limite máximo de saques permitidos por dia.

As principais funções do programa incluem:

- `menu()`: Exibe o menu de opções para o usuário.
- `esperar_tecla()`: Aguarda até que o usuário pressione uma tecla para continuar a execução do programa.
- `exibir_extrato()`: Exibe o extrato bancário na tela.
- `atualizar_saldo()`: Atualiza o saldo da conta após uma transação.
- `efetuar_deposito()`: Realiza um depósito na conta.
- `depositar()`: Função auxiliar para realizar um depósito.
- `efetuar_saque()`: Realiza um saque na conta.
- `pode_realizar_saque()`: Verifica se um saque pode ser realizado com base nos limites estabelecidos.
- `sacar()`: Função auxiliar para realizar um saque.
- O loop `while True` controla a execução contínua do programa.

## Estrutura de Classes
- Conta:  Classe base para instanciar uma conta
- Conta Corrente: Classe especialista da classe Conta
- Cliente: Classe base para instanciar um cliente
- PessoaFisica: Classe especialista de uma classe Cliente
- Extrato: Classe para guardar as transações efetuadas para cada conta
- Depoisto: Classe que representa um depósito
- Saque: Classe que representa um saque

## Executando o Programa

Para executar o programa, abra um terminal, navegue até o diretório onde o arquivo `Banco.py` está localizado e execute o seguinte comando:

```
python caixa_eletronico.py
```

Isso iniciará o programa e você poderá interagir com ele através do menu de opções.

--- 

Este README fornece uma visão geral do funcionamento e das funcionalidades do programa, bem como instruções sobre como executá-lo. Você pode adicionar mais detalhes ou informações específicas conforme necessário.