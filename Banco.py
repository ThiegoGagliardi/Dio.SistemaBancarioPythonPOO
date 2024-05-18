
import os
import time
import sys
import re

from model.PessoaFisica import PessoaFisica
from model.ContaCorrente import ContaCorrente
from model.Conta import Conta

clientes = []

def criar_cliente():

   global clientes

   cpf     = input("Informe o cpf do Cliente:")
   cliente = buscar_cliente(cpf)

   if cliente:
      print('Cliente já cadastrado')
      esperar_tecla()
      return 
   
   nome     = input("Informe o nome do cliente:")
   data_nascimento = input("Informe data nascimento:")
   endereco = input("Informe o  endereco:")

   cliente = PessoaFisica(nome, data_nascimento, re.sub('[^0-9]', '', cpf), endereco)

   clientes.append(cliente)
   
   print('Cliente cadastrado com sucesso.')
   esperar_tecla();

def buscar_cliente(cpf = None):
   
   global clientes

   if not(cpf):
      cpf = input("Informe o cpf do Cliente:")
   
   for cliente in clientes:
      if (cliente.cpf == cpf):
        return cliente
   
   return None

def verificar_cliente(cliente):
   
   if not cliente:
      print('Cliente não localizado.')
      esperar_tecla();
      return False
   
   return True

def criar_conta():

   global contas  

   cliente = buscar_cliente()

   if not verificar_cliente(cliente):
      return
     
   conta = ContaCorrente.criar_nova_conta(cliente);

   cliente.adicionar_conta(conta)

   print(f'Conta cadastrado com sucesso para o cpf {cliente.cpf}')
   esperar_tecla();

def buscar_conta(cliente):
   cc = input("Informe o numero da conta:")

   return cliente.buscar_conta(cc)

def verificar_conta(conta):

   if not conta:
      print('Conta não localizada.')
      esperar_tecla();
      return  False
   
   return True;

def listar_contas():
   
   global contas  

   cliente = buscar_cliente()

   if not verificar_cliente(cliente):
      return
       
   print("Dados Cliente: \n")
   print(cliente)

   print("Dados Conta:\n")
   print(cliente.listar_contas())

   esperar_tecla();

def menu():
    print("[u] Criar Cliente")
    print("[c] Criar Conta Corrente")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[l] Listar Contas")
    print("[q] Sair")

def solicitar_opcao():

   while True:

      os.system('cls')
      
      menu()

      opcao = input("Digite a opção desejada:")

      if opcao == "c":
            
         os.system('cls')
         exibir_titulo("Cadastrar Conta Corrente")
         criar_conta()
        
      elif opcao == "d":      
            
         os.system('cls')
         exibir_titulo("Efetuar Deposito")
         efetuar_deposito()

      elif opcao == "s":
      
         os.system('cls')
         exibir_titulo("Efetuar Saque")
         efetuar_saque()
      elif opcao == "e": 
      
         os.system('cls')
         exibir_titulo("Exibir extrato")
         exibir_extrato()

      elif opcao == "l": 
            
         os.system('cls')
         exibir_titulo("Listar contas")
         listar_contas()                         
   
      elif opcao == "u": 
            
         os.system('cls')
         exibir_titulo("Cadastrar cliente")
         criar_cliente()          
      
      elif opcao == "q":
            
         print("Encerrando ...")
         time.sleep(2)
         os.system('cls')
         break;
            

def exibir_titulo(texto):

    os.system('cls')

    linha = '*'*len(texto)

    print(linha)
    print(texto)
    print(linha)

    print()        


def esperar_tecla():
   print("Pressione qualquer tecla para continuar...")
   sys.stdin.read(1)     

def exibir_extrato():

   global contas

   cliente = buscar_cliente()

   if (not verificar_cliente(cliente)):
      return     

   conta = buscar_conta(cliente)

   if (not(verificar_conta(conta))):
      return   
      
   print(conta.verificar_extrato())
   esperar_tecla()

def efetuar_deposito():

   global contas   

   cliente = buscar_cliente()

   if not (verificar_cliente(cliente)):
      return   

   conta = buscar_conta(cliente)

   if (not (verificar_conta(conta))):
      return
         
   valor_deposito = int(input("Digite o valor para deposito:"));
   retorno, mensagem = conta.depositar(valor_deposito)

   if not(retorno):
      print(f'Deposito não efetuado: {mensagem}')
   else:
      print('Deposito efetuado com sucesso')

   esperar_tecla()   

def efetuar_saque():

   global contas  

   cliente = buscar_cliente()

   if not verificar_cliente(cliente):
      return
   
   conta = buscar_conta(cliente)

   if (not verificar_conta(conta)):
      return   
         
   valor_saque = int(input("Digite o valor para saque:"));   
   retorno,mensagem = conta.sacar(valor_saque)

   if (not retorno):
      print(f'Saque não efetuado: {mensagem}')
   else:      
      print(f'Saque efetuado com sucesso, novo saldo: {conta.saldo}')

   esperar_tecla()


def main(): 
    os.system('cls');    
    solicitar_opcao()    

if __name__ == '__main__':
    main();
