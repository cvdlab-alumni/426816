cc = 0.004

c1 = CUBOID([0.3,0.2,3])
c2 = CUBOID([0.4,0.2,0.3])
comp = COLOR([150*cc,75*cc,0*cc])(STRUCT([c1,T([1])([0.7])(c1),
	T([1])([0.3])(c2),T([1,3])([0.3,2.7])(c2)]))

def BLOCK(n,comp):
	base = CUBOID([n,n])
	block = COLOR([150*cc,75*cc,0*cc])(STRUCT([base]))
	line1 = STRUCT([comp])
	for i in range(n):
		line1 = STRUCT([line1,T([1])([i])(comp)])
	line2 = R([1,2])(PI/2)(line1)
	block = COLOR([150*cc,75*cc,0*cc])(STRUCT([block,base,line1,line2,T([1])([n])(line2),T([2])([n])(line1),T([3])([3])(base)]))
	return block


block1 = BLOCK(14,comp)
block2 = T([3])([3])(BLOCK(13,comp))
block3 = T([3])([6])(BLOCK(12,comp))
block4 = T([3])([9])(BLOCK(11,comp))
block5 = T([3])([12])(BLOCK(10,comp))
block6 = T([2,3])([1,15])(BLOCK(9,comp))
block7 = T([2,3])([2,18])(BLOCK(8,comp))
block8 = T([2,3])([3,21])(BLOCK(7,comp))
block9 = T([2,3])([4,24])(BLOCK(6,comp))
block10 = T([2,3])([4,27])(BLOCK(5,comp))
block11 = T([2,3])([4,30])(BLOCK(4,comp))
block12 = T([2,3])([4,33])(BLOCK(3,comp))
block13 = T([2,3])([4,36])(BLOCK(2,comp))

estense = STRUCT([block1,block2,block3,block4,block5,block6,
	block7,block8,block9,block10,block11,block12,block13])

VIEW(estense)