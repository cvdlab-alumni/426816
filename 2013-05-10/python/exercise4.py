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

########### ES3

p0 = [[-0.3,0,0],[-0.3,0.4,0],[0.3,0.4,0],[0.3,0,0]]
c0 = BEZIER(S1)(p0)
#l0 = MAP(c0)(Dom1D)

p0_back = [[-0.3,0,0.02],[-0.3,0.4,0.02],[0.3,0.4,0.02],[0.3,0,0.02]]
c0_back = BEZIER(S1)(p0_back)
#l0_back = MAP(c0_back)(Dom1D)

p0b = [[0.3,0,0],[0.3,-0.4,0],[-0.3,-0.4,0],[-0.3,0,0]]
c0b = BEZIER(S1)(p0b)
#l0b = MAP(c0b)(Dom1D)

p0b_back = [[0.3,0,0.02],[0.3,-0.4,0.02],[-0.3,-0.4,0.02],[-0.3,0,0.02]]
c0b_back = BEZIER(S1)(p0b_back)
#l0b_back = MAP(c0b_back)(Dom1D)

p1 = [[-0.27,0,0],[-0.27,0.37,0],[0.27,0.37,0],[0.27,0,0]]
c1 = BEZIER(S1)(p1)
#l1 = MAP(c1)(Dom1D)

p1_back = [[-0.27,0,0.02],[-0.27,0.37,0.02],[0.27,0.37,0.02],[0.27,0,0.02]]
c1_back = BEZIER(S1)(p1_back)
#l1_back = MAP(c1_back)(Dom1D)

p1b = [[0.27,0,0],[0.27,-0.37,0],[-0.27,-0.37,0],[-0.27,0,0]]
c1b = BEZIER(S1)(p1b)
#l1b = MAP(c1b)(Dom1D)

p1b_back = [[0.27,0,0.02],[0.27,-0.37,0.02],[-0.27,-0.37,0.02],[-0.27,0,0.02]]
c1b_back = BEZIER(S1)(p1b_back)
#l1b_back = MAP(c1b_back)(Dom1D)

p2 = [[-0.07,0,0],[-0.07,0.09,0],[0.07,0.09,0],[0.07,0,0]]
c2 = BEZIER(S1)(p2)
#l2 = MAP(c2)(Dom1D)

p2_back = [[-0.07,0,0.02],[-0.07,0.09,0.02],[0.07,0.09,0.02],[0.07,0,0.02]]
c2_back = BEZIER(S1)(p2_back)
#l2_back = MAP(c2_back)(Dom1D)

p2b = [[0.07,0,0],[0.07,-0.09,0],[-0.07,-0.09,0],[-0.07,0,0]]
c2b = BEZIER(S1)(p2b)
#l2b = MAP(c2b)(Dom1D)

p2b_back = [[0.07,0,0.02],[0.07,-0.09,0.02],[-0.07,-0.09,0.02],[-0.07,0,0.02]]
c2b_back = BEZIER(S1)(p2b_back)
#l2b_back = MAP(c2b_back)(Dom1D)

p3 = [[-0.045,0,0],[-0.045,0.06,0],[0.045,0.06,0],[0.045,0,0]]
c3 = BEZIER(S1)(p3)
#l3 = MAP(c3)(Dom1D)

p3_back = [[-0.045,0,0.02],[-0.045,0.06,0.02],[0.045,0.06,0.02],[0.045,0,0.02]]
c3_back = BEZIER(S1)(p3_back)
#l3_back = MAP(c3_back)(Dom1D)

p3b = [[0.045,0,0],[0.045,-0.06,0],[-0.045,-0.06,0],[-0.045,0,0]]
c3b = BEZIER(S1)(p3b)
#l3b = MAP(c3b)(Dom1D)

p3b_back = [[0.045,0,0.02],[0.045,-0.06,0.02],[-0.045,-0.06,0.02],[-0.045,0,0.02]]
c3b_back = BEZIER(S1)(p3b_back)
#l3b_back = MAP(c3b_back)(Dom1D)

s01 = BEZIER(S2)([c0,c1])
surf01 = MAP(s01)(Dom2D_inv)

s02 = BEZIER(S2)([c0b,c1b])
surf02 = MAP(s02)(Dom2D_inv)

s03 = BEZIER(S2)([c0,c0_back])
surf03 = MAP(s03)(Dom2D)

s04 = BEZIER(S2)([c1,c1_back])
surf04 = MAP(s04)(Dom2D)

s05 = BEZIER(S2)([c0b,c0b_back])
surf05 = MAP(s05)(Dom2D)

s06 = BEZIER(S2)([c1b,c1b_back])
surf06 = MAP(s06)(Dom2D)

s07 = BEZIER(S2)([c0_back,c1_back])
surf07 = MAP(s07)(Dom2D_inv)

s08 = BEZIER(S2)([c0b_back,c1b_back])
surf08 = MAP(s08)(Dom2D_inv)

surf0 = STRUCT([surf01,surf02,surf03,surf04,surf05,surf06,surf07,surf08])

s11 = BEZIER(S2)([c2,c3])
surf11 = MAP(s11)(Dom2D_inv)

s12 = BEZIER(S2)([c2b,c3b])
surf12 = MAP(s12)(Dom2D_inv)

s13 = BEZIER(S2)([c2,c2_back])
surf13 = MAP(s13)(Dom2D_inv)

s14 = BEZIER(S2)([c3,c3_back])
surf14 = MAP(s14)(Dom2D_inv)

s15 = BEZIER(S2)([c2_back,c3_back])
surf15 = MAP(s15)(Dom2D_inv)

s16 = BEZIER(S2)([c2b_back,c3b_back])
surf16 = MAP(s16)(Dom2D_inv)

s17 = BEZIER(S2)([c2b,c2b_back])
surf17 = MAP(s17)(Dom2D_inv)

s18 = BEZIER(S2)([c3b,c3b_back])
surf18 = MAP(s18)(Dom2D_inv)

surf1 = STRUCT([surf11,surf12,surf13,surf14,surf15,surf16,surf17,surf18])

p4 = [[0.06,-0.025,0],[0.28,-0.025,0]]
c4 = BEZIER(S1)(p4)
#l4 = MAP(c4)(Dom1D)

p4_back = [[0.06,-0.025,0.02],[0.28,-0.025,0.02]]
c4_back = BEZIER(S1)(p4_back)
#l4_back = MAP(c4_back)(Dom1D)

p4b = [[0.06,0.025,0],[0.28,0.025,0]]
c4b = BEZIER(S1)(p4b)
#l4b = MAP(c4b)(Dom1D)

p4b_back = [[0.06,0.025,0.02],[0.28,0.025,0.02]]
c4b_back = BEZIER(S1)(p4b_back)
#l4b_back = MAP(c4b_back)(Dom1D)

s21 = BEZIER(S2)([c4,c4b])
surf21 = MAP(s21)(Dom2D)

s22 = BEZIER(S2)([c4_back,c4b_back])
surf22 = MAP(s22)(Dom2D)

s23 = BEZIER(S2)([c4,c4_back])
surf23 = MAP(s23)(Dom2D)

s24 = BEZIER(S2)([c4b,c4b_back])
surf24 = MAP(s24)(Dom2D)

surf2 = STRUCT([surf21,surf22,surf23,surf24])

radii = STRUCT([surf2,
                R([1,2])(PI/3)(surf2),
                R([1,2])(2*PI/3)(surf2),
                R([1,2])(3*PI/3)(surf2),
                R([1,2])(4*PI/3)(surf2),
                R([1,2])(5*PI/3)(surf2),
                R([1,2])(6*PI/3)(surf2),])

p5 = [[-0.34,0,0.018],[-0.34,0.44,0.018],[0.34,0.44,0.018],[0.34,0,0.018]]
c5 = BEZIER(S1)(p5)
#l5 = MAP(c5)(Dom1D)

p5b = [[0.34,0,0.018],[0.34,-0.44,0.018],[-0.34,-0.44,0.018],[-0.34,0,0.018]]
c5b = BEZIER(S1)(p5b)
#l5b = MAP(c5b)(Dom1D)

p5_back = [[-0.34,0,0.268],[-0.34,0.44,0.268],[0.34,0.44,0.268],[0.34,0,0.268]]
c5_back = BEZIER(S1)(p5_back)
l5_back = MAP(c5_back)(Dom1D)

p5b_back = [[0.34,0,0.268],[0.34,-0.44,0.268],[-0.34,-0.44,0.268],[-0.34,0,0.268]]
c5b_back = BEZIER(S1)(p5b_back)
l5b_back = MAP(c5b_back)(Dom1D)

p6 = [[-0.27,0,0.286],[-0.27,0.37,0.286],[0.27,0.37,0.286],[0.27,0,0.286]]
c6 = BEZIER(S1)(p6)

p6b = [[0.27,0,0.286],[0.27,-0.37,0.286],[-0.27,-0.37,0.286],[-0.27,0,0.286]]
c6b = BEZIER(S1)(p6b)

s30 = BEZIER(S2)([c5,c0])
surf30 = MAP(s30)(Dom2D)

s31 = BEZIER(S2)([c5b,c0b])
surf31 = MAP(s31)(Dom2D)

s32 = BEZIER(S2)([c5,c5_back])
surf32 = MAP(s32)(Dom2D)

s33 = BEZIER(S2)([c5b,c5b_back])
surf33 = MAP(s33)(Dom2D)

s41 = BEZIER(S2)([c1,c6])
surf41 = MAP(s41)(Dom2D)

s42 = BEZIER(S2)([c1b,c6b])
surf42 = MAP(s42)(Dom2D)

p7 = [[-0.3,0,0.286],[-0.3,0.4,0.286],[0.3,0.4,0.286],[0.3,0,0.286]]
c7 = BEZIER(S1)(p7)
l7 = MAP(c7)(Dom1D)

p7b = [[0.3,0,0.286],[0.3,-0.4,0.286],[-0.3,-0.4,0.286],[-0.3,0,0.286]]
c7b = BEZIER(S1)(p7b)
l7b = MAP(c7b)(Dom1D)

s43 = BEZIER(S2)([c6,c7])
surf43 = MAP(s43)(Dom2D)

s44 = BEZIER(S2)([c6b,c7b])
surf44 = MAP(s44)(Dom2D)

s45 = BEZIER(S2)([c5_back,c7])
surf45 = MAP(s45)(Dom2D)

s46 = BEZIER(S2)([c5b_back,c7b])
surf46 = MAP(s46)(Dom2D)

surf4 = STRUCT([surf41,surf42,surf43,surf44])

tire = STRUCT([surf0,surf1,radii,surf4])

casing = COLOR([0,0,0])(STRUCT([surf30,surf31,surf32,surf33,surf45,surf46]))

wheel = S([1,2,3])([2.75,2.75,2.75])(STRUCT([tire,casing]))

wheel1 =  T([1,2,3])([-3.5,-0.5,-1.8])(wheel)

wheel2 = T([1,2,3])([-3.5,-0.5,1.8])(R([1,3])(PI)(wheel))

wheel3 = T([1,2,3])([3.5,-0.5,-1.8])(wheel)

wheel4 = T([1,2,3])([3.5,-0.5,1.8])(R([1,3])(PI)(wheel))


########### ES4

p0 = [[-0.1,0,0.9],[-0.1,0,1],[0.1,0,1],[0.1,0,0.9]]
c0 = BEZIER(S1)(p0)
l0 = MAP(c0)(Dom1D)

p0b = [[0.1,0,0.9],[0.1,0,0.8],[-0.1,0,0.8],[-0.1,0,0.9]]
c0b = BEZIER(S1)(p0b)
l0b = MAP(c0b)(Dom1D)

p1 = [[-0.1,0.85,0.85],[-0.1,0.95,0.95],[0.1,0.95,0.95],[0.1,0.85,0.85]]
c1 = BEZIER(S1)(p1)
l1 = MAP(c1)(Dom1D)

p1b = [[0.1,0.85,0.85],[0.1,0.75,0.75],[-0.1,0.75,0.75],[-0.1,0.85,0.85]]
c1b = BEZIER(S1)(p1b)
l1b = MAP(c1b)(Dom1D)

p3 = [[-0.15,0.9,0.4],[-0.15,1.25,0.3],[0.15,1.25,0.3],[0.15,0.9,0.4]]
c3 = BEZIER(S1)(p3)
l3 = MAP(c3)(Dom1D)

p3b = [[0.15,0.9,0.4],[0.15,0.55,0.5],[-0.15,0.55,0.5],[-0.15,0.9,0.4]]
c3b = BEZIER(S1)(p3b)
l3b = MAP(c3b)(Dom1D)

p2 = [[-0.1,0.9,0],[-0.1,1,0],[0.1,1,0],[0.1,0.9,0]]
c2 = BEZIER(S1)(p2)
l2 = MAP(c2)(Dom1D)

p2b = [[0.1,0.9,0],[0.1,0.8,0],[-0.1,0.8,0],[-0.1,0.9,0]]
c2b = BEZIER(S1)(p2b)
l2b = MAP(c2b)(Dom1D)

s01 = BEZIER(S2)([c0,c1,c2])
surf01 = MAP(s01)(Dom2D)

s02 = BEZIER(S2)([c0b,c1b,c2b])
surf02 = MAP(s02)(Dom2D)

surf0 = STRUCT([surf01,surf02])

steeringwheel_part1 = STRUCT([surf0,R([1,2])(PI)(surf0)])


p4 = [[0.6,-0.4,0.2],[0,-0.3,3.5]]
c4 = BEZIER(S1)(p4)
l4 = MAP(c4)(Dom1D)

p4b = [[0.6,0.4,0.2],[0,0.4,3.5]]
c4b = BEZIER(S1)(p4b)
l4b = MAP(c4b)(Dom1D)

p4_back = [[0.65,-0.4,0.2],[0.05,-0.3,3.5]]
c4_back = BEZIER(S1)(p4_back)
l4_back = MAP(c4_back)(Dom1D)

p4b_back = [[0.65,0.4,0.2],[0.05,0.4,3.5]]
c4b_back = BEZIER(S1)(p4b_back)
l4b_back = MAP(c4b_back)(Dom1D)

s11 = BEZIER(S2)([c4,c4b])
surf11 = MAP(s11)(Dom2D)

s12 = BEZIER(S2)([c4_back,c4b_back]) 
surf12 = MAP(s12)(Dom2D_inv)

s13 = BEZIER(S2)([c4,c4_back])
surf13 = MAP(s13)(Dom2D_inv)

s14 = BEZIER(S2)([c4b,c4b_back])
surf14 = MAP(s14)(Dom2D)

steeringwheel_part2 = STRUCT([surf11,surf12,surf13,surf14])

steeringwheel = R([2,3])(-3*PI/2)(R([1,3])(PI)(STRUCT([S([1,2,3])([3,4,4.1])(STRUCT([steeringwheel_part1,R([1,3])(PI)(steeringwheel_part1)])),steeringwheel_part2,R([2,3])((2*PI)/3)(steeringwheel_part2),R([2,3])((4*PI)/3)(steeringwheel_part2)])))


model = STRUCT([prof,wheel1,wheel2,wheel3,wheel4,R([1,2])(0.2)(T([1,2])([0.5,0.9])(S([1,2,3])([0.15,0.15,0.15])(steeringwheel)))])

VIEW(model)