class LeitorArquivos(object):

	# Recebe o caminho do arquivo, o separador utilizado e retorna um vetor de vetores.
	@staticmethod
	def lerCSV(caminho, separador, encoding="utf-8"):
		arquivo = open(caminho, "r", encoding=encoding);
		linhas = arquivo.readlines();
		arquivo.close();

		matLinhas = [];
		for linha in linhas:
			matLinhas.append(linha.strip().split(separador));
		#
		return matLinhas;
	#
#
