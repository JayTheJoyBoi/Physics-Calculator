# Note: If using command line version, comment out line 2 and uncomment line 3
from gui import *
#from cli import *
# Most code goes here, How to actually interpret data
async def test(menu,args):
    menu.print(args["Print Value: "])
    a = await menu.input("A: ")
# LEAVE THIS AT THE END
main({"test":{"funct":test,'args':{"Print Value: ":'entry'}}})