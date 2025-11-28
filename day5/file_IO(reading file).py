# | Mode   | Meaning (Easy Explanation)                  |
# | ------ | ------------------------------------------- |
# | `"r"`  | Read file (file must exist)                 |
# | `"w"`  | Write file → **delete old data**, write new |
# | `"a"`  | Append → add data at end (keep old data)    |
# | `"x"`  | Create new file (error if file exists)      |
# | `"r+"` | Read + Write (file must exist)              |
# | `"w+"` | Write + Read (deletes old data)             |
# | `"a+"` | Append + Read                               |

#reading a file

F = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt", "r")

data = F.read()
print(data)#reads whole file

print(type(data))#type of data

data1 = F.read(5)#print 5 characters of file
print(data1)

data2 = F.readline()#reads one line 
print(data2)

F.close

#writing a file 

#overwrite the file
F = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","w")
data3 = F.write("i want to learn python \n")#\n will move to the next line
print(data3)
F.close()

#adds data in the last
Z = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","a")
data4 = Z.write("i will also learn sql ")
print(data4)
Z.close()

#w or a mode creates fie if it does not exists
D = open(r"sample.txt","a")
D.close()

#reads and write data
A = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","a")
data6 = A.write("i am learning")
print(data6)
A.close()

#reading and writing data (it overwritess the data from  starting)
B = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","r+")
data7 = B.write("abc")
print(data7)
B.close

#overwrite the file
F = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","w")
data8 = F.write("i want to learn python \n")#\n will move to the next line
print(data8)
F.close()

#adds data in the last
Z = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","a")
data9 = Z.write("i will also learn sql ")
print(data9)
Z.close()

#w or a mode creates fie if it does not exists
D = open(r"sample.txt","a")
D.close()

#reads and write data
E = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","a")
data10 = E.write("i am learning")
print(data10)
E.close()

#reading and writing data (it overwritess the data from  starting)
G = open(r"C:\Users\DELL\OneDrive\Desktop\Zalak clg\PY_CODES\python\day5\demo.txt","w+")
data11 = G.read()
print(data11)
data12 = G.write("abcd")
print(data12)
G.close()