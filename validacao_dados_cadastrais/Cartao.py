import datetime;

class Cartao(object):
	
	# construtor
	def __init__(self, id, idCliente, numero, cvc, validade):
		# private
		self._validade = "";
		self._valido = True;

		# public
		self.id = id;
		self.idCliente = idCliente;
		self.numero = numero;
		self.cvc = cvc;
		self.validade = validade;
	#
	
	@property # retorna a validade no formato dia/mes/ano
	def validade(self):
		return "%s/%s/%s" % (str(self._validade.day), str(self._validade.month), str(self._validade.year));
	#

	@validade.setter # recebe string no formato "dia/mes/ano"
	def validade(self, validade):
		s = validade.split("/");
		self._validade = datetime.date(int(s[2]),int(s[1]),int(s[0]));
	#
	
	@property # retorna se o cartão é válido (True) ou inválido (False)
	def valido(self):
		return self._valido;
	#

	def invalidar(self):
		self._valido = False;
	#
		
	def __str__(self):
		return("\nID: %s\nID Cliente: %s\nNumero: %s\nCVC: %s\nValidade: %s\n" % (self.id, self.idCliente, self.numero, self.cvc, self.validade));
	#
#
