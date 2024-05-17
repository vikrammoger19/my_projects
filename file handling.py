# f=open("abc.txt",'w')
# lines=["line1","line2","line3","line4"]
# for i in lines:
#     f.writelines(i+"\n")

# f=open("abc.txt",'r')
# for i in f:
#     print(i)

f=open("dog - Copy.jpg","rb")

f1=open("dog.jpg","wb")
for i in f:
    f1.write(i)

# f = open("MyTxt.txt", 'r')
# i = 0
# while True:
#     i = i + 1
#     lines = f.readline()
#     if not lines:
#         break;
#     m1 = lines.split(",")[0]
#     m2 = lines.split(",")[1]
#     m3 = lines.split(",")[2]
#     print(f"marks of student {i} in maths is {m1}")
#     print(f"marks of student {i} in physics is {m2}")
#     print(f"marks of student {i} in chemistry is {m3}")
#     print(lines)
