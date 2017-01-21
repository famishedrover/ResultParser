from connect_url import open_url
from bs4 import BeautifulSoup
import pickle
import os
from make_earlier_file import create_earlier_file , url , append_url , f
from Data import data

ALREADY_EXISTS = "already"
CREATED = "created"

def output_result () :
	supply_refer = []
	supply_link = []
	supply_date = []

	f_new = 'scraped_data.pkl'
	f_old = f

	if not os.path.exists(f_old) :
		create_earlier_file()
		print f_old +' created.'
		return CREATED


	r = open_url(url)

	soup = BeautifulSoup(r.content , "html.parser")

	links = soup.find("table" , {"id" : "AutoNumber1"}).find_all("tr")



	with open( f_new , 'wb') as out :
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


	latest = False 
	with open(f_new , 'rb' ) as n , open(f_old , 'rb') as o :
		data_new = pickle.load (n)
		data_old = pickle.load (o)

		if data_new.link == data_old.link :
			print 'Database already to the latest version.'
			latest = True
			return ALREADY_EXISTS

		else :
			pass




	if not latest :
		with open (f_new , 'rb') as n , open (f_old , 'rb') as o  :
			data_old = pickle.load(o)
			while True :
				try : 
					data_new = pickle.load(n) 
					if (data_new.link == data_old.link) :
						break
					else :

						supply_date.append(data_new.date)
						supply_link.append(data_new.link)
						supply_refer.append(data_new.refer)	

				except  :
					break

	#removing earlier_file.pkl and renaming scraped_data.pkl as earlier_file.pkl


	# print supply_refer 
	# print supply_link
	# print supply_date

	return supply_refer , supply_link , supply_date

	os.remove(f_old)
	os.rename(f_new , f_old)










	# for ks in k:
	# 	print ks.text
	# 	try :
	# 		print  ks.find("a").get("href")
	# 	except :
	# 		pass	



