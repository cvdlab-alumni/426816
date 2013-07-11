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

Dom1D = INTERVALS(1)(20)
Dom2D = PROD([Dom1D, Dom1D])
rot_domain = PROD([INTERVALS(1)(20),INTERVALS(PI/2)(20)])
cc = 0.004

p0 = [[0,0.2,0],[1.5,0.2,0]]
c0 = BEZIER(S1)(p0)
p1 = [[0,-0.2,0],[1.5,-0.2,0]]
c1 = BEZIER(S1)(p1)
s01 = BEZIER(S2)([c0,c1])
surf01 = MAP(s01)(Dom2D)

p2 = [[1.5,0.2,0],[4,1.8,0],[6.3,0,0],[6.4,0.2,0],[6.5,0,0]]
c2 = BEZIER(S1)(p2)
p3 = [[1.5,-0.2,0],[4,-1.8,0],[6.3,0,0],[6.4,-0.2,0],[6.5,0,0]]
c3 = BEZIER(S1)(p3)
s23 = BEZIER(S2)([c2,c3])
surf23 = MAP(s23)(Dom2D)

p4 = [[0.5,-1,0],[0.1,11.5,0]]
c4 = BEZIER(S1)(p4)
p5 = [[-0.5,-1,0],[-0.1,11.5,0]]
c5 = BEZIER(S1)(p5)
s45 = BEZIER(S2)([c4,c5])

stem = MAP(s45)(Dom2D)

l = STRUCT([surf01,surf23])
leaf = R([1,2])(PI/7)(l)
doubleleaf1 = STRUCT([leaf,R([1,3])(-PI)(leaf)])
doubleleaf2 = T([2])([3.5])(S([1,2,3])([0.85,0.85,0.85])(doubleleaf1))
doubleleaf3 = T([2])([6.5])(S([1,2,3])([0.7,0.7,0.7])(doubleleaf1))
doubleleaf4 = T([2])([9])(S([1,2,3])([0.55,0.55,0.55])(doubleleaf1))
lastleaf = T([2])([10.5])(S([1,2,3])([0.4,0.4,0.4])(R([1,2])(PI/2)(l)))

arm1 = R([2,3])(PI/9)(T([2])([1])(STRUCT([stem,doubleleaf1,doubleleaf2,doubleleaf3,doubleleaf4,lastleaf])))

rotangle = 6*PI/15
firstline = COLOR([0.5,0.5,0.5])(STRUCT([arm1,R([1,2])(rotangle)(arm1),R([1,2])(rotangle*2)(arm1),
	R([1,2])(rotangle*3)(arm1),R([1,2])(rotangle*4)(arm1)]))


arm2 = R([1,2])(PI/5)(R([2,3])(PI/14)(T([2])([1])(STRUCT([stem,doubleleaf1,doubleleaf2,doubleleaf3,doubleleaf4,lastleaf]))))

secondline = COLOR([0.5,0.5,0.5])(STRUCT([arm2,R([1,2])(rotangle)(arm2),R([1,2])(rotangle*2)(arm2),
	R([1,2])(rotangle*3)(arm2),R([1,2])(rotangle*4)(arm2)]))

cyl1 = COLOR([0,0,0])(T([3])([-4])(CYLINDER(1,4)))
cyl2 = COLOR([0,0,0])(T([3])([-0.3])(CYLINDER(1.5,1.5)))
cyl3 = R([2,3])(PI)(COLOR([0.5,0.5,0.5])(CYLINDER(0.05,30)))

q1 = [[1,0,0],[1,0,1]]
q2 = [[1,0,1],[2.5,0,1.5],[3,0,3]]
light = COLOR([1,1,1,0.8])(T([3])([1])(STRUCT([SURFACE(q1),SURFACE(q2)])))

gloria = STRUCT([firstline,secondline,cyl1,cyl2,cyl3,light])

VIEW(gloria)