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

rot_domain = PROD([INTERVALS(1)(20),INTERVALS(PI/2)(20)])
cc = 0.004

points = [[0,0],[1.7,0],[3,5],[1.3,5],[0,0]]

surf1 = R([2,3])(PI/2)(COLOR([0,0,0])(SOLIDIFY(POLYLINE(points))))

points2 = [[0,0],[0.3,0],[0.3,5.1],[0,5.1],[0,0]]

surf3 = R([1,3])(-PI/12.5)(R([1,2])(PI/2)(R([2,3])(PI/2)(COLOR([0,0,0])(SOLIDIFY(POLYLINE(points2))))))

block1 = STRUCT([surf1])
block2 = T([2])([0.3])(block1)
block3 = STRUCT([surf3])
block4 = T([1])([1.7])(block3)
block5 = COLOR([0.5,0.5,0.5])(CUBOID([1.7,0.3]))
block6 = T([1,3])([1.3,5])(block5)

basecyl = T([1,2,3])([0.4,0.15,3.3])(COLOR([1,1,0])(CYLINDER(1.3,0.2)))

cyl1 = T([1,2,3])([1.5,0.15,5])(COLOR([0,168*cc,107*cc])(CYLINDER(0.1,1.7)))
cyl2 = T([1,2,3])([0.15,1.35,0.15])(R([2,3])(PI/2)(COLOR([0,123*cc,167*cc])(CYLINDER(0.3,2.4))))

rot_domain = PROD([INTERVALS(1)(20),INTERVALS(PI/2)(20)])
p1 = [[0,0,0],[0.4,0,0]]
p2 = [[0.4,0,0],[0.4,0,0.28]]
p3 = [[0.4,0,0.28],[0,0,0.28]]
c1 = BEZIER(S1)(p1)
c2 = BEZIER(S1)(p2)
c3 = BEZIER(S1)(p3)
s1 = MAP(ROTATIONALSURFACE(c1))(rot_domain)
s2 = MAP(ROTATIONALSURFACE(c2))(rot_domain)
s3 = MAP(ROTATIONALSURFACE(c3))(rot_domain)
b_cyl = T([1])([1.7])(COLOR([0,0,0])(CUBOID([0.4,0.3])))
cyl3 = STRUCT([b_cyl,T([2])([0.29])(COLOR([0,0,0])(R([2,3])(PI/2)(T([1])([1.7])(STRUCT([s1,s2,s3])))))])

flamingo = STRUCT([block1,block2,block3,block4,block5,block6,basecyl,
		cyl1,cyl2,cyl3])

VIEW(flamingo)