import argparse
from bs4 import BeautifulSoup
 
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="Mostrar version", action="store_true")
parser.add_argument("-sf", "--sourceFile", help="Ruta del archivo")
parser.add_argument("-of", "--outFile", help="Nombre de archivo de salida")
args = parser.parse_args()
 
# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.version:
    print ("Primera version!!!")
if args.sourceFile:
    print ("Nombre del archivo: ", args.sourceFile)
    f = open(args.sourceFile, 'r')
    bs = BeautifulSoup(f.read(), 'html.parser')
    for tr in bs.find_all('tr'):
        col = '{'
        for td in tr.find_all('td'):
            col += td.get_text()
            col += ','
        col += '}'
        print(col)
    f.close()
if args.outFile and args.sourceFile:
    print ("Nombre del archivo de salida", args.make)
