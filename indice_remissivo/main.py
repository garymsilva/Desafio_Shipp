from IndiceRemissivo import IndiceRemissivo

# Limpa caracteres especiais
def limpar(palavra):
	_palavra = "";

	for char in palavra:
		if (char not in ".,:;!#)(}{]['?^"):
			_palavra += char;
	
	return _palavra;
# fim limpar()

# Lê um arquivo de texto e retorna um array de palavras.
def getArrayPalavras(caminho):
	arquivo = open(caminho, "r", encoding="utf-8");
	linhas = arquivo.readlines();
	arquivo.close();

	buffer = [];
	for linha in linhas:
		arr = linha.split();
		for palavra in arr:
			buffer.append(limpar(palavra.lower()));
	
	return buffer;
# fim getArrayPalavras()

def main():
	palavras = getArrayPalavras("palavras.txt");
	indice = IndiceRemissivo();
	indice.contaPalavras(palavras);
	print(indice);

	print("\n\n--------------TESTES--------------")
	palavras_teste = ["dobro","sujo","porque","neles","e","onde","quando"];

	for p in palavras_teste:
		print("%s: %d" % (p, indice.ocorrencias(p)));

# fim main()

main();
