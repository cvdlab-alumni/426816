#Per problemi di tempo non sono riuscita a completare la traduzione da Plasm.js a pyplasm in modo ottimale.

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

#-----------------------------ES3-----------------------------

def tree(h,r,d):
	sp = [[0,0,0],[h/3,0,0]]
	c1 = BEZIER(S1)(sp)
	p2 = [[h/3,0,0],[0,0,(h*2)/3]]
	c2 = BEZIER(S1)(p2)
	dom = PROD([INTERVALS(1)(d),INTERVALS(2*PI)(d)])
	s1 = MAP(ROTATIONALSURFACE(c1))(dom)
	s2 = MAP(ROTATIONALSURFACE(c2))(dom)
	cone1 = COLOR([0,0.66,0.42])(STRUCT([s1,s2]))
	cone2 = COLOR([0.5,1,0])(STRUCT([s1,s2]))
	cone3 = COLOR([0.18,0.31,0.31])(STRUCT([s1,s2]))
	cone = cone1
	if ((2*random.random())>=1):
		cone = cone1
	if ((2*random.random())<1):
		cone = cone2
	if (((2*random.random()))+1>=2):
		cone = cone3
	trunk = COLOR([0.7,0.4,0.3])(CYLINDER([r,h/3])(d))
	return STRUCT([T([3])([h/3])(cone),trunk])

def generate_trees(p,n):
	t = tree(0.3,0.025,10)
	num_tree = n
	sp = val_matrix[p]
	x = sp[0]
	y = sp[1]
	z = sp[2]
	trees = T([1,2,3])([x,y,z])(t)
	a = p
	for i in range(1,num_tree-1):
		t = tree(0.3,0.025,10)
		a = a+1
		sp = val_matrix[a]
		x = sp[0]
		y = sp[1]
		z = sp[2]
		trees = STRUCT([trees,T([1,2,3])([x,y,z])(t)])
	return trees


def forest(p,n):
	forest = generate_trees(p-100-n,n/2)
	forest = STRUCT([forest,generate_trees(p,n)])
	forest = STRUCT([forest,generate_trees(p+100+n,n)])
	forest = STRUCT([forest,generate_trees(p+200+2*n,n)])
	forest = STRUCT([forest,generate_trees(p+300+3*n,n)])
	return forest

f = forest(1613,20)

#-----------------------------ES4-----------------------------

def building(range_x,range_y):
	y = random.random()*0.2
	x = random.random()*0.2
	z = random.random()*0.2
	return T([1,2,3])([range_x,range_y,0])(CUBOID([z,x,y]))

def groupOfBuildings(range_x,range_y):
	buildings = building(-1,-1)
	for i in range(1,range_x*2):
		for j in range(1,range_y*2):
			buildings = STRUCT([buildings,building(i*(0.25),j*(0.25))])
	return buildings

settlement1 = T([1,2,3])([2,13.5,-0.6])(groupOfBuildings(2,1))
settlement2 = T([1,2,3])([8,4.5,-1.3])(groupOfBuildings(2,1))
settlements = STRUCT([settlement1,settlement2])


VIEW(STRUCT([DTM,lake1,lake2,f,settlements]))