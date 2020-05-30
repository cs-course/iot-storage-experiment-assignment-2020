###
 # @Author: Xiuxu Jin(jyxk)
 # @Date: 2020-05-26 20:08:39
 # @LastEditors: Xiuxu Jin
 # @LastEditTime: 2020-05-26 20:31:30
 # @Description: file content
 # @Email: jyxking007@gmail.com
### 
###
 # @Author: Xiuxu Jin(jyxk)
 # @Date: 2020-05-26 20:08:39
 # @LastEditors: Xiuxu Jin
 # @LastEditTime: 2020-05-26 20:08:39
 # @Description: file content
 # @Email: jyxking007@gmail.com
### 
#!/bin/bash
# Get script location
called=$_
if [[ $called == $0 ]]; then
    SCRIPT_PATH="$0"
else
    SCRIPT_PATH="${BASH_SOURCE[0]}"
fi
SCRIPT_DIR=$( cd "$(dirname $SCRIPT_PATH )" && pwd )

# Get OSM location (GOPATH default to ~/go)
osm=/usr/local/bin/osm
echo $SCRIPT_DIR
# Setting up OSM with local configuration file "osm.conf"
$osm --osmconfig $SCRIPT_DIR/osm.conf \
    config set-context osm-minio \
        --provider=s3 \
        --s3.access_key_id=hust \
        --s3.secret_key=hust_obs \
        --s3.endpoint=http://127.0.0.1:9000

# Check this configuration
$osm --osmconfig $SCRIPT_DIR/osm.conf \
    config view

# Prepare alias for simplified command line
alias osm="osm --osmconfig $SCRIPT_DIR/osm.conf"