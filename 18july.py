#file handling  : 
"""
r+  : read  +  write   == > exiting file  
w+  : read + write  ==>  new create file  ==>  exiting  file  ==> over write  
a+  : read +  write  ==>  new create file  ==>  exiting  file  ==> append

seek()   ==> move cursor 
"""

"""with  open ("yash.txt","r+") as f :
    f. write("hello")
    f.seek(0)
    context =f.read()
    print(context)
    f.close()
"""

"""
with  open("saloni.txt","w+") as f :
    f.write("hello saloni  how are you  ???\n")
    f.write("plz decribe  your property ...\n")
    f.write("100 vega\n")
    f.seek(0)
    r=f.read()
    print(r)
    f.close()
"""

"""with  open("saloni.txt","w+") as f :
    f.write("my name is saloni .\n")
    f.write("live in ahm.\n")
    f.write("study  in LJ OLD.\n")
    f.seek(0)
    r=f.read()
    print(r)
    f.close()
"""

"""
with  open("utsav.txt","a+") as f :
    f.write("hello utsav  how are you  ???\n")
    f.write("live in ahm .\n")
    f.write("study  in LJ OLD.\n")
    f.seek(0)
    r=f.read()
    print(r)
    f.close()
"""

"""with  open("utsav.txt","a+") as f :
    f.write("utsav borad  ???\n")
    f.write(" best friend name is  yash patel.\n")
    f.write("dushman name is  jinang shah.\n")
    f.seek(0)
    r=f.read()
    print(r)
    f.close()
"""