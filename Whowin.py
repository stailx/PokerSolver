class Packet:
        def __init__(self):
                print("Appel de la méthode __init__")
                tab=[]
                for i in range (0,52):
                        MaCarte=Carte(i)
                        tab.append(MaCarte)
                self.tab=tab
                self.avancement=0

        def sort(self):
                self.tab.sort()
                print("sorted")

        def piocher(self):
                self.avancement+=1
                
class Carte:

        def __init__(self,ID):
                self.ID=ID
                
        def GetCorlor(self):
                return(self.  
        
        def GetHauteur(self):
                return(int(self.ID/4))
        
        
MonPacket=Packet()
print(MonPacket.tab[0].GetCorlor)
