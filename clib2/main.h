#ifndef __MAIN_H__
#define __MAIN_H__

#include <windows.h>

/*  To use this exported function of dll, include this header
 *  in your project.
 */

#ifdef BUILD_DLL
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT __declspec(dllimport)
#endif


#ifdef __cplusplus
extern "C"
{
#endif

#define NB_CARTES (4*13)


int DLL_EXPORT multiplier(long, long);
double  DLL_EXPORT MainHasard(int);
double  DLL_EXPORT Equitemaincontremain(int ,int ,int ,int ,int);
double  DLL_EXPORT EquitemaincontremainRandom(int ,int ,int ,int ,int,int);
int DLL_EXPORT Quigagne(int ,int ,int ,int ,int ,int ,int ,int ,int);
double DLL_EXPORT offorsuited(int,int,int,int,int,int,int,int);



#ifdef __cplusplus
}
#endif

#endif // __MAIN_H__
