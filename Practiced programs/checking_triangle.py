def triangle(a,b,c): 
  if(a+b>c and a+c>b and b+c>a): 
    print("Triangle can be formed with",a,b,c,"as sides.") 
  else: 
    print("Triangle can not be formed with",a,b,c,"as sides") 
 
a = int(input ("Enter 1st side:")) 
b = int(input ("Enter 2nd side:")) 
c = int(input ("Enter 3rd side:")) 
 
triangle(a,b,c)
