from Cliente import Cliente;
from Cartao import Cartao;
from lib.LeitorArquivos import LeitorArquivos;
from lib.Set import Set;
import datetime;

# constantes
ID = 0;
NOME = 1;
SOBRENOME = 2;
TELEFONE = 3;
EMAIL = 4;
CPF = 5;

IDCLIENTE = 1;
NUMERO = 2;
CVC = 3;
VALIDADE = 4;

PREFIXO = "prefixo";
TAMANHO = "tamanho";

# funções

def checarContatosDuplicados(clientes):
	dados = {};
	for cliente in clientes.toArray():
		# coleta telefones
		if(cliente.telefone not in dados.keys()):
			dados[cliente.telefone] = [];
		#
		dados[cliente.telefone].append(cliente);

		# coleta emails
		if(cliente.email not in dados.keys()):
			dados[cliente.email] = [];
		#
		dados[cliente.email].append(cliente);
	#

	# testa tudo
	for arrayClientes in dados.values():
		if(len(arrayClientes) > 1):
			for cliente in arrayClientes:
				cliente.desativar();
			#
		#
	#
#

def validarCartoes(cartoes):
	
	bandeiras = [
		{ # ELO
			"nome": "elo",
			"prefixo": [636368, 636369, 438935, 504175, 451416, 636297, 5067, 4576, 4011, 506699],
			"tamanho": [16],
			"cvc": 3
		},
		{ # MASTER
			"nome": "master",
			"prefixo": [51, 52, 53, 54, 55],
			"tamanho": [16],
			"cvc": 3
		},
		{ # VISA
			"nome": "visa",
			"prefixo": [4],
			"tamanho": [13, 16],
			"cvc": 3
		},
		{ # AMEX
			"nome": "amex",
			"prefixo": [34, 37],
			"tamanho": [15],
			"cvc": 4
		}
	];

	for cartao in cartoes.toArray():
		valido = False;
		for bandeira in bandeiras:
			print(bandeira["nome"]);
			cvc = len(cartao.cvc) == bandeira["cvc"];
			print("cvc: %s"% str(cvc))
			tamanho = len(cartao.numero) in bandeira["tamanho"];
			print("tamanho: %s"% str(tamanho))
			validade = datetime.date.today() < cartao._validade;
			print("validade: %s"% str(validade))
			prefixo = False;

			for n in bandeira["prefixo"]:
				if(str(n) == cartao.numero[:len(str(n))]):
					prefixo = True;
					break;
				#
			#
			print("prefixo: %s"% str(prefixo))

			if(cvc & tamanho & prefixo & validade):
				valido = True;
				print("cartao %s match na bandeira %s" % (cartao.id, bandeira["nome"]));
				break;
			#
		#
		if(not valido):
			cartao.invalidar();
		#
	#
#

# main

def main():
	# -- carregar clientes -- #
	clientesCSV = LeitorArquivos.lerCSV("./data/clientes.csv", ",");
	del(clientesCSV[0]); # remove o cabeçalho
	
	clientes = Set();
	for linha in clientesCSV:
		cliente = Cliente(
			linha[ID],
			linha[NOME],
			linha[SOBRENOME],
			linha[TELEFONE],
			linha[EMAIL],
			linha[CPF]
		);
		clientes.add(cliente.id, cliente);
	#

	# -- carregar cartões -- #
	cartoesCSV = LeitorArquivos.lerCSV("./data/cartoes.csv", ",");
	del(cartoesCSV[0]); # remove o cabeçalho

	cartoes = Set();
	for linha in cartoesCSV:
		cartao = Cartao(
			linha[ID],
			linha[IDCLIENTE],
			linha[NUMERO],
			linha[CVC],
			linha[VALIDADE]
		);
		cartoes.add(cartao.id, cartao);

		cliente = clientes.get(cartao.idCliente);
		if(cliente):
			cliente.addCartao(cartao);
		else:
			print("cliente não encontrado\n");
		#
	#

	# -- verificar telefones e emails duplicados -- #
	checarContatosDuplicados(clientes);

	# -- verificar cartões -- #
	validarCartoes(cartoes);

	clientes = clientes.toArray();
	# -- imprimir clientes ativos -- #

	print("\nCLIENTES ATIVOS\n")
	for cliente in clientes:
		if(cliente.ativo):
			print("ID: %s Nome: %s %s" % (cliente.id, cliente.nome, cliente.sobrenome));
		#
	#

	# -- imprimir clientes inativos -- #
	print("\nCLIENTES INATIVOS\n")
	for cliente in clientes:
		if(not cliente.ativo):
			print("ID: %s Nome: %s %s" % (cliente.id, cliente.nome, cliente.sobrenome));
		#
	#

	cartoes = cartoes.toArray();
	# -- imprimir cartões válidos -- #
	print("\nCARTÕES VÁLIDOS\n");
	for cartao in cartoes:
		if(cartao.valido):
			print("ID: %s Numero: %s CVC: %s Validade: %s" % (cartao.id, cartao.numero, cartao.cvc, cartao.validade));
		#
	#

	# -- imprimir cartões inválidos -- #
	print("\nCARTÕES INVÁLIDOS\n");
	for cartao in cartoes:
		if(not cartao.valido):
			print("ID: %s Numero: %s CVC: %s Validade: %s" % (cartao.id, cartao.numero, cartao.cvc, cartao.validade));
		#
	#
#

main()
