import sys 
import os

def criarArchive(nome):
	with open(nome, 'wb') as archive:
		print('Create Archiver')
		archive.close()

def addFile(nome, caminhoArchive):
	with open(caminhoArchive, 'ab+') as archive:
		arqPath = open(nome, 'rb')
		data = arqPath.read()
		header = nome+'|'+str(len(data))+'|'
		#print('>> '+ header + str(data) +':'+str(len(data)+len(header)))
		archive.write(header.encode())
		archive.write(data)
		archive.close()
	print('Add to Archiver')

def extractFile(nome):#new
	with open('Archiver$', 'rb') as f:
		pos = 0
		f.seek(0, 0)
		while True:
			data = f.read() 	
			header = data.split(b'|')	
			if (header[0].decode() == nome):
				f.seek(pos, 0)
				data = f.read()
				header = (data).split(b'|')
				pos += len(header[0].decode()) + len(header[1].decode()) + 2
				f.seek(pos, 0)
				data = f.read(int(header[1].decode()))
				o = open(nome, 'wb')
				o.write(data)
				o.close()
				print('Concluido')
				break
			pos += len(header[0].decode()) + len(header[1].decode()) + 2 + int(header[1].decode())
			f.seek(pos, 0)
		f.close()

def listarArchive(nomeArchive):#implementar dic
	with open(nomeArchive, 'rb') as f:
		pos = 0
		f.seek(0, 0)
		while True:
			try:
				data = f.read() 	
				header = data.split(b'|')	
				print(header[0].decode() + '\t' + header[1].decode() + ' Bytes')
				pos += len(header[0]) + len(header[1]) + 2 + int(header[1])
				f.seek(pos, 0)
			except:
				break			 
		f.close()

def deleteFile(nome):
	with open('Archiver$', 'rb') as f:
		pos = 0
		f.seek(0, 0)
		antesLixo = b''
		while True:
			data = f.read()
			header = data.split(b'|')
			if (header[0].decode() == nome):
				print('Deleting file...')
				f.seek(pos, 0)
				data = f.read()
				header = (data).split(b'|')
				headerSize = len(header[0].decode()) + len(header[1].decode()) + 2
				f.seek(pos, 0)
				pos += len(header[0].decode()) + len(header[1].decode()) + 2 + int(header[1].decode())
				lixo = f.read(int(header[1].decode()) + headerSize)
				f.seek(pos, 0)
				depoisLixo = f.read()
				f.close()
				with open('Archiver$', 'wb') as f:
					f.write(antesLixo + depoisLixo)
					f.close()
				break

			f.seek(pos, 0)
			headerSize = len(header[0].decode()) + len(header[1].decode()) + 2
			antesLixo += f.read(int(header[1].decode()) + headerSize)

			pos += len(header[0].decode()) + len(header[1].decode()) + 2 + int(header[1].decode())
			f.seek(pos, 0)	 		
		f.close()

def showArchiver():
	f = open('Archiver$', 'rb')
	data = f.read()
	print(data)
	f.close()

	

def simpleManager():
	archive = 'Archiver$'
	banner = '''
._____________Archiver_____________.
[0]\tdumpArchive()
[1]\tcriarArchive(nome)
[2]\taddFile(nome, caminhoArchive)
[3]\textractFile(nome)
[4]\tlistarArchive(nomeArchive)
[5]\tdeleteFile(nome)
[6]\tsair()
			'''
	while True:
		print(banner)
		try:
			o = int(input('>> '))
			if (o == 0):
				showArchiver()
				os.system('pause')
			elif (o == 1):
				criarArchive(archive)
				os.system('pause')
			elif (o == 2):
				nome = input('File Name: ')
				addFile(nome, archive)
				os.system('pause')
			elif (o == 3):
				nome = input('File Name to Extract: ')
				extractFile(nome)
				os.system('pause')
			elif (o == 4):
				listarArchive(archive)
				os.system('pause')
			elif (o == 5):
				nome = input('File Name to Delete: ')
				deleteFile(nome)
				os.system('pause')
			elif (o == 6):
				break
		except Exception as erro:
			print(erro)
			os.system('pause')
			pass
		os.system('cls')

simpleManager()
