import pickle 
from Data import data


def print_file (file) :
	with open (file , 'rb') as inp  :
			i = 0
			while True :
				try : 
					print ''
					i += 1
					print i
					data_obtained = pickle.load(inp) 
					print data_obtained.refer
					print data_obtained.link
					print data_obtained.date
				except  :
					break

if __name__ == "__main__" :
	print_file('earlier_file.pkl')