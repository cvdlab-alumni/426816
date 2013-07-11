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

var points1 = [/*prima fila*/[0,0,0],[0.5,0,0],[1,0,0],[1.5,0,0],[2,0,0],[2.5,0,0],
	[3,0,0],[3.5,0,0],[4,0,0],[4.5,0,0],[5,0,0],
	/*seconda fila*/[0,0.5,0],[5,0.5,0],
	/*terza fila*/[0,1,0],[5,1,0],
	/*quarta fila*/[0,1.5,0],[5,1.5,0],
	/*quinta fila*/[0,2,0],[5,2,0],
	/*sesta fila*/[0,2.5,0],[5,2.5,0],
	/*settima fila*/[0,3,0],[5,3,0],
	/*ottava fila*/[0,3.5,0],[5,3.5,0],
	/*nona fila*/[0,4,0],[5,4,0],
	/*decima fila*/[0,4.5,0],[5,4.5,0],
	/*undicesima fila*/[0,5,0],[5,5,0],
	/*dodicesima fila*/[0,5.5,0],[5,5.5,0],
	/*tredicesima fila*/[0,6,0],[5,6,0],
	/*quattordicesima fila*/[0,6.5,0],[5,6.5,0],
	/*quindicesima fila*/[0,7,0],[5,7,0],
	/*sedicesima fila*/[0,7.5,0],[0.5,7.5,0],[1,7.5,0],[1.5,7.5,0],[2,7.5,0],[2.5,7.5,0],
	[3,7.5,0],[3.5,7.5,0],[4,7.5,0],[4.5,7.5,0],[5,7.5,0]];

var points2 = [/*prima fila*/[0,0,0],[0.5,0,0],[1,0,0],[1.5,0,0],[2,0,0],[2.5,0,0],
	[3,0,0],[3.5,0,0],[4,0,0],[4.5,0,0],[5,0,0],
	/*seconda fila*/[0,0.5,0],[5,0.5,0],
	/*terza fila*/[0,1,0],[5,1,0],
	/*quarta fila*/[0,1.5,0],[5,1.5,0],
	/*quinta fila*/[0,2,0],[5,2,0],
	/*sesta fila*/[0,2.5,0],[5,2.5,0],
	/*settima fila*/[0,3,0],[5,3,0],
	/*ottava fila*/[0,3.5,0],[5,3.5,0],
	/*nona fila*/[0,4,0],[5,4,0],
	/*decima fila*/[0,4.5,0],[5,4.5,0],
	/*undicesima fila*/[0,5,0],[0.5,5,0],[1,5,0],[1.5,5,0],[2,5,0],[2.5,5,0],
	[3,5,0],[3.5,5,0],[4,5,0],[4.5,5,0],[5,5,0]];

var cells1 = [[1,11,13],[1,13,2],[3,15,17],[3,17,4],[5,19,21],[5,21,6],[7,23,25],[7,25,8],
	[9,27,29],[9,29,10],[12,31,33],[12,33,14],[16,35,37],[16,37,18],
	[20,39,40],[20,40,22],[24,41,42],[24,42,26],[28,43,44],[28,44,30],[32,45,46],
	[32,46,34],[36,47,48],[36,48,38]];
var s1 = COLOR([0,0,0])(SIMPLICIAL_COMPLEX(points1)(cells1));
var cells2 = [[0,1,11],[2,13,15],[2,15,3],[4,17,19],[4,19,5],[6,21,23],[6,23,7],
	[8,25,27],[8,27,9],[10,29,31],[10,31,12],[14,33,35],[14,35,16],[18,37,39],
	[18,39,20],[22,40,41],[22,41,24],[26,42,43],[26,43,28],[30,44,45],[30,45,32],
	[34,46,47],[34,47,36],[38,48,49]];
var s2 = COLOR([255,255,255])(SIMPLICIAL_COMPLEX(points1)(cells2));

var cells3 = [[1,11,13],[1,13,2],[3,15,17],[3,17,4],[5,19,21],[5,21,6],[7,23,25],[7,25,8],
	[9,27,29],[9,29,10],[12,30,31],[12,31,14],[16,32,33],[16,33,18],[20,34,35],[20,35,22],
	[24,36,37],[24,37,26],[28,38,39]];
var s3 = COLOR([0,0,0])(SIMPLICIAL_COMPLEX(points2)(cells3));
var cells4 = [[0,1,11],[2,13,15],[2,15,3],[4,17,19],[4,19,5],[6,21,23],[6,23,7],
	[8,25,27],[8,27,9],[10,29,30],[10,30,12],[14,31,32],[14,32,16],[18,33,34],[18,34,20],
	[22,35,36],[22,36,24],[26,37,38],[26,38,28]];
var s4 = COLOR([255,255,255])(SIMPLICIAL_COMPLEX(points2)(cells4));

var surface1 = STRUCT([s1,s2]);
var surface2 = R([0,2])(-PI/2)(surface1);
var surface3 = T([2])([5])(STRUCT([s1,s2]));
var surface4 = T([0])([5])(surface2);
var surface5 = R([1,2])(PI/2)(STRUCT([s3,s4]));
var surface6 = T([0,1,2])([5,7.5,5])(R([0,1])(PI)(R([1,2])(PI)(surface5)));
var block = STRUCT([surface1,surface2,surface3,surface4,surface5,surface6]);

var basecyl = T([0,1,2])([2.5,-2,-1.5])(R([1,2])(PI/2)(COLOR([1,1,0])(CYLINDER(4,0.5))));

var p0 = [[1.5,0,1.5],[2,0,1.5],[2,0,2],[1.5,0,2]];
var c0 = BEZIER(S0)(p0);
var surf0 = MAP(ROTATIONAL_SURFACE(c0))(rot_domain);
var p1 = [[1.5,0,1.5],[1,0,1.5],[1,0,2],[1.5,0,2]];
var c1 = BEZIER(S0)(p1);
var surf1 = MAP(ROTATIONAL_SURFACE(c1))(rot_domain);
var p2 = [[1.5,-2,1.5],[2,-2,1.5],[2,-2,2],[1.5,-2,2]];
var c2 = BEZIER(S0)(p2);
var s2 = BEZIER(S1)([c0,c2]);
var surf2 = MAP(s2)(Dom2D);
var p3 = [[1.5,-2,1.5],[1,-2,1.5],[1,-2,2],[1.5,-2,2]];
var c3 = BEZIER(S0)(p3);
var s3 = BEZIER(S1)([c1,c3]);
var surf3 = MAP(s3)(Dom2D);

var cyltube = COLOR([30*cc,144*cc,255*cc])(T([0,1,2])([2.5,1.5,-0.1])(CYLINDER(0.7,0.25)));
var tube1 = T([0])([0.7])(COLOR([30*cc,144*cc,255*cc])(R([0,2])(PI/2)(STRUCT([surf0,surf1,surf2,surf3]))));

var p4a = [[0,0,0],[-0.25,0.25,0],[1.5,0.25,0],[1.25,0,0]];
var p4b = [[0,0,0],[-0.25,-0.25,0],[1.5,-0.25,0],[1.25,0,0]];
var c4a = BEZIER(S0)(p4a);
var c4b = BEZIER(S0)(p4b);
var s4 = BEZIER(S1)([c4a,c4b]);
var surf4 = MAP(s4)(Dom2D);
var p5a = [[0,0,0.25],[-0.25,0.25,0.25],[1.5,0.25,0.25],[1.25,0,0.25]];
var p5b = [[0,0,0.25],[-0.25,-0.25,0.25],[1.5,-0.25,0.25],[1.25,0,0.25]];
var c5a = BEZIER(S0)(p5a);
var c5b = BEZIER(S0)(p5b);
var s5 = BEZIER(S1)([c5a,c5b]);
var surf5 = MAP(s5)(Dom2D);
var s6 = BEZIER(S1)([c4a,c5a]);
var surf6 = MAP(s6)(Dom2D);
var s7 = BEZIER(S1)([c4b,c5b]);
var surf7 = MAP(s7)(Dom2D);
var base = T([0,1,2])([2.5,6.5,-0.1])(S([0,1])([1.8,1.5])(R([0,1])(-PI/2)(STRUCT([surf4,surf5,surf6,surf7]))));
var cyl = T([0,1,2])([2.5,5.5,0.1])(R([1,2])(-PI/3-PI/3.5)(CYLINDER(0.25,6)));

var leg1 = COLOR([30*cc,144*cc,255*cc])(STRUCT([base,cyl,T([1,2])([11,3])(R([1,2])(-PI/2)(base))]));
var leg2 = T([2])([5])(R([0,2])(PI/2)(leg1));
var leg3 = T([0,2])([5,5])(R([0,2])(PI)(leg1));
var leg4 = T([0])([5])(R([0,2])(3*PI/2)(leg1));

var table = STRUCT([block,basecyl,cyltube,tube1,leg1,leg2,leg3,leg4]);

DRAW(table);