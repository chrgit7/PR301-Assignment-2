from TkinterDrawer import *
from MyParser import *
from MySourceReader import *
from TurtlePrompt import *
import argparse
from GraphicsDrawer import *

if __name__ == '__main__':
    # data = sys.stdin.readlines()
    data = []
    parser = argparse.ArgumentParser('Interface')
    parser.add_argument('-a', '--arguments', type=str, metavar='', help='Choose your graphics program')
    args = parser.parse_args()
    drawer = ""
    if args.arguments == "t":
        drawer = TurtlePrompt()
    elif args.arguments == "tdemo":
        drawer = MySourceReader(MyParser(TurtleDrawer()), data)
    elif args.arguments == "tkdemo":
        drawer = MySourceReader(MyParser(TkinterDrawer()), data)
    elif args.arguments == "grdemo":
        s = MySourceReader(MyParser(GraphicsDrawer()), data)
        s.go()
    else:
        print("No valid command line arguments. Running Tkinter demo")
        drawer = MySourceReader(MyParser(TkinterDrawer()), data)
    drawer.go()

    # python Start.py -a t
    # python Start.py -a tkdemo
    # python Start.py -a tdemo
    # python Start.py -a grdemo
