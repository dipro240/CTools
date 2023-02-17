import argparse
import os
import os.path
import pathlib
import collections
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

    if args.sort > 0: # toz tutaj bude sort
        global sortnum
        print("sortLOG69: ziju<3")
        docasnysranec = pathlib.PurePath(finalf.with_name(fname + '.temp.txt'))
        sortnuto = open(docasnysranec,  'w', encoding='utf-8')
        with open(finalf, encoding='utf-8') as infile:
            counts = collections.Counter(l.strip() for l in infile)
            for line, count in counts.most_common():
                if sortnum > 0:
                    sortnum -= sortnum
                    line = line.strip(',')
                    sortnuto.write(f"{line}\n")
        sortnuto.close()
        os.remove(finalf)
        os.rename(docasnysranec, finalf)
        print("sort konciiii")

    if args.remduplicates == 1:  # toz tutaj se zacinaji ty oddelovaciiiiii veci
        print("deduplikatorrr aaa tutaajjj")
        if sortnum == 0:
            print("KAMO DEBILE KOKOTE VSAK UZS SORTOVAL TO I MAZE SMH ZY SES KOKOT")
        else:
            def remove_duplicate():
                hesla = open(finalf, 'r', encoding='utf-8').read()
                hesla = hesla.split()
                clean_list = []
                for heslo in hesla:
                    if heslo not in clean_list:
                        clean_list.append(heslo)
                return clean_list
                hesla.close()

            docasnysranec = pathlib.PurePath(finalf.with_name(fname + '.temp.txt'))
            no_duplicate_hesla = open(docasnysranec, 'w', encoding='utf-8')

            for heslo in remove_duplicate():
                heslo = heslo.strip(',')
                no_duplicate_hesla.write(f"{heslo}\n")
            no_duplicate_hesla.close()
            os.remove(finalf)
            os.rename(docasnysranec, finalf)
            print("deduplikator konciiii")


MAPA_komandu = {'sPass': separate_pass}

parser = argparse.ArgumentParser(usage="%(prog)s <command> <patha> [OPTIONY]",
                                 formatter_class=argparse.RawTextHelpFormatter,
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

parser.add_argument("-s", "--sort", default=0, const=100, metavar="cislo", nargs='?', type=int,
                    help="Sortne ze od nejvic top hesla co tam je visco a navic muzes rict kolik toho chces\n"
                         " ")

parser.add_argument("-v", "--verbosity",
                    help="kokot ukecanej jak olga na dotacnim seminari", action="store_true")

args = parser.parse_args()

print("Toz tak startuju TY TŮLY")

kpath = pathlib.PurePath(args.patha)
sortnum = args.sort
outpath = args.outputpath
if outpath == 0:
    outpath = kpath.parent
else:
    outpath = pathlib.PurePath(args.outputpath)
fname = args.name
if fname == 0:
    fname = kpath.stem + "-CTooled.txt"
else:
    fname = fname + ".txt"
kfile = open(kpath, 'r', encoding='latin-1')
final = open(outpath / fname, 'w', encoding='utf-8')
finalf = outpath / fname

func = MAPA_komandu[args.command]
func()

print("KAMO BUCO BUXO HTOVEEEEEEE")
