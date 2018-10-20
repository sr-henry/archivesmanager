import sys 
import os

def criarArchive(nomeArchive):
	with open(nomeArchive, 'wb') as archive:
		print('Create Archiver')
		archive.close()

def addFile(nome, nomeArchive):
	with open(nomeArchive, 'ab+') as archive:
		arqPath = open(nome, 'rb')
		data = arqPath.read()
		header = nome+'|'+str(len(data))+'|'
		archive.write(header.encode())
		archive.write(data)
		archive.close()
	print('Add to '+nomeArchive)

def extractFile(nome, nomeArchive):
	with open(nomeArchive, 'rb') as archive:
		pos = 0
		archive.seek(0, 0)
		while True:
			data = archive.read() 	
			header = data.split(b'|')	
			if (header[0].decode() == nome):
				archive.seek(pos, 0)
				data = archive.read()
				header = (data).split(b'|')
				pos += len(header[0].decode()) + len(header[1].decode()) + 2
				archive.seek(pos, 0)
				data = archive.read(int(header[1].decode()))
				file = open(nome, 'wb')
				file.write(data)
				file.close()
				print('Done!')
				break
			pos += len(header[0].decode()) + len(header[1].decode()) + 2 + int(header[1].decode())
			archive.seek(pos, 0)
		archive.close()

def listarArchive(nomeArchive):
	with open(nomeArchive, 'rb') as archive:
		pos = 0
		archive.seek(0, 0)
		while True:
			try:
				data = archive.read() 	
				header = data.split(b'|')
				print(header[0].decode() + '\t' + header[1].decode() + ' Bytes')
				pos += len(header[0]) + len(header[1]) + 2 + int(header[1])
				archive.seek(pos, 0)
			except:
				break			 
		archive.close()

def deleteFile(nome, nomeArchive):
	with open(nomeArchive, 'rb') as archive:
		pos = 0
		archive.seek(0, 0)
		antesLixo = b''
		while True:
			data = archive.read()
			header = data.split(b'|')
			if (header[0].decode() == nome):
				print('Deleting file...')
				archive.seek(pos, 0)
				data = archive.read()
				header = (data).split(b'|')
				headerSize = len(header[0].decode()) + len(header[1].decode()) + 2
				archive.seek(pos, 0)
				pos += len(header[0].decode()) + len(header[1].decode()) + 2 + int(header[1].decode())
				lixo = archive.read(int(header[1].decode()) + headerSize)
				archive.seek(pos, 0)
				depoisLixo = archive.read()
				archive.close()
				with open(nomeArchive, 'wb') as archive:
					archive.write(antesLixo + depoisLixo)
					archive.close()
				print('Done!')
				break
			archive.seek(pos, 0)
			headerSize = len(header[0].decode()) + len(header[1].decode()) + 2
			antesLixo += archive.read(int(header[1].decode()) + headerSize)
			pos += len(header[0].decode()) + len(header[1].decode()) + 2 + int(header[1].decode())
			archive.seek(pos, 0)	 		
		archive.close()

def defaultManager():
	_help_ = '''
create    [-c]    ‹novoarchive.arq› ‹arq1› ‹arq2› ...
insert    [-i]    ‹archive.arq›     ‹arq›
list      [-l]    ‹archive.arq›
extract   [-e]    ‹archive.arq›     ‹arq›
remove    [-r]    ‹archive.arq›     ‹arq›
'''
	try:
		opr = sys.argv[1]
		if (opr == '-c'):
			i = 3
			while i < len(sys.argv):
				file = sys.argv[i]
				print(file)
				addFile(file, sys.argv[2])
				i+=1
		elif (opr == '-i'):
			addFile(sys.argv[3], sys.argv[2])
		elif (opr == '-l'):
			listarArchive(sys.argv[2])
		elif (opr == '-e'):
			extractFile(sys.argv[3], sys.argv[2])
		elif (opr == '-r'):
			deleteFile(sys.argv[3], sys.argv[2])
	except:
		print(_help_)

defaultManager()