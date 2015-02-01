import csv
import sys

def main(argv):
	fich_csv = open(argv[1], "rU")
	csv_reader = csv.reader(fich_csv) #, delimiter='\t') 
	for row in csv_reader:
		print row 

main(sys.argv)