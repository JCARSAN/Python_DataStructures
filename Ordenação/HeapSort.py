def max_heapfy(A,i,limite):
    left = 2 * i + 1
    right = 2 * i + 2
    if(left <= limite and A[left] > A[i]):
        maior = left
    else:
        maior = i
    if(right <= limite and A[right] > A[maior]):
        maior = right
    if(maior != i):
        aux = A[i]
        A[i] = A[maior]
        A[maior] = aux
        max_heapfy(A,maior,limite)

def build_maxheapfy(A):
    tamanho = len(A) - 1
    tamanho_heap = int(tamanho/2) - 1
    while(tamanho_heap >= 0):
        max_heapfy(A,tamanho_heap,tamanho)
        tamanho_heap = tamanho_heap - 1

def heapsort(A):
    build_maxheapfy(A)
    tamanho = len(A) - 1
    i = 1
    while(tamanho >= 1):
        aux = A[0]
        A[0] = A[tamanho]
        A[tamanho] = aux
        tamanho = tamanho - 1
        max_heapfy(A,0,tamanho)