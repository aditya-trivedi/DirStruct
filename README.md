# DirStruct
Linux File System Simulation Using Python

Implement a directory structure for a Linux Based opera ng System. You are not suppose to create actual files or directories. You should only give
the implementa on of the Directory Structure like how would a directory Structure look if I create a Directory. I will give you the output in detail. You can
assume that there exist no Directory Structure in the beginning.

Tasks :
1. Create a Directory
a. Input – Absolute Path String – Example create_directory(“/home/prathiba/mydirectory/”)
b. Output – Tuple or Pair (string,bool) indica ng (path,True) or (“No such file or Directory”, False)
2. Create a File within a Directory
a. Input – Absolute Path String – Example create_file(“/home/prathiba/mydirectory/”)
b. Output – Tuple or Pair (string,bool) indica ng (path,True) or (“No such file or Directory”, False)
c. Note that if you are trying to create a file within a file, it should throw an excep on
3. List at a par cular path
a. Input – Absolute Path String – Example list(“/home/prathiba/mydirectory/”)
b. Output – Key value pair (Type:list(string)) indica ng the files and directories in that path
4. Check if a file/directory exists in the directory structure.
a. Input – String – Example check_existence(“mydirectory”)
b. Output – True/False
5. Search a file or a directory in the en re structure star ng from that path.
a. Input - String - Example search("path", "searchstring"). search("/", "ssh")
b. Output - Print all the paths which ends with the searchstring
/run/user/1000/keyring/ssh
/snap/core18/1098/etc/default/ssh
/snap/core18/1098/etc/init.d/ssh
/snap/core18/1098/etc/ssh
/snap/core18/1098/usr/bin/ssh
/snap/core18/1074/etc/default/ssh


Important Notes  :
Always Add "/" at starting and ending of the path.
Don't add "/" for the check_existence function
