#!/usr/bin/python

import re, sys

l = [(1,"juca"),(22,"james"),(53,"xuxa"),(44,"delicia")]

result = next((i for i, v in enumerate(l) if v[0] >= 22), None)
# 2
print result

sys.exit(0)

a = [1,2,3]
b = [4,5,6] 
l = zip(a,b)
print l
m = map(lambda x: x[0]*x[1], l)
print m
r = reduce(lambda x,y: x + y, m)
print r
sys.exit(0)

l = [1, 2, 3, 4, 5, 6]
o = [(l[i],l[i+1]) for i in range(0,len(l),2)]
print o
sys.exit(0)

libs = ['libIce.so.33', 'libIce.so.3.3.1', 'libIce.so.32', 'libIce.so.3.2.0']  

#libs = ['    </td>\n', '<td><blockquote>For each year, libIce.so.33 we show the rank for Jordan and a bar representing the popular ity of that name. \n', '\tThe longer the bar, t he more popular the name. The more popular the name in  \n', '   a given year, the numerically lower the rank, with ra nk 1 being the most popular.\n', '</blockquote >\n', '<p><table width="96%" class="layout">\n', '   <tr><th width=8%>Year</th><th width=8%>Rank</th><th colspan=2>Popu larity of male name Jordan</th></tr></table>\ n', '<table width=96% class=layout><tr libIce.so.3.3.1 valign="bottom">\n', '\t<td class="nobarborder" width="8%" align="center">2014</t d>\n', '\t<td class="nobarborder" width="8%" align="center">55</td>\n', '  <td class=bluebar width=79.464%>&nbsp;</td>\n', '  <td width=4.536%></td></tr></table>\n', '<table width=96% class=layout><tr valign=" bottom">\n', '\t<td class="nobarborder" width="8%" align="center">2013</td>\n', '\t<td class="nobarborder" width="8%" ali gn="center">53</td>\n', '  <td class=blueba r width=79.632%>&nbsp;</td>\n', '  <td width=4.36799 libIce.so.32 999999999%></td></tr></table>\n', '<table width=96% class=layout><tr v align="bottom">\n', '\t<td class="nobarbor der" width="8%" align="center">2012</td>\n', '\t<td class="nobarborder" width="8%" align="center">48</td>\n', '  <td class= bluebar width=80.052%>&nbsp;</td>\n', ' <td width=3.94799999999999%></td></tr></table>\n', '<table width=96% class=layout><tr valign="bottom">\n', '\t<td class="nob arborder" width="8%" align="center">2011 </td>\n', '\t<td class="nobarborder" width="8%" align="center">46</td>\n', '  <td class=bluebar width=80.22%>&nbsp;</td>\n', '  <td width=3.78%></td></tr></table>\n' , '<table width=96% class=layout><tr valign="bottom">\n', '\t<td class="nobarborder" width="8%" align="center">2010</td>\n', '\t<td class="nobarborder" width="8%" al ign="center">46</td>\n', '  <td class=bluebar width=80.22%>&nbsp;</td>\n', '  <td width=3.78%></td></tr></table>\n', '<table width=96% class=layout><tr valign="botto m">\n', '\t<td class="nobarb libIce.so.3.2.0 order" width="8%" align="center">2009</td>\n', '\t<td class="nobarborder" width="8%" align="cente r">45</td>\n', '  <td class=bluebar wid th=80.304%>&nbsp;</td>\n', '  <td width=3.696%></td></tr></table>\n', '<table width=96% class=layout><tr valign="bottom">\n', '\t<td class="nobarborder" width="8%" a lign="center">2008</td>\n', '\t<td class="nobarborder" width="8%" align="center">48</td>\n', '  <td class=bluebar width=80.052 %>&nbsp;</td>\n', '  <td width=3.94799 999999999%></td></tr></table>\n', '<table width=96% class=layout><tr valign="bottom">\n', '\t<td class="nobarborder" width="8%" align="center">2007</td>\n', '\t<td c lass="nobarborder" width="8%" align="center">45</td>\n', '  <td class=bluebar width=80.304%>&nbsp;</td>\n', '  <td width=3.696% ></td></tr></table>\n', '<table width =96% class=layout><tr valign="bottom">\n', '\t<td class="nobarborder" width="8%" align="center">2006</td>\n', '\t<td class="noba rborder" width="8%" align="center">4 6</td>\n', '  <td class=bluebar width=80.22%>&nbsp;</td>\n', '  <td width=3.78%></td></tr></table>\n', '<table width=96% class=la yout><tr valign="bottom">\n', '\t<t d class="nobarborder" width="8%" align="center">2005</td>\n', '\t<td class="nobarborder" width="8%" align="center">46</td>\n', ' <td class=bluebar width=80.22%>&nbsp ;</td>\n', '  <td width=3.78%></td></tr></table>\n', '<table width=96% class=layout><tr valign="bottom">\n', '\t<td class="nobarb order" width="8%" align="center">20 04</td>\n', '\t<td class="nobarborder" width="8%" align="center">43</td>\n', '  <td class=bluebar width=80.472%>&nbsp;</td>\n', ' <td width=3.52799999999999%></td></ tr></table>\n']

versions = []  

regex = re.compile('.*libIce.so\.([0-9]+\.[0-9]+\.[0-9]+).*')  
#regex = re.compile('(align)')

# print(regex)
# print out:
# <_sre.SRE_Pattern object at 0x8d6c3c8>

def match(s):  
    m = regex.match(s)  
    print m
    if m:  
        return m.group(1)  

versions = [x for x in map(match,libs) if x]

print versions
sys.exit(0)

# this prints out
# ['3.3.1', '3.2.0']


#################

xs = [1, 2, 3]

# all of those are equivalent - the output is [2, 4, 6]
# 1. map
ys = map(lambda x: x * 2, xs)
print(ys)

# 2. list comprehension
ys = [x * 2 for x in xs]
print(ys)

# 3. explicit loop
ys = []
for x in xs:
    ys.append(x * 2)

#################

xs = [1, 2, 3]
ys = [2, 4, 6]

def f(x, y):
    return (x * 2, y // 2)

# output: [(2, 1), (4, 2), (6, 3)]
# 1. map
zs = map(f, xs, ys)
print zs

# 2. or to use list comp for the same result
zs = [f(x, y) for x, y in zip(xs, ys)]
print zs

# to unzip
xs2, ys2 = zip(*zs)
print list(xs2)
print list(ys2)

# 3. explicit loop
zs = []
for x, y in zip(xs, ys):
    zs.append(f(x, y))

def f2(x, y):
    return (x, y)

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print zipped
x2, y2 = zip(*zipped)
print(x == list(x2))
print(y == list(y2))
zs2 = [f2(x,y) for x,y in zip(x2,y2)]
print zs2
