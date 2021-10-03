from enum import Enum
from tkinter import *
import random
from PIL import ImageTk,Image
from ctypes import *
from tkinter import ttk

zelib=CDLL("C:\\Users\\Theo\\Desktop\\old bureau omen\\pyPoker\\clib2.dll")
zelib.MainHasard.argtypes  = [c_int]
zelib.MainHasard.restype = c_double

zelib.Equitemaincontremain.argtypes  = [c_int,c_int,c_int,c_int,c_int]
zelib.Equitemaincontremain.restype = c_double

zelib.Quigagne.argtypes  = [c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int]
zelib.Quigagne.restype = c_int

zelib.offorsuited.argtypes  = [c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int]
zelib.offorsuited.restype = c_double

zelib.EquitemaincontremainRandom.argtypes  = [c_int,c_int,c_int,c_int,c_int,c_int]
zelib.EquitemaincontremainRandom.restype = c_double

class Color(Enum):
        coeur = 0
        carreaux = 1
        pique = 2
        trefle = 3

class Hauteur(Enum):
        deux = 0
        trois = 1
        quatre = 2
        cinq = 3
        six = 4
        sept = 5
        huit = 6
        neuf = 7
        T = 8
        J = 9
        Q = 10
        K = 11
        A = 12

class Valeur(Enum):
        Hauteur = 0
        Paire = 1
        Double_Paire = 2
        Brelan = 3
        Suite = 4
        Couleur = 5
        Full = 6
        Carre = 7
        QuinteFlush = 8

class ValeuretHauteur:
        def __init__(self,valeur,H1,H2,H3,H4,H5):
                tab=[H1,H2,H3,H4,H5]
                self.hauteur=tab
                self.valeur=valeur

class TwoCard:
        def __init__(self,carte1,carte2):
                tab=[carte1,carte2]
                self.carte=tab
        def afficher(self):
                return "" + str(self.carte[0].afficher()) +"/" + str(self.carte[1].afficher())

class Board:
        def __init__(self,carte1,carte2,carte3,carte4,carte5):
                tab=[carte1,carte2,carte3,carte4,carte5]
                self.carte=tab
        def afficher(self):
                return "" + str(self.carte[0].afficher()) +"/" + str(self.carte[1].afficher())+"/" + str(self.carte[2].afficher())+"/" + str(self.carte[3].afficher())+"/" + str(self.carte[4].afficher())

class SevenCard:
        def __init__(self,carte1,carte2,carte3,carte4,carte5,carte6,carte7):
                tab=[carte1,carte2,carte3,carte4,carte5,carte6,carte7]
                self.carte=tab
        def afficher(self):
                return "" + str(self.carte[0].afficher()) +"/" + str(self.carte[1].afficher())+"/" + str(self.carte[2].afficher())+"/" + str(self.carte[3].afficher())+"/" + str(self.carte[4].afficher()) +"/" + str(self.carte[5].afficher()) +"/" + str(self.carte[6].afficher())

class Packet:
        def __init__(self):
                #print("Appel de la méthode __init__")
                tab=[]
                for i in range (0,52):
                        MaCarte=Carte(i)
                        tab.append(MaCarte)
                self.tab=tab
                self.avancement=0

        def shuffle(self):
                try:
                        random.shuffle(self.tab)
                except:
                        print("An exception occurred")
                #print("SORTED")

        def piocher(self):
                tampon=self.tab[0]
                del self.tab[0]
                return tampon
        
        def piochernumero(self,ID):
                for i in range(len(self.tab)):
                        if ID==self.tab[i].ID:
                                Carte=self.tab[i]
                                del self.tab[i]
                                break
                        
                return Carte

class Carte:
        def __init__(self,ID):
                self.ID=ID
                
        def GetColor(self):
                return(Color(self.ID%4).name)
        
        def GetColorValue(self):
                return(self.ID%4)
        
        def GetHauteur(self):
                return(Hauteur(self.ID//4).name)
        
        def GetHauteurValue(self):
                return((self.ID)//4)

        def afficher(self):
                return ""+self.GetHauteur()+" "+self.GetColor()
        
def IsCouleur(Mon_Showdown):
        color=[]
        result=[]
        Iscouleur=-1
        for i in range(0,7):
                color.append(Mon_Showdown.carte[i].GetColorValue())
                
        for i in range(0,4):
                if(color.count(i)>4):
                        Iscouleur=i
                        
        if(Iscouleur==-1):
                return ValeuretHauteur(0,0,0,0,0,0) 
        else:
                #print("couleur")
                for i in range(0,7):
                        if(Mon_Showdown.carte[i].GetColorValue()==Iscouleur):
                                result.append(Mon_Showdown.carte[i].GetHauteurValue())
        
                        if(len(result)==5):
                                break;
        

                #print(result)
                return ValeuretHauteur(5,result[0],result[1],result[2],result[3],result[4])   
        
def IsSuite(Mon_Showdown):
        Issuite=-1
        new_list=[]
        for element in Mon_Showdown.carte:
                if element.GetHauteurValue() not in new_list:
                        new_list.append(element.GetHauteurValue())
                        
        if(len(new_list)>4 and new_list[0]==12 and new_list[-1]==0 and new_list[-2]==1 and new_list[-3]==2 and new_list[-4]==3):
                Issuite=1
                i=0
        else:
                for i in range(len(new_list)-4):
                        if((new_list[i])==(new_list[i+1]+1)==(new_list[i+2]+2)==(new_list[i+3]+3)==(new_list[i+4]+4)):
                                Issuite=1
                                break
                        
                        
        if(Issuite==-1):
                return ValeuretHauteur(0,0,0,0,0,0)
        else:
                return ValeuretHauteur(4,new_list[i+1],0,0,0,0)

def IsBrelan(Mon_Showdown):
        IsBrelan=-1
        for i in range(0,5):
                if(Mon_Showdown.carte[i].GetHauteurValue()==Mon_Showdown.carte[i+1].GetHauteurValue()==Mon_Showdown.carte[i+2].GetHauteurValue()):
                        IsBrelan=1
                        hauteur=Mon_Showdown.carte[i].GetHauteurValue()
                        del Mon_Showdown.carte[i]
                        del Mon_Showdown.carte[i]
                        del Mon_Showdown.carte[i]
                        break
        
        if(IsBrelan==-1):
                return ValeuretHauteur(0,0,0,0,0,0) 
        else:
                #print("Brelan")
                return ValeuretHauteur(3,hauteur,hauteur,hauteur,Mon_Showdown.carte[0].GetHauteurValue(),Mon_Showdown.carte[1].GetHauteurValue())

def IsFull(Mon_Showdown):
        IsBrelan=-1
        Ispaire=-1
        for i in range(0,5):
                if(Mon_Showdown.carte[i].GetHauteurValue()==Mon_Showdown.carte[i+1].GetHauteurValue()==Mon_Showdown.carte[i+2].GetHauteurValue()):
                        IsBrelan=1
                        hauteur=Mon_Showdown.carte[i].GetHauteurValue()
                        del Mon_Showdown.carte[i]
                        del Mon_Showdown.carte[i]
                        del Mon_Showdown.carte[i]
                        break
        while i<len(Mon_Showdown.carte)-1:
                if(Mon_Showdown.carte[i].GetHauteurValue()==Mon_Showdown.carte[i+1].GetHauteurValue()):
                        Ispaire=1
                        hauteurPair=Mon_Showdown.carte[i].GetHauteurValue()
                i=i+1
                        
                        
                
        if(IsBrelan==-1 or Ispaire==-1 ):
                return ValeuretHauteur(0,0,0,0,0,0) 
        else:
                #print("Full:",hauteur," ",hauteurPair)
                return ValeuretHauteur(6,hauteur,hauteur,hauteur,hauteurPair,hauteurPair)

def IsCarre(Mon_Showdown):
        IsCarre=-1
        for i in range(0,4):
                if(Mon_Showdown.carte[i].GetHauteurValue()==Mon_Showdown.carte[i+1].GetHauteurValue()==Mon_Showdown.carte[i+2].GetHauteurValue()==Mon_Showdown.carte[i+3].GetHauteurValue()):
                        IsCarre=1
                        hauteur=Mon_Showdown.carte[i].GetHauteurValue()
                        break
        
        if(IsCarre==-1):
                return ValeuretHauteur(0,0,0,0,0,0) 
        else:
                #print("Carre")
                if(i==0):
                        x=4
                else:
                        x=0
                return ValeuretHauteur(7,hauteur,hauteur,hauteur,hauteur,Mon_Showdown.carte[x].GetHauteurValue()) 

def IsPaire(Mon_Showdown):
        IsPaire=0
        hauteur=[]
        #print("a",Mon_Showdown.carte[6].ID)
        i=0
        while i<(len(Mon_Showdown.carte)-1):
                #print(i,"aaaa")
                if(Mon_Showdown.carte[i].GetHauteurValue()==Mon_Showdown.carte[i+1].GetHauteurValue()):
                        hauteur.append(Mon_Showdown.carte[i].GetHauteurValue())
                        IsPaire+=1
                        del Mon_Showdown.carte[i]
                        del Mon_Showdown.carte[i]
                        i=i-2
                        if(IsPaire==2):
                                break
                else:
                        i=i+1        
        if(IsPaire==0):
                #print("hauteur",Mon_Showdown.carte[0].GetHauteur(),Mon_Showdown.carte[1].GetHauteur(),Mon_Showdown.carte[2].GetHauteur(),Mon_Showdown.carte[3].GetHauteur(),Mon_Showdown.carte[4].GetHauteur())
                return ValeuretHauteur(0,Mon_Showdown.carte[0].GetHauteurValue(),Mon_Showdown.carte[1].GetHauteurValue(),Mon_Showdown.carte[2].GetHauteurValue(),Mon_Showdown.carte[3].GetHauteurValue(),Mon_Showdown.carte[4].GetHauteurValue())
        elif(IsPaire==1):
                #print("Paire",Hauteur(hauteur[0]).name,"/",Mon_Showdown.carte[0].GetHauteur(),Mon_Showdown.carte[1].GetHauteur(),Mon_Showdown.carte[2].GetHauteur())
                return ValeuretHauteur(1,hauteur[0],hauteur[0],Mon_Showdown.carte[0].GetHauteurValue(),Mon_Showdown.carte[1].GetHauteurValue(),Mon_Showdown.carte[2].GetHauteurValue())
        elif(IsPaire==2):
                #print("double Paire",Hauteur(hauteur[0]).name,Hauteur(hauteur[1]).name,"/",Mon_Showdown.carte[0].GetHauteur())
                return ValeuretHauteur(2,hauteur[0],hauteur[0],hauteur[1],hauteur[1],Mon_Showdown.carte[0].GetHauteurValue())
        
def ValeurHand(HeroHand,Board):
        arreter=0
        Mon_Showdown=SevenCard(HeroHand.carte[0],HeroHand.carte[1],Board.carte[0],Board.carte[1],Board.carte[2],Board.carte[3],Board.carte[4])
        Mon_Showdown_copie=SevenCard(HeroHand.carte[0],HeroHand.carte[1],Board.carte[0],Board.carte[1],Board.carte[2],Board.carte[3],Board.carte[4])
        Mon_Showdown.carte.sort(key=lambda Carte: Carte.ID,reverse=True)
        Mon_Showdown_copie.carte.sort(key=lambda Carte: Carte.ID,reverse=True)
        
        #quinteflush
        if(arreter==0):
                Result=IsCarre(Mon_Showdown)
                arreter=Result.valeur
                
        if(arreter==0):
                Result=IsFull(Mon_Showdown_copie)
                arreter=Result.valeur
                #print(arreter,":test2")
        if(arreter==0):
                Result=IsCouleur(Mon_Showdown)
                arreter=Result.valeur
                #print(arreter,":testcouleur")
        if(arreter==0):
                Result=IsSuite(Mon_Showdown)
                arreter=Result.valeur
                #print(arreter,":test suite")
        if(arreter==0):
                Result=IsBrelan(Mon_Showdown)
                arreter=Result.valeur
                #print(arreter,":test5")
        if(arreter==0):
                Result=IsPaire(Mon_Showdown) #double paire paire et hauteur
                arreter=Result.valeur

        return Result #ValeuretHauteur


def WhoWin(HeroHand,VilainHand,Board):
        #print("board: ",Board.afficher())
        ValeurHero=ValeurHand(HeroHand,Board)
        ValeurVilain=ValeurHand(VilainHand,Board)
        
        if(ValeurHero.valeur>ValeurVilain.valeur):
                return 1
        elif(ValeurHero.valeur<ValeurVilain.valeur):
                return -1
        else:
                i=0
                while(i<5):
                        if(ValeurHero.hauteur[i]>ValeurVilain.hauteur[i]):
                                return 1
                        elif(ValeurHero.hauteur[i]<ValeurVilain.hauteur[i]):
                                return -1       
                        i=i+1
                        
                return 0

def NumberToImgString(i):
        nom="2c.PNG"
        if(i//4==0):
                nom='2'+nom[1:]
        elif(i//4==1):
                nom='3'+nom[1:]
        elif(i//4==2):
                nom='4'+nom[1:]
        elif(i//4==3):
                nom='5'+nom[1:]
        elif(i//4==4):
                nom='6'+nom[1:]
        elif(i//4==5):
                nom='7'+nom[1:]
        elif(i//4==6):
                nom='8'+nom[1:]
        elif(i//4==7):
                nom='9'+nom[1:]
        elif(i//4==8):
                nom='T'+nom[1:]
        elif(i//4==9):
                nom='J'+nom[1:]
        elif(i//4==10):
                nom='Q'+nom[1:]
        elif(i//4==11):
                nom='K'+nom[1:]
        elif(i//4==12):
                nom='A'+nom[1:]
               # 
        if(i%4==0):
                nom=nom[0]+'h'+nom[2:]
        elif(i%4==1):
                nom=nom[0]+'d'+nom[2:]
        elif(i%4==2):
                nom=nom[0]+'s'+nom[2:]
        elif(i%4==3):
                nom=nom[0]+'c'+nom[2:]

        return "Assets/"+nom


def main():
        MonPacket=Packet()
        MonPacket.shuffle()
        MonPacket.shuffle()
        HeroHand=TwoCard(MonPacket.piocher(),MonPacket.piocher())#random
        VilainHand=TwoCard(MonPacket.piocher(),MonPacket.piocher())#random
        Mon_Board=Board(MonPacket.piocher(),MonPacket.piocher(),MonPacket.piocher(),MonPacket.piocher(),MonPacket.piocher())
        #print(HeroHand.afficher())
        #print(VilainHand.afficher())
        #print(Mon_Board.afficher())
        #print("--")

        
        #ValeurHand(HeroHand,Mon_Board)
        

        #print(MonPacket.tab[1].GetColor())
        #print(MonPacket.tab[1].GetHauteur())

        return WhoWin(HeroHand,VilainHand,Mon_Board)

def callback():
        global index2
        global label
        if index2==9:
                result=zelib.Quigagne(cartechoisi[0],cartechoisi[1],cartechoisi[2],cartechoisi[3],cartechoisi[4],cartechoisi[5],cartechoisi[6],cartechoisi[7],cartechoisi[8])
                
                if(result==0):
                        label.config(text="victoire")
                elif(result==1):
                        label.config(text="défaite")
                else:
                        label.config(text="égalité")

                print("------------------------")
        if index2==8:
            win=0
            n=0
            cartedispo=[]
            for i in range(52):
                cartedispo.append(i)
            for element in cartechoisi:
                cartedispo.remove(element)
            print(cartedispo)

            for river in cartedispo:
                result=zelib.Quigagne(cartechoisi[0],cartechoisi[1],cartechoisi[2],cartechoisi[3],cartechoisi[4],cartechoisi[5],cartechoisi[6],cartechoisi[7],river)
                n=n+1
                if(result==0):
                        win=win+1
                elif(result==-1):
                        win=win+0.5

            text=str(win/n*100)[:5]+" %  "
            label.config(text=text)

        if index2==7:
            win=0
            n=0
            cartedispo=[]
            for i in range(52):
                cartedispo.append(i)
            for element in cartechoisi:
                cartedispo.remove(element)
            print(cartedispo)

            for river in cartedispo:
                for turn in cartedispo:
                    if turn!=river:
                        result=zelib.Quigagne(cartechoisi[0],cartechoisi[1],cartechoisi[2],cartechoisi[3],cartechoisi[4],cartechoisi[5],cartechoisi[6],turn,river)
                        n=n+1
                        if(result==0):
                            win=win+1
                        elif(result==-1):
                            win=win+0.5

            text=str(win/n*100)[:5]+" %  "
            label.config(text=text)
        
def choosefct():
        doublon=0
        global index2
        global cartechoisi
        global photochoisi
        global canvasF1
        if index2<9:
                deplacement=50
                vfix=(v.get()+4)%52
                for i in range(len(cartechoisi)):
                        if cartechoisi[i]==vfix:
                                doublon=1
                if(doublon==0):                
                        cartechoisi.append(vfix)
                        img = ImageTk.PhotoImage(Image.open(NumberToImgString(v.get())))  
                        photochoisi.append(img)
                        print(NumberToImgString(v.get()))

                        if(index2==0):
                                deplacement=50
                        elif(index2==1):
                                deplacement=110
                        elif(index2==2):
                                deplacement=300
                        elif(index2==3):
                                deplacement=360
                        elif(index2==4):
                                deplacement=500
                        elif(index2==5):
                                deplacement=560
                        elif(index2==6):
                                deplacement=620
                        elif(index2==7):
                                deplacement=680
                        elif(index2==8):
                                deplacement=740
     
                        canvasF1.create_image(deplacement,50, image=photochoisi[index2]) 
                        index2+=1
                
        
def clearfct():
        global index2
        global cartechoisi
        global photochoisi
        global canvasF1

        index2=0
        cartechoisi=[]
        photochoisi=[]

#########
def callback2():
        global index3
        global cartechoisi2
        
        nbwin=0
        nbegal=0
        if index3==4:
            result=zelib.Equitemaincontremain(nbiteration.get(),cartechoisi2[0],cartechoisi2[1],cartechoisi2[2],cartechoisi2[3])  
            print(result)
            text=str(result*100)[:5]+" %  "
            label2.config(text=text)
            print("------------------------")
        
def choosefct2():
        doublon=0
        global index3
        global cartechoisi2
        global photochoisi2
        global canvasF2
        if index3<4:
                deplacement=50
                wfix=(w.get()+4)%52
                for i in range(len(cartechoisi2)):
                        if cartechoisi2[i]==wfix:
                                doublon=1
                if(doublon==0):                
                        cartechoisi2.append(wfix)
                        img = ImageTk.PhotoImage(Image.open(NumberToImgString(w.get()))) 
                        photochoisi2.append(img)
                        #print(NumberToImgString(wfix))

                        if(index3==0):
                              deplacement=50
                        elif(index3==1):
                                deplacement=110
                        elif(index3==2):
                                deplacement=640
                        elif(index3==3):
                                deplacement=700
                       
     
                        canvasF2.create_image(deplacement,50, image=photochoisi2[index3]) 
                        index3+=1
                
        
def clearfct2():
        global index3
        global cartechoisi2
        global photochoisi2
        global canvasF2

        index3=0
        cartechoisi2=[]
        photochoisi2=[]

def ShowWinorLoose():
        global index
        frames[index].grid_forget()
        index=1
        frames[1].grid(row=0)
def ShowPourcentage():
        global index
        frames[index].grid_forget()
        index=2
        frames[2].grid(row=0)
def ShowRange():
        global index
        frames[index].grid_forget()
        index=3
        frames[3].grid(row=0)

def Showsuited():
        global index
        frames[index].grid_forget()
        index=4
        frames[4].grid(row=0)

def ShowNash():
        global index
        frames[index].grid_forget()
        index=5
        frames[5].grid(row=0)

def onLeftClick1(event):
    global range1
    global canvasF31
    global rectangle1
    
    thistuple=showPosEvent(event)
    print(thistuple[1])
    if range1[thistuple[0]][thistuple[1]]==0:
        range1[thistuple[0]][thistuple[1]]=1
        rectangle1.append(canvasF31.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2 , fill="red")) 
    else:
        rectangle1.append(canvasF31.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2  , fill="white")) 
        range1[thistuple[0]][thistuple[1]]=0

def onLeftClick2(event):
    global range2
    global canvasF32
    global rectangle2
    thistuple=showPosEvent(event)
    print(thistuple[1])
    if range2[thistuple[0]][thistuple[1]]==0:
        range2[thistuple[0]][thistuple[1]]=1
        rectangle2.append(canvasF32.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2 , fill="red")) 
    else:
        rectangle2.append(canvasF32.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2  , fill="white")) 
        range2[thistuple[0]][thistuple[1]]=0


    
def showPosEvent(event):
    print ('Widget=%s X=%s Y=%s'%(event.widget, event.x,event.y))
    if(event.x>392):
        return (-1,-1)
    if(event.y>392):
        return (-1,-1)
    thistuple=((event.x-2)//30,(event.y-2)//30)
    
    return thistuple


def clearfct3import(numerocanvas):
    if numerocanvas==1:
        global range1
        global canvasF31
        global rectangle1
        for element in rectangle1:
            canvasF31.delete(element)
        for i in range(0,13):
            for j in range(0,13):
                range1[i][j]=0
    else:
        global range2
        global canvasF32
        global rectangle2  
        for element in rectangle2:
            canvasF32.delete(element)
        for i in range(0,13):
            for j in range(0,13):
                range2[i][j]=0
            
def clearfct3():
    global range1
    global range2
    global canvasF32
    global canvasF31
    global rectangle1
    for element in rectangle2:
        canvasF32.delete(element)
    for element in rectangle1:
        canvasF31.delete(element)
    for i in range(0,13):
        for j in range(0,13):
            range1[i][j]=0
            range2[i][j]=0

def callback3():
    global range1 
    global range2
    global nbiteration3
    global label33
    nb=0
    
    liste1=ConvertRangeBUG(range1)
    liste2=ConvertRangeBUG(range2)
    nbpick=nbiteration3.get()//35
    print(nbpick)

    choix1=(random.choices(liste1, k=nbpick))
    choix2=(random.choices(liste2, k=nbpick))
    print(choix2[0])
    result=0
    
    for i in range (0,nbpick):
        if(choix1[i][0]!=choix2[i][0] and choix1[i][0]!=choix2[i][1] and choix1[i][1]!=choix2[i][0] and choix1[i][1]!=choix2[i][1]):
            nb=nb+1
            tmp=zelib.EquitemaincontremainRandom(35,choix1[i][0],choix1[i][1],choix2[i][0],choix2[i][1],random.randrange(500000))
            result=result+tmp
            #print(tmp)    
    print(result/nb)
    text=str(result/nb*100)[:5]+" %  "
    label33.config(text=text)
    
def save32fct():
    global varEntre31
    global range2
    entre31=varEntre31.get()
    nomf="Save/"+entre31+".txt"
    fichier = open(nomf, "w")
    for x in range(0,13):
        for y in range(0,13):
            fichier.write(str(range2[x][y]))
    fichier.close()
    fichier = open("index.csv", "a")
    fichier.write(entre31+"\n")
    fichier.close()
    listeProduits.append(entre31+"\n")
    
    print(entre31+"savegardé ")
    
def save31fct():
    global varEntre31
    global range1
    global listeProduits
    global ComboBox31
    entre31=varEntre31.get()
    nomf=entre31+".txt"
    fichier = open(nomf, "w")
    for x in range(0,13):
        for y in range(0,13):
            fichier.write(str(range1[x][y]))
    fichier.close()
    fichier = open("index.csv", "a")
    fichier.write(entre31+"\n")
    fichier.close()
    listeProduits.append(entre31+"\n")
    ComboBox31["values"] = listeProduits
    
    
    print(entre31+"savegardé ")

def import31fct():
    global ComboBox31
    global range1
    global canvasF31
    global rectangle1

    clearfct3import(1)
    ComboBoxvaleur=ComboBox31.get()
    print("import "+ComboBoxvaleur)
    fichier = open(ComboBoxvaleur[0:len(ComboBoxvaleur)-1]+".txt", "r")
    contenu=fichier.read()
    for x in range(0,13):
        for y in range(0,13):
            range1[x][y]=int(contenu[13*x+y])
    fichier.close()
    
    for x in range(0,13):
        for y in range(0,13):
            if range1[x][y]==1:
                rectangle1.append(canvasF31.create_rectangle( (x)*30+2 , (y)*30+2 ,(1+x)*30+2 , (1+y)*30+2 , fill="red"))
    
def import32fct():
    global ComboBox31
    global range2
    global canvasF32
    global rectangle2

    clearfct3import(2)
    
    ComboBoxvaleur=ComboBox31.get()
    print("import "+ComboBoxvaleur)
    fichier = open(ComboBoxvaleur[0:len(ComboBoxvaleur)-1]+".txt", "r")
    contenu=fichier.read()
    for x in range(0,13):
        for y in range(0,13):
            range2[x][y]=int(contenu[13*x+y])
    fichier.close()
    
    for x in range(0,13):
        for y in range(0,13):
            if range2[x][y]==1:
                rectangle2.append(canvasF32.create_rectangle( (x)*30+2 , (y)*30+2 ,(1+x)*30+2 , (1+y)*30+2 , fill="red"))

            
    
    


def ConvertRangeBUG(range1):
    liste=[]
    print("a")
    for x in range(0,13):
        for y in range(0,13):
            #print(range1[x][y])
            if range1[y][x]==1:
                newx=(13-x)%13
                newy=(13-y)%13
                if x<y:
                    #suitted
                    liste.append((newx*4,newy*4))
                    liste.append((newx*4+1,newy*4+1))
                    liste.append((newx*4+2,newy*4+2))
                    liste.append((newx*4+3,newy*4+3))
                elif x==y:
                    #paire
                    liste.append((newx*4,newy*4+1))
                    liste.append((newx*4,newy*4+2))
                    liste.append((newx*4,newy*4+3))
                    liste.append((newx*4+1,newy*4+2))
                    liste.append((newx*4+1,newy*4+3))
                    liste.append((newx*4+2,newy*4+3))
                else:
                    #off
                    liste.append((newx*4,newy*4+1))
                    liste.append((newx*4,newy*4+2))
                    liste.append((newx*4,newy*4+3))
                    
                    liste.append((newx*4+1,newy*4))
                    liste.append((newx*4+1,newy*4+2))
                    liste.append((newx*4+1,newy*4+3))
                    
                    liste.append((newx*4+2,newy*4))
                    liste.append((newx*4+2,newy*4+1))
                    liste.append((newx*4+2,newy*4+3))

                    liste.append((newx*4+3,newy*4))
                    liste.append((newx*4+3,newy*4+1))
                    liste.append((newx*4+3,newy*4+2))

    return liste

def ConvertRange(range1):
    liste=[]
    for x in range(0,13):
        for y in range(0,13):
            if range1[y][x]==1:
                newx=(13-x)%13
                newy=(13-y)%13
                if x<y:
                    print("suited")
                    liste.append((newx,newy,1))
                elif(newx==newy):
                    #off
                    liste.append((newx,newy,2))
                else:
                    #off
                    liste.append((newx,newy,0))
    return liste
            

def callback4():
    global listbox
    global suited1
    global suited2
    global label43
    global nbiteration4
    
    tab=[]
    continuer=1
    for i in range(0,4):
        if listbox[i].get()=="":
            print("error")
            continuer=0
            break
        tab.append(lettertohauteur(listbox[i].get()))
    if(continuer):
        print(tab)
        result=0
        nbpick=nbiteration4.get()
        
        result=result+zelib.offorsuited(nbpick,tab[0],tab[1],suited1.get(),tab[2],tab[3],suited2.get(),random.randrange(100000))
            #print(result)
        result=result
        text=str(result*100)[:5]+" %  "
        label43.config(text=text)

def clearfct5import(numerocanvas):
    if numerocanvas==1:
        global range51
        global canvasF51
        global rectangle51
        for element in rectangle51:
            canvasF51.delete(element)
        for i in range(0,13):
            for j in range(0,13):
                range51[i][j]=0
    else:
        global range52
        global canvasF52
        global rectangle52  
        for element in rectangle52:
            canvasF52.delete(element)
        for i in range(0,13):
            for j in range(0,13):
                range52[i][j]=0
            
def clearfct5():
    global range51
    global range52
    global canvasF52
    global canvasF51
    global rectangle51
    for element in rectangle52:
        canvasF52.delete(element)
    for element in rectangle51:
        canvasF51.delete(element)
    for i in range(0,13):
        for j in range(0,13):
            range51[i][j]=0
            range52[i][j]=0

def getTuple(carteadverse):
    newx=(13-carteadverse[0])%13
    newy=(13-carteadverse[1])%13

    return (newx,newy,carteadverse[2])

    


def PushRangefct():
    global range52
    global canvas51
    global range51
    global rectangle51


    rangeFull=[]
    for x in range(13):
        for y in range(x,13):
            if(x==y):
                rangeFull.append((x,y,2))
            else:
                rangeFull.append((x,y,1))
                rangeFull.append((x,y,0))
        
    doubleBB=2*nombreBB.get()


    clearfct5import(1)
    for carte in rangeFull:
        EV=0
        totalCombo=0
        thistuple=getTuple(carte)
        for carteadverse in rangeFull:
            nbCombo=NombreCombo(carte,carteadverse)
            totalCombo=totalCombo+nbCombo
            
            tupleadv=getTuple(carteadverse)
            #print(range52[carteadverse[0]][carteadverse[1]])
            if (carteadverse[2]==0):
                if range52[carteadverse[0]][carteadverse[1]]==1:
                    equity=zelib.offorsuited(30,thistuple[0],thistuple[1],thistuple[2],tupleadv[0],tupleadv[1],tupleadv[2],random.randrange(100000))
                    EV=EV+(equity-0.5)*doubleBB*nbCombo
                else:
                    EV=EV+nbCombo
            else:
                if range52[carteadverse[1]][carteadverse[0]]==1:
                    equity=zelib.offorsuited(30,thistuple[0],thistuple[1],thistuple[2],tupleadv[0],tupleadv[1],tupleadv[2],random.randrange(100000))
                    EV=EV+(equity-0.5)*doubleBB*nbCombo
                else:
                    EV=EV+nbCombo

        if(EV>-0.5*totalCombo):
            if(carte[2]==0):
                range51[carte[0]][carte[1]]=1
                rectangle51.append(canvasF51.create_rectangle( (carte[0])*30+2 , (carte[1])*30+2 ,(1+carte[0])*30+2 , (1+carte[1])*30+2 , fill="red")) 
            else:
                range51[carte[1]][carte[0]]=1
                rectangle51.append(canvasF51.create_rectangle( (carte[1])*30+2 , (carte[0])*30+2 ,(1+carte[1])*30+2 , (1+carte[0])*30+2 , fill="red")) 
            
        else:
            if(carte[2]==0):
                range51[carte[0]][carte[1]]=0
            else:
                range51[carte[1]][carte[0]]=0

def CallRangefct():
    global range52
    global canvas52
    global range51
    global rectangle52

    rangeFull=[]
    for x in range(13):
        for y in range(x,13):
            if(x==y):
                rangeFull.append((x,y,2))
            else:
                rangeFull.append((x,y,1))
                rangeFull.append((x,y,0))

    doubleBB=2*nombreBB.get()
    clearfct5import(2)
    print(range51)
    rangePush=ConvertRange(range51)
    print(rangePush)

    for mainacall in rangeFull:
        EV=0
        totalCombo=0
        thistuple=getTuple(mainacall)
        for cartePush in rangePush:
            tupleadv=getTuple(cartePush)
            nbCombo=NombreCombo(mainacall,cartePush)
            totalCombo=totalCombo+nbCombo
            equity=zelib.offorsuited(30,thistuple[0],thistuple[1],thistuple[2],cartePush[0],cartePush[1],cartePush[2],random.randrange(100000))
            #print(thistuple,tupleadv)
            #print(equity)
            EV=EV+(equity-0.5)*doubleBB*nbCombo
                
        if(EV>-totalCombo):
            if(mainacall[2]==0):
                range52[mainacall[0]][mainacall[1]]=1
                rectangle52.append(canvasF52.create_rectangle( (mainacall[0])*30+2 , (mainacall[1])*30+2 ,(1+mainacall[0])*30+2 , (1+mainacall[1])*30+2 , fill="red")) 
            else:
                range52[mainacall[1]][mainacall[0]]=1
                rectangle52.append(canvasF52.create_rectangle( (mainacall[1])*30+2 , (mainacall[0])*30+2 ,(1+mainacall[1])*30+2 , (1+mainacall[0])*30+2 , fill="red")) 
            
        else:
            if(mainacall[2]==0):
                range52[mainacall[0]][mainacall[1]]=0
            else:
                range52[mainacall[1]][mainacall[0]]=1
            
def AutoNashfct():
    for i in range(3):
        PushRangefct()
        CallRangefct()

def save52fct():
    global varEntre51
    global range52
    entre51=varEntre51.get()
    nomf="Save/"+entre51+".txt"
    fichier = open(nomf, "w")
    for x in range(0,13):
        for y in range(0,13):
            fichier.write(str(range52[x][y]))
    fichier.close()
    fichier = open("index.csv", "a")
    fichier.write(entre51+"\n")
    fichier.close()
    listeProduits.append(entre51+"\n")
    
    print(entre51+"savegardé ")
    
def save51fct():
    global varEntre51
    global range51
    global listeProduits
    global ComboBox51
    entre51=varEntre51.get()
    nomf="Save/"+entre51+".txt"
    fichier = open(nomf, "w")
    for x in range(0,13):
        for y in range(0,13):
            fichier.write(str(range51[x][y]))
    fichier.close()
    fichier = open("index.csv", "a")
    fichier.write(entre51+"\n")
    fichier.close()
    listeProduits.append(entre51+"\n")
    ComboBox31["values"] = listeProduits

def import51fct():
    global ComboBox51
    global range51
    global canvasF51
    global rectangle51

    clearfct5import(1)
    ComboBoxvaleur=ComboBox51.get()
    print("import "+ComboBoxvaleur)
    fichier = open("Save/"+ComboBoxvaleur[0:len(ComboBoxvaleur)-1]+".txt", "r")
    contenu=fichier.read()
    for x in range(0,13):
        for y in range(0,13):
            range51[x][y]=int(contenu[13*x+y])
    fichier.close()
    
    for x in range(0,13):
        for y in range(0,13):
            if range51[x][y]==1:
                rectangle51.append(canvasF51.create_rectangle( (x)*30+2 , (y)*30+2 ,(1+x)*30+2 , (1+y)*30+2 , fill="red"))
    
def import52fct():
    global ComboBox51
    global range52
    global canvasF52
    global rectangle2

    clearfct5import(2)
    
    ComboBoxvaleur=ComboBox51.get()
    print("import "+ComboBoxvaleur)
    fichier = open("Save/"+ComboBoxvaleur[0:len(ComboBoxvaleur)-1]+".txt", "r")
    contenu=fichier.read()
    for x in range(0,13):
        for y in range(0,13):
            range52[x][y]=int(contenu[13*x+y])
    fichier.close()
    
    for x in range(0,13):
        for y in range(0,13):
            if range52[x][y]==1:
                rectangle52.append(canvasF52.create_rectangle( (x)*30+2 , (y)*30+2 ,(1+x)*30+2 , (1+y)*30+2 , fill="red"))

            
def onLeftClick51(event):
    global range51
    global canvasF51
    global rectangle51
    
    thistuple=showPosEvent(event)
    print(thistuple[1])
    if range51[thistuple[0]][thistuple[1]]==0:
        range51[thistuple[0]][thistuple[1]]=1
        rectangle51.append(canvasF51.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2 , fill="red")) 
    else:
        rectangle51.append(canvasF51.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2  , fill="white")) 
        range51[thistuple[0]][thistuple[1]]=0

def onLeftClick52(event):
    global range52
    global canvasF52
    global rectangle52
    thistuple=showPosEvent(event)
    print(thistuple[1])
    if range52[thistuple[0]][thistuple[1]]==0:
        range52[thistuple[0]][thistuple[1]]=1
        rectangle52.append(canvasF52.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2 , fill="red")) 
    else:
        rectangle52.append(canvasF52.create_rectangle( (thistuple[0])*30+2 , (thistuple[1])*30+2 ,(1+thistuple[0])*30+2 , (1+thistuple[1])*30+2  , fill="white")) 
        range52[thistuple[0]][thistuple[1]]=0

def NombreCombo(Tuple_Hero,My_Tuple):# (fixe , variabe)
    if(My_Tuple[2]==0):
        carteencommun=0
        if(My_Tuple[0]==Tuple_Hero[0]):
            carteencommun=carteencommun+1
        if(My_Tuple[0]==Tuple_Hero[1]):
            carteencommun=carteencommun+1
        if(My_Tuple[1]==Tuple_Hero[0]):
            carteencommun=carteencommun+1
        if(My_Tuple[1]==Tuple_Hero[1]):
            carteencommun=carteencommun+1
        if(carteencommun==0):
            return 12
        if(carteencommun==1):
            return 9
        if(carteencommun==2 and Tuple_Hero[2]==0):
            return 7
        return 6

    if(My_Tuple[2]==2):#yes
        carteencommun=0
        if(My_Tuple[0]==Tuple_Hero[0]):
            carteencommun=carteencommun+1
        if(My_Tuple[0]==Tuple_Hero[1]):
            carteencommun=carteencommun+1
        if(My_Tuple[1]==Tuple_Hero[0]):
            carteencommun=carteencommun+1
        if(My_Tuple[1]==Tuple_Hero[1]):
            carteencommun=carteencommun+1
        if(carteencommun==0):
            return 6
        if(carteencommun==2):
            return 3
        if(carteencommun==4):
            return 1

    if(My_Tuple[2]==1):#yes
        carteencommun=0
        if(My_Tuple[0]==Tuple_Hero[0]):
            carteencommun=carteencommun+1
        if(My_Tuple[0]==Tuple_Hero[1]):
            carteencommun=carteencommun+1
        if(My_Tuple[1]==Tuple_Hero[0]):
            carteencommun=carteencommun+1
        if(My_Tuple[1]==Tuple_Hero[1]):
            carteencommun=carteencommun+1
        if(carteencommun==0):
            return 4
        if(carteencommun==1):
            return 3
        if(carteencommun==2 and  Tuple_Hero[2]==1):
            return 3
        return 2
        
        
        
    

def lettertohauteur(char):
    if(char=='2'):
        return 1
    if(char=='3'):
        return 2
    if(char=='4'):
        return 3
    if(char=='5'):
        return 4
    if(char=='6'):
        return 5
    if(char=='7'):
        return 6
    if(char=='8'):
        return 7
    if(char=='9'):
        return 8
    if(char=='T'):
        return 9
    if(char=='J'):
        return 10
    if(char=='Q'):
        return 11
    if(char=='K'):
        return 12
    if(char=='A'):
        return 0
    return -1

    
        
##################

fenetre=Tk()
frames = [Frame(fenetre, width=500, height=500),Frame(fenetre, width=500, height=500),Frame(fenetre, width=500, height=500),Frame(fenetre, width=500, height=500),Frame(fenetre, width=500, height=500),Frame(fenetre, width=500, height=500)]
index = 0
index2=0
labelx=Label(frames[0],text="bonjour")
labelx.grid(columnspan=1)
frames[index].grid(row=0)

menu_widget = Menu(fenetre)
submenu_widget = Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Win or Loose",
                           command=ShowWinorLoose)
submenu_widget.add_command(label="% Win",
                           command=ShowPourcentage)
submenu_widget.add_command(label="range",
                           command=ShowRange)
submenu_widget.add_command(label="suitedORoff",
                           command=Showsuited)
submenu_widget.add_command(label="Nash",
                           command=ShowNash)
menu_widget.add_cascade(label="Menu", menu=submenu_widget)
fenetre.config(menu=menu_widget)

##win or loose
label =  Label(frames[1], text="")
button = Button(frames[1], text="calculate", command=callback)
choose = Button(frames[1], text="choose", command=choosefct)
clearbtn= Button(frames[1], text="clear", command=clearfct)

clearbtn.grid(row=13,column=11)
choose.grid(row=13,column=1)
label.grid(row=12,column=6)
button.grid(row=13,column=6)

LabelheroHand=Label(frames[1], text="Hero hand:")
LabelVilainHand=Label(frames[1], text="VilainHand:")
LabelBoard=Label(frames[1], text="Board:")

LabelheroHand.grid(row=9,column=1)
LabelVilainHand.grid(row=9,column=5)
LabelBoard.grid(row=9,column=9)

canvasF1 = Canvas(frames[1], width = 800, height = 100)
canvasF1.grid(row=10,columnspan=15)

#
v =IntVar()
photo=[]
cartechoisi=[]
photochoisi=[]
radiobutton_widget=[]
for i in range(0,52):
        nom=NumberToImgString(i)
                
        photo.append(PhotoImage(file=nom))
        
        radiobutton_widget.append( Radiobutton(frames[1],
                                   image=photo[i],
                                   variable=v, value=i,
                                   indicatoron=False))

        radiobutton_widget[i].grid(row=i%4,column=i//4)
## %Win
index3=0
w =IntVar()
photo2=[]
cartechoisi2=[]
photochoisi2=[]
radiobutton_widget2=[]
for i in range(0,52):
        nom=NumberToImgString(i)
                
        photo2.append(PhotoImage(file=nom))
        
        radiobutton_widget2.append( Radiobutton(frames[2],
                                   image=photo2[i],
                                   variable=w, value=i,
                                   indicatoron=False))

        radiobutton_widget2[i].grid(row=i%4,column=i//4)

label2 =  Label(frames[2], text="")
nbiteration=IntVar()
scale = Scale( frames[2],variable = nbiteration, from_ = 10000, to = 2000000, orient = HORIZONTAL) 
button2 = Button(frames[2], text="calculate", command=callback2)
choose2 = Button(frames[2], text="choose", command=choosefct2)
clearbtn2= Button(frames[2], text="clear", command=clearfct2)


clearbtn2.grid(row=13,column=11)
choose2.grid(row=13,column=1)
label2.grid(row=12,column=6)
button2.grid(row=13,column=6)
scale.grid(row=9,columnspan=14) 

LabelheroHand2=Label(frames[2], text="Hero hand:")
LabelVilainHand2=Label(frames[2], text="VilainHand:")

LabelheroHand2.grid(row=9,column=1)
LabelVilainHand2.grid(row=9,column=10)

canvasF2 = Canvas(frames[2], width = 800, height = 100)
canvasF2.grid(row=10,columnspan=15)


## Range

range1=[]
range2=[]
rectangle1=[]
rectangle2=[]
nbiteration3=IntVar()
label33 =  Label(frames[3], text="")

for i in range(0,13):
    ligne=[]
    ligne2=[]
    for j in range(0,13):
        ligne.append(0)
        ligne2.append(0)
   
    range1.append(ligne)
    range2.append(ligne2)

    
canvasF31 = Canvas(frames[3], width = 388, height = 388,bg='#ffffff',relief=FLAT)
for i in range(0,14):
        canvasF31.create_line(2+30*i, 0, 2+30*i, 392)
        canvasF31.create_line(0, 2+30*i, 392, 2+30*i)

canvasF31.grid(row=1,column=1,padx=5,ipadx=2,pady=5,ipady=2)
canvasF31.bind('<Button-1>', onLeftClick1)
canvasF32 = Canvas(frames[3], width = 388, height = 388,bg='#ffffff',relief=FLAT)
canvasF32.bind('<Button-1>', onLeftClick2)
for i in range(14):
        canvasF32.create_line(2+30*i, 0, 2+30*i, 392)
        canvasF32.create_line(0, 2+30*i, 392, 2+30*i)
canvasF32.grid(row=1,column=2,padx=5,ipadx=2,pady=5,ipady=2)

button3 = Button(frames[3], text="calculate", command=callback3)
clearbtn3= Button(frames[3], text="clear", command=clearfct3)
scale3 = Scale( frames[3],variable = nbiteration3, from_ = 100000, to = 10000000, orient = HORIZONTAL)

save31=Button(frames[3], text="save", command=save31fct)
save32=Button(frames[3], text="save", command=save32fct)

import31=Button(frames[3], text="import", command=import31fct)
import32=Button(frames[3], text="import", command=import32fct)



varEntre31=StringVar()


entry31 = Entry(frames[3],textvariable=varEntre31,width=40)


listeProduits=[]
fichier = open("index.csv", "r")
for ligne in fichier:
    listeProduits.append(ligne)
fichier.close()


ComboBox31 = ttk.Combobox(frames[3], values=listeProduits) #ComboBox31.get
ComboBox31.current(0)


ComboBox31.grid(row=0,columnspan=4)

entry31.grid(row=2, columnspan=2, column=1)

save31.grid(row=2,column=1)
save32.grid(row=2,column=2)

import31.grid(row=0,column=1)
import32.grid(row=0,column=2)

scale3.grid(row=3,columnspan=4)
button3.grid(row=3,column=1)
clearbtn3.grid(row=3,column=2)
label33.grid(row=4,columnspan=4)

##suited ou offsuit

label41=Label(frames[4],text="Hero:")
label42=Label(frames[4],text="Vilain:")
label43 =  Label(frames[4], text="")
nbiteration4=IntVar()

listbox=[]


listbox.append(ttk.Combobox(frames[4],values=["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K","A"]))
listbox.append(ttk.Combobox(frames[4],values=["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K","A"]))
listbox.append(ttk.Combobox(frames[4],values=["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K","A"]))
listbox.append(ttk.Combobox(frames[4],values=["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K","A"]))

suited1=IntVar()
check1 = Checkbutton(frames[4], text="suited", variable=suited1)
suited2=IntVar()
check2 = Checkbutton(frames[4], text="suited", variable=suited2)

button4 = Button(frames[4], text="calculate", command=callback4)
scale4 = Scale( frames[4],variable = nbiteration4, from_ = 10000, to = 2000000, orient = HORIZONTAL) 

scale4.grid(row=3,columnspan=4)

button4.grid(row=5,columnspan=4)

listbox[0].grid(row=1,column=1,padx=5,pady=10)
listbox[1].grid(row=1,column=2,padx=5,pady=10)
listbox[2].grid(row=2,column=1,padx=5,pady=10)
listbox[3].grid(row=2,column=2,padx=5,pady=10)
check1.grid(row=1,column=3,padx=5,pady=10)
check2.grid(row=2,column=3,padx=5,pady=10)
label41.grid(row=1,column=0)
label42.grid(row=2,column=0)
label43.grid(row=4,columnspan=4)

##NASH

range51=[]
range52=[]
rectangle51=[]
rectangle52=[]
nombreBB=IntVar()
label53 =  Label(frames[5], text="")

for i in range(0,13):
    ligne51=[]
    ligne52=[]
    for j in range(0,13):
        ligne51.append(0)
        ligne52.append(0)
   
    range51.append(ligne51)
    range52.append(ligne52)

    
canvasF51 = Canvas(frames[5], width = 388, height = 388,bg='#ffffff',relief=FLAT)
for i in range(0,14):
        canvasF51.create_line(2+30*i, 0, 2+30*i, 392)
        canvasF51.create_line(0, 2+30*i, 392, 2+30*i)

canvasF51.grid(row=1,column=1,padx=5,ipadx=2,pady=5,ipady=2)
canvasF51.bind('<Button-1>', onLeftClick51)
canvasF52 = Canvas(frames[5], width = 388, height = 388,bg='#ffffff',relief=FLAT)
canvasF52.bind('<Button-1>', onLeftClick52)
for i in range(14):
        canvasF52.create_line(2+30*i, 0, 2+30*i, 392)
        canvasF52.create_line(0, 2+30*i, 392, 2+30*i)
canvasF52.grid(row=1,column=2,padx=5,ipadx=2,pady=5,ipady=2)

button5 = Button(frames[5], text="PushRangefct", command=PushRangefct)
buttoncall5= Button(frames[5], text="CallRangefct", command=CallRangefct)
button5auto= Button(frames[5], text="auto", command=AutoNashfct)
clearbtn5= Button(frames[5], text="clear", command=clearfct5)
scale51 = Scale( frames[5],variable = nombreBB, from_ = 1, to = 20, orient = HORIZONTAL)

save51=Button(frames[5], text="save", command=save51fct)
save52=Button(frames[5], text="save", command=save52fct)

import51=Button(frames[5], text="import", command=import51fct)
import52=Button(frames[5], text="import", command=import52fct)

varEntre51=StringVar()

entry51 = Entry(frames[5],textvariable=varEntre51,width=40)

ComboBox51 = ttk.Combobox(frames[5], values=listeProduits) #ComboBox31.get
ComboBox51.current(0)


ComboBox51.grid(row=0,columnspan=4)

entry51.grid(row=2, columnspan=2, column=1)

save51.grid(row=2,column=1)
save52.grid(row=2,column=2)

import51.grid(row=0,column=1)
import52.grid(row=0,column=2)

scale51.grid(row=4,columnspan=4)
button5.grid(row=3,column=1)
button5auto.grid(row=6,columnspan=4)
buttoncall5.grid(row=3,column=2)
clearbtn5.grid(row=5,columnspan=4)



fenetre.mainloop()
