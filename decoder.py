house = ["_eval", "_exec", "_byte", "_bytes", "_bit", "_bits", "_system", "_encode", "_decode", "_delete", "_exit", "_print", "_input"]
baguette = input("ENTER THE TEXT, OR FACE GIGN: ")
grenade = "print"
for door in house:
  baguette.replace(door, grenade)
print(baguette)
print("Crypter has been defused!, Counter Terrorists win!")

'''
if for some reason it fails to defuse, replace the decode function keyword with a print statement

'''

'''
def __decode__(self,_execute: str)->exec:return(None,self._system(self._bytes(_execute)))[0]
                                                     ^^^^^^^^^^^^ REPLACE THIS WITH "print"
def __decode__(self,_execute: str)->exec:return(None,self._exec(self._bytes(_execute)))[0]
                                                     ^^^^^^^^^^ replace with the print statement
'''
