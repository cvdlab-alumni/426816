//function tha draw a circle
var circle = function(r){
	return function(v){
		return [r*COS(v[0]),r*SIN(v[0])];
	};
};

//function that draw a cylinder
function CYLINDER(r,h){
	var domain = DOMAIN([[-2*PI,2*PI]])([50]);
	var crc = circle(r);
	var model = MAP(crc)(domain);
	return EXTRUDE([h])(model);
};

//-----------------------------ES1-----------------------------

var val_matrix = new Array();

var RANDOM = function(x,y){
	var z = COS(x)+SIN(y)*Math.random();
	if (((y>=13.5)&&(y<=14.5))&&((x>=2)&&(x<=3.5)))
		z = -0.6;
	if (((y>=4.5)&&(y<=5.5))&&((x>=8)&&(x<=9.5)))
		z = -1.3;
	var a = [x,y,z];
	val_matrix.push(a);
	return z; 
};

var find_z = function(x,y){
	var z = null;
	for (var i = 0; i <= val_matrix.length-1; i++) {
		var a = val_matrix[i];
		if((a[0]==x)&&(a[1]==y))
			z = a[3];
	};
	return z;
};

var domain = DOMAIN([[0, 10], [0, 15]])([60,60]);
var mapping = function (v) {
	var u = v[0];
	var v = v[1];
	return [u, v, RANDOM(u,v)];
};
var model = MAP(mapping)(domain);

var DTM = COLOR([205/255,133/255,63/255])(model);

//-----------------------------ES2-----------------------------

var lake1 = T([0,1,2])([1.5,2,-1.2])(COLOR([0/255,149/255,182/255,0.8])(CUBOID([3,5,0.5])));

var lake2 = T([0,1,2])([7.5,9.5,-1])(COLOR([0/255,149/255,182/255,0.8])(R([0,2])(0.4)(CUBOID([2,3,0.5]))));

var lakes = STRUCT([lake1,lake2]);

//-----------------------------ES3-----------------------------

var tree = function(h,r,d){
	var sp = [[0,0,0],[h/3,0,0]];
	var c1 = BEZIER(S0)(sp);
	var p2 = [[h/3,0,0],[0,0,(h*2)/3]];
	var c2 = BEZIER(S0)(p2);
	var dom = DOMAIN([[0,1],[0,2*PI]])([d,d]);
	var s1 = MAP(ROTATIONAL_SURFACE(c1))(dom);
	var s2 = MAP(ROTATIONAL_SURFACE(c2))(dom);
	var cone1 = COLOR([0/255,168/255,107/255])(STRUCT([s1,s2]));
	var cone2 = COLOR([127/255,255/255,0/255])(STRUCT([s1,s2]));
	var cone3 = COLOR([47/255,79/255,79/255])(STRUCT([s1,s2]));
	var cone = cone1;
	if ((sp.length*Math.random())>=1)
		cone = cone1;
	if ((sp.length*Math.random())<1)
		cone = cone2;
	if (((sp.length*Math.random()))+1>=2)
		cone = cone3;
	var trunk = COLOR([123/255,27/255,2/255])(CYLINDER(r,h/3));
	return STRUCT([T([2])([h/3])(cone),trunk]);
};

var generate_trees = function(p,n){
	var t = tree(0.3,0.025,10);
	var num_tree = n;
	var sp = val_matrix[p];
	var x = sp[0];
	var y = sp[1];
	var z = sp[2];
	var trees = T([0,1,2])([x,y,z])(t);
	var a = p;
	for (var i = 1; i <= num_tree-1; i++) {
		t = tree(0.3,0.025,10);
		a++;
		sp = val_matrix[a];
		x = sp[0];
		y = sp[1];
		z = sp[2];
		trees = STRUCT([trees,T([0,1,2])([x,y,z])(t)]);
	};
	return trees;
};

var forest = function(p,n){
	var forest = generate_trees(p-100-n,n/2);
	var forest = STRUCT([forest,generate_trees(p,n)]);
	var forest = STRUCT([forest,generate_trees(p+100+n,n)]);
	var forest = STRUCT([forest,generate_trees(p+200+2*n,n)]);
	var forest = STRUCT([forest,generate_trees(p+300+3*n,n)]);
	return forest;
};

var f = forest(1613,20);

//-----------------------------ES4-----------------------------

var building = function(range_x,range_y){
	var y = Math.random()*0.2;
	var x = Math.random()*0.2;
	var z = Math.random()*0.2;
	if (range_x==0 && range_y==0)
		return;
	return T([0,1,2])([range_x,range_y,0])(CUBOID([z,x,y]));
};

var groupOfBuildings = function(range_x,range_y){
	var buildings = building(0,0);
	for (var i = 0; i < range_x; i=i+0.25) {
		for (var j = 0; j < range_y; j=j+0.25) {
			buildings = STRUCT([buildings,building(i,j)]);
		};
	};
	return buildings;
};

var settlement1 = T([0,1,2])([2,13.5,-0.6])(groupOfBuildings(1.5,1));
var settlement2 = T([0,1,2])([8,4.5,-1.3])(groupOfBuildings(1.5,1));
var settlements = STRUCT([settlement1,settlement2]);


var model = STRUCT([DTM,lakes,f,settlements]);
DRAW(model);