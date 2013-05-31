//Serena Sforza - matr. 426816
//3D model of a pair of glasses rayban wayfarer.


//central part

//right half

var Dom1D = INTERVALS(1)(20);
var Dom2D = DOMAIN([[0,1], [0,1]])([20,20]);

//bottom line 0
var p0 = [[0,0,0],[3.5,0,0],[-2,-10,0],[20,-8,0],[10,2,0],[13,2,0]];
var c0 = BEZIER(S0)(p0);

//bottom line 1
var p1 = [[2,0,0],[3.5,-5.5,0],[13,-7.5,0],[11.5,2,0]];
var c1 = BEZIER(S0)(p1);

//filling_z
var p0b = [[0,0,0.8],[3.5,0,0.8],[-2,-10,0.8],[20,-8,0.8],[10,2,0.8],[13,2,0.8]];
var c0b = BEZIER(S0)(p0b);

var p1b = [[2,0,0.8],[3.5,-5.5,0.8],[13,-7.5,0.8],[11.5,2,0.8]];
var c1b = BEZIER(S0)(p1b);

var s0 = BEZIER(S1)([c0,c0b]);
var surf0 = MAP(s0)(Dom2D);

var s1 = BEZIER(S1)([c1,c1b]);
var surf1 = MAP(s1)(Dom2D);

//filling_x
var s2 = BEZIER(S1)([c0,c1]);
var surf2 = MAP(s2)(Dom2D);

var s3 = BEZIER(S1)([c0b,c1b]);
var surf3 = MAP(s3)(Dom2D);


//top line 0
var p2 = [[2,0,0],[2,2,0],[2.5,2,0],[10.5,4,0],[11.5,2,0]];
var c2 = BEZIER(S0)(p2);


//top line 1
var p3 = [[0,1.5,0],[2,2,0],[3.5,3.5,0],[4.5,4,0],[12.5,4,0],
			[12.5,3.2,0],[13,3.3,0]];
var c3 = BEZIER(S0)(p3);


//filling_z
var p2b = [[2,0,0.8],[2,2,0.8],[2.5,2,0.8],[10.5,4,0.8],[11.5,2,0.8]];
var c2b = BEZIER(S0)(p2b);

var s4 = BEZIER(S1)([c2,c2b]);
var surf4 = MAP(s4)(Dom2D);

var p3b = [[0,1.5,0.8],[2,2,0.8],[3.5,3.5,0.8],[4.5,4,0.8],[12.5,4,0.8],
			[12.5,3.2,0.8],[13,3.3,0.8]];
var c3b = BEZIER(S0)(p3b);

var s8 = BEZIER(S1)([c3,c3b]);
var surf8 = MAP(s8)(Dom2D);

//filling_x
p00 = [[0,0,0],[0,1.5,0]];
c00 = BEZIER(S0)(p00);
p11 = [[13,3.3,0],[13,2,0]];
c11 = BEZIER(S0)(p11);
p22 = [[2,0,0],[2,1.5,0]];
c22 = BEZIER(S0)(p22);
p33 = [[11.5,3.3,0],[11.5,2,0]];
c33 = BEZIER(S0)(p33);

p00b = [[0,0,0.8],[0,1.5,0.8]];
c00b = BEZIER(S0)(p00b);
p11b = [[13,3.3,0.8],[13,2,0.8]];
c11b = BEZIER(S0)(p11b);
p22b = [[2,0,0.8],[2,1.5,0.8]];
c22b = BEZIER(S0)(p22b);
p33b = [[11.5,3.3,0.8],[11.5,2,0.8]];
c33b = BEZIER(S0)(p33b);

var s5 = BEZIER(S1)([c2,c3]);
var surf5 = MAP(s5)(Dom2D);

var s6 = BEZIER(S1)([c00,c22]);
var surf6 = MAP(s6)(Dom2D);

var s7 = BEZIER(S1)([c11,c33]);
var surf7 = MAP(s7)(Dom2D);

var s5b = BEZIER(S1)([c2b,c3b]);
var surf5b = MAP(s5b)(Dom2D);

var s6b = BEZIER(S1)([c00b,c22b]);
var surf6b = MAP(s6b)(Dom2D);

var s7b = BEZIER(S1)([c11b,c33b]);
var surf7b = MAP(s7b)(Dom2D);

var s9 = BEZIER(S1)([c11,c11b]);
var surf9 = MAP(s9)(Dom2D);

var surf_right = COLOR([1,1,0])(STRUCT([surf0,surf1,surf2,surf3,
		surf4,surf5,surf5b,surf6,surf6b,surf7,surf7b,surf8,surf9]));


//glass
var p4 = [[2,0,0.4],[3.5,-5.5,0.4],[13,-7.5,0.4],[11.5,2,0.4]];
var c4 = BEZIER(S0)(p4);

var p5 = [[0,1.5,0.4],[2,2,0.4],[3.5,3.5,0.4],[4.5,4,0.4],[12.5,4,0.4],
			[12.5,3.2,0.4],[13,3.3,0.4]];
var c5 = BEZIER(S0)(p5);

var s10 = BEZIER(S1)([c4,c5]);
var surf10 = MAP(s10)(Dom2D);
var surf_glass_right = COLOR([0,0,1,0.5])(surf10);

var surf_tot_right = STRUCT([surf_right,surf_glass_right]);


//left half

var surf_tot_left = T([2])([0.8])(R([0,2])(PI)(surf_tot_right));


//sidepieces

//sidepiece_right
var h2 = [[12.7,3.2,0],[12.5,3.2,0],[12.4,1.6,0],[12.7,2,0],
			[12.9,1.6,0],[13,3.2,0],[12.7,3.2,0]];
var k2 = BEZIER(S0)(h2);

var h3 = [[12.8,3.2,-2],[12.5,3.2,-2],[12.5,1.1,-2],[12.8,2,-2],
			[13,1.1,-2],[13,3.2,-2],[12.8,3.2,-2]];
var k3 = BEZIER(S0)(h3);

var h4 = [[12.8,3.15,-4],[12.5,3.15,-4],[12.5,0.65,-4],[12.8,1.7,-4],
			[13,0.65,-4],[13,3.15,-4],[12.8,3.15,-4]];
var k4 = BEZIER(S0)(h4);

var h5 = [[12.8,2.9,-6],[12.5,2.9,-6],[12.5,0.5,-6],[12.8,1,-6],
			[13,0.5,-6],[13,2.9,-6],[12.8,2.9,-6]];
var k5 = BEZIER(S0)(h5);

var h6 = [[12.8,2.6,-8],[12.5,2.6,-8],[12.5,0.25,-8],[12.8,0.8,-8],
			[13,0.25,-8],[13,2.6,-8],[12.8,2.6,-8]];
var k6 = BEZIER(S0)(h6);

var h7 = [[12.8,2.1,-10],[12.5,2.1,-10],[12.5,-0.2,-10],[12.8,0.6,-10],
			[13,-0.2,-10],[13,2.1,-10],[12.8,2.1,-10]];
var k7 = BEZIER(S0)(h7);

var h8 = [[12.8,2,-10.5],[12.5,2,-10.5],[12.5,0.25,-10.5],[12.8,0.6,-10.5],
			[13,0.25,-10.5],[13,2,-10.5],[12.8,2,-10.5]];
var k8 = BEZIER(S0)(h8);

var h9 = [[12.8,1.8,-11],[12.5,1.8,-11],[12.5,0.4,-11],[12.8,0.7,-11],
			[13,0.4,-11],[13,1.8,-11],[12.8,1.8,-11]];
var k9 = BEZIER(S0)(h9);

var h10 = [[12.8,1.65,-11.5],[12.5,1.65,-11.5],[12.5,0.6,-11.5],[12.8,0.7,-11.5],
			[13,0.6,-11.5],[13,1.65,-11.5],[12.8,1.65,-11.5]];
var k10 = BEZIER(S0)(h10);

var h11 = [[12.8,1.5,-12],[12.5,1.5,-12],[12.5,0.6,-12],[12.8,0.7,-12],
			[13,0.6,-12],[13,1.5,-12],[12.8,1.5,-12]];
var k11 = BEZIER(S0)(h11);

var h12 = [[12.8,1.3,-12.5],[12.5,1.3,-12.5],[12.5,0.3,-12.5],[12.8,0.7,-12.5],
			[13,0.3,-12.5],[13,1.3,-12.5],[12.8,1.3,-12.5]];
var k12 = BEZIER(S0)(h12);

var h13 = [[12.8,1.1,-13],[12.5,1.1,-13],[12.5,-0.1,-13],[12.8,0.7,-13],
			[13,-0.1,-13],[13,1.1,-13],[12.8,1.1,-13]];
var k13 = BEZIER(S0)(h13);

var h14 = [[12.8,0.8,-13.5],[12.5,0.8,-13.5],[12.5,-0.9,-13.5],[12.8,0.7,-13.5],
			[13,-0.9,-13.5],[13,0.8,-13.5],[12.8,0.8,-13.5]];
var k14 = BEZIER(S0)(h14);

var h15 = [[12.8,0.3,-14.5],[12.35,0.3,-14.5],[12.5,-2.9,-14.5],[12.8,-0.3,-14.5],
			[13,-2.9,-14.5],[13.05,0.3,-14.5],[12.8,0.3,-14.5]];
var k15 = BEZIER(S0)(h15);

var h16 = [[12.8,-0.7,-16],[12.35,-0.7,-16],[12.5,-6.5,-16],[12.8,-0.8,-16],
			[13,-6.5,-16],[13.05,-0.7,-16],[12.8,-0.7,-16]];
var k16 = BEZIER(S0)(h16);

var h17 = [[12.8,-0.85,-16.25],[12.35,-0.85,-16.25],[12.5,-6.9,-16.25],[12.8,-0.8,-16.25],
			[13,-6.9,-16.25],[13.05,-0.85,-16.25],[12.8,-0.85,-16.25]];
var k17 = BEZIER(S0)(h17);

var h18 = [[12.8,-1.08,-16.5],[12.35,-1.08,-16.5],[12.5,-7.1,-16.5],[12.8,-0.8,-16.5],
			[13,-7.1,-16.5],[13.05,-1.08,-16.5],[12.8,-1.08,-16.5]];
var k18 = BEZIER(S0)(h18);

var h19 = [[12.8,-1.45,-17],[12.35,-1.45,-17],[12.5,-7.1,-17],[12.8,-0.8,-17],
			[13,-7.1,-17],[13.05,-1.45,-17],[12.8,-1.45,-17]];
var k19 = BEZIER(S0)(h19);

var h20 = [[12.8,-2,-17.5],[12.35,-2,-17.5],[12.5,-6.6,-17.5],[12.8,-0.8,-17.5],
			[13,-6.6,-17.5],[13.05,-2,-17.5],[12.8,-2,-17.5]];
var k20 = BEZIER(S0)(h20);

var h21 = [[12.8,-2.7,-18],[12.35,-2.7,-18],[12.5,-5.1,-18],[12.6,-2,-18],
			[13,-5.1,-18],[13.05,-2.7,-18],[12.8,-2.7,-18]];
var k21 = BEZIER(S0)(h21);

var h22 = [[12.8,-3,-18.2],[12.4,-3,-18.2],[12.5,-4,-18.2],[12.8,-3,-18.2],
			[13,-4,-18.2],[13,-3,-18.2],[12.8,-3,-18.2]];
var k22 = BEZIER(S0)(h22);

var h23 = [[12.8,-3.2,-18.3],[12.8,-3.2,-18.3],[12.5,-3,-18.3],[12.8,-4,-18.3],
			[13,-3,-18.3],[12.7,-3.2,-18.3],[12.8,-3.2,-18.3]];
var k23 = BEZIER(S0)(h23);

//filling_z
var stg10 = BEZIER(S1)([k2,k3,k4,k5,k6,k7]);
var stg11 = MAP(stg10)(Dom2D);

var stg20 = BEZIER(S1)([k7,k8,k9,k10,k11,k12,k13,k14]);
var stg21 = MAP(stg20)(Dom2D);

var stg40 = BEZIER(S1)([k14,k15,k16]);
var stg41 = MAP(stg40)(Dom2D);

var stg30 = BEZIER(S1)([k16,k17,k18]);
var stg31 = MAP(stg30)(Dom2D);

var stg50 = BEZIER(S1)([k18,k19,k20,k21,k22,k23]);
var stg51 = MAP(stg50)(Dom2D);

var stg60 = BEZIER(S1)([k23,[12.75,-3.25,-18.31]]);
var stg61 = MAP(stg60)(Dom2D);

var sidepiece_right = COLOR([1,1,0])(STRUCT([stg11,stg21,stg41,stg31,stg51,stg61]));

//sidepiece_left

var sidepiece_left = T([0])([-25.4])(sidepiece_right);


//pins e nosepieces

//pins
var a0 = [[0,0,0],[0.3,0.2,0],[0.8,0.2,0],[1.1,0,0]];
var b0 = BEZIER(S0)(a0);

var a0b = [[0,0,0.1],[0.3,0.2,0.1],[0.8,0.2,0.1],[1.1,0,0.1]];
var b0b = BEZIER(S0)(a0b);

var a1 = [[0,0,0],[0.3,-0.2,0],[0.8,-0.2,0],[1.1,0,0]];
var b1 = BEZIER(S0)(a1);

var a1b = [[0,0,0.1],[0.3,-0.2,0.1],[0.8,-0.2,0.1],[1.1,0,0.1]];
var b1b = BEZIER(S0)(a1b);

var aa = BEZIER(S1)([b0,b1]);
var da = MAP(aa)(Dom2D);

var ab = BEZIER(S1)([b0,b0b]);
var db = MAP(ab)(Dom2D);

var ac = BEZIER(S1)([b0b,b1b]);
var dc = MAP(ac)(Dom2D);

var ad = BEZIER(S1)([b1,b1b]);
var dd = MAP(ad)(Dom2D);

var d = STRUCT([da,db,dc,dd]);

var pin_right = R([0,1])([0.1])(T([0,1,2])([11.5,1.4,0.8])(d));

var pin_left = T([2])([1.7])(R([0,2])([PI])(pin_right));

//poggianaso
var a2 = [[0,0,0],[0,0.6,0],[2.2,0.6,0],[2.2,0,0]];
var b2 = BEZIER(S0)(a2);

var a2b = [[0,0,0.4],[0,0.6,0.4],[2.2,0.6,0.4],[2.2,0,0.4]];
var b2b = BEZIER(S0)(a2b);

var a3 = [[0,0,0],[2.2,0,0]];
var b3 = BEZIER(S0)(a3);

var a3b = [[0,0,0.4],[2.2,0,0.4]];
var b3b = BEZIER(S0)(a3b);

var aa2 = BEZIER(S1)([b2,b3]);
var da2 = MAP(aa2)(Dom2D);

var ab2 = BEZIER(S1)([b2,b2b]);
var db2 = MAP(ab2)(Dom2D);

var ac2 = BEZIER(S1)([b2b,b3b]);
var dc2 = MAP(ac2)(Dom2D);

var ad2 = BEZIER(S1)([b3,b3b]);
var dd2 = MAP(ad2)(Dom2D);

var d2 = STRUCT([da2,db2,dc2,dd2]);

var nosepiece_right = T([0,1])([1.6,-1.5])(R([0,1])([-PI/3.2])(R([1,2])([-PI/2])(d2)));

var nosepiece_left = T([0,1])([-2,-1.4])(R([0,1])([(PI/3.3)+PI])(R([1,2])([-PI/2])(d2)));

var nosepieces = COLOR([1,1,0,0.8])(STRUCT([nosepiece_right,nosepiece_left]));

//final model
var model = STRUCT([surf_tot_right,
		    surf_tot_left,
		    nosepieces,
		    pin_left,
		    pin_right,
		    sidepiece_left,
		    sidepiece_right]);
