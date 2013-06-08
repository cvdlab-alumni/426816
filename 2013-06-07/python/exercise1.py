from pyplasm import *
import random

#-----------------------------ES1-----------------------------

val_matrix = []

def RANDOM(x,y):
	z = COS(x)+SIN(y)*random.random()
	if (((y>=13.5) and (y<=14.5)) and ((x>=2) and (x<=3.5))):
		z = -0.6
	if (((y>=4.5) and (y<=5.5)) and ((x>=8) and (x<=9.5))):
		z = -1.3
	a = [x,y,z]
	val_matrix.append(a)
	return z 

dom1 = INTERVALS(10)(60)
dom2 = INTERVALS(15)(60)
domain = PROD([dom1,dom2])
def mapping(v):
	u = v[0]
	v = v[1]
	return [u, v, RANDOM(u,v)]

model = MAP(mapping)(domain)

DTM = COLOR([0.6,0.4,0.2])(model)
VIEW(DTM)