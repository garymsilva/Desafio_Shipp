class Set(object):

	def __init__(self):
		self._objetos = {};
		self._cache = self._objetos.keys();
	#
	
	# adiciona um objeto no set
	def add(self, key, objeto):
		self._objetos[key] = objeto;
	#
	
	# atualiza um objeto no set
	def update(self, key, objeto):
		self.add(key, objeto);
	#
	
	# retorna um objeto a partir da chave
	def get(self, key):
		if key in self._cache:
			return self._objetos[key];
		else:
			return None
		#
	#
	
	# remove um objeto a partir da chave
	def remove(self, key):
		del(self._objetos[key]);
	#
	
	# retorna uma nova instância de Set() contendo os mesmos objetos
	def clone(self):
		cloneSet = Set();

		for key in self._cache:
			cloneSet.add(key, self._objetos[key]);
		#
		
		return cloneSet;
	#

	# retorna o conjunto de objetos na forma de um array
	def toArray(self):
		return self._objetos.values();
	#

	# Override do print
	def __str__(self):
		string = "";

		for key in self._cache:
			objeto = self._objetos[key];
			string += "\n%s" % str(objeto);
		#
		
		return string;
	#
#
