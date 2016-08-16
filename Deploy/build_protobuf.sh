#/bin/bash 

#Base
protoc -I=.. --python_out=.. ../message.proto

#Market
protoc -I=../Market --python_out=../Market --proto_path=.. ../Market/commodities.proto 
protoc -I=../Market --python_out=../Market --proto_path=.. ../Market/trade.proto

#Mapping
protoc -I=../Mapping --python_out=../Mapping --proto_path=.. ../Mapping/map.proto
protoc -I=../Mapping --python_out=../Mapping --proto_path=.. ../Mapping/region.proto