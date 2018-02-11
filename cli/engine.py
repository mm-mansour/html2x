import os
import argparse

parser = argparse.ArgumentParser(description="convert html link or file into a pdf, png, or jpg file.")
parser.add_argument("source", metavar="file", type=str,
                    help="source as a file or link")

parser.add_argument("--extension", dest="extension", action="store", default="png",
                    help="target file extension [png, jpg, pdf] (default: png)")

parser.add_argument("--wh", dest="wh", action="store", default=None,
                    help="target file width,height in pixels (default: None)")

args = parser.parse_args()

link = args.source
extension = args.extension
if args.wh is not None:
    wh = args.wh
    os.system("/usr/bin/firefox -headless -screenshot exported/output.png {} --window-size={}".format(link, wh))
else:
    os.system("/usr/bin/firefox -headless -screenshot exported/output.png {}".format(link))

if extension != "png":
    os.system("convert exported/output.png exported/output.{}".format(extension))
    os.system("rm exported/output.png")

os.system("chmod 666 exported/output.{}".format(extension))
