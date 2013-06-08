#Per problemi di tempo non sono riuscita a completare la traduzione da Plasm.js a pyplasm in modo ottimale.

#-----------------------------ES1-----------------------------

val_matrix = new Array()

RANDOM = function(x,y){
	z = COS(x)+SIN(y)*Math.random()
	if (((y>=13.5)&&(y<=14.5))&&((x>=2)&&(x<=3.5)))
		z = -0.6
	if (((y>=4.5)&&(y<=5.5))&&((x>=8)&&(x<=9.5)))
		z = -1.3
	a = [x,y,z]
	val_matrix.push(a)
	return z 
}

domain = DOMAIN([[0, 10], [0, 15]])([60,60])
mapping = function (v) {
	u = v[0]
	v = v[1]
	return [u, v, RANDOM(u,v)]
}
model = MAP(mapping)(domain)

DTM = COLOR([205/255,133/255,63/255])(model)
VIEW(DTM)

#-----------------------------ES2-----------------------------

lake1 = T([1,2,3])([1.5,2,-1.2])(COLOR([0/255,149/255,182/255,0.8])(CUBOID([3,5,0.5])))
VIEW(lake1)

lake2 = T([1,2,3])([7.5,9.5,-1])(COLOR([0/255,149/255,182/255,0.8])(R([1,3])(0.4)(CUBOID([2,3,0.5]))))
VIEW(lake2)

#-----------------------------ES3-----------------------------

tree = function(h,r,d){
	sp = [[0,0,0],[h/3,0,0]]
	c1 = BEZIER(S1)(sp)
	p2 = [[h/3,0,0],[0,0,(h*2)/3]]
	c2 = BEZIER(S1)(p2)
	dom = DOMAIN([[0,1],[0,2*PI]])([d,d])
	s1 = MAP(ROTATIONAL_SURFACE(c1))(dom)
	s2 = MAP(ROTATIONAL_SURFACE(c2))(dom)
	cone1 = COLOR([0/255,168/255,107/255])(STRUCT([s1,s2]))
	cone2 = COLOR([127/255,255/255,0/255])(STRUCT([s1,s2]))
	cone3 = COLOR([47/255,79/255,79/255])(STRUCT([s1,s2]))
	cone = cone1
	if ((sp.length*Math.random())>=1)
		cone = cone1
	if ((sp.length*Math.random())<1)
		cone = cone2
	if (((sp.length*Math.random()))+1>=2)
		cone = cone3
	trunk = COLOR([123/255,27/255,2/255])(CYLINDER(r,h/3))
	return STRUCT([T([2])([h/3])(cone),trunk])
}

generate_trees = function(p,n){
	t = tree(0.3,0.025,10)
	num_tree = n
	sp = val_matrix[p]
	x = sp[0]
	y = sp[1]
	z = sp[2]
	trees = T([1,2,3])([x,y,z])(t)
	a = p
	for (i = 1 i <= num_tree-1 i++) {
		t = tree(0.3,0.025,10)
		a++
		sp = val_matrix[a]
		x = sp[0]
		y = sp[1]
		z = sp[2]
		trees = STRUCT([trees,T([1,2,3])([x,y,z])(t)])
	}
	return trees
}

forest = function(p,n){
	forest = generate_trees(p-100-n,n/2)
	forest = STRUCT([forest,generate_trees(p,n)])
	forest = STRUCT([forest,generate_trees(p+100+n,n)])
	forest = STRUCT([forest,generate_trees(p+200+2*n,n)])
	forest = STRUCT([forest,generate_trees(p+300+3*n,n)])
	return forest
}

f = forest(1613,20)
VIEW(f)

#-----------------------------ES4-----------------------------

building = function(range_x,range_y){
	y = Math.random()*0.2
	x = Math.random()*0.2
	z = Math.random()*0.2
	if (range_x==0 && range_y==0)
		return
	return T([1,2,3])([range_x,range_y,0])(CUBOID([z,x,y]))
}

/*groupOfBuildings = function(range_x,range_y){
	buildings = building(0,0)
	for (i = 0 i < range_x i=i+0.25) {
		for (j = 0 j < range_y j=j+0.25) {
			buildings = STRUCT([buildings,building(i,j)])
		}
	}
	return buildings
}

settlement1 = T([1,2,3])([2,13.5,-0.6])(groupOfBuildings(1.5,1))
settlement2 = T([1,2,3])([8,4.5,-1.3])(groupOfBuildings(1.5,1))
settlements = STRUCT([settlement1,settlement2])
VIEW(settlements)*/

#-----------------------------ES5-----------------------------

groupOfBuildings = function(range_x,range_y){
	buildings = building(0,0)
	for (i = 0 i < range_x i=i+0.25) {
		for (j = 0 j < range_y j=j+0.25) {
			buildings = STRUCT([buildings,building(i,j)])
			if(j==0.25){
				road = T([1])([j+0.18])(COLOR([1/3,1/3,1/3])(CUBOID([range_x,0.04,0.01])))
				buildings = STRUCT([buildings,road])
			}
		}
		road = T([0])([i+0.18])(COLOR([1/3,1/3,1/3])(CUBOID([0.04,range_y,0.01])))
		buildings = STRUCT([buildings,road])
	}
	return buildings
}

settlement1 = T([1,2,3])([2,13.5,-0.6])(groupOfBuildings(1.5,1))
settlement2 = T([1,2,3])([8,4.5,-1.3])(groupOfBuildings(1.5,1))
settlements = STRUCT([settlement1,settlement2])
VIEW(settlements)