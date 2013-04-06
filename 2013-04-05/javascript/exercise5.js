//Utility functions

//T(dims)(values)(object)

T = function (dims) {
  dims = dims.map(function(dim){
    return dim - 1;
  });
    return function (values) {
      return function (object) {
       return object.clone().translate(dims, values);
      };
    };
  }

//R
R = function (dims) {
  dims = dims.map(function(dim){
    return dim - 1;
  });
    return function (angle) {
      return function (object) {
        return object.clone().rotate(dims, angle);
      };
    };
  }

//S
S = function (dims) {
  dims = dims.map(function(dim){
    return dim - 1;
  });
    return function (values) {
      return function (object) {
        return object.clone().scale(dims, values);
      };
    };
  }
function (dims) {
  dims = dims.map(function(dim){
    return dim - 1;
  });
    return function (values) {
      return function (object) {
        return object.clone().scale(dims, values);
      };
    };
  }

S3=S2
S2=S1
S1=S0


GRID = SIMPLEX_GRID
VIEW = DRAW
NN = REPLICA

//Funzione che definisce un arco di circonferenza
function arc(alpha,r,R){
  var domain = DOMAIN([[0,alpha], [r,R]])([36,1]);
  var mapping = function(v){
    var a = v[0];
    var r = v[1];
    return [r*COS(a), r*SIN(a)];
  };
  var model = MAP(mapping)(domain);
  return model;
};


//Exercise5

//################# STEP ##################################################################################################

depth = 0.25; 

raiser = 2.5/14;

var point = [[0,0],[0,0.14+raiser],[depth,raiser],[depth,0.14+raiser]];

var cells = [[0,1,2],[1,2,3]];

step2D = SIMPLICIAL_COMPLEX(point)(cells);

step3D = MAP([S1,S3,S2])(EXTRUDE([1.1])(step2D));

//############### RAMP #####################################################################################################

ramp1 = T([1,2,3])([2.5,5.5,-0.03857])(STRUCT(NN(14)([step3D,T([1,3])([0.25,0.17857])])));

ramp2 = T([1,2,3])([1.25,5.5,-0.03857+2.5])(STRUCT(NN(14)([step3D,T([1,3])([0.25,0.17857])])));

ramp3 = T([1,2,3])([5.5,5.5,5-0.03857])(STRUCT(NN(14)([step3D,T([1,3])([0.25,0.17857])])));

//############################################################################################################################

building5 = STRUCT([ramp1,ramp2,ramp3]);
