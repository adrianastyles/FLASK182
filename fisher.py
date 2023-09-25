from random import randrange

def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp

#FUNCION PARA BARAJAR
def shuffle(A):

    for i in range (len(A)-1):

        #GENERA UN NUMERO ALEATORIO
        j = randrange(i, len(A))

        #INTERCAMBIA EL ELEMENTO ACTUAL CON EL INDICE GENERADO ACTUALMENTE
        swap(A, i, j)

if __name__ == '__ main__':
    A = [1,2,3,4,5,6]
    shuffle(A)
    #IMPRIME LA LISTA BARAJADA
    print(A)