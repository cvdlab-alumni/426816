//-----------------------------V Function-----------------------------

function vertexs(origin){
	var s = '';
	var o = origin;

	for (var i=0; i<o.length; i++){
		var currVal = o[i][2];									
		if (currVal===""){												
			s+='v '+' '+o[i][0]+' '+o[i][1]+' '+o[i][2]+'\n';
		}
		else{
			s+='v '+' '+o[i][0]+' '+o[i][1]+' 0 \n';
		}
	}
	return s;
}

//-----------------------------FV Function-----------------------------
function facets(origin){
	var s = '';
	var o = origin;

	var length1 = o.length;
	for(var i=0; i<length1; i++){
		var length2 = o[i].length;
		for(var j=0; j<length2;j++){
			if(j == 0){s+='f '+o[i][j]+' ';}					
			else{
				if(j == length2-1){s+=o[i][j]+'\n';}					
				else{
					s+=o[i][j]+' ';									
				}
			}
 		}
	}
	return s;
}

FV = [[5,6,7,8],
[0,5,8],
[0,4,5],
[1,2,4,5],
[2,3,5,6],
[0,8,7], [3,6,7], [1,2,3], [0,1,4]
]

V = [[0,6],
[0,0],
[3,0],
[6,0],
[0,3],
[3,3],
[6,3],
[6,6],
[3,6]]

//print
function print_main(V,FV){
	console.log(vertexs(V));
	console.log(facets(FV));
}

print_main(V,FV);