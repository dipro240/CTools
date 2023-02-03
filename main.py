import os
import os.path
import argparse
import ntpath
from pathlib import Path

def separate_pass():
    klajny = kfile.readline()
    while klajny:
        atLocation = klajny.find('@')
        realSeperator = atLocation + klajny[atLocation:].find(':')
        password = klajny[realSeperator + 1:]
        final.write(password)
        klajny = kfile.readline()
    kfile.close()
    final.close()

    if args.remduplicates == 1: #toz tutaj se zacinaji ty oddelovaciiiiii veci
        def remove_duplicate():
            hesla = open(finalf, 'r').read()
            hesla = hesla.split()
            clean_list = []
            for heslo in hesla:
                if heslo not in clean_list:
                    clean_list.append(heslo)
            return clean_list
            hesla.close()
        no_duplicate_hesla = open(finalf + '.temp.txt', 'w')

        for heslo in remove_duplicate():
            heslo = heslo.strip(',')
            no_duplicate_hesla.write(f"{heslo}\n")
        no_duplicate_hesla.close() 
        os.remove(finalf)
        os.rename(finalf + '.temp.txt', finalf)




MAPA_komandu = {'sPass' : separate_pass}

parser = argparse.ArgumentParser(usage="%(prog)s <command> <patha> [OPTIONY]", formatter_class=argparse.RawTextHelpFormatter,
                                 description="wordlist z komba ktery do nej narves.",
                                 epilog="Olga. Nehackovatelne")

parser.add_argument("command", nargs='?', default="sPass", choices=MAPA_komandu.keys(), metavar="command",
                    help="brasko tutaj vlastne vybiras co chces zeo delat zeo\n"
                    "-sPass - defaultni - proste jen separuje hesla od mailu\n"
                    "-rPass - oddela heslo jakoze uplne ho pojebe, zbyvaju jen maily\n"
                    "-ePass - editacni saskarna, mozes sortovat a removovat duplikaty take saskarny (-rD, -s...)\n"
                    " ")

parser.add_argument("patha", help="sem zandas ten centralni kombo fajl")

parser.add_argument("-out", "--outputpath", metavar=("<path>"),
                    help="Necheme byt in chceme byt out - rekni insanii kam to chces ulozit,\n"
                         "jinak to ulozi tam kde zrovna ses %(metavar)s\n"
                         " ",
                    default=0)

parser.add_argument("-n", "--name", default=0, metavar="<newname>",
                    help="Nastavi nove jmeno souboru kdyz uz teda tam chces cpat aj ten adresar\n(nebo i bez nej kdyz ses gay)"
                    " Defaultni novy jmeno je ve formatu <nazevpuvodnihokomba:command>\n"
                    " ")

parser.add_argument("-rD", "--remduplicates", action="store_true",
                    help="Vymaze ti z listu hesel duplikaty; procisti rasu\n"
                    " ")

parser.add_argument("-s", "--sort", default=100, metavar="[cislo]",
                    help="Sortne ze od nejvic top hesla co tam je visco a navic muzes rict kolik toho chces\n"
                    " ")

parser.add_argument("-v", "--verbosity",
                    help="kokot ukecanej jak olga na dotacnim seminari", action="store_true")

args = parser.parse_args()

print("Toz tak startuju TY TŮLY")

kpath = args.patha
fname = args.name 
if fname == 0:
    fname = "\CTooled-" + ntpath.basename(kpath)
else:
    fname = "\\" + fname + ".txt"
outpath = args.outputpath
if outpath == 0:
    outpath = os.path.dirname(os.path.abspath(kpath))
kfile = open(kpath, 'r', encoding='latin-1')
final = open(outpath + fname, 'w', encoding='utf-8')
finalf = outpath + fname

func = MAPA_komandu[args.command]
func()

print("KAMO BUCO BUXO HTOVEEEEEEE")
