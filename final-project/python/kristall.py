from pyplasm import *

#-----------------------UTILITY FUNCTIONS-------------------------

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

#------------------------------------------------------------------

Dom1D = INTERVALS(1)(20)
Dom2D = PROD([Dom1D,Dom1D])
rot_domain = PROD([INTERVALS(1)(20),INTERVALS(PI/2)(20)])
cc = 0.004

block = COLOR([0.5,0.5,0.5])(CUBOID([5,7.5,5]))

basecyl = T([1,2,3])([2.5,-2,-1.5])(R([2,3])(PI/2)(COLOR([1,1,0])(CYLINDER(4,0.5))))

p0 = [[1.5,0,1.5],[2,0,1.5],[2,0,2],[1.5,0,2]]
c0 = BEZIER(S1)(p0)
surf0 = MAP(ROTATIONALSURFACE(c0))(rot_domain)
p1 = [[1.5,0,1.5],[1,0,1.5],[1,0,2],[1.5,0,2]]
c1 = BEZIER(S1)(p1)
surf1 = MAP(ROTATIONALSURFACE(c1))(rot_domain)
p2 = [[1.5,-2,1.5],[2,-2,1.5],[2,-2,2],[1.5,-2,2]]
c2 = BEZIER(S1)(p2)
s2 = BEZIER(S2)([c0,c2])
surf2 = MAP(s2)(Dom2D)
p3 = [[1.5,-2,1.5],[1,-2,1.5],[1,-2,2],[1.5,-2,2]]
c3 = BEZIER(S1)(p3)
s3 = BEZIER(S2)([c1,c3])
surf3 = MAP(s3)(Dom2D)

cyltube = COLOR([30*cc,144*cc,255*cc])(T([1,2,3])([2.5,1.5,-0.1])(CYLINDER(0.7,0.25)))
tube1 = T([1])([0.7])(COLOR([30*cc,144*cc,255*cc])(R([1,3])(-PI/2)(STRUCT([surf0,surf1,surf2,surf3]))))

p4a = [[0,0,0],[-0.25,0.25,0],[1.5,0.25,0],[1.25,0,0]]
p4b = [[0,0,0],[-0.25,-0.25,0],[1.5,-0.25,0],[1.25,0,0]]
c4a = BEZIER(S1)(p4a)
c4b = BEZIER(S1)(p4b)
s4 = BEZIER(S2)([c4a,c4b])
surf4 = MAP(s4)(Dom2D)
p5a = [[0,0,0.25],[-0.25,0.25,0.25],[1.5,0.25,0.25],[1.25,0,0.25]]
p5b = [[0,0,0.25],[-0.25,-0.25,0.25],[1.5,-0.25,0.25],[1.25,0,0.25]]
c5a = BEZIER(S1)(p5a)
c5b = BEZIER(S1)(p5b)
s5 = BEZIER(S2)([c5a,c5b])
surf5 = MAP(s5)(Dom2D)
s6 = BEZIER(S2)([c4a,c5a])
surf6 = MAP(s6)(Dom2D)
s7 = BEZIER(S2)([c4b,c5b])
surf7 = MAP(s7)(Dom2D)
base = T([1,2,3])([2.5,6.5,-0.1])(S([1,2])([1.8,1.5])(R([1,2])(-PI/2)(STRUCT([surf4,surf5,surf6,surf7]))))
cyl = T([1,2,3])([2.5,5.5,0.1])(R([2,3])(-PI/3-PI/3.5)(CYLINDER(0.25,6)))

leg1 = COLOR([30*cc,144*cc,255*cc])(STRUCT([base,cyl,T([2,3])([11,3])(R([2,3])(-PI/2)(base))]))
leg2 = T([3])([5])(R([1,3])(-PI/2)(leg1))
leg3 = T([1,3])([5,5])(R([1,3])(-PI)(leg1))
leg4 = T([1])([5])(R([1,3])(-3*PI/2)(leg1))

table = STRUCT([block,basecyl,cyltube,tube1,leg1,leg2,leg3,leg4])

VIEW(table)