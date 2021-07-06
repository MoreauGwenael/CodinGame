#!perl -p
s/(.)([+-]\d+)/chr$2+ord$1/ge