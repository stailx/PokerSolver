

#ifndef MAIN_H_INCLUDED
#define MAIN_H_INCLUDED

#define NB_CARTES (4*13)

typedef enum {coeur=0, carreaux=1, trefle=2, pique=3,x}COULEUR;
typedef enum {deux, trois, quatre, cinq,six,sept,huit,neuf,T,J,Q,K,A}HAUTEUR;
typedef struct
{
    COULEUR couleur; //x = indeterminé
    char hauteur; // 0 inderterminé
    int carteID;// -1 indeterminé
    HAUTEUR mothauteur;
}carte;

typedef struct
{
    carte carte[7];

}showdown;

typedef struct
{
    int valeurs[6];
}valeur;

#endif // CARTEDISTRIBUTION_H_INCLUDED
