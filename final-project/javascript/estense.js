var cc = 0.004;

var c1 = CUBOID([0.3,0.2,3]);
var c2 = CUBOID([0.4,0.2,0.3]);
var comp = COLOR([150*cc,75*cc,0*cc])(STRUCT([c1,T([0])([0.7])(c1),
	T([0])([0.3])(c2),T([0,2])([0.3,2.7])(c2)]));

var BLOCK = function (n,comp){
	var base = CUBOID([n,n]);
	var block = COLOR([150*cc,75*cc,0*cc])(STRUCT([base]));
	var line1 = STRUCT([comp]);
	for (var i = 1; i <= n-1; i++) {
		line1 = STRUCT([line1,T([0])([i])(comp)]);
	};
	var line2 = R([0,1])(PI/2)(line1);
	block = COLOR([150*cc,75*cc,0*cc])(STRUCT([block,base,line1,line2,T([0])([n])(line2),T([1])([n])(line1),T([2])([3])(base)]));
	return block;
};

var block1 = BLOCK(14,comp);
var block2 = T([2])([3])(BLOCK(13,comp));
var block3 = T([2])([6])(BLOCK(12,comp));
var block4 = T([2])([9])(BLOCK(11,comp));
var block5 = T([2])([12])(BLOCK(10,comp));
var block6 = T([1,2])([1,15])(BLOCK(9,comp));
var block7 = T([1,2])([2,18])(BLOCK(8,comp));
var block8 = T([1,2])([3,21])(BLOCK(7,comp));
var block9 = T([1,2])([4,24])(BLOCK(6,comp));
var block10 = T([1,2])([4,27])(BLOCK(5,comp));
var block11 = T([1,2])([4,30])(BLOCK(4,comp));
var block12 = T([1,2])([4,33])(BLOCK(3,comp));
var block13 = T([1,2])([4,36])(BLOCK(2,comp));

var estense = STRUCT([block1,block2,block3,block4,block5,block6,
	block7,block8,block9,block10,block11,block12,block13]);

DRAW(estense);