import random

def merge(lista,linf,med,lsup):
	lista_esq = copia_lista(lista,linf,med)
	lista_dir = copia_lista(lista,med+1,lsup)
	i = 0
	j = 0
	k = linf
	tamanho_lesq = len(lista_esq)
	tamanho_ldir = len(lista_dir)
	while(i< tamanho_lesq and j< tamanho_ldir):
		if(lista_esq[i] <= lista_dir[j]):
			lista[k] = lista_esq[i]
			i = i + 1
		else:
			lista[k] = lista_dir[j]
			j = j + 1
		k = k + 1
	while(i<tamanho_lesq or j < tamanho_ldir):
		if(i < tamanho_lesq):
			lista[k] = lista_esq[i]
			k = k + 1
			i = i + 1
		if(j < tamanho_ldir):
			lista[k] = lista_dir[j]
			k = k + 1
			j = j + 1

def merge_sort(lista,linf,lsup):
	if(linf<lsup):
		med = int((linf+lsup)/2)
		merge_sort(lista,linf,med)
		merge_sort(lista,med+1,lsup)
		merge(lista,linf,med,lsup)

def geraVetorAleatorio(tamanho,linf,lsup):
	i = 0
	resp = []
	while(i < tamanho):
		resp.append(random.randint(linf,lsup))
		i = i + 1
	return resp

def copia_lista(lista,pos_inic,pos_fim):
	lista_resp = []
	while(pos_inic <= pos_fim):
		lista_resp.append(lista[pos_inic])
		pos_inic = pos_inic + 1
	return lista_resp
