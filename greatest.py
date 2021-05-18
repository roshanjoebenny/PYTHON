  
x=int(input('Give the first no :'))
y=int(input('Give the second no :')) 
z=int(input('Give the third no :'))
if(x>y):
   if(x>z):
     print('{0} is the greatest among {1},{2},{3}.'.format(x,x,y,z))
   else:
     print('{0} is the greatest among {1},{2},{3}.'.format(z,x,y,z))
else:
   if(y>z):
      print('{0} is the greatest among {1},{2},{3}.'.format(y,x,y,z))
   else:
      print('{0} is the greatest among {1},{2},{3}.'.format(z,x,y,z))
