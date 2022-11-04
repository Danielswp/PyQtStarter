dss='hello pyqt5'
print('dss',dss)

#1
print('\n#1')
s2=dss[1:];print('s2,',s2)
s3=dss[1:3];print('s3,',s3)
s4=dss[:3];print('s4,',s4)

#2
print('\n#2')
s2=dss[-1];print('s2',s2)
s3=dss[1:-2];print('s3',s3)
dn=len(dss);print('dn',dn)
s4=dss[1:dn];print('s4',s4)

#3
print('\n#3')
print('s2+s3',s2+s3,"dd")
print('s3*2',s3*2)
print('s3+s3',s3+s3)

x1 = dss.join(['a','.','c'])
print('x1',x1)

x2 = " dasddasd "
print(x2.strip())
print(x2.lstrip())
x3 = x2.rstrip() + x2.lstrip()
print(x3)

x4 = "jack is a lovely boy."
print(x4.find("lovely"));
print(x4.find("cute"));

print(("jack">"tom"))
print(("jack"=="tom"))
print(("jack"<"tom"))
print(("jack"=="jack"))

print("jaCk is a Boy".upper())
print("jaCk is a Boy".lower())
print("jaCk is a Boy你好啊！Hello .".lower())
print("jaCk is a Boy".swapcase())
print("jaCk is a Boy".capitalize())
print("jaCk is a Boy".split(' '))