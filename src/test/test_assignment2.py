from main.assignment2 import NewvilleMethod,evaluatePolynomialOnX,NewtonsForward,cubicSplineInterpolation,hermiteInterpolation

def testAllExercises():
    #testNewvilleMethod()
    #testNewtonsForward()
    #testCubineSplineInterpolation()
    testHermiteInterpolation()
def testNewvilleMethod():
    points = [(3.6,1.675),(3.8,1.436),(3.9,1.318)]
    lagrangePolynomial = NewvilleMethod(points)


    #print(lagrangePolynomial)
    print(evaluatePolynomialOnX(lagrangePolynomial, 3.7))
    print()
def testNewtonsForward():
    points = [(7.2,23.549),(7.4,25.3913),(7.5,26.8224),(7.6,27.4589)]
    newtonsTable = NewtonsForward(points)
    print(newtonsTable)

def testHermiteInterpolation():
    points = [(3.6,1.675,-1.195),(3.8,1.436,-1.188),(3.9,1.318,-1.182)]
    hermiteTable = hermiteInterpolation(points)
    print(hermiteTable)
def testCubineSplineInterpolation():
    points = [(2,3),(5,5),(8,7),(10,9)]
    A,b,x = cubicSplineInterpolation(points)

    
    print(A)
    print(b.tolist())
    print(x.tolist())
