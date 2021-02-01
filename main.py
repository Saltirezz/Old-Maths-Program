
ty = "Minimum"
a = 1
b = 1
c = -6
stringarray = []
array = []
numbers = [2,5,-23,10]

#1ST UNIT###################################################################

#Gradient-------------------------------------------------------------------
def gradient(x1,x2,y1,y2,perp):
  
    if x2 - x1 != 0 and y2 - y1 != 0:
      if perp == False:
        return (y2-y1)/(x2-x1)
      else:
        return(x2-x1)/(y2-y1)*-1
    else:
      return 0

#Medians--------------------------------------------------------------------
def medians(letters, points):
  #letters = ["P","Q","R"]
  #points = [[2,8],[5,8],[4,-2]]
  curpoints = []
  expoint = []
  midpoint = []
  for i in range(0,len(points)):
    expoint.append(points[i])
    if i > 0:
      del expoint[0]
      del curpoints[0]
      del curpoints[0]
    for x in range(0,len(points)):
      if x != i:
        curpoints.append(points[x])
    midpoint.append((curpoints[0][0] + curpoints[1][0])/2)
    midpoint.append((curpoints[0][1] + curpoints[1][1])/2)
    m = gradient(midpoint[0],expoint[0][0],midpoint[1],expoint[0][1],False)
    a = expoint[0][1] + (expoint[0][0]*-1)*m  
    e1 = i
    e2 = i + 1
    if i == 2:
      e2 = 0
    if a > 0:
      a = "+"+str(a)
    del midpoint[0]
    del midpoint[0]
    print("From "+letters[i]+": y="+str(m)+"x"+str(a))
#Altitudes------------------------------------------------------------------
def altitudes(letters,points):

  #0 - A
  #1 - B
  #2 - C
  #[x][0] = x
  #[x][1] = y

  expoint = []
  curpoints = []
  for i in range(0,len(points)):
    expoint.append(points[i])
    if i > 0:
      del expoint[0]
    for x in range(0,len(points)):
      if x != i:
        curpoints.append(points[x])
    e1 = i
    e2 = i + 1
    if i == 2:
      e2 = 0
    m = gradient(curpoints[e1][0],curpoints[e2][0],curpoints[e1][1],curpoints[e2][1],True)
    a = expoint[0][1] + (expoint[0][0]*-1)*m
    if a > 0:
      a = "+"+str(a)
    print("From "+letters[i]+": y="+str(m)+"x"+str(a))
#Perpendicular Bisectors---------------------------------------------------
def perpbisectors(points):
  #points = [[6,-4],[-2,-2]]
  midpoint = []
  m = gradient(points[0][0],points[1][0],points[0][1],points[1][1],True)
  midpoint.append((points[0][0] + points[1][0])/2)
  midpoint.append((points[0][1] + points[1][1])/2)
  a = midpoint[1] + (midpoint[0]*-1)*m
  if a > 0:
      a = "+"+str(a)
  return("PERPENDICULAR BISECTORS || y="+str(m)+"x"+str(a)+" ||")

#2CND UNIT##################################################################

#Completing The Square in a(x+/-a) +/- b------------------------------------
def comsquare(a,b,c):
  array = [a,b,c]
  #0 = a
  #1 = b
  #2 = c
  #(x - K) - L +/- P

  #check if any dont perfectly divide by a
  for i in range(1,len(array)):
      array[i] = array[i] / 4
  print(array)
  k = array[1] / 2
  l = (k*k) * -1
  p = array[2]
  if type(l) == float:
      l = l*array[0]
  l = l + p*array[0]
  if k > 0:
      k = str(k) + "+"
  else:
      k = str(k)
  if l > 0:
      l = str(l) + "+"
  else:
      l = str(l)
  print(str(array[0])+"(x "+k+")^2 "+l)
#Synthetic Division---------------------------------------------------------
def syntheticdiv(numbers,y):
  #use root -> if its (x+3) then y = -3 and if its (x-3) then y = 3
  randomarray = [numbers[0]]
  roots = []
  remainder = numbers[0]

  for i in range(1,len(numbers)):
    remainder = (remainder*y)+numbers[i]
    randomarray.append(remainder)
  root1, root2 = factorising(randomarray[0],randomarray[1],randomarray[2])
  
  return "SYNTHETIC DIVISON || Remainder: "+str(remainder)+ " // Roots: "+str(root1)+","+str(root2)+","+str(y)+" ||"
#Factorising----------------------------------------------------------------
def factorising(a,b,c):
  #just gives out roots
  def print_factors(y1):
    z = False 
    if y1 < 0:
      y1 = y1 * -1
      z = True
    for i in range(1, y1 + 1):
      if y1 % i == 0 and z == False:
        array.append(i)
      elif y1 % i == 0 and z == True:
        array.append(-i)
    
    return array

  
  x1 = 0
  x2 = 0
  y1 = a*c #times to make this 
  y2 = b #add to make this
  dobreak = False
  m = print_factors(y1)
  for i in range(0,len(m)):
    x = m.pop(i)
    for l in range(0,len(m)):
      
      if m[l] * x == y1 and m[l]+x == y2:
        
        x1 = m[l]
        x2 = x
        dobreak = True
        break
      elif m[l] * (x*-1) == y1 and (m[l]*-1) + x == y2:
        x1 = m[l] * -1
        x2 = x 
        dobreak = True
        break
      elif  x * (m[l]*-1) == y1 and m[l] + (x*-1) == y2:
        x1 = m[l] 
        x2 = x * -1
        dobreak = True
        break
      elif  (x*-1) * (m[l]*-1) == y1 and (m[l]*-1) + (x*-1) == y2:
        x1 = m[l] * -1 
        x2 = x * -1
        dobreak = True
        break
    if dobreak == True:
      break
    m.insert(i,x)
  x1 = (x1*-1)/a
  x2 = (x2*-1)/a
  return x1, x2

def quadratics(a,b,c, ty):
  #completing the square---------------------
  multiplier = 1
  if b > 0:
    multiplier = -1  
  xx1 = (b/2)*-1
  xx2 = (((b/2)*(b/2))*multiplier) + c
  #-------------------------------------------
  x1, x2 = factorising(a,b,c)
  if a < 0:
    ty = "Maximum"
  
  #boring cringe text formatting to make non cringe strings----------------
  return "QUADRATICS || "+ty+" | // Roots | "+str(x1)+" and "+str(x2)+"| // Turning Point | ("+str(xx1)+","+str(xx2)+") | // Y-Intercept | "+str(c)+" ||"
#Quadratic Inequalities-----------------------------------------------------
def inequalities(aa,bb,cc):
  aa = 12
  bb = 69
  cc = 14
  roots = factorising(aa, bb, cc)
  roots.sort()
  print(roots)
  print("Is the statement A or B? || A - ax^2+bx+c > 0 || B - ax^2+bx+c < 0")
  statement = input("Answer: ")
  # smallestroot = roots[0]
  if statement == "A" or statement == "a":
    if(aa > 0):
      return("Minimum: x < " + str(roots[0]) + ", x > " + str(roots[1]))
    else:
      return(str(roots[0])+" < x < "+str(roots[1]) + "\n")
  elif statement == "B" or statement == "b":
    if(aa > 0):
      return(str(roots[0])+" < x < "+str(roots[1]) + "\n")
    else:
      return("Maximum: x < " + str(roots[0]) + ", x > " + str(roots[1])+"\n")
#---------------------------------------------------------------------------

#OUTPUT
#print(quadratics(a,b,c, ty))
#print(syntheticdiv(numbers, 2))
#print("ALTITUDES ||")
#print(altitudes(["B","C","D"],[[1,6],[7,3],[-5,-1]]))
numbers = [10,1,-8,6]
remainder = 3
y = -3
randomarray = []
print(medians(["A", "B", "C"], [[4,0],[-4,16],[18, 20]]))