import matplotlib.pyplot as plt
import sys
import csv
import os


if __name__ == "__main__":
	plty = []
	pltx = []
	bucket = sys.argv[1]
	numClients = int(sys.argv[2])
	filenum = int(sys.argv[3])
	filesize = int(sys.argv[4])
	xserial_s = int(sys.argv[5])
	yserial_s = int(sys.argv[6])
	file_csv = open('data.csv','w')
	file_csv.close()
	datapath = "data.csv"
	os.remove(datapath)
	cmond_s = "python3 froot.py "+ bucket + " "
	if xserial_s!=0 and xserial_s!=2:
		print('argvError-5')
		exit()
	else:
		xserial = xserial_s
		
	if yserial_s!=1 and yserial_s!=3:
		print('argvError-6')
		exit()
	else :
		yserial = yserial_s

	if xserial==0:
		for i in range(filesize):
			print('size:',8*(i+1),'MB')
			cmond = cmond_s + sys.argv[2]+ " " + sys.argv[3] + " " + str((i+1)*1024*8000)
			os.system(cmond)
	else:
		for j in range(numClients):
			print('clients:',j+1)
			cmond = cmond_s + str(j+1) + " " + sys.argv[3] + " " + sys.argv[4]
			os.system(cmond)

	file_csv = open('data.csv')
	reader = csv.reader(file_csv)
	orig = list(reader)

	for row in orig:
		pltx.append(float(row[xserial]))
		plty.append(float(row[yserial]))
	plt.xticks(fontsize=5)
	plt.yticks(fontsize=6)
	if xserial==0:
		plt.xlabel('size / MB', fontsize=8)
	else:
		plt.xlabel('numClients',fontsize=8)
	if yserial==1:
		plt.ylabel('speed / MB/s', fontsize=8)
	else:
		plt.ylabel('duration 99th%ile / s',fontsize=8)
	plt.plot(pltx,plty,linestyle='-')
	#plty.sort(reverse=True)
	#if yserial_s='v':
	#	plt.axis([0,filesize+1,0,int(plty[0]+1)])
	plt.show()


