#!/usr/bin/python

import sys
import mymodule

class parentClass:
	var1 = "i am var1"
	var2 = "i am var2"

class childClass(parentClass):
	#pass
	var2 = "i am not var2"

parentObject = parentClass()
print parentObject.var1
print parentObject.var2

childObject = childClass()
print childObject.var1
print childObject.var2

class mom:
	var1 = "hey i am mom"

class dad:
	var2 = "hey son i am dad"

class child(mom,dad):
	var3 = "i am the child"

childobj = child()
print childobj.var1
print childobj.var2
print childobj.var3

#print mymodule.testit()
