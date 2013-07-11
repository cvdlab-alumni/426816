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

#------------------------------------------------------------------

cc = 0.004

#vase 1
base = T([1,2,3])([-1.5,-1.5,-0.03])(CUBOID([3,3,0.03]))
p0 = [[0,0,0],[1,0,0],[1,0,0.1]]
surface0 = SURFACE(p0)
p1 = [[1,0,0.1],[1,0,0.3],[0.7,0,0.4],[0.8,0,0.6]]
surface1 = SURFACE(p1)
p3 = [[0,0,0.7],[0.6,0,0.7],[1.1,0,0.4],[1.1,0,0.6]]
surface3 = SURFACE(p3)
p4 = [[1.1,0,0.6],[1.1,0,0.8],[1.1,0,0.5],[0.5,0,1.4]]
surface4 = SURFACE(p4)
p5 = [[0.5,0,1.4],[0.45,0,1.5],[0.2,0,1.5],[0,0,1.5]]
surface5 = SURFACE(p5)
cyl = CYLINDER(0.3,0.05)
p6 = [[0,0,3.9],[0.5,0,3.9]]
surface6 = SURFACE(p6)
p7 = [[0.5,0,3.9],[3,0,7.7]]
surface7 = SURFACE(p7)
p8 = [[0,0,3.9],[0.2,0,3.9]]
surface8 = SURFACE(p8)
p9 = [[0.2,0,3.9],[1.3,0,6.9],[1.5,0,9.7]]
surface9 = SURFACE(p9)

vase1 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([base,
	surface0,surface1,surface3,surface4,
	T([3])([0.8])(surface3),T([3])([0.8])(surface4),
	T([3])([1.6])(surface3),T([3])([1.6])(surface4),
	T([3])([2.4])(surface3),T([3])([2.4])(surface4),
	T([3])([2.4])(surface5),T([3])([3.88])(cyl),
	surface6,surface7,surface8,surface9]))
#VIEW(vase1)

#vase 2
vase2 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([base,
	surface0,surface1,surface3,surface4,
	T([3])([0.8])(surface3),T([3])([0.8])(surface4),
	T([3])([1.6])(surface3),T([3])([1.6])(surface4),
	T([3])([2.4])(surface3),T([3])([2.4])(surface4),
	T([3])([2.4])(surface5),T([3])([3.88])(cyl),
	surface6,surface7]))
#VIEW(vase2)

#vase3
p10 = [[1.6,0,0],[0.3,0,1]]
surface10 = SURFACE(p10)
p11 = [[0.3,0,1],[0.3,0,1.6]]
surface11 = SURFACE(p11)
p12 = [[0,0,1.6],[0.6,0,1.6],[1.1,0,1.3],[1.1,0,1.3]]
surface12 = SURFACE(p12)
p13 = [[1.1,0,1.3],[1.1,0,1.7],[1.1,0,1.4],[0.5,0,2.3]]
surface13 = SURFACE(p13)
p14 = [[0.5,0,2.3],[0.4,0,2.5],[0.4,0,3],[0.2,0,3],[0,0,3]]
surface14 = SURFACE(p14)
p15 = [[0,0,3],[0.5,0,3]]
surface15 = SURFACE(p15)
p16 = [[0.5,0,3],[3,0,6.8]]
surface16 = SURFACE(p16)

vase3 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([surface10,
	surface11,surface12,surface13,surface14,
	T([3])([3])(cyl),surface15,surface16]))
#VIEW(vase3)

#vase4
p17 = [[0,0,0],[1,0,0],[1,0,0.1]]
surface17 = SURFACE(p17)
p18 = [[1,0,0.1],[0.1,0,0.9],[0.3,0,1.5]]
surface18 = SURFACE(p18)
p19 = [[0,0,1.5],[0.6,0,1.5],[1.1,0,1.2],[1.1,0,1.4]]
surface19 = SURFACE(p19)
p20 = [[1.1,0,1.4],[1.1,0,1.6],[1.1,0,1.3],[0.5,0,2.2],[0.5,0,3]]
surface20 = SURFACE(p20)
p21 = [[0,0,2.1],[0.2,0,2.1]]
surface21 = SURFACE(p21)
p22 = [[0.2,0,2.1],[1.3,0,5.1],[1.5,0,7.9]]
surface22 = SURFACE(p22)
p23 = [[0,0,2.1],[1,0,2.1]]
surface23 = SURFACE(p23)
p24 = [[1,0,2.1],[3.2,0,4.2],[3,0,5.9]]
surface24 = SURFACE(p24)

vase4 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([base,
	surface17,surface18,
	T([3])([0.9])(S([1,2,3])([0.4,0.4,0.4])(surface19)),
	T([3])([0.9])(S([1,2,3])([0.4,0.4,0.4])(surface20)),
	surface21,surface22,surface23,surface24]))
#VIEW(vase4)

#vase5
p25 = [[0,0,0],[2,0,0]]
surface25 = SURFACE(p25)
p26 = [[2,0,0],[2,0,0.8]]
surface26 = SURFACE(p26)
p27 = [[2,0,0.8],[0,0,0.8]]
surface27 = SURFACE(p27)
p28 = [[0.3,0,0.8],[0.2,0,4.3],[1,0,4.8]]
surface28 = SURFACE(p28)
p29 = [[0.3,0,4.8],[0.6,0,6],[1.5,0,6.5]]
surface29 = SURFACE(p29)
p30 = [[0.9,0,6.4],[0.9,0,7],[1.8,0,7.5]]
surface30 = SURFACE(p30)
p31 = [[1.1,0,7.4],[1.1,0,7.8],[2,0,8.3]]
surface31 = SURFACE(p31)

vase5 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([surface25,
	surface26,surface27,surface28,surface29,surface30,surface31]))
#VIEW(vase5)

vases = STRUCT([vase1,
	T([1])([8])(vase2),
	T([1])([16])(vase3),
	T([1])([24])(vase4),
	T([1])([32])(vase5)])
VIEW(vases)