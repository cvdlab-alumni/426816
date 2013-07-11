from pyplasm import *

#-----------------------UTILITY FUNCTIONS-------------------------

#function that draw a surface with ROTATIONALSURFACE
def SURFACE(p):
	points = p
	dom1 = INTERVALS(1)(40)
	dom2 = INTERVALS(2*PI)(40)
	rot_domain = PROD([dom1,dom2])
	c = BEZIER(S1)(points)
	surface = MAP(ROTATIONALSURFACE(c))(rot_domain)
	return surface

#function that draw a cylinder with BEZIER CURVES
def CYLINDER(r,h):
	dom1 = INTERVALS(1)(40)
	dom2 = INTERVALS(2*PI)(40)
	rot_domain = PROD([dom1,dom2])
	p1 = [[0,0,0],[r,0,0]]
	p2 = [[r,0,0],[r,0,h]]
	p3 = [[r,0,h],[0,0,h]]
	c1 = BEZIER(S1)(p1)
	c2 = BEZIER(S1)(p2)
	c3 = BEZIER(S1)(p3)
	s1 = MAP(ROTATIONALSURFACE(c1))(rot_domain)
	s2 = MAP(ROTATIONALSURFACE(c2))(rot_domain)
	s3 = MAP(ROTATIONALSURFACE(c3))(rot_domain)
	cylinder = STRUCT([s1,s2,s3])
	return cylinder

#function that draw a sphere with BEZIER CURVES
def SPHERE(r):
	scalefactor = 1.36
	dom1 = INTERVALS(1)(40)
	dom2 = INTERVALS(2*PI)(40)
	rot_domain = PROD([dom1,dom2])
	p0 = [[0,0,0],[r*scalefactor,0,0],[r*scalefactor,0,r*2],[0,0,r*2]]
	c0 = BEZIER(S1)(p0)
	sphere = MAP(ROTATIONALSURFACE(c0))(rot_domain)
	return sphere

#------------------------------------------------------------------
#HIDE(firstchair)
dom1 = INTERVALS(1)(40)
dom2 = INTERVALS(1.611*PI)(40)
rot_domain = PROD([dom1,dom2])

p0 = [[5,0,5],[5.5,0,5],[5.5,0,5.5],[5,0,5.5]]
c0 = BEZIER(S1)(p0)
surface0 = MAP(ROTATIONALSURFACE(c0))(rot_domain)
p1 = [[5,0,5],[4.5,0,5],[4.5,0,5.5],[5,0,5.5]]
c1 = BEZIER(S1)(p1)
surface1 = MAP(ROTATIONALSURFACE(c1))(rot_domain)

an = STRUCT([surface0,surface1])
p4 = [[0,0,0],[1,0,0],[2,0,0.5]]
surface4 = T([1,2,3])([-4,3,5.5])(COLOR([0,1,1])(SURFACE(p4)))
sphere1 = T([1,2,3])([-3.5,-3.5,5.5])(COLOR([0,0,0])(SPHERE(1)))
sphere2 = T([1,2,3])([1.7,4.5,5.5])(COLOR([0,0,0])(SPHERE(1)))
anello1 = R([1,3])(-PI/4)(STRUCT([an,surface4,sphere1,sphere2]))

p2 = [[3.5,0,5],[4,0,5],[4,0,5.5],[3.5,0,5.5]]
p3 = [[3.5,0,5],[3,0,5],[3,0,5.5],[3.5,0,5.5]]
anello2 = STRUCT([SURFACE(p2),SURFACE(p3)])
p5 = [[0,0,0],[2.5,0,0],[3.5,0,0.5]]
surface5 = T([3])([5.07])(COLOR([0,0,0])(SURFACE(p5)))

legpart1 = CYLINDER(0.35,8)
legpart2 = T([3])([-0.25])(COLOR([0,0,0])(CYLINDER(0.35,0.25)))
leg = STRUCT([legpart1,legpart2])
structure = STRUCT([anello2,T([1,2,3])([0.8,-3.4,-2.7])(leg),T([1,2,3])([3.2,1.5,-2.7])(leg),T([1,2,3])([-3,-1.8,-2.7])(leg),T([1,2,3])([0,3.5,-2.7])(leg)]) 
seat = STRUCT([surface5,structure])

firstchair = STRUCT([anello1,T([1,2,3])([4,-3.45,-2.5])(R([2,3])(-PI/6.3)(seat))])
VIEW(firstchair)