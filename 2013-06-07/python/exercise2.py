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

#-----------------------------ES2-----------------------------

lake1 = T([1,2,3])([1.5,2,-1.2])(COLOR([0,0.58,0.71,0.8])(CUBOID([3,5,0.5])))

lake2 = T([1,2,3])([7.5,9.5,-1])(COLOR([0,0.58,0.71,0.8])(R([1,3])(-0.4)(CUBOID([2,3,0.5]))))


VIEW(STRUCT([DTM,lake1,lake2]))