class ListaNos(object):
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.next = prox

class Solution(object):
    def getMid(self, head):
        countEsq, countDir = head, head.next

        while countDir and countDir.next:
            countEsq = countEsq.next
            countDir = countDir.next.next
        
        return countEsq
    
    def merge(self, lista1, lista2):
        atualNo = lista = ListaNos()
        while lista1 and lista2:
            if lista1.val < lista2.val:
                atualNo.next = lista1
                lista1 = lista1.next
            else:
                atualNo.next = lista2
                lista2 = lista2.next
            atualNo = atualNo.next
        
        if lista1:
            atualNo.next = lista1
        if lista2:
            atualNo.next = lista2
            
        return lista.next

    # main
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        esq = head
        meio = self.getMid(head)
        dir = meio.next
        meio.next = None


        esq = self.sortList(esq)
        dir = self.sortList(dir)

        return self.merge(esq, dir)
