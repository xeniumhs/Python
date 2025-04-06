a=2e3
a=1e1
print(a,type(a))

#type_conversion
x=1
y=2.33
z=2+3j

c=complex(y)
print(c,type(c))

a="sss\n\teeee"
print(a)
#""-to print escape seqq
a='sss\n\teeee'
print(a)

txt=" I ate banananana "
print("e b" in txt)
print(len(txt))
print(txt)
#slicing string
print(txt[3::2])

#strip
print(txt.strip())
#replace
print(txt.replace("b","RR"))

a="data science xen"

print(a.split("a"))

# boolean
print(9>2)
print(9<2)