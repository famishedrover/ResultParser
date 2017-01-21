from connect_url import open_url
from bs4 import BeautifulSoup
import pickle
from Data import data

url = "http://exam.dtu.ac.in/result.htm"
f = 'earlier_file.pkl'
append_url = "http://exam.dtu.ac.in/"





def create_earlier_file():


	r = open_url(url)
	soup = BeautifulSoup(r.content , "html.parser")
	links = soup.find("table" , {"id" : "AutoNumber1"}).find_all("tr")
	with open( f , 'wb') as out :
		count = 0
		for link in links :
			count += 1
			if(count<3):
				continue
			k = link.find_all("td")

			try :
				refer =  str(k[1].text.strip())
				link =  append_url + str (k[1].find("a").get("href"))
				date =  str(k[3].text.strip())
				data_obtained = data(refer , link , date)
				# putting data in the class data
				# and then in the file 
				pickle.dump (data_obtained, out , pickle.HIGHEST_PROTOCOL)

			except :
				pass



if __name__ == "__main__" :
	from print_pkl_file import print_file
	create_earlier_file()
	print 'File Contains :'
	print_file(f)	




	# with open (f , 'rb') as inp :
	# 	i = 0
	# 	while True :
	# 		try : 
	# 			print ''
	# 			i += 1
	# 			print i
	# 			data_obtained = pickle.load(inp) 
	# 			print data_obtained.refer
	# 			print data_obtained.link
	# 			print data_obtained.date
	# 		except  :
	# 			break











	# for ks in k:
	# 	print ks.text
	# 	try :
	# 		print  ks.find("a").get("href")
	# 	except :
	# 		pass	



