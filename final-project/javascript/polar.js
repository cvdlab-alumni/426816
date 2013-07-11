//-----------------------UTILITY FUNCTIONS-------------------------

//function that draw a cylinder with BEZIER CURVES
function CYLINDER(r,h){
	var rot_domain = DOMAIN([[0,1],[0,2*PI]])([40,40]);
	var p1 = [[0,0,0],[r,0,0]];
	var p2 = [[r,0,0],[r,0,h]];
	var p3 = [[r,0,h],[0,0,h]];
	var c1 = BEZIER(S0)(p1);
	var c2 = BEZIER(S0)(p2);
	var c3 = BEZIER(S0)(p3);
	var s1 = MAP(ROTATIONAL_SURFACE(c1))(rot_domain);
	var s2 = MAP(ROTATIONAL_SURFACE(c2))(rot_domain);
	var s3 = MAP(ROTATIONAL_SURFACE(c3))(rot_domain);
	var cylinder = STRUCT([s1,s2,s3]);
	return cylinder;
};

var BLOCK = function (n){
	var c1 = COLOR([255,255,255])(CUBOID([0.1,0,3]));
	var c2 = COLOR([0,0,0])(CUBOID([0.1,0,3]));
	var block1 = STRUCT([c1]);
	var block2 = STRUCT([T([0])([0.1])(c2)]);
	for (var i = 2; i <= n-1; i++) {
		if (i%2==0){
			block1 = STRUCT([block1,T([0])([i/10])(c1)]);
		}
		else{
			block2 = STRUCT([block2,T([0])([i/10])(c2)]);
		}
	};
	block = STRUCT([block1,block2]);
	return block;
};

//------------------------------------------------------------------

var cc = 0.004;

var b1 = BLOCK(29);
var b2 = R([0,1])(PI/2)(BLOCK(3));

var base = COLOR([0.5,0.5,0.5])(CUBOID([2.9,0.3]));

var basecyl = COLOR([1,1,0])(CYLINDER(1.5,0.2));

var cyl = COLOR([0,123*cc,167*cc])(R([1,2])(PI/2)(CYLINDER(0.4,3)));

var polar = STRUCT([base,b1,b2,T([1])([0.3])(b1),
	T([0])([2.9])(b2),T([2])([3])(base),
	T([2])([3])(basecyl),T([0,2])([3,3])(basecyl),
	T([0,1,2])([1.45,1.5,0.399])(cyl)]);

DRAW(polar);