from pyplasm import *
import scipy
from scipy import *

############################################################################
def VERTEXTRUDE((V,coords)):
    """
        Utility function to generate the output model vertices in a 
        multiple extrusion of a LAR model.
        V is a list of d-vertices (each given as a list of d coordinates).
        coords is a list of absolute translation parameters to be applied to 
        V in order to generate the output vertices.
        
        Return a new list of (d+1)-vertices.
    """
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def cumsum(iterable):
    # cumulative addition: list(cumsum(range(4))) => [0, 1, 3, 6]
    iterable = iter(iterable)
    s = iterable.next()
    yield s
    for c in iterable:
        s = s + c
        yield s

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])

############################################################################

Dom1D = INTERVALS(1)(60)
#Dom2D = PROD([Dom1D,Dom1D])
Dom2D = GRID([10,10])
Dom2D_inv = MAP([S2,S1])(GRID([10,10]))

########### ES2

#profilo laterale, piano xy, z=0

p01 = [[-5.3,0,0],[-4.8,0.9,0],[-3.2,0.7,0],[-3,1.2,0]]
c01 = BEZIER(S1)(p01)
l01 = MAP(c01)(Dom1D)

p02 = [[-3,1.2,0],[-1,0.7,0],[0,1.7,0]]
c02 = BEZIER(S1)(p02)
l02 = MAP(c02)(Dom1D)

p03 = [[0,1.7,0],[0.5,0.3,0],[1.8,0.4,0],[2,2.2,0]]
c03 = BEZIER(S1)(p03)
l03 = MAP(c03)(Dom1D)

p04 = [[2,2.2,0],[4.2,1.8,0],[5.1,0.5,0],[5.3,0,0]]
c04 = BEZIER(S1)(p04)
l04 = MAP(c04)(Dom1D)

p05 = [[-5.3,0,0],[-5.3,-1,0],[-3.2,-1,0]]
c05 = BEZIER(S1)(p05)
l05 = MAP(c05)(Dom1D)

p06 = [[-3.2,-1,0],[2,-1,0]]
c06 = BEZIER(S1)(p06)
l06 = MAP(c06)(Dom1D)

p07 = [[2,-1,0],[5.3,-0.6,0],[5.3,0,0]]
c07 = BEZIER(S1)(p07)
l07 = MAP(c07)(Dom1D)

l0 = STRUCT([l01,l02,l03,l04,l05,l06,l07])


#profilo frontale, piano zy, x=0

p11 = [[0,-1.1,0],[0,-1.13,-1.25],[0,-1.1,-1.5],[0,0.2,-1.45],[0,0.95,-0.1],[0,1.7,-0.4],[0,1.7,0]]
c11 = BEZIER(S1)(p11)
l11 = MAP(c11)(Dom1D)

p12 = [[0,-1.1,0],[0,-1.13,1.25],[0,-1.1,1.5],[0,0.2,1.45],[0,0.95,0.1],[0,1.7,0.4],[0,1.7,0]]
c12 = BEZIER(S1)(p12)
l12 = MAP(c12)(Dom1D)

l1 = STRUCT([l11,l12])


#profilo dall'alto, piano xz, y=0

p21 = [[-5.3,0,0],[-5.3,0,0.75],[-5.3,0,1.25],[0,0,1.2],[4.5,0,1.4],[5.3,0,0]]
c21 = BEZIER(S1)(p21)
l21 = MAP(c21)(Dom1D)

p22 = [[-5.3,0,0],[-5.3,0,-0.75],[-5.3,0,-1.25],[0,0,-1.2],[4.5,0,-1.4],[5.3,0,0]]
c22 = BEZIER(S1)(p22)
l22 = MAP(c22)(Dom1D)

l2 = STRUCT([l21,l22])


#profili uniti

prof = STRUCT([l0,l1,l2])

VIEW(prof)