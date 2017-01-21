import requests 

def open_url ( url , index = 1 ) :
	try :
		print ('Please Wait...')
		r = requests.get(url)
		print 'Connected : ' + str (index) 
		return r 
	except :
		print (url+'\ncould not be fetched.')
		return -1 