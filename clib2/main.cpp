#include "main.h"
#include "main2.h"
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */


extern "C"
    {
        int multiplier(long a, long b)
        {

            return a * b;
        }


    carte initCarteParId(int i);
    carte initCarteParHautCoul(char hauteur, int couleur);
    valeur IsSuite(showdown hero) ;
    showdown retirerdoublon(showdown hero1);

    void jeuNeuf(carte jeu[NB_CARTES] )
            {
                for ( int i = 0 ; i < NB_CARTES  ; ++i )
                {
                jeu[i]=initCarteParId(i);
                }
            }
            void affichegagnant(int gagnanttamp,int* loose,int* draw,int* win)
            {
                if (gagnanttamp==1)
                {
                    //printf("Vous avez perdu \n");
                    (*loose)++;
                }
                if (gagnanttamp==0)
                {
                    //printf("Vous avez gagné \n");
                    (*win)++;
                    }
                if (gagnanttamp==-1)
                {
                        //printf("égalité \n");
                    (*draw)++;
                }
            }
            int melangerJeu( carte cartes[] ) {
               for ( int i = 0 ; i < NB_CARTES ; ++i ) {
                  int j = rand() % NB_CARTES;                // choix d'une position au hasard
                  carte tmp = cartes[i];             // échange de la carte à cette position
                  cartes[i] = cartes[j];
                  cartes[j] = tmp;
               }
               return NB_CARTES - 1;          // retourne l'indice prochaine carte
            }

            carte carteSuivante( carte cartes[] , int* pindice )
            {
               return cartes[(*pindice)--];   // extrait la carte, et passe à l'indice suivant

            }
            void affichercartes(carte cartes)
            {
                //printf("hauteur:%c et couleur:%d \n",cartes.hauteur,cartes.couleur);
            }
            showdown trihauteur(showdown hero) // ordre décroissant
            {
                int i=6;
                int j;
                int maxi;
                carte temp;

                while(i>-1)
                {
                    //printf("test %c,%c,%c,%c,%c,%c,%c,",hero.carte[0].hauteur,hero.carte[1].hauteur,hero.carte[2].hauteur,hero.carte[3].hauteur,hero.carte[4].hauteur,hero.carte[5].hauteur,hero.carte[6].hauteur);
                    maxi=0;
                    for(j=0; j<=i; j++)
                    {
                        if(hero.carte[j].mothauteur>hero.carte[maxi].mothauteur)
                        {
                            maxi=j;
                        }
                    }
                    temp=hero.carte[i];
                    hero.carte[i]=hero.carte[maxi];
                    hero.carte[maxi]=temp;
                    i--;
                }

                return  hero;
            }

            valeur Initzero(valeur* zero)
            {
                valeur zera=*zero;
                int i;
                for(i=0; i<6; i++)
                {
                   zera.valeurs[i]=0;
                }
                return zera;
            }

            valeur IsPair(showdown hero) //100 %
            {
                valeur res;
                res=Initzero(&res);
                int i;
                int j=2;
                for(i=5; i>-1; i--)
                {
                    if(hero.carte[i].hauteur==hero.carte[i+1].hauteur && res.valeurs[0]<2)
                    {
                        res.valeurs[0]=res.valeurs[0]+1;
                        res.valeurs[res.valeurs[0]]=hero.carte[i].mothauteur;
                    }
                }
                if (res.valeurs[0]==2)
                {
                    if(res.valeurs[1]==hero.carte[5].mothauteur  && res.valeurs[1]==hero.carte[6].mothauteur)
                    {
                        if(res.valeurs[2]==hero.carte[4].mothauteur)
                        {
                            res.valeurs[3]=hero.carte[2].mothauteur;
                        }
                        else
                        {
                            res.valeurs[3]=hero.carte[4].mothauteur;
                        }
                    }
                    else{res.valeurs[3]=hero.carte[6].mothauteur;}
                }
                else if(res.valeurs[0]==1)
                {
                    for(i=6; i>-1; i--)
                    {
                        if(res.valeurs[1]!=hero.carte[i].mothauteur && j<5)
                        {
                            res.valeurs[j]=hero.carte[i].mothauteur;
                            j++;
                        }
                    }
                }
                return res;
            }
            valeur IsBrelan(showdown hero) //100%
            {
                valeur res;
                res=Initzero(&res);
                int i;
                for(i=0; i<5; i++)
                {
                    if(hero.carte[i].hauteur==hero.carte[i+1].hauteur && hero.carte[i+1].hauteur==hero.carte[i+2].hauteur)
                    {
                        res.valeurs[0]=3;
                        res.valeurs[1]=hero.carte[i].mothauteur;
                        if(i==4)
                        {
                            res.valeurs[2]=hero.carte[3].mothauteur;
                            res.valeurs[3]=hero.carte[2].mothauteur;
                        }
                        else if(i==3)
                        {
                            res.valeurs[2]=hero.carte[6].mothauteur;
                            res.valeurs[3]=hero.carte[2].mothauteur;
                        }
                        else
                        {
                            res.valeurs[2]=hero.carte[6].mothauteur;
                            res.valeurs[3]=hero.carte[5].mothauteur;
                        }
                    }
                }
                return res;
            }
            valeur IsCarre(showdown hero, valeur valeurpre)  // 100%
            {
                valeur res;
                res=valeurpre;
                int i;
                for(i=0; i<4; i++)
                {
                    if(hero.carte[i].mothauteur==hero.carte[i+1].mothauteur && hero.carte[i+1].mothauteur==hero.carte[i+2].mothauteur && hero.carte[i+2].mothauteur==hero.carte[i+3].mothauteur)
                    {
                        res=Initzero(&res);
                        res.valeurs[0]=7;
                        res.valeurs[1]=hero.carte[i].mothauteur;
                        if(hero.carte[i].mothauteur==hero.carte[6].mothauteur)
                        {
                            res.valeurs[2]=hero.carte[2].mothauteur;
                        }
                        else
                        {
                            res.valeurs[2]=hero.carte[6].mothauteur;
                        }
                    }
                }
                return res;
            }
            valeur IsFull(showdown hero, valeur valeurpre) //100 %
            {
                valeur res;
                res=valeurpre;
                int i;
                int j;
                for(i=0; i<5; i++)
                {
                    if(hero.carte[i].mothauteur==hero.carte[i+1].mothauteur && hero.carte[i+1].mothauteur==hero.carte[i+2].mothauteur)
                    {
                        for(j=0; j<6; j++)
                        {
                            if(j !=i && j!=(i+1) && hero.carte[j].hauteur==hero.carte[j+1].hauteur)
                            {
                                res=Initzero(&res);
                                res.valeurs[0]=6;
                                res.valeurs[1]=hero.carte[i].mothauteur;
                                res.valeurs[2]=hero.carte[j].mothauteur;
                            }
                        }
                    }
                }
                return res;
            }
            valeur IsQuinteFlush(showdown hero, valeur valeurpre)
            {
                int n,j,i;

                showdown cartesuite;
                valeur resnew;
                for(j=3; j>-1; j--)
                {
                    n=0;
                    for(i=6; i>-1; i--)
                    {
                        if(hero.carte[i].couleur==j)
                        {

                            cartesuite.carte[n]=hero.carte[i];
                            n++;
                        }
                    }
                    if(n>4)
                    {
                        resnew=IsSuite(trihauteur(cartesuite));
                        if (resnew.valeurs[0]!=0)
                            {
                                valeurpre.valeurs[0]=8;
                                for(i=1;i<6;i++)
                                {
                                    valeurpre.valeurs[i]=resnew.valeurs[i];
                                }
                            }
                    }
                }
                return valeurpre;
            }
            showdown retirerdoublon(showdown hero)
            {
                int i;
                int j;
                carte tampo;
                for(i=0; i<6; i++)
                {
                    if(hero.carte[i].mothauteur==hero.carte[i+1].mothauteur)
                    {
                        tampo=hero.carte[1+i];
                        for(j=i+1;j<6;j++)
                        {
                            hero.carte[j]=hero.carte[j+1];
                        }
                        hero.carte[6]=tampo;
                    }
                }
                return hero;
            }
            valeur IsSuite(showdown hero) // 90 % manque A quand =1
            {
                //printf("%d %d %d %d %d %d %d  azeeazaz",hero.carte[0].mothauteur,hero.carte[1].mothauteur,hero.carte[2].mothauteur,hero.carte[3].mothauteur,hero.carte[4].mothauteur,hero.carte[5].mothauteur,hero.carte[6].mothauteur);
                valeur res;
                res=Initzero(&res);
                int i;
                showdown hero2= retirerdoublon(hero);

                for(i=6; i>3; i--)
                {

                    if( (hero2.carte[i].mothauteur==(hero2.carte[i-1].mothauteur+1) && hero2.carte[i-1].mothauteur==(hero2.carte[i-2].mothauteur+1) && hero2.carte[i-2].mothauteur==(hero2.carte[i-3].mothauteur+1) &&hero2.carte[i-3].mothauteur==(hero2.carte[i-4].mothauteur+1))&&(res.valeurs[0]==0))
                    {

                        res.valeurs[0]=4;
                        res.valeurs[1]=hero.carte[i].mothauteur;

                    }

                }
                for(i=6; i>3; i--)
                {
                if((hero2.carte[i].hauteur=='A' && hero2.carte[0].hauteur=='2' && hero2.carte[1].mothauteur==(hero2.carte[0].mothauteur+1) &&hero2.carte[2].mothauteur==(hero2.carte[1].mothauteur+1) &&hero2.carte[3].mothauteur==(hero2.carte[2].mothauteur+1))&&(res.valeurs[0]==0))
                    {
                        res.valeurs[0]=4;
                        res.valeurs[1]=2;
                    }
                }
                //printf("%d ",res.valeurs[0]);
                return res;
            }
            valeur IsCouleur(showdown hero) // 100 %
            {
                valeur res;
                res=Initzero(&res);
                int i;
                int j;
                int k[7];
                int n;
                for(j=3; j>-1; j--)
                {
                    n=0;
                    for(i=6; i>-1; i--)
                    {
                        if(hero.carte[i].couleur==j)
                        {


                            k[n]=hero.carte[i].mothauteur;
                            n++;
                        }
                    }
                    if(n>4)
                    {
                        res.valeurs[0]=5;
                        res.valeurs[1]=k[0];
                        res.valeurs[2]=k[1];
                        res.valeurs[3]=k[2];
                        res.valeurs[4]=k[3];
                        res.valeurs[5]=k[4];
                    }
                }


                return res;
            }
            valeur Hauteur(showdown hero) // 100 %
            {
                valeur res;
                int i;
                res=Initzero(&res);
                res.valeurs[0]=0;
                for(i=1; i<6; i++)
                {
                    res.valeurs[i]=hero.carte[7-i].mothauteur;
                }
                return res;
            }
            valeur Force(showdown hero)
            {
                int p=0;  // compteur quinte flush
                int q=0;// compteur carre et full
                valeur res;
                res=Initzero(&res);
                hero=trihauteur(hero);

                //printf("testb %d %d %d %d %d %d  \n",res.valeurs[0],res.valeurs[1],res.valeurs[2],res.valeurs[3],res.valeurs[4],res.valeurs[5]);

                res=IsCouleur(hero);  // 5
                if(res.valeurs[0]==5)
                {
                    p++;
                }
                if(res.valeurs[0]==0)
                {
                    res=IsSuite(hero);
                }   // 4
                if(res.valeurs[0]==0)
                {
                    res=IsBrelan(hero); //3
                    if(res.valeurs[0]==3)
                    {
                        q++;
                    }
                }  //3
                if(res.valeurs[0]==0){res=IsPair(hero);}  // 1 et 2
                if(res.valeurs[0]==0)  //0
                {
                    res=Hauteur(hero);
                }

                //printf("testc %d %d %d %d %d %d  \n",res.valeurs[0],res.valeurs[1],res.valeurs[2],res.valeurs[3],res.valeurs[4],res.valeurs[5]);
                if (q && res.valeurs[0]<7)
                {
                    res=IsCarre(hero,res); // 7
                }
                if (q && res.valeurs[0]<6){res=IsFull(hero,res);}
                if (p)
                    {
                        res=IsQuinteFlush(hero,res);
                }
                //printf("%d dzdz  \n",res.valeurs[0]);
                //printf("cartes1 %c,%c,%c,%c,%c,%c,%c, \n",hero.carte[0].hauteur,hero.carte[1].hauteur,hero.carte[2].hauteur,hero.carte[3].hauteur,hero.carte[4].hauteur,hero.carte[5].hauteur,hero.carte[6].hauteur);
                //printf("testb %d %d %d %d %d %d  \n",res.valeurs[0],res.valeurs[1],res.valeurs[2],res.valeurs[3],res.valeurs[4],res.valeurs[5]);

                return res;
            }
            int compare(valeur herovaleur,valeur vilainvaleur)
            {
                int boole=-1;
                int i=0;
                //printf("hero draw valeur %d %d %d %d %d %d  \n",herovaleur.valeurs[0],herovaleur.valeurs[1],herovaleur.valeurs[2],herovaleur.valeurs[3],herovaleur.valeurs[4],herovaleur.valeurs[5]);
                //printf("vilain draw valeur %d %d %d %d %d %d  \n",vilainvaleur.valeurs[0],vilainvaleur.valeurs[1],vilainvaleur.valeurs[2],vilainvaleur.valeurs[3],vilainvaleur.valeurs[4],vilainvaleur.valeurs[5]);
                do
                {
                    if(herovaleur.valeurs[i]>vilainvaleur.valeurs[i])
                    {
                        boole=0;
                        //printf("hero valeur %d %d %d %d %d %d  \n",herovaleur.valeurs[0],herovaleur.valeurs[1],herovaleur.valeurs[2],herovaleur.valeurs[3],herovaleur.valeurs[4],herovaleur.valeurs[5]);
                    }
                    else if(herovaleur.valeurs[i]<vilainvaleur.valeurs[i])
                    {
                        boole=1;
                        //printf("vilain valeur %d %d %d %d %d %d  \n",vilainvaleur.valeurs[0],vilainvaleur.valeurs[1],vilainvaleur.valeurs[2],vilainvaleur.valeurs[3],vilainvaleur.valeurs[4],vilainvaleur.valeurs[5]);
                    }
                    i++;
                }while (i<6 && boole==-1);
                //printf("a %d  \n",boole);
                return boole;
            }
            int gagnant(carte catehero[2],carte cartevlan[2],carte board[5])
            {
                int i;
                int gagnant;
                valeur herovaleur;
                herovaleur=Initzero(&herovaleur);
                valeur vilainvaleur;
                vilainvaleur=Initzero(&vilainvaleur);
                showdown hero;
                for (i=0 ; i<2; i++)
                {
                    hero.carte[i]=catehero[i];
                }
                for (i=2 ; i<7; i++)
                {
                    hero.carte[i]=board[i-2];
                }
                showdown vilain;
                for (i=0 ; i<2; i++)
                {
                    vilain.carte[i]=cartevlan[i];
                }
                for (i=2 ; i<7; i++)
                {
                    vilain.carte[i]=board[i-2];
                }
                herovaleur=Force(hero);
                vilainvaleur=Force(vilain);
                //printf("hero %c,%c,%c,%c,%c,%c,%c, \n",hero.carte[0].hauteur,hero.carte[1].hauteur,hero.carte[2].hauteur,hero.carte[3].hauteur,hero.carte[4].hauteur,hero.carte[5].hauteur,hero.carte[6].hauteur);
                //printf("hero %d,%d,%d,%d,%d,%d,%d, \n",hero.carte[0].couleur,hero.carte[1].couleur,hero.carte[2].couleur,hero.carte[3].couleur,hero.carte[4].couleur,hero.carte[5].couleur,hero.carte[6].couleur);
                //printf("hero %d,%d,%d,%d,%d,%d,%d, \n",hero.carte[0].carteID,hero.carte[1].carteID,hero.carte[2].carteID,hero.carte[3].carteID,hero.carte[4].carteID,hero.carte[5].carteID,hero.carte[6].carteID);
                //printf("vilain %c,%c,%c,%c,%c,%c,%c, \n",vilain.carte[0].hauteur,vilain.carte[1].hauteur,vilain.carte[2].hauteur,vilain.carte[3].hauteur,vilain.carte[4].hauteur,vilain.carte[5].hauteur,vilain.carte[6].hauteur);

                gagnant=compare(herovaleur,vilainvaleur);
                return gagnant;
            }
            void Supprimercarte(int ID, carte cartes[NB_CARTES])
            {
                int i=NB_CARTES-1;
                while(cartes[i].carteID!=ID)
                {
                    i--;
                }
                carte temp=cartes[i];
                while(i>0)
                {
                    cartes[i]=cartes[i-1];
                    i--;
                }
                cartes[0]=temp;
                for(i=51;i>-1;i--)
                {
                    //printf(" aaa %d \n",cartes[i].carteID);
                }
            }
            carte initCarteParHautCoul(char hauteur, int couleur)
            {
                carte carteInitialise;
                carteInitialise.hauteur=hauteur;
                switch (couleur)
                {
                case 0:carteInitialise.couleur=coeur;
                    break;
                case 1:carteInitialise.couleur=carreaux;
                    break;
                case 2:carteInitialise.couleur=trefle;
                    break;
                case 3:carteInitialise.couleur=pique;
                    break;
                }
                switch(hauteur)
                {
                    case '2':carteInitialise.mothauteur=deux;
                        break;
                    case '3':carteInitialise.mothauteur=trois;
                        break;
                    case '4':carteInitialise.mothauteur=quatre;
                        break;
                    case '5':carteInitialise.mothauteur=cinq;
                        break;
                    case '6':carteInitialise.mothauteur=six;
                        break;
                    case '7':carteInitialise.mothauteur=sept;
                        break;
                    case '8':carteInitialise.mothauteur=huit;
                        break;
                    case '9':carteInitialise.mothauteur=neuf;
                        break;
                    case 'T':carteInitialise.mothauteur=T;
                        break;
                    case 'J':carteInitialise.mothauteur=J;
                        break;
                    case 'Q':carteInitialise.mothauteur=Q;
                        break;
                    case 'K':carteInitialise.mothauteur=K;
                        break;
                    case 'A':carteInitialise.mothauteur=A;
                        break;
                }
                carteInitialise.carteID=(couleur+4*((carteInitialise.mothauteur)+1))%52;
                return carteInitialise;
            }
            carte initCarteParId(int i)
            {
                carte carteInitialise;
                carteInitialise.carteID = i;
                int valeur=1+(i/4);
                switch (valeur)
                {
                    case 2: carteInitialise.hauteur='2';
                            carteInitialise.mothauteur=deux;
                    break;
                    case 3:carteInitialise.hauteur='3';
                        carteInitialise.mothauteur=trois;
                    break;
                    case 4:carteInitialise.hauteur='4';
                        carteInitialise.mothauteur=quatre;
                    break;
                    case 5:carteInitialise.hauteur='5';
                    carteInitialise.mothauteur=cinq;
                    break;
                    case 6:carteInitialise.hauteur='6';
                    carteInitialise.mothauteur=six;
                    break;
                    case 7:carteInitialise.hauteur='7';
                    carteInitialise.mothauteur=sept;
                    break;
                    case 8:carteInitialise.hauteur='8';
                    carteInitialise.mothauteur=huit;
                    break;
                    case 9:carteInitialise.hauteur='9';
                    carteInitialise.mothauteur=neuf;
                    break;
                    case 10:carteInitialise.hauteur='T';
                        carteInitialise.mothauteur=T;
                    break;
                    case 11:carteInitialise.hauteur='J';
                        carteInitialise.mothauteur=J;
                    break;
                    case 12:carteInitialise.hauteur='Q';
                        carteInitialise.mothauteur=Q;
                    break;
                    case 13:carteInitialise.hauteur='K';
                        carteInitialise.mothauteur=K;
                    break;
                    case 1:carteInitialise.hauteur='A';
                        carteInitialise.mothauteur=A;
                    break;
                }
                int couleur=i%4;
                switch (couleur)
                {
                case 0:carteInitialise.couleur=coeur;
                    break;
                case 1:carteInitialise.couleur=carreaux;
                    break;
                case 2:carteInitialise.couleur=trefle;
                    break;
                case 3:carteInitialise.couleur=pique;
                    break;
                }
                return carteInitialise;
            }
            void DealBoardftr(carte flop[3],carte turn[1],carte rver[1],carte board[5],carte cartes[NB_CARTES],int* indiceptr)
            {
                //printf(" flop \n");
                int i=0;
                while ( i< 3)
                {
                    carte cartepioche = carteSuivante( cartes , indiceptr );
                    //affichercartes(cartepioche);
                    flop[i]=cartepioche;
                    board[i]=cartepioche;
                    i++;
                }
                //printf(" turn \n");
                carte cartepioche = carteSuivante( cartes , indiceptr );
                //affichercartes(cartepioche);
                turn[0]=cartepioche;
                board[3]=cartepioche;

               // printf(" river \n");

                cartepioche = carteSuivante( cartes , indiceptr );
                //affichercartes(cartepioche);
                rver[0]=cartepioche;
                board[4]=cartepioche;
            }
            void DealBoard(carte board[5],carte cartes[NB_CARTES],int* indiceptr)
            {
                //printf(" flop \n");
                int i=0;
                while ( i< 3)
                {
                    carte cartepioche = carteSuivante( cartes , indiceptr );
                    //affichercartes(cartepioche);
                    board[i]=cartepioche;
                    i++;
                }
                //printf(" turn \n");
                carte cartepioche = carteSuivante( cartes , indiceptr );
                //affichercartes(cartepioche);
                //turn[0]=cartepioche;
                board[3]=cartepioche;

               // printf(" river \n");

                cartepioche = carteSuivante( cartes , indiceptr );
                //affichercartes(cartepioche);
                //rver[0]=cartepioche;
                board[4]=cartepioche;
            }
            void DealPocket(carte cartepocket[2],carte cartes[NB_CARTES],int* indiceptr)
            {
                int i=0;
                //printf("votre main est \n");
                while ( i< 2 )
                {
                    carte cartepioche = carteSuivante( cartes , indiceptr );
                    //affichercartes(cartepioche);
                    cartepocket[i]=cartepioche;
                    i++;
                }

            }
            double  MainHasard(int nbsimulation)
            {
                int win=0;
                int loose=0;
                int draw=0;
                int n=0;
                carte cartes[NB_CARTES];
                carte catehero[2];
                carte cartevlan[2];
                carte board[5];
                srand(time(NULL));



                    do
                    {
                        jeuNeuf(cartes);
                        int indice = melangerJeu(cartes);
                        indice = melangerJeu(cartes);
                        indice = melangerJeu(cartes);
                        indice = melangerJeu(cartes);
                        indice = melangerJeu(cartes);
                        DealPocket(catehero,cartes,&indice);
                        DealPocket(cartevlan,cartes,&indice);
                        DealBoard(board,cartes,&indice);
                        n++;
                        int gagnanttamp=gagnant(catehero,cartevlan,board);
                        affichegagnant(gagnanttamp,&loose,&draw,&win);
                    }
                    while(n<nbsimulation);//gagnanttamp.valeurs[0]==0
                    return (win+0.5*draw)/(float)n;

            }
            double  Equitemaincontremain(int nbsimulation,int hero1,int hero2,int vilain1,int vilain2)
            {
                int win=0;
                int loose=0;
                int draw=0;
                int n=0;
                carte cartes[NB_CARTES];
                carte catehero[2];
                carte cartevlan[2];
                carte board[5];
                srand(time(NULL));

                printf("equite main vs opp \n");
                printf("Combien de main à simuler \n");

                    catehero[0]=initCarteParId(hero1);
                    catehero[1]=initCarteParId(hero2);
                    cartevlan[0]=initCarteParId(vilain1);
                    cartevlan[1]=initCarteParId(vilain2);
                    do
                    {

                        jeuNeuf(cartes);
                        int indice = melangerJeu(cartes);
                        indice = melangerJeu(cartes);
                        Supprimercarte(catehero[0].carteID,cartes);
                        Supprimercarte(cartevlan[0].carteID,cartes);
                        Supprimercarte(catehero[1].carteID,cartes);
                        Supprimercarte(cartevlan[1].carteID,cartes);
                        n++;
                        DealBoard(board,cartes,&indice);
                        int gagnanttamp=gagnant(catehero,cartevlan,board);
                        affichegagnant(gagnanttamp,&loose,&draw,&win);
                    }while(n<nbsimulation);
                    return (win+0.5*draw)/(float)n;
            }
            double  EquitemaincontremainRandom(int nbsimulation,int hero1,int hero2,int vilain1,int vilain2,int random)
            {
                int win=0;
                int loose=0;
                int draw=0;
                int n=0;
                carte cartes[NB_CARTES];
                carte catehero[2];
                carte cartevlan[2];
                carte board[5];
                srand(random);

                printf("equite main vs opp \n");
                printf("Combien de main à simuler \n");

                    catehero[0]=initCarteParId(hero1);
                    catehero[1]=initCarteParId(hero2);
                    cartevlan[0]=initCarteParId(vilain1);
                    cartevlan[1]=initCarteParId(vilain2);
                    do
                    {

                        jeuNeuf(cartes);
                        int indice = melangerJeu(cartes);
                        indice = melangerJeu(cartes);
                        Supprimercarte(catehero[0].carteID,cartes);
                        Supprimercarte(cartevlan[0].carteID,cartes);
                        Supprimercarte(catehero[1].carteID,cartes);
                        Supprimercarte(cartevlan[1].carteID,cartes);
                        n++;
                        DealBoard(board,cartes,&indice);
                        int gagnanttamp=gagnant(catehero,cartevlan,board);
                        affichegagnant(gagnanttamp,&loose,&draw,&win);
                    }while(n<nbsimulation);
                    return (win+0.5*draw)/(float)n;
            }
        int Quigagne(int hero1,int hero2,int vilain1,int vilain2,int Board1,int Board2,int Board3,int Board4,int Board5)
        {
            carte catehero[2];
            carte cartevlan[2];
            carte board[5];
            srand(time(NULL));

            catehero[0]=initCarteParId(hero1);
            catehero[1]=initCarteParId(hero2);
            cartevlan[0]=initCarteParId(vilain1);
            cartevlan[1]=initCarteParId(vilain2);

            board[0]=initCarteParId(Board1);
            board[1]=initCarteParId(Board2);
            board[2]=initCarteParId(Board3);
            board[3]=initCarteParId(Board4);
            board[4]=initCarteParId(Board5);
            int gagnanttamp=gagnant(catehero,cartevlan,board);
            return gagnanttamp;
        }
        double offorsuited(int nbsimulation,int hauteurhero1,int hauteurhero2,int suited1,int hauteurvilain1,int hauteurvilain2,int suited2,int random)
        {
            int win=0;
            int loose=0;
            int draw=0;
            int n=0;
            int nb=0;
            int couleur[4];
            carte cartes[NB_CARTES];
            carte catehero[2];
            carte cartevlan[2];
            carte board[5];
            srand(random);
            int hero1;
            int hero2;
            int vilain1;
            int vilain2;

            if(hauteurhero1==hauteurhero2){suited1=0;}
            if(hauteurvilain1==hauteurvilain2){suited2=0;}
            while(nb<nbsimulation)
            {
                n=0;
                couleur[0] = rand() % 4;
                hero1=hauteurhero1*4+couleur[0] ;
                if(suited1==0)
                {
                    couleur[1]  = (couleur[0]+(rand() % 3)+1)%4;
                    hero2=hauteurhero2*4+couleur[1];
                }
                else
                {
                    hero2=hauteurhero2*4+couleur[0];
                }
                // vilain
                if(suited2==1)
                {
                    do
                    {
                        couleur[2]  = rand() % 4;
                        vilain1=hauteurvilain1*4+couleur[2]  ;
                        vilain2=hauteurvilain2*4+couleur[2]  ;
                    }while(hero1==vilain1 || hero1==vilain2 || hero2==vilain1 || hero2==vilain2);
                }
                else
                {
                    do
                    {
                        couleur[2]  = rand() % 4;
                        couleur[3]  = (couleur[2]+(rand() % 3)+1)%4;
                        vilain1=hauteurvilain1*4+couleur[2]  ;
                        vilain2=hauteurvilain2*4+couleur[3]  ;
                    }
                    while(hero1==vilain1 || hero1==vilain2 || hero2==vilain1 || hero2==vilain2);

                }

                catehero[0]=initCarteParId(hero1);
                catehero[1]=initCarteParId(hero2);
                cartevlan[0]=initCarteParId(vilain1);
                cartevlan[1]=initCarteParId(vilain2);
                do
                {

                    jeuNeuf(cartes);
                    int indice = melangerJeu(cartes);
                    indice = melangerJeu(cartes);
                    Supprimercarte(catehero[0].carteID,cartes);
                    Supprimercarte(cartevlan[0].carteID,cartes);
                    Supprimercarte(catehero[1].carteID,cartes);
                    Supprimercarte(cartevlan[1].carteID,cartes);
                    n++;
                    DealBoard(board,cartes,&indice);
                    int gagnanttamp=gagnant(catehero,cartevlan,board);
                    affichegagnant(gagnanttamp,&loose,&draw,&win);
                }while(n<100);
                nb+=100;
            }
            return (win+0.5*draw)/(float)nb;
        }

    }



