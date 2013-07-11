//-----------------------UTILITY FUNCTIONS-------------------------

//function that draw a surface with ROTATIONAL_SURFACE
var SURFACE = function (p){
	var points = p;
	var rot_domain = DOMAIN([[0,1],[0,2*PI]])([40,40]);
	var c = BEZIER(S0)(points);
	var surface = MAP(ROTATIONAL_SURFACE(c))(rot_domain);
	return surface;
};

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

var cc = 0.004;

//vase 1
var base = T([0,1,2])([-1.5,-1.5,-0.03])(CUBOID([3,3,0.03]));
var p0 = [[0,0,0],[1,0,0],[1,0,0.1]];
var surface0 = SURFACE(p0);
var p1 = [[1,0,0.1],[1,0,0.3],[0.7,0,0.4],[0.8,0,0.6]];
var surface1 = SURFACE(p1);
var p3 = [[0,0,0.7],[0.6,0,0.7],[1.1,0,0.4],[1.1,0,0.6]];
var surface3 = SURFACE(p3);
var p4 = [[1.1,0,0.6],[1.1,0,0.8],[1.1,0,0.5],[0.5,0,1.4]];
var surface4 = SURFACE(p4);
var p5 = [[0.5,0,1.4],[0.45,0,1.5],[0.2,0,1.5],[0,0,1.5]];
var surface5 = SURFACE(p5);
var cyl = CYLINDER(0.3,0.05);
var p6 = [[0,0,3.9],[0.5,0,3.9]];
var surface6 = SURFACE(p6);
var p7 = [[0.5,0,3.9],[3,0,7.7]];
var surface7 = SURFACE(p7);
var p8 = [[0,0,3.9],[0.2,0,3.9]];
var surface8 = SURFACE(p8);
var p9 = [[0.2,0,3.9],[1.3,0,6.9],[1.5,0,9.7]];
var surface9 = SURFACE(p9);

var vase1 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([base,
	surface0,surface1,surface3,surface4,
	T([2])([0.8])(surface3),T([2])([0.8])(surface4),
	T([2])([1.6])(surface3),T([2])([1.6])(surface4),
	T([2])([2.4])(surface3),T([2])([2.4])(surface4),
	T([2])([2.4])(surface5),T([2])([3.88])(cyl),
	surface6,surface7,surface8,surface9]));
//DRAW(vase1);

//vase 2
var vase2 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([base,
	surface0,surface1,surface3,surface4,
	T([2])([0.8])(surface3),T([2])([0.8])(surface4),
	T([2])([1.6])(surface3),T([2])([1.6])(surface4),
	T([2])([2.4])(surface3),T([2])([2.4])(surface4),
	T([2])([2.4])(surface5),T([2])([3.88])(cyl),
	surface6,surface7]));
//DRAW(vase2);

//vase3
var p10 = [[1.6,0,0],[0.3,0,1]];
var surface10 = SURFACE(p10);
var p11 = [[0.3,0,1],[0.3,0,1.6]];
var surface11 = SURFACE(p11);
var p12 = [[0,0,1.6],[0.6,0,1.6],[1.1,0,1.3],[1.1,0,1.3]];
var surface12 = SURFACE(p12);
var p13 = [[1.1,0,1.3],[1.1,0,1.7],[1.1,0,1.4],[0.5,0,2.3]];
var surface13 = SURFACE(p13);
var p14 = [[0.5,0,2.3],[0.4,0,2.5],[0.4,0,3],[0.2,0,3],[0,0,3]];
var surface14 = SURFACE(p14);
var p15 = [[0,0,3],[0.5,0,3]];
var surface15 = SURFACE(p15);
var p16 = [[0.5,0,3],[3,0,6.8]];
var surface16 = SURFACE(p16);

var vase3 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([surface10,
	surface11,surface12,surface13,surface14,
	T([2])([3])(cyl),surface15,surface16]));
//DRAW(vase3);

//vase4
var p17 = [[0,0,0],[1,0,0],[1,0,0.1]];
var surface17 = SURFACE(p17);
var p18 = [[1,0,0.1],[0.1,0,0.9],[0.3,0,1.5]];
var surface18 = SURFACE(p18);
var p19 = [[0,0,1.5],[0.6,0,1.5],[1.1,0,1.2],[1.1,0,1.4]];
var surface19 = SURFACE(p19);
var p20 = [[1.1,0,1.4],[1.1,0,1.6],[1.1,0,1.3],[0.5,0,2.2],[0.5,0,3]];
var surface20 = SURFACE(p20);
var p21 = [[0,0,2.1],[0.2,0,2.1]];
var surface21 = SURFACE(p21);
var p22 = [[0.2,0,2.1],[1.3,0,5.1],[1.5,0,7.9]];
var surface22 = SURFACE(p22);
var p23 = [[0,0,2.1],[1,0,2.1]];
var surface23 = SURFACE(p23);
var p24 = [[1,0,2.1],[3.2,0,4.2],[3,0,5.9]];
var surface24 = SURFACE(p24);

var vase4 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([base,
	surface17,surface18,
	T([2])([0.9])(S([0,1,2])([0.4,0.4,0.4])(surface19)),
	T([2])([0.9])(S([0,1,2])([0.4,0.4,0.4])(surface20)),
	surface21,surface22,surface23,surface24]));
//DRAW(vase4);

//vase5
var p25 = [[0,0,0],[2,0,0]];
var surface25 = SURFACE(p25);
var p26 = [[2,0,0],[2,0,0.8]];
var surface26 = SURFACE(p26);
var p27 = [[2,0,0.8],[0,0,0.8]];
var surface27 = SURFACE(p27);
var p28 = [[0.3,0,0.8],[0.2,0,4.3],[1,0,4.8]];
var surface28 = SURFACE(p28);
var p29 = [[0.3,0,4.8],[0.6,0,6],[1.5,0,6.5]];
var surface29 = SURFACE(p29);
var p30 = [[0.9,0,6.4],[0.9,0,7],[1.8,0,7.5]];
var surface30 = SURFACE(p30);
var p31 = [[1.1,0,7.4],[1.1,0,7.8],[2,0,8.3]];
var surface31 = SURFACE(p31);

var vase5 = COLOR([34*cc,139*cc,34*cc,0.6])(STRUCT([surface25,
	surface26,surface27,surface28,surface29,surface30,surface31]));
//DRAW(vase5);

var vases = STRUCT([vase1,
	T([0])([8])(vase2),
	T([0])([16])(vase3),
	T([0])([24])(vase4),
	T([0])([32])(vase5)]);
DRAW(vases);