try:
	f = open('archiver.$', 'rb')
	print(f.read())
	f.close()
except Exception as e:
	print(e)
