import re

#Max S setting, think carbide is 12,000 really not sure
max = 12000

#Place file path here
infile = 'C:\Users\user\Documents\WinDoge.nc'

#output placed in same directory with .out
outfile = infile + '.out'
with open(infile, 'r') as f:
    lines = f.readlines()

of = open(outfile, 'w')
for line in lines:
	regex = re.compile('(S\d?\d?\d)')	
	if regex.search(line) is not None:		
		s = regex.search(line).group(1)
		m = (int(s[1:]) * max) / 255
		line = regex.sub('S' + str(m), line, m)
		of.write(line)	
	else:
		of.write(line)
