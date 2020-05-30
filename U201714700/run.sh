endpoint="http://127.0.0.1:9000"
bucket="loadgen"
ObjectNamePrefix="loadgen"
AccessKey="hust"
AccessSecret="hust_obs"
filename="minio.txt

declare  -a  NumClient
declare  -a  NumSample
declare  -a  ObjectSize

NumClient=(1    1    1    1     1     1     1      1      1       1        1        1    2    4    8    16   32   64    70   80    90  100  2        4      8     16     32      64     1     1    1   1   1    1    1    1    1  )
NumSample=(100  100  100  100   100   100   100    100    100     100      100      100  100  100  100  100  100  100   100  100  100  100  100     100    100    100    100    100     5    10   20  40  80  160  320  640  1280  )
ObjectSize=(1024 2048 4096 10240 20480 40960 102400 204800 409600 1048576  4194304 4096 4096 4096 4096 4096 4096 4096 4096 4096 4096 4096  102400 102400 102400 102400 102400 102400   4096  4096 4096 4096 4096 4096 4096 4096 4096 )


for(( i=0;i<${#NumClient[@]};i++)) 
do  
    # 命令
    ./s3bench -accessKey=$AccessKey -accessSecret=$AccessSecret -bucket=$bucket -endpoint=$endpoint \ >> $filename
    -numClients=${NumClient[i]} -numSamples=${NumSample[i]} -objectNamePrefix=$ObjectNamePrefix -objectSize=${ObjectSize[i]} | awk '($3=="99th" || $1=="Total" || $1=="Results" || $1 =="Number"){ print}'  >> $filename
    echo "---------------------------------------------------------------------------------------------done"
done
