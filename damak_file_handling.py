"""
file  handling  :  .txt  

1. read : exiting  open  only  read .  
2. write : new  file  create   +  write  +  exiting  file open  ==> overwrite .
3. append :new  file  create   +  write  +  exiting  file open  ==> last add 

function  : 

fopen  ==> file  open  
with open  ==> file  open 
fclose  ==> file  close

"""

# ex :1  write  mode  

"""
with  open("damak.txt","w") as f : 
    f.write("my name is  damak.\n")
    f.write("live in ahmedabad.\n")
    f.write("study  in royal.")
    f.close()
"""

# ex :2 write  mode  ==> exiting  file . 
"""with  open("damak.txt","w") as f : 
    f.write("favorite  color  is  blue.\n")
    f.write("dream to meet nareadra modi.\n")
    f.close()
"""

# ex :3 append mode   ===> new file  

"""with  open("ram.txt","a") as f : 
    f.write("my name is  ram.\n")
    f.write("live in ahmedabad.\n")
    f.write("study  in AU.")
    f.close()
"""
# ex :4 append mode   ===> exiting file  

"""
with  open("ram.txt","a") as f : 
    f.write("study in royal.\n")
    f.write("favourite  food is  pizza.\n")
    f.close()
"""

# ex :5 read mode : exiting  file  open only  read. 

"""with  open("damak.txt","r") as f :
    # context = f.read()  # all  context read. 
    # context = f.readline()  # read only first line. 
    context = f.readlines()  # read all line store in to the  list. 
    
    print(context)
    
"""
"""
task  : 1 ask user to enter the  string  and  seprate  the  vowel and  conconant in seprate  vowel .txt  and  consonant .txt  file.

input  :"my name is ram."
output  : 
    vowel.txt : ae ia 
    consonant.txt : my nm s rm.

task :2  print  reverse of the string  and store  in  reverse.txt  file.

input  : "my name is  ram."
output  : 
    reverse.txt : .mar 

"""
