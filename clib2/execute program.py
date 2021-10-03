from ctypes import *
zelib=CDLL("C:\\Users\\theo\\Desktop\\Nouveau dossier (2)\\clib2\\bin\\Debug\\clib2.dll")
zelib.MainHasard.argtypes  = [c_int]
zelib.MainHasard.restype = c_double

res = zelib.MainHasard(100000)
print(res)

zelib.Equitemaincontremain.argtypes  = [c_int,c_int,c_int,c_int,c_int]
zelib.Equitemaincontremain.restype = c_double

res = zelib.Equitemaincontremain(1000000,0,1,4,5)
print(res)

zelib.Quigagne.argtypes  = [c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int]
zelib.Quigagne.restype = c_int

res = zelib.Quigagne(1000000,3,1,4,35,38,39,43,47,51)
print(res)



