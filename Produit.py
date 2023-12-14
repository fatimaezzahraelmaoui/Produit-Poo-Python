
class Produit:
    nmbre_produit = 0
    def __init__(self,referance,designation,prix_achat,prix_vente,stock=0):
        self.__Referance = referance
        self.__Designation = designation
        self.__Prix_achat = prix_achat
        self.__Prix_vente = prix_vente
        self.__Stock = stock
        Produit.nmbre_produit += 1
    
    @property
    def Referance(self):
        return self.__Referance
    @Referance.setter
    def Referance(self,referance):
        self.__Referance = referance
        
    def getDesignation(self):
        return self.__Designation
    def setNom(self,designation):
        self.__Designation = designation
    
    @property
    def Prix_achat(self):
        return self.__Prix_achat
    @Prix_achat.setter
    def Prenom(self,prix_achat):
        self.__Prix_achat =prix_achat
    
    def getPrix_vende(self):
        return self.__Prix_vente
    def setAge(self,prix_vende):
        self.__Prix_achat = prix_vende
    
    @property
    def Stock(self):
        return self.__Stock
    @Stock.setter
    def setStock(self,stock):
        self.__Stock = stock

    def AfficherInfo(self):
        print("Referance est :",self.__Referance)
        print("Designation est :",self.__Designation)
        print("Date d'achat est :",self.__Prix_achat)
        print("Date de vende est :",self.__Prix_vente)
        print("le stock est :", self.__Stock)
    
    def Equals(self,referance):
        if self.__Referance == referance:
            return True
        else:
            return False
        
class Comonde:
    def __init__(self,date,quantite):
        self.__Date = date
        self.__Quantite = quantite
        
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self,date):
        self.__Date = date
    
    @property
    def Quantite(self):
        return self.__Quantite
    @Quantite.setter
    def setStock(self,quantite):
        self.__Quantite = quantite
    
    def AfficherInfo(self):
        print("la date est :",self.__Date)
        print("la quantite est :",self.__Quantite)

    @property
    def Acheter(self):
        return("cette comonde est acheter les produit")

P1 = Produit(3,"v-soin",200,400,2)
P2 = Produit(7,"Vichi",350,730,9)
print(P1.AfficherInfo())
print(P1.Prix_achat)
print(P1.nmbre_produit)

C1 = Comonde("31/07/2023",23)
print(C1.AfficherInfo())
print(C1.Date)
print(C1.Acheter)

