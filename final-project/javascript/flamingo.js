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

//------------------------------------------------------------------
var Dom1D = INTERVALS(1)(20);
var Dom2D = DOMAIN([[0,1], [0,1]])([20,20]);
var rot_domain = DOMAIN([[0,1],[0,PI/2]])([40,40]);
var cc = 0.004;

var points = [/*prima fila*/[0,0,0],[0.1,0,0],[0.2,0,0],[0.3,0,0],[0.4,0,0],[0.5,0,0],
	[0.6,0,0],[0.7,0,0],[0.8,0,0],[0.9,0,0],[1,0,0],[1.1,0,0],[1.2,0,0],
	[1.3,0,0],[1.4,0,0],[1.5,0,0],[1.6,0,0],[1.7,0,0],
	/*seconda fila*/[1.3,0,5],[1.4,0,5],[1.5,0,5],[1.6,0,5],[1.7,0,5],
	[1.8,0,5],[1.9,0,5],[2,0,5],[2.1,0,5],[2.2,0,5],[2.3,0,5],[2.4,0,5],
	[2.5,0,5],[2.6,0,5],[2.7,0,5],[2.8,0,5],[2.9,0,5],[3,0,5]];

var cells1 = [[1,19,2],[2,19,20],[3,21,4],[4,21,22],[5,23,6],[6,23,24],
	[7,25,8],[8,25,26],[9,27,10],[10,27,28],[11,29,12],[12,29,30],[13,31,14],
	[14,31,32],[15,33,16],[16,33,34]];

var surf1 = COLOR([0,0,0])(SIMPLICIAL_COMPLEX(points)(cells1));

var cells2 = [[0,1,18],[1,18,19],[2,20,3],[3,20,21],[4,22,5],[5,22,23],
	[6,24,7],[7,24,25],[8,26,9],[9,26,27],[10,28,11],[11,28,29],
	[12,30,13],[13,30,31],[14,32,15],[15,32,33],[16,34,17],[17,34,35]];

var surf2 = COLOR([255,255,255])(SIMPLICIAL_COMPLEX(points)(cells2));

var points2 = [/*prima fila*/[0,0.3,0],[0,0.2,0],[0,0.1,0],[0,0,0],
	/*seconda fila*/[1.3,0.3,5],[1.3,0.2,5],[1.3,0.1,5],[1.3,0,5]];

var cells3 = [[0,1,4],[1,4,5],[2,6,3],[3,6,7]];

var surf3 = COLOR([0,0,0])(SIMPLICIAL_COMPLEX(points2)(cells3));

var cells4 = [[1,5,2],[2,5,6]];

var surf4 = COLOR([255,255,255])(SIMPLICIAL_COMPLEX(points2)(cells4));

var block1 = STRUCT([surf1,surf2]);
var block2 = T([1])([0.3])(block1);
var block3 = STRUCT([surf3,surf4]);
var block4 = T([0])([1.7])(block3);
var block5 = COLOR([0.5,0.5,0.5])(CUBOID([1.7,0.3]));
var block6 = T([0,2])([1.3,5])(block5);

var basecyl = T([0,1,2])([0.4,0.15,3.3])(COLOR([1,1,0])(CYLINDER(1.3,0.2)));

var cyl1 = T([0,1,2])([1.5,0.15,5])(COLOR([0,168*cc,107*cc])(CYLINDER(0.1,1.7)));
var cyl2 = T([0,1,2])([0.15,1.35,0.15])(R([1,2])(PI/2)(COLOR([0,123*cc,167*cc])(CYLINDER(0.3,2.4))));

var rot_domain = DOMAIN([[0,1],[0,PI/2]])([40,40]);
var p1 = [[0,0,0],[0.4,0,0]];
var p2 = [[0.4,0,0],[0.4,0,0.28]];
var p3 = [[0.4,0,0.28],[0,0,0.28]];
var c1 = BEZIER(S0)(p1);
var c2 = BEZIER(S0)(p2);
var c3 = BEZIER(S0)(p3);
var s1 = MAP(ROTATIONAL_SURFACE(c1))(rot_domain);
var s2 = MAP(ROTATIONAL_SURFACE(c2))(rot_domain);
var s3 = MAP(ROTATIONAL_SURFACE(c3))(rot_domain);
var b_cyl = T([0])([1.7])(COLOR([0,0,0])(CUBOID([0.4,0.3])));
var cyl3 = STRUCT([b_cyl,T([1])([0.29])(COLOR([0,0,0])(R([1,2])(PI/2)(T([0])([1.7])(STRUCT([s1,s2,s3])))))]);

var flamingo = STRUCT([block1,block2,block3,block4,block5,block6,basecyl,
		cyl1,cyl2,cyl3]);

DRAW(flamingo);