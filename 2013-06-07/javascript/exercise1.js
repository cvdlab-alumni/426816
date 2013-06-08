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


var model = STRUCT([DTM]);
DRAW(model);
