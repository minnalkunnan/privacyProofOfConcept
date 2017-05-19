from pymongo import MongoClient

client = MongoClient()
db = client['project1']
collection = db['entries']

with open('workfile') as file:
	#lines = [line for line in file]
	lines = [line.rstrip('\n') for line in file]
	lines = [line for line in lines if line.strip()]
	#lines = [line.rstrip(' ') for line in file]
	for line in lines:
		firstLine = line.split('>')

		print("First line")
		print(firstLine[0])

		secondLine = firstLine[1].split('}')[0]
		thirdLine = firstLine[1].split('}')[1]
		#print("Second line")
		realSecondLine = secondLine.split('\\r\\n')
		#print(realSecondLine)
		#print("Third Line")
		#print(thirdLine)

		index1 = firstLine[0].find('\'')
		index2 = firstLine[0][index1+1:].find('\'')
		request = firstLine[0][index1+1:index1+index2+1]
		print(request)

		print("\nNew Request Info\n")
		index1 = secondLine.find('Referer: ')
		index2 = secondLine[index1:].find('\\r\\n')
		referer = secondLine[index1:index1+index2]
		print(referer)

		index1 = secondLine.find('Content-Length: ')
		index2 = secondLine[index1:].find('\\r\\n')
		contentLength = secondLine[index1:index1+index2]
		print(contentLength)

		index1 = secondLine.find('User-Agent: ')
		index2 = secondLine[index1:].find('\\r\\n')
		userAgent = secondLine[index1:index1+index2]
		print(userAgent)

		index1 = secondLine.find('Connection: ')
		index2 = secondLine[index1:].find('\\r\\n')
		connection = secondLine[index1:index1+index2]
		print(connection)

		index1 = secondLine.find('Forwarded: ')
		index2 = secondLine[index1:].find('\\r\\n')
		forwarded = secondLine[index1:index1+index2]
		print(forwarded)

		index1 = secondLine.find('Host: ')
		index2 = secondLine[index1:].find('\\r\\n')
		host = secondLine[index1:index1+index2]
		print(host)

		index1 = secondLine.find('Accept: ')
		index2 = secondLine[index1:].find('\\r\\n')
		accept = secondLine[index1:index1+index2]
		print(accept)

		index1 = secondLine.find('Accept-Language: ')
		index2 = secondLine[index1:].find('\\r\\n')
		acceptLanguage = secondLine[index1:index1+index2]
		print(acceptLanguage)

		index1 = secondLine.find('Content-Type: ')
		index2 = secondLine[index1:].find('\\r\\n')
		contentType = secondLine[index1:index1+index2]
		print(contentType)

		index1 = secondLine.find('Accept-Encoding: ')
		index2 = secondLine[index1:].find('\\r\\n')
		acceptEncoding = secondLine[index1:index1+index2]
		print(acceptEncoding)

		print(thirdLine)

		entry = {
			"Request": request,
			"Referer": referer,
			"Content-Length": contentLength,
			"User-Agent": userAgent,
			"Connection": connection,
			"Forwarded": forwarded,
			"Host": host,
			"Accept": accept,
			"Accept-Language": acceptLanguage,
			"Content-Type": contentType,
			"Accept-Encoding": acceptEncoding
		}

		entry_id = collection.insert_one(entry).inserted_id
		print(entry_id)
