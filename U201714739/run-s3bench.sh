###
 # @Author: Xiuxu Jin(jyxk)
 # @Date: 2020-05-26 21:25:05
 # @LastEditors: Xiuxu Jin
 # @LastEditTime: 2020-05-26 22:48:38
 # @Description: file content
 # @Email: jyxking007@gmail.com
### 
###
 # @Author: Xiuxu Jin(jyxk)
 # @Date: 2020-05-26 21:25:05
 # @LastEditors: Xiuxu Jin
 # @LastEditTime: 2020-05-26 21:25:06
 # @Description: file content
 # @Email: jyxking007@gmail.com
### 
#!/bin/sh

# Locate s3bench

s3bench=~/go/bin/s3bench

if [ -n "$GOPATH" ]; then
    s3bench=$GOPATH/bin/s3bench
fi

# -accessKey        Access Key
# -accessSecret     Secret Key
# -bucket=loadgen   Bucket for holding all test objects.
# -endpoint=http://127.0.0.1:9000 Endpoint URL of object storage service being tested.
# -numClients=8     Simulate 8 clients running concurrently.
# -numSamples=256   Test with 256 objects.
# -objectNamePrefix=loadgen Name prefix of test objects.
# -objectSize=1024          Size of test objects.
for i in {1..32..2} 
do 
    for j in {32..1024..32}
    do
        $s3bench \
            -accessKey=hust \
            -accessSecret=hust_obs \
            -bucket=loadgen \
            -endpoint=http://127.0.0.1:9000 \
            -numClients=8 \
            -numSamples=256 \
            -objectNamePrefix=loadgen \
            -objectSize=$(( 1024*32 ))
    done
done

# build your own test script with designated '-numClients', '-numSamples' and '-objectSize'
# 1. Use loop structure to generate test batch (E.g.: to re-evaluate multiple s3 servers under the same configuration, or to gather data from a range of parameters);
# 2. Use redirection (the '>' operator) for storing program output to text files;
# 3. Observe and analyse the underlying relation between configuration parameters and performance metrics.