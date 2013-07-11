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

//function that draw a sphere with BEZIER CURVES
var SPHERE = function (r){
	var scalefactor = 1.36;
	var rot_domain = DOMAIN([[0,1],[0,2*PI]])([40,40]);
	var p0 = [[0,0,0],[r*scalefactor,0,0],[r*scalefactor,0,r*2],[0,0,r*2]];
	var c0 = BEZIER(S0)(p0);
	var sphere = MAP(ROTATIONAL_SURFACE(c0))(rot_domain);
	return sphere;
};

//------------------------------------------------------------------
//HIDE(firstchair)
var Dom1D = INTERVALS(1)(20);
var Dom2D = DOMAIN([[0,1], [0,1]])([20,20]);
var rot_domain = DOMAIN([[0,1],[0,(29/18)*PI]])([40,40]);

var p0 = [[5,0,5],[5.5,0,5],[5.5,0,5.5],[5,0,5.5]];
var c0 = BEZIER(S0)(p0);
var surface0 = MAP(ROTATIONAL_SURFACE(c0))(rot_domain);
var p1 = [[5,0,5],[4.5,0,5],[4.5,0,5.5],[5,0,5.5]];
var c1 = BEZIER(S0)(p1);
var surface1 = MAP(ROTATIONAL_SURFACE(c1))(rot_domain);

var an = STRUCT([surface0,surface1]);
var p4 = [[0,0,0],[1,0,0],[2,0,0.5]];
var surface4 = T([0,1,2])([-4,3,5.5])(COLOR([0,1,1])(SURFACE(p4)));
var sphere1 = T([0,1,2])([-3.5,-3.5,5.5])(COLOR([0,0,0])(SPHERE(1)));
var sphere2 = T([0,1,2])([1.7,4.5,5.5])(COLOR([0,0,0])(SPHERE(1)));
var anello1 = R([0,2])(PI/4)(STRUCT([an,surface4,sphere1,sphere2]));

var p2 = [[3.5,0,5],[4,0,5],[4,0,5.5],[3.5,0,5.5]];
var p3 = [[3.5,0,5],[3,0,5],[3,0,5.5],[3.5,0,5.5]];
//var anello2 = T([0,1,2])([4,-3.5,-2.5])(R([1,2])(-PI/6.5)(STRUCT([SURFACE(p2),SURFACE(p3)])));
var anello2 = STRUCT([SURFACE(p2),SURFACE(p3)]);
var p5 = [[0,0,0],[2.5,0,0],[3.5,0,0.5]];
var surface5 = T([2])([5.07])(COLOR([0,0,0])(SURFACE(p5)));

var legpart1 = CYLINDER(0.35,8);
var legpart2 = T([2])([-0.25])(COLOR([0,0,0])(CYLINDER(0.35,0.25)));
var leg = STRUCT([legpart1,legpart2]);
var structure = STRUCT([anello2,T([0,1,2])([0.8,-3.4,-2.7])(leg),T([0,1,2])([3.2,1.5,-2.7])(leg),T([0,1,2])([-3,-1.8,-2.7])(leg),T([0,1,2])([0,3.5,-2.7])(leg)]); 
var seat = STRUCT([surface5,structure]);

var firstchair = STRUCT([anello1,T([0,1,2])([4,-3.45,-2.5])(R([1,2])(-PI/6.3)(seat))]);
DRAW(firstchair)