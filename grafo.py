# Grafo - nodos enlazados -
# Autor: Javier Rivera
# Colaboradores: Antony Duque Marbelis Zambrano

class Nodo:
    def __init__ (self, valor):
        self.info = valor
        self.arcos = []
        
    def enlace (self, ndestino, peso = 1, bdir = False):
        if (type(ndestino) == type(self)):
            arco = Arco(ndestino, peso)
            self.arcos.append(arco)
            if (bdir == True):
                arco = Arco(self, peso)
                ndestino.arcos.append(arco)
            return True
        return False
        
    def muestra_enlaces (self):
        for arco in self.arcos: 
            print arco.nodo.info,
            print arco.peso
            
    def existe_enlace(self, ndestino):
        for arco in self.arcos:
            if (arco.nodo == ndestino):
                return arco
        return False
    def existe_enlace_peso(self, ndestino):
        for arco in self.arcos:
            if (arco.nodo == ndestino):
                return arco
        return False
        
    def eli_enlace (self, ndestino):
        arco = self.existe_enlace(ndestino)
        if (arco != False):
            self.arcos.remove(arco)
            return True
        return False
            
    def __del__(self):
        del self.arcos
        
class Arco:
    def __init__ (self, ndestino, peso=0):
        self.nodo = ndestino
        self.peso = peso
class Arista:
    def __init__ (self,norigen, ndestino, peso=0):
        self.origen = norigen
        self.nodo = ndestino
        self.peso = peso

class Grafo:
    def __init__(self, dirigido = True):
        self.__nodos = []
        self.__dirigido = dirigido
        
    def buscaNodo (self, valor):
        for nodo in self.__nodos:
            if (nodo.info == valor):
                return nodo
        return False
    
    def enlace(self, valOrigen, valDestino, peso = 1, bdir = False):
        
        norigen = self.buscaNodo(valOrigen)
        if (not(norigen)):
            return False
            
        ndestino = self.buscaNodo(valDestino)
        if (not(ndestino)):
            return False
        
        if (self.__dirigido == False):
            bdir = True
            
        norigen.enlace(ndestino, peso, bdir)
        return True

    # metodo insetar para el grafo orginal	
    def ins_nodo (self, valor):
        if (self.buscaNodo(valor) == False):
            nodo = Nodo(valor)
            self.__nodos.append(nodo)
            return nodo
        return False
        
    def eli_nodo(self, valor):
        nodoE = self.buscaNodo(valor)
        if (nodoE == False):
            return False
            
        for nodo in self.__nodos:
            nodo.eli_enlace(nodoE)
        
        self.__nodos.remove(nodoE)
        return True
    
    def existen_islas(self):
        for nodo in self.__nodos:
            if (len(nodo.arcos) == 0):
                esIsla = True
                for norigen in self.__nodos:
                    if (norigen.existe_enlace(nodo) != False):
                        esIsla = False
                        break
                        
                if (esIsla == True):
                    return True
        return False
        
    def __str__(self):
        grafo  = ""
        for nodo in self.__nodos:
            grafo = grafo + nodo.info
            arcos = ""
            for arco in nodo.arcos:
                if (arcos != ""):
                    arcos = arcos + ", "
                arcos = arcos + arco.nodo.info + ":" + str(arco.peso)
            grafo = grafo + "(" + arcos + ") "
        return grafo

    def existe_camino(self, nOrigen, nDestino, inicializador=True):
            if (inicializador == True):
                self.__listaC=[]
            self.__listaC.append(nOrigen.info)
            if (nOrigen.existe_enlace(nDestino)):
                self.__listaC.append(nDestino.info)
                return True,self.__listaC

            for arco in nOrigen.arcos:
                if (arco.nodo.info in self.__listaC):
                    continue
                encuentra = self.existe_camino(arco.nodo, nDestino,False)

                if (encuentra):
                    return True,self.__listaC
                self.__listaC.pop(len(self.__listaC)-1)

            return False

    #indica que nodo tiene mas aristas de salidas 
    def nodoMasSalidas(self):
        mayor = 0
        for nodo in self.__nodos:
            if (len(nodo.arcos) > mayor):
                mayor=len(nodo.arcos)
                vertice=nodo.info
            
        return vertice , mayor
            
    #indica que nodo tiene mas aristas de llegada
    def nodoMasllegadas(self):
        mayor = 0
        for nodo in self.__nodos:
            con=self.entradas(nodo.info) 
            if (con > mayor ):			
                mayor = con
                vertice = nodo.info

        return vertice , mayor
                         
    def entradas (self, valor):
        cont = 0
        for nodo in self.__nodos :
            for arco in nodo.arcos :
                if ( arco.nodo.info == valor):
                    cont = cont +1
        return cont	
    #indica el nodo con mas lazos
    def nodoMaslaz0s(self):
        cont=0
        mayor=0
        for nodo in self.__nodos:
            for arcos in nodo.arcos:
                if (arcos.nodo.info==nodo.info):
                    cont=cont+1
            if(cont>mayor):
                mayor=cont
                vertice=nodo.info

        return vertice , mayor
    
    #verifica si un nodo tiene camino asi mismo
    def caminoAsimismo(self, nOrigen, nDestino, inicializador = True ):

        if (inicializador == True):
            self.__listaC=[]
        self.__listaC.append(nOrigen.info)
        if (nOrigen.existe_enlace(nDestino)):
            self.__listaC.append(nDestino.info)
            return False

        for arco in nOrigen.arcos:
            if (arco.nodo.info in self.__listaC):

                return True

            encuentra = self.existe_camino(arco.nodo, nDestino,False)

            if (encuentra):
                return True,self.__listaC
            self.__listaC.pop(len(self.__listaC)-1)

        return False

    #indica si un grafo es simple
    def Grafosimple(self):
        for nodo in self.__nodos:
            pos = 1
            n=len(nodo.arcos)
            for arco in nodo.arcos:
                if (nodo.info == arco.nodo.info):
                    return False

                for arc in range ( pos , n ):
                    if (arco.nodo.info == nodo.arcos[arc].nodo.info):
                        return False				
                pos = pos + 1
        return True

    #busca el nodo con mas aristas
    def nodoMasAristas(self):
        mayor = 0
        for nodo in self.__nodos:
            salida = len (nodo.arcos)
            entrar = self.entradas(nodo.info)
            suma = salida + entrar

            if(suma > mayor):
                mayor = suma
                vertice = nodo.info
        return mayor , vertice


    def Nodo_que_me_sigue(self, valor):
        lista_seguidores = []

        for nodo in self.__nodos:
            
            for arco in nodo.arcos: 
                
                if(arco.nodo.info == valor ):
                    lista_seguidores.append(nodo.info)

        return lista_seguidores

    def Nodo_que_sigo(self, valor):
        b=[]
        for nodo in self.__nodos:
            for arco in nodo.arcos: 
                if(nodo.info == valor): 
                    a = self.Nodo_que_me_sigue(valor)
        
                    if(arco.nodo.info in  a ):
                        b.append(arco.nodo.info)
        return "seguidores",a,"seguidos",b

    #retorna en numeros la cantidad de caminos que exiten entre dos nodos
    def CaminosaDosnodos(self, nOrigen , nDestino, inicializador=True):
        cont=0
        if (inicializador == True):
            self.__listaC=[]
        self.__listaC.append(nOrigen.info)
        if (nOrigen.existe_enlace(nDestino)):
            self.__listaC.append(nDestino.info)
            cont= cont+1

        for arco in nOrigen.arcos:
            if (arco.nodo.info in self.__listaC):
                continue
            encuentra = self.CaminosaDosnodos(arco.nodo, nDestino,False)
            if (encuentra):
                cont=cont+1
            self.__listaC.pop(len(self.__listaC)-1)

        return cont

    #el peso que hay de un nodo a otro antony y marbelis
    def arco_masPeso(self, nOrigen , nDestino, inicializador=True):		
        
        if (inicializador == True):
            self.__listaC = []
            self.__arista = Arista( None, None, 0) 
        self.__listaC.append(nOrigen.info)
        existeArco = nOrigen.existe_enlace(nDestino)
        
        if (existeArco):
            self.__listaC.append(nDestino.info)
            if(self.__arista.peso < existeArco.peso):
                self.__arista.peso = existeArco.peso
                self.__arista.origen = nOrigen.info
                self.__arista.ndestino = nDestino.info
            return True, self.__arista.origen,self.__arista.ndestino

        for arco in nOrigen.arcos:
            
            if (arco.nodo.info in self.__listaC):
                continue
            
            
    
            encuentra = self.arco_masPeso(arco.nodo,nDestino,False)
            
            if (encuentra):
                if (self.__arista.peso < arco.peso):
                    self.__arista.peso = arco.peso
                    self.__arista.origen = nOrigen.info
                    self.__arista.ndestino = arco.nodo.info				
                return True,self.__arista.origen,self.__arista.ndestino

            self.__listaC.pop(len(self.__listaC)-1)

        return False
    #antony y marbelis
    def ins_subgrafo(self ,*valor):
        subgrafo = Grafo()

        for val in valor:

            if(self.buscaNodo(val)==False):
                return
            subgrafo.ins_nodo(val)

        for arco in valor:

            nodo = self.buscaNodo(arco)
            if (len(nodo.arcos) != 0 ):

                for arco in nodo.arcos:

                    if (subgrafo.buscaNodo(arco.nodo.info) != False):
                        subgrafo.enlace(nodo.info,arco.nodo.info)

        return subgrafo
# Principal

g = Grafo()
nodo1 = g.ins_nodo("A")
nodo2 = g.ins_nodo("B")
nodo3 = g.ins_nodo("C")
nodo4 = g.ins_nodo("D")
nodo5 = g.ins_nodo("E")
nodo6 = g.ins_nodo("F")
nodo7 = g.ins_nodo("G")
#prueba subgrafo

nodo1.enlace(nodo2,1)		
nodo2.enlace(nodo3,5)
nodo3.enlace(nodo4,6)
nodo1.enlace(nodo5,3)
nodo5.enlace(nodo6,2)

print g.arco_masPeso(nodo1,nodo6)
print g.ins_subgrafo("A","B","C")
