import sys
import common.add as addmethod

def main():
	res = addmethod.add(sys.argv[1],sys.argv[2])
	print 'result is {}'.format(res)
if __name__ == "__main__":
	main()