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

cc = 0.004

def BLOCK(n):
	c1 = COLOR([255,255,255])(CUBOID([0.1,0,3]))
	c2 = COLOR([0,0,0])(CUBOID([0.1,0,3]))
	block1 = STRUCT([c1])
	block2 = STRUCT([T([0])([0.1])(c2)])
	for i in range(n-1):
		i = i + 1
		if (i%2==0):
			block1 = STRUCT([block1,T([1])([i*0.1])(c1)])
		else:
			block2 = STRUCT([block2,T([1])([i*0.1])(c2)])
	block = STRUCT([block1,block2])
	return block

b1 = BLOCK(29)
b2 = R([1,2])(PI/2)(BLOCK(3))

base = COLOR([0.5,0.5,0.5])(CUBOID([2.9,0.3]))

basecyl = COLOR([1,1,0])(CYLINDER(1.5,0.2))

cyl = COLOR([0,123*cc,167*cc])(R([2,3])(PI/2)(CYLINDER(0.4,3)))

polar = STRUCT([base,b1,b2,T([2])([0.3])(b1),
	T([1])([2.9])(b2),T([3])([3])(base),
	T([3])([3])(basecyl),T([1,3])([3,3])(basecyl),
	T([1,2,3])([1.45,1.5,0.399])(cyl)])

VIEW(polar)