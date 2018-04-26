class IndiceRemissivo(object):

	# Construtor
	def __init__(self):
		self._indice = {};		# dicionário que guarda as palavras e suas ocorrências
		self._palavras = [];	# cache das palavras já computadas

	# Computa uma palavra no índice
	def contaPalavra(self, palavra):
		if(palavra == ""):
			return;

		if (palavra in self._palavras):
			self._indice[palavra] += 1;
		else:
			self._indice[palavra] = 1;
			self._palavras = self._indice.keys();

	# Recebe um array de palavras para computar
	def contaPalavras(self, palavras):
		for palavra in palavras:
			self.contaPalavra(palavra);

	# Recebe uma palavra e retorna o número de ocorrências
	def ocorrencias(self, palavra):
		if palavra in self._palavras:
			return self._indice[palavra];
		else:
			return 0

	# Override do "print" do objeto
	def __str__(self):
		string = "# ---------- ÍNDICE ---------- #\n\n";

		for palavra in self._palavras:
			string += "%s: %s\n" % (palavra, self._indice[palavra]);
		
		return(string);

	# Limpa índice
	def reset(self):
		self._indice = {};
