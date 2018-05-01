from lib.Set import Set;

class Cliente(object):

	# construtor
	def __init__(self, id, nome, sobrenome, telefone, email, cpf):
		# private
		self._cartoes = Set();
		self._ativo = True;
		self._cpf = "";

		# public
		self.id = id;
		self.nome = nome;
		self.sobrenome = sobrenome;
		self.telefone = telefone;
		self.email = email;
		self.cpf = cpf;
	#

	# insere cartão na lista do cliente
	def addCartao(self, cartao):
		self._cartoes.add(cartao.id, cartao);
	#
	
	@property # retorna se o cliente está aivo (True) ou inativo (False)
	def ativo(self):
		return self._ativo;
	#

	@ativo.setter
	def ativo(self, estado):
		self._ativo = estado;
	#

	def desativar(self):
		self.ativo = False;
	#
	
	@property # cpf getter
	def cpf(self):
		return self._cpf;
	#

	@cpf.setter
	def cpf(self, CPF):
		if(self.validaCPF(CPF)):
			self._cpf = CPF;
			self._ativo = True;
		else:
			self._ativo = False;
			print("\nCPF inválido, o cliente ID:%s ficará inativo.\n" % self.id);
		#
	#

	# verifica se um CPF é válido
	@staticmethod
	def validaCPF(cpf):
		cpfCalculado = cpf[0:9];

		for i in [0, 1]:
			soma = 0;
			cont = 10+i;

			for char in cpfCalculado:
				soma += int(char)*cont;
				cont -= 1;
			#
		
			resto = soma % 11;
			if(resto < 2):
				cpfCalculado += str(0);
			else:
				cpfCalculado += str(11-resto);
			#
		#
		
		if(cpf == cpfCalculado):
			return True;
		else:
			return False;
		#
	#

	# Override do print do objeto
	def __str__(self):
		return("\n# Cliente\nID: %s\nNome: %s %s\nTelefone: %s\nEmail: %s\nCPF: %s\n\n## Cartões:%s\n--------------------\n" % (self.id, self.nome, self.sobrenome, self.telefone, self.email, self.cpf, str(self._cartoes)));
	#
#
