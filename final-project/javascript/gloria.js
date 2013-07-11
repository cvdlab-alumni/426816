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

//function that draw a surface with ROTATIONAL_SURFACE
var SURFACE = function (p){
	var points = p;
	var rot_domain = DOMAIN([[0,1],[0,2*PI]])([40,40]);
	var c = BEZIER(S0)(points);
	var surface = MAP(ROTATIONAL_SURFACE(c))(rot_domain);
	return surface;
};

//------------------------------------------------------------------

var Dom1D = INTERVALS(1)(20);
var Dom2D = DOMAIN([[0,1], [0,1]])([20,20]);
var rot_domain = DOMAIN([[0,1],[0,PI/2]])([40,40]);
var cc = 0.004;

var p0 = [[0,0.2,0],[1.5,0.2,0]];
var c0 = BEZIER(S0)(p0);
var p1 = [[0,-0.2,0],[1.5,-0.2,0]];
var c1 = BEZIER(S0)(p1);
var s01 = BEZIER(S1)([c0,c1]);
var surf01 = MAP(s01)(Dom2D);

var p2 = [[1.5,0.2,0],[4,1.8,0],[6.3,0,0],[6.4,0.2,0],[6.5,0,0]];
var c2 = BEZIER(S0)(p2);
var p3 = [[1.5,-0.2,0],[4,-1.8,0],[6.3,0,0],[6.4,-0.2,0],[6.5,0,0]];
var c3 = BEZIER(S0)(p3);
var s23 = BEZIER(S1)([c2,c3]);
var surf23 = MAP(s23)(Dom2D);

var p4 = [[0.5,-1,0],[0.1,11.5,0]];
var c4 = BEZIER(S0)(p4);
var p5 = [[-0.5,-1,0],[-0.1,11.5,0]];
var c5 = BEZIER(S0)(p5);
var s45 = BEZIER(S1)([c4,c5]);

var stem = MAP(s45)(Dom2D);

var l = STRUCT([surf01,surf23]);
var leaf = R([0,1])(PI/7)(l);
var doubleleaf1 = STRUCT([leaf,R([0,2])(PI)(leaf)]);
var doubleleaf2 = T([1])([3.5])(S([0,1,2])([0.85,0.85,0.85])(doubleleaf1));
var doubleleaf3 = T([1])([6.5])(S([0,1,2])([0.7,0.7,0.7])(doubleleaf1));
var doubleleaf4 = T([1])([9])(S([0,1,2])([0.55,0.55,0.55])(doubleleaf1));
var lastleaf = T([1])([10.5])(S([0,1,2])([0.4,0.4,0.4])(R([0,1])(PI/2)(l)));

var arm1 = R([1,2])(PI/9)(T([1])([1])(STRUCT([stem,doubleleaf1,doubleleaf2,doubleleaf3,doubleleaf4,lastleaf])));

var rotangle = 6*PI/15;
var firstline = COLOR([0.5,0.5,0.5])(STRUCT([arm1,R([0,1])([rotangle])(arm1),R([0,1])([rotangle*2])(arm1),
	R([0,1])([rotangle*3])(arm1),R([0,1])([rotangle*4])(arm1)]));


var arm2 = R([0,1])(PI/5)(R([1,2])(PI/14)(T([1])([1])(STRUCT([stem,doubleleaf1,doubleleaf2,doubleleaf3,doubleleaf4,lastleaf]))));

var secondline = COLOR([0.5,0.5,0.5])(STRUCT([arm2,R([0,1])([rotangle])(arm2),R([0,1])([rotangle*2])(arm2),
	R([0,1])([rotangle*3])(arm2),R([0,1])([rotangle*4])(arm2)]));

var cyl1 = COLOR([0,0,0])(T([2])([-4])(CYLINDER(1,4)));
var cyl2 = COLOR([0,0,0])(T([2])([-0.3])(CYLINDER(1.5,1.5)));
var cyl3 = R([1,2])(PI)(COLOR([0.5,0.5,0.5])(CYLINDER(0.05,30)));

var q1 = [[1,0,0],[1,0,1]];
var q2 = [[1,0,1],[2.5,0,1.5],[3,0,3]];
var light = COLOR([1,1,1,0.8])(T([2])([1])(STRUCT([SURFACE(q1),SURFACE(q2)])));

var gloria = STRUCT([firstline,secondline,cyl1,cyl2,cyl3,light]);

DARW(gloria);