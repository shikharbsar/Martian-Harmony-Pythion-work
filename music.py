import numpy as np
import cv2
def f(x):
	return {
		q[0]+2:'F1',
		q[0]+a1/2:'E1',
		q[1]+2:'D1',
		q[1]+a1/2:'C1',
		q[2]+2:'B1',
		q[2]+a1/2:'A1',
		q[3]+2:'G1',
		q[3]+a1/2:'G19',
		q[4]+2:'F1',
		q[4]+a1/2:'F61',
		q[5]+2:'E1',
		q[5]+a1/2:'D1',
		q[6]+2:'C36',
		q[6]+a1/2:'C233',
		q[7]+2:'A2',
		q[7]+a1/2:'G2',
		q[8]+2:'F2',
		q[8]+a1/2:'E2',
		q[9]+2:'D2',
		q[9]+a1/2:'D25',
		q[10]+2:'C2',
		296:'V1',
		q[10]+a1/2:'C21',
		292:'A!@',
		282:'B@!',
		278:'G4',
		309:'24',
		305:'p&'
	}[x]
read = cv2.imread('m812.jpg')
read = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
ret,binaryImage = cv2.threshold(read, 150, 255, cv2.THRESH_BINARY)
np.set_printoptions(threshold='nan')
print len(binaryImage[0])
q=[]
i=0
for x in xrange(0,len(binaryImage)):
	for y in xrange(0,2):
		for z in xrange(0,len(binaryImage[0])-3):
			if binaryImage[x][y+z]==0:
				c=0
			else: 
				c=1
				break
		if c==0 :
			q.insert(i,x)
			i+=1
			break
a1=q[1]-q[0]
#q.insert(i,q[0]-a1)
#q.insert(i,q[len(q)-1]+a1)
#i+=1
# for x in xrange(0,len(q)-1):
# 	if q[x+1]-q[x]>=2*a1:
# 		#q.insert(i,q[x]+a1)
# 		#i+=1
# 		q.insert(i,q[x+1]-a1)
# 		i+=1
print a1/2	
print q
print(binaryImage[256])
pt=[]
i=0
a2=q[0]+2
l=0
for x in xrange(0,len(binaryImage[0])):
	if binaryImage[a2][x]==0:
		y=x
		while binaryImage[a2][y]!=255:
			y+=1
		l=max(l,y-x)
#print binaryImage[q[1]+2]
print l
for x in xrange(0,len(q)):
	for t in xrange(0,len(binaryImage[0])-l):
		for y in xrange(0,l-2):
			if binaryImage[q[x]+2][t+y]==0:
				c=0
			else:
				c=1
				break
		if c==0:
			for y in xrange(0,l-8):
				if binaryImage[q[x]+2+2][t+y]==0:
					c=0
				else:
					c=1
					break		
		if binaryImage[q[x]+2][t+y+4]==0:
			c=1
		if c==0:
			pt.append([t,q[x]+2])
for x in xrange(0,len(q)):
	for t in xrange(0,len(binaryImage[0])-l):
		for y in xrange(0,l-2):
			if binaryImage[q[x]+a1/2][t+y]==0:
				c=0
			else:
				c=1
				break
		if c==0:
			for y in xrange(0,l-8):
				if binaryImage[q[x]+a1/2+2][t+y]==0:
					c=0
				else:
					c=1
					break
		if binaryImage[q[x]+a1/2][t+y+4]==0:
			c=1
		if c==0:
			pt.append([t,q[x]+a1/2])
for x in xrange(0,len(q)):
	for t in xrange(0,len(binaryImage[0])-14):
		if binaryImage[q[x]+a1/2+1][t]==0 and binaryImage[q[x]+a1/2+1][t+12]==0:
			if binaryImage[q[x]+a1/2+1][t+1]==0 and binaryImage[q[x]+a1/2+1][t+12-1]==0:	
				if binaryImage[q[x]+a1/2+1][t+3]==255 and binaryImage[q[x]+a1/2+1][t+12-3]==255 and binaryImage[q[x]+a1/2+1][t+4]==255 and binaryImage[q[x]+a1/2+1][t+12-4]==255 and binaryImage[q[x]+a1/2+1][t+5]==255 and binaryImage[q[x]+a1/2+1][t+12-5]==255:
					if binaryImage[q[x]+a1/2+1][t+6]==255:
						c=0
					else:
						c=1
				else:
					c=1
			else:
				c=1
		else:
			c=1
		if c==0:
			pt.append([t,q[x]+a1/2])
for x in xrange(0,len(q)):
	for t in xrange(0,len(binaryImage[0])-14):
		if binaryImage[q[x]+2][t]==0 and binaryImage[q[x]+2][t+12]==0:
			if binaryImage[q[x]+2][t+1]==0 and binaryImage[q[x]+2][t+12-1]==0:	
				if binaryImage[q[x]+2][t+3]==255 and binaryImage[q[x]+2][t+12-3]==255 and binaryImage[q[x]+2][t+4]==255 and binaryImage[q[x]+2][t+12-4]==255 and binaryImage[q[x]+2][t+5]==255 and binaryImage[q[x]+2][t+12-5]==255:
					if binaryImage[q[x]+2][t+6]==255:
						c=0
					else:
						c=1
				else:
					c=1
			else:
				c=1
		else:
			c=1
		if c==0:
			pt.append([t,q[x]+2])
pt = np.array(pt)
pt=pt[np.argsort(pt[:,0])]
nm=len(pt)
print pt
#print binaryImage[q[len(q)-1]+6]
fi=[]
for x in xrange(0,nm-1):
	if  (pt[x][0]+1==pt[x+1][0] and pt[x][1]==pt[x+1][1]) :
		continue
	else:
		fi.append([pt[x][0],f(pt[x][1])])
fi.append([pt[nm-1][0],f(pt[nm-1][1])])
nm=len(fi)
fin=[]
for x in range(0,nm):
	for y in range(x+1,nm):
		if fi[y][0]-fi[x][0]<=4 and fi[x][1]==fi[y][1]:
			c=1
			break
		else :
			c=0
	if c==0:
		fin.append([fi[x][0],fi[x][1]])
#print len(fi)
#print fi[2][0]
print fin
nm=len(fin)
for x in xrange(0,nm):
	for y in xrange(x+1,nm):
		if fin[x][1][1]==fin[y][1][1]:
			if(fin[y][0]-fin[x][0]<=80):
				fin[x][1]+=' 0.25'
			elif fin[y][0]-fin[x][0]>80 and fin[y][0]-fin[x][0]<=130:
				fin[x][1]+=' 0.5'
			elif fin[y][0]-fin[x][0]>130 and fin[y][0]-fin[x][0]<280:
				fin[x][1]+=' 1'
			break
#print binaryImage[66]
print fin

cv2.imshow('canvas',binaryImage)
cv2.waitKey(0)
