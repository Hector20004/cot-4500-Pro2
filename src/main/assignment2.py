from math import pow
import numpy as np

def multiplyPolinomials(a,b):
    prod = [0 for i in range(len(a) + len(b) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            prod[i + j] += a[i] * b[j]
    for x in reversed(prod):
        if x == 0.0:
            prod.pop()
    return prod
def addPolynomials(a,b):
    s = [0 for i in range(max(len(a),len(b)))]
    for i in range(len(a)):
        s[i] += a[i]
    for i in range(len(b)):
        s[i] += b[i]
    return s
def scalePolynomial(a,k):
    b = [0 for i in range(len(a))]
    for i in range(len(a)):
        b[i] = a[i] * k
    return b
def evaluatePolynomialOnX(p,x):
    res = 0.0
    for i in range(len(p)):
        res += pow(x,i) * p[i]
    return res
def computeNewVilleEntrie(x1,x2,Px1,Px2):
    div = x2 - x1
    leftPol = multiplyPolinomials([-x1,1],Px2)
    rightPol = multiplyPolinomials([-x2,1],Px1)
    substractPol = addPolynomials(leftPol,scalePolynomial(rightPol,-1))
    resultPol = scalePolynomial(substractPol, 1 / div)

    return resultPol
def NewvilleMethod(points):
    newvilleTable = [[]]

    for x,fx in points:
        newvilleTable[0].append([fx])
    i = 0
    while len(newvilleTable[i]) > 1:
        newvilleTable.append([])
        for j in range(len(newvilleTable[i]) - 1):
            newvilleTable[i + 1].append(computeNewVilleEntrie(points[j][0],points[j + i + 1][0],
                                    newvilleTable[i][j],newvilleTable[i][j+1]))
        #print(newvilleTable[i+1])
        i += 1
    return newvilleTable[i][0]

def NewtonsForward(points):
    n = len(points)
    newtonsTable = np.zeros((n+1,n))
    for ind,p in enumerate(points):
        x,fx = p
        newtonsTable[0][ind] = x
        newtonsTable[1][ind] = fx   
    for i in range(2,n+1):
        for j in range(i-1,n):
            newtonsTable[i][j] = ((newtonsTable[i-1][j] - newtonsTable[i-1][j-1]) / (newtonsTable[0][j] - newtonsTable[0][j-i+1]))
    
    
    pol = [0 for i in range(len(points) - 1)]
    pol[0] += newtonsTable[1][0]
    multpol = [1]
    for i  in range(len(points) - 1):
        multpol = multiplyPolinomials(multpol,[-points[i][0],1])
        pol = addPolynomials(pol,scalePolynomial(multpol,newtonsTable[i+2][i+1]))
        #print(pol)
        #print(evaluatePolynomialOnX(pol,7.3))

    return newtonsTable,pol

def hermiteInterpolation(points):
    np.set_printoptions(linewidth=np.inf)
    hermiteTable = np.zeros((len(points) * 2 - 1,len(points) * 2))
    for ind,p in enumerate(points):
        x,fx,ffx = p
        hermiteTable[0][ind * 2] = x
        hermiteTable[0][ind* 2 + 1] = x
        hermiteTable[1][ind*2] = fx
        hermiteTable[1][ind*2 + 1] = fx
    for i in range(2,len(hermiteTable)):
        for j in range(i-1,len(hermiteTable[i])):
            if i == 2 and j % 2 == 1:
                hermiteTable[i][j] = points[j // 2][2]
                continue
            hermiteTable[i][j] = (hermiteTable[i-1][j] - hermiteTable[i-1][j-1]) / (hermiteTable[0][j] - hermiteTable[0][j - i + 1])
    hermiteTable = np.transpose(hermiteTable)
    return hermiteTable
def cubicSplineInterpolation(points):
    hs = []
    n = len(points)
    for i in range(1,n):
        hs.append(points[i][0] - points[i-1][0])
    A = np.zeros((n,n))
    A[0][0] = 1
    A[-1][-1] = 1
    for i in range(1,n-1):
        A[i][i-1] = hs[i-1]
        A[i][i] = 2 * (hs[i-1] + hs[i])
        A[i][i+1] = hs[i]

    b = np.zeros(n)

    for i in range(1,n-1):
        b[i] = 3 * ((points[i+1][1] - points[i][1]) / hs[i] - (points[i][1] - points[i-1][1]) / hs[i-1])

    x = np.linalg.solve(A,b)
    a = np.round(A,decimals=8)
    b = np.round(b,decimals=8)
    x = np.round(x,decimals=8)
    return A,b,x