class Ramo:
	def __init__(self,elemento,pai=None,esquerda=None,direita=None):
		self.elemento = elemento
		if(isinstance(pai,Ramo) or pai == None):
			self.pai = pai
		else:
			raise TypeError('arg2 deve ser do tipo Ramo!')
		if(isinstance(esquerda,Ramo) or esquerda == None):
			self.esquerda = esquerda
		else:
			raise TypeError('arg3 deve ser do tipo Ramo!')
		if(isinstance(direita,Ramo) or direita == None):
			self.direita = direita
		else:
			raise TypeError('arg3 deve ser do tipo Ramo!')
	def getPai(self):
		return self.pai
	def getEsquerda(self):
		return self.esquerda
	def getDireita(self):
		return self.direita
	def getElemento(self):
		return self.elemento
	def setPai(self,elemento):
		if(isinstance(elemento,Ramo) or elemento == None):
			self.pai = elemento
		else:
			raise TypeError('O arg1 precisa ser do tipo Ramo')
	def setEsquerda(self,elemento):
		if(isinstance(elemento,Ramo) or elemento == None):
			self.esquerda = elemento
		else:
			raise TypeError('O arg1 prcisa ser do tipo Ramo')
	def setDireita(self,elemento):
		if(isinstance(elemento,Ramo) or elemento == None):
			self.direita = elemento
		else:
			raise TypeError('O arg1 prcisa ser do tipo Ramo')