#essentials
def gradient(x1,x2,y1,y2,perp):
    numerator = y2-y1
    denominator = x2-x1
    if numerator != 0 and denominator != 0:
        if perp == False:
            return numerator/denominator
        else:
            return (denominator/numerator)*-1
    else:
        return 0

def discriminant(equationNums):
    return (equationNums[1]*equationNums[1]) - (4*equationNums[0]*equationNums[2])

def quadraticFormula(equationNums):
    x1 = ((equationNums[1]*-1)+(discriminant(equationNums)**(1/2)))/(2*equationNums[0])
    x2 = ((equationNums[1]*-1)-(discriminant(equationNums)**(1/2)))/(2*equationNums[0])
    return [x1,x2]

def polynomialRoots(values,root):
    #having trouble with implementing berkleys algorithm so have to use synthetic div ):
    roots = [root]
    newEquation = []
    remainder = 0
    for i in range(1,len(equation)):
        newEquation.append((newEquation[i]-1*roots[0])+equation[i])
    remainder = newEquation[len(newEquation)-1]
    newEquation.pop(len(newEquation)-1)
    if lastVal != 0:
        return [0]
    else:
        roots.extend(quadraticFormula(newEquation))
        return roots
    
#straight line
def medianOfTriangle(points):
    #points - three points of triangle
    midPoints = []
    medianPoints = []
    midpoint = []
    finalVals = []
    for i in range(0,3):
        medianPoints.append(points[i])
        if i > 0:
            del medianPoints[0]
            del midPoints[0]
            del midPoints[0]
        for x in range(0,3):
            if x != i:
                midPoints.append(points[x])
        midpoint = [(midPoints[0][0] + midPoints[1][0])/2,(midPoints[0][1] + midPoints[1][1])/2]
        currentGradient = gradient(midpoint[0],medianPoints[0][0],midpoint[1],medianPoints[0][1],False)
        c = medianPoints[0][1] + (medianPoints[0][0]*-1)*currentGradient
        finalVals.append([currentGradient,c])
        del midpoint[0]
        del midpoint[0]
    return finalVals

def altitudeOfTriangle(points):
    #points - three points of triangle
    altitudesPoints = []
    oppositePoints = []
    finalVals = []
    
    for i in range(0,3):
        altitudesPoints.append(points[i])
        if i > 0:
            del altitudesPoints[0]
        for x in range(0,3):
            if x != i:
                oppositePoints.append(points[x])
        pointer = i + 1
        if i == 2:
            pointer = 0
        currentGradient = gradient(oppositePoints[i][0],oppositePoints[pointer][0],oppositePoints[i][1],oppositePoints[pointer][1],True)
        c = altitudesPoints[0][1] + (altitudesPoints[0][0]*-1)*currentGradient
        finalVals.append([currentGradient,c])
    return finalVals

def perpendicularBisector(points):
    midpoint = []
    currentGradient = gradient(points[0][0],points[1][0],points[0][1],points[1][1],True)
    midpoint = [(points[0][0]+points[1][0])/2,(points[0][1]+points[1][1])/2]
    c = midpoint[1] + (midpoint[0]*-1)*currentGradient
    return [currentGradient,c]
#quadratic stuff
def completingTheSquare(values):
    newValues = []
    for i in values:
        newValues.append(i/values[0])
    turningPoint = [newValues[1]/2,newValues[1]**2+newValues[2]]
    return turningPoint

def quadraticInequality(values,aboveORbelow):
    roots = quadraticFormula(values)
    roots.sort()
    if aboveORbelow == True :
        if values[0] > 0 :
            return ["min","x<"+str(roots[0])+",x>"+str(roots[1])]
        else:
            return ["min",str(roots[0])+"<x<"+str(roots[1])]
    else:
        if values[0] > 0:
            return ["max",str(roots[0])+"<x<"+str(roots[1])]
        else:
            return ["max","x<"+str(roots[0])+",x>"+str(roots[1])]

        
            










