import Ramo

class ArvoreBinariaBusca:
	def __init__(self,ramo):
		#assert isinstance(ramo,Ramo), 'O arg1 não é do tipo Ramo'
		if(not isinstance(ramo,Ramo)):
			raise TypeError('O arg1 não é do tipo Ramo')
		self.__raiz = ramo
	def getRaiz(self):
		return self.__raiz
	def percorreArvore(self,no):
		if(no):
			self.percorreArvore(no.getEsquerda())
			print(no.getElemento(),end=' ')
			self.percorreArvore(no.getDireita())
	def minimo(self,no):
		if(no.getEsquerda() == None):
			return no
		return self.minimo(no.getEsquerda())
	def maximo(self,no):
		if(no.getDireita() == None):
			return no
		return self.maximo(no.getDireita())
	def successor(self,no):
		if(no.getDireita() == None):
			return no
		return self.sucessor(no.getDireita())
	def antecessor(self,no):
		return no.getEsquerda()
	def busca(self,chave,no):
		if(chave == no.getElemento()):
			return no
		if(chave < no.getElemento()):
			if(no.getEsquerda() != None):
				no = no.getEsquerda()
			else:
				return None
		if(chave > no.getElemento()):
			if(no.getDireita() != None):
				no = no.getDireita()
			else:
				return None
		return self.busca(chave,no)
	def buscaInserir(self,valor,no):
		if(valor == no.getElemento()):
			return None
		if(valor < no.getElemento()):
			if(no.getEsquerda() != None):
				no = no.getEsquerda()
			else:
				return no
		elif(valor > no.getElemento()):
			if(no.getDireita() != None):
				no = no.getDireita()
			else:
				return no
		return self.buscaInserir(valor,no)
	def insere(self,chave):
		no = self.getRaiz()
		if(chave < no.getElemento()):
			no = self.buscaInserir(chave,no)
			if(not no):
				return
			novo_ramo = Ramo(chave,no)
			if(chave < no.getElemento()):
				no.setEsquerda(novo_ramo)
			elif(chave > no.getElemento()):
				no.setDireita(novo_ramo)
		elif(chave > no.getElemento()):
			no = self.buscaInserir(chave,no)
			if(not no):
				return
			novo_ramo = Ramo(chave,no)
			if(chave < no.getElemento()):
				no.setEsquerda(novo_ramo)
			elif(chave > no.getElemento()):
				no.setDireita(novo_ramo)
	def transplant(self,r1,r2):
		if(not(isinstance(r1,Ramo) and isinstance(r2,Ramo))):
			raise TypeError('os args1 e arg2 devem ser do tipo Ramo')
		if(r1.getPai() == None):
			self.__raiz = r2
		elif(r1.getElemento() == r1.getPai().getEsquerda().getElemento()):
			r1.getPai().setEsquerda(r2)
		else:
			r1.getPai().setDireita(r2)
		if(r2):
			r2.setPai(r1.getPai())
	def remove(self,chave):
		no = self.busca(chave,self.getRaiz())
		if(not no):
			return
		if(not no.getEsquerda()):
			self.transplant(no,no.getDireita())
		elif(not no.getDireita()):
			self.transplant(no,no.getEsquerda())
		else:
			sucessor = self.minimo(no.getDireita())
			sucessor.setEsquerda(no.getEsquerda())
			pai = sucessor.getPai()
			if(sucessor.getPai().getElemento() != no.getElemento()):
				pai.setEsquerda(sucessor.getDireita())
				sucessor.setDireita(pai)
				self.transplant(no,sucessor)
			else:
				self.transplant(no,sucessor)