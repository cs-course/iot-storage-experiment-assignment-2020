import sys
import threading
import time
import boto3
import csv

def genFile(filename,fileSize):
	#file path
	filePath=filename+"test.txt"
	# 生成固定大小的文件
	# date size
	file_p = open(filePath,'w')
	file_p.write('\x00'*filesize)
	file_p.close()

class myThread(threading.Thread):
	def __init__(self, bucket,tasks,data,start_num):
		threading.Thread.__init__(self)
		self.bucket = bucket
		self.tasks = tasks
		self.data = data
		self.start_num = start_num
		self.time_r = []
		self.y = []
	def run(self):
		s3 = boto3.resource('s3',endpoint_url="http://127.0.0.1:9000")
		time_r_s = time.time()
		for i in range(self.tasks):
			key ="test" + str(self.start_num+1+i) + ".txt"
			t_start = time.time()
			s3.Bucket('chen1').put_object(Key=key,Body=self.data)
			self.y.append(int(time.time()*1000 - t_start*1000))
		self.time_r.append(time.time()-time_r_s)

if __name__ == "__main__":
	threads = []
	time_r = []
	plty = []
	bucket = sys.argv[1]
	numClients = int(sys.argv[2])
	filenum = int(sys.argv[3])
	filesize = int(sys.argv[4])
	
	genFile('',filesize)
	data = open('test.txt','rb').read()
	s3 = boto3.resource('s3',endpoint_url="http://127.0.0.1:9000")
	s3.Bucket('chen1').put_object(Key='txt.txt',Body=data)

	i = 0
	# time_start = time.time()
	numtask = int(filenum/numClients)
	m = filenum % numClients
	# start clients
	while i < numClients:
		tasks = numtask
		if i < m:
			tasks = tasks + 1
			start_num = i*tasks
		else:
			start_num = i*tasks + m
		thread_my = myThread(bucket,tasks,data,start_num)
		thread_my.start()
		threads.append(thread_my)
		i = i+1
	for t in threads:
		t.join()
	# get result
	for t in threads:
		plty = plty + t.y
		time_r = time_r + t.time_r
	time_r.sort()
	plty.sort(reverse=True)
	# total throughput
	through = float(format(filesize*filenum/1000/1000/time_r[numClients-1],'.2f'))
	print(through)
	# total duration 99th%
	duration = float(format(plty[int(filenum*1/100)+1]/1000,'.3f'))
	print(duration)
	row = [filesize/1000/1000,through,numClients,duration]
	file_csv = open('data.csv','a',newline="")
	content = csv.writer(file_csv)
	content.writerow(row)
	file_csv.close()

