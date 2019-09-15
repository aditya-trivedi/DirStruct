directory = []
files = []
def create_directory(path):
	direc = path.rsplit("/",2)
	if len(direc) == 3:
		if "/"+direc[1]+"/" in directory:
			print("(\"Directory Already Exists\",False)")
		else:
			directory.append("/"+direc[1]+"/")
			print("(\"Directory Created\",True)")
	else:
		if path in directory:
			print("(\"Directory Already Exists\",False)")
		elif direc[0]+"/"  in directory:
			directory.append(path)
			print("(\"Directory Created\",True)")
		else:
			print("(\"No such file or Directory\",False)")

def create_file(path):
	direc = path.rsplit("/",2)
	if len(direc) == 3:
		if "/"+direc[1]+"/" in files:
			print("(\"File Already Exists\",False)")
		else:
			files.append("/"+direc[1]+"/")
			print("(\"File Created\",True)")
	else:
		if path in files:
			print("(\"File Already Exists\",False)")
		elif direc[0]+"/"  in directory:
			files.append(path)
			print("(\"File Created\",True)")
		else:
			print("(\"No such file or Directory\",False)")

def check_existence(dir_name):
	for i in directory:
		direc = i.rsplit("/",2)
		if direc[len(direc)-2] == dir_name :
			print("True")
	for i in files:
		direc = i.rsplit("/",2)
		if direc[len(direc)-2] == dir_name :
			print("True")
	print("False")
def list(path):
	if(path =="/"):
		for i in directory:
			print(i.split("/")[1])
	for i in directory:
		print((i.rsplit(path,1))[1].split("/")[0])

def search(path,sstr):
	for i in directory:
		if( i.endswith(sstr+"/") and i.startswith(path)):
			print(i)
	for i in files:
		if( i.endswith(sstr+"/") and i.startswith(path)):
			print(i)

while 1:
	command = input()
	exec("command")

			



