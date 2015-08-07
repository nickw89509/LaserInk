outputlevel.py is a quick little script that takes the output from Object Works and alters the S command given different max. I take no responsibility in any damaged caused by running this script. 

#Example
```
G1X0.5 S6
G1X1 S7
G1X1.5 S7
G1X2 S7
G1X2.5 S7
```
would become 
```
G1X0.5 S282
G1X1 S329
G1X1.5 S329
G1X2 S329
G1X2.5 S329
```
given 12,000 maximum setting instead of the 255 Object Works sets as max.