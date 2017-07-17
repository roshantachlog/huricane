h1=input("enter the hour1")
m1=input("Enter the minut1")
h2=input("enter the hour2")
m2=input("enter the minut2")
if h2>=h1:
	difhr=h2-h1
	print "difrentce" ,difhr
elif h1>h2:
	difhr=24-h1 + h2
	print difhr
	
if m2>=m1:
	difmt=m2-m1
	print "diff mnt",difmt
elif m1>m2:
	difmt=60-m1+m2
	print "difmt", difmt		
 