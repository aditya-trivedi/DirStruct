directory = ["/"]
files = ["/"]
#function to create a directory
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
#function to  create a file
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

#function to check the existence of a path
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

#funtion to list all directories in a path
def list(path):
	if(path =="/"):
		for i in directory:
			print(i.split("/")[1])
	for i in directory:
		print((i.rsplit(path,1))[1].split("/")[0])

#function to search a file in a given path
def search(path,sstr):
	if path not in directory:
		print("(\"No such file or Directory\",False)")
	for i in directory:
		if( i.endswith(sstr+"/") and i.startswith(path)):
			print(i)
	for i in files:
		if( i.endswith(sstr+"/") and i.startswith(path)):
			print(i)

			
#to take input from the user
while 1:
	command = input()
	exec("command")

			



