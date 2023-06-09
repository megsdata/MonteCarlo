#define functions to run the simulation
import random
import os
import os.path
import sys
####
#### use module load python/3.11.1 
####
#this function make individual DNA barcodes
##### Make a set 
def makeBarcodes(code_length):
	return ''.join(random.choice('ACTG') for _ in range(code_length))

#this function pools it into a list
#### code_length 35, 
def makeBarcodesList(list_length, code_length):
	barcodepool = set()
	for i in range(list_length):
		barcodepool.add(makeBarcodes(code_length))
	return barcodepool

#monte carlo simulation
### num_simulations=1000, intended_cells=5*10^6
def runMonteCarlo(num_simulations, intended_cells, barcodepool):
	nEvent = 0
	barcoded = []
	for i in range(1, num_simulations):
		print("Sim "+ str(i))
		for j in range(int(intended_cells)):
			barcoded.append(random.sample(list(barcodepool), 1)[0])
			singleRepPercent = 1.0 * len([bc for bc in barcoded if barcoded.count(bc) == 1]) / len(barcoded)
			if singleRepPercent < .95:
					nEvent += 1
			if nEvent > .05 * num_simulations:
					break
	pvalue = 1.0 * nEvent / num_simulations
	if pvalue < .05:
			print('Sufficient library diversity')
	else:
			print('Insufficient library diversity')


def usage():
	print ("Usage:  %s" % os.path.basename(sys.argv[0] + ' num_simulations, intended_cells, barcodepool' ))


def main():
	if len(sys.argv)>1:
		args = sys.argv[1:]
		if "-h" in args or "--help" in args:
			usage();
			sys.exit(2)
		else:

			num_simulations=int(sys.argv[1])
			list_length=int(sys.argv[2])
			code_length=35 #int(sys.argv[3])
			intended_cells=5*10**6 #int(sys.argv[4])
			barcodepool=makeBarcodesList(list_length, code_length)

			runMonteCarlo(num_simulations, intended_cells, barcodepool)
	else:
		usage()


if __name__ == "__main__":
	sys.exit(main())

			