#/bin/bash 

#Market
protoc -I=../Market --python_out=../Market ../Market/commodities.proto 
protoc -I=. --python_out=. move.proto

#Mapping
protoc -I=../Mapping --python_out=../Mapping ../Mapping/map.proto
protoc -I=../Mapping --python_out=../Mapping ../Mapping/region.proto