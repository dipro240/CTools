import os.path
import argparse

parser = argparse.ArgumentParser(usage="%(prog)s <patha> [OPTIONY]",
                                 description="wordlist z komba ktery do nej narves.",
                                 epilog="Olga. Nehackovatelne")

group = parser.add_mutually_exclusive_group()

parser.add_argument("patha", help="sem zandas ten centralni kombo fajl")
parser.add_argument("-out", "--outputpath", metavar=("<path>"),
                    help="Necheme byt in chceme byt out - rekni insanii kam to chces ulozit, "
                         "jinak to ulozi tam kde zrovna ses %(metavar)s",
                    default=os.path.dirname(os.path.abspath(__file__)))
group.add_argument("-v", "--verbosity",
                    help="kokot ukecanej jak olga na dotacnim seminari", action="store_true", default=0)
group.add_argument("-q", "--quiet",
                   help="PROSTE DRZ HUBU", action="store_true")

args = parser.parse_args()

print("Toz tak startuju TY TŮLY")
kpath = args.patha
outpath = args.outputpath

print(kpath)

kfile = open(kpath, 'r', encoding='utf-8')
final = open(outpath + '\purepass.txt', 'w', encoding='utf-8')
klajny = kfile.readline()
while klajny:
    atLocation = klajny.find('@')
    realSeperator = atLocation + klajny[atLocation:].find(':')
    password = klajny[realSeperator + 1:]
    final.write(password)
    print(f"{password} zapsano")
    klajny = kfile.readline()
kfile.close()
final.close()

print("KAMO BUCO BUXO HTOVEEEEEEE")
