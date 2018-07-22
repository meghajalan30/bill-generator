
import json
f=open("backup.JSON",'r')
f1=open("data.html",'r')
f2=open("bill.html",'w+')
temp=f1.read()
build=''
content = json.load(f) #a list of dictionaries is formed
l=len(content['billdetail'])
#print(l)
total=0
for i in range (0,l):
    amount=float(content['billdetail'][i]['unitCost'])*float(content['billdetail'][i]['qty'])
    content['billdetail'][i]['amount']=amount
    #print(amount)
    total+=amount
#print(total)
show='<script>'
fin=temp.find(show)
build=build+str(temp[0:fin+len(show)])
#print(build)
c=0
while c<l:
    build=build+"var row"+str(c)+"= document.createElement('tr');\n var col"+str(c)+"1= document.createElement('td');\n var col"+str(c)+"2= document.createElement('td'); \n var col"+str(c)+"3= document.createElement('td');\n var col"+str(c)+"4= document.createElement('td'); \n var col"+str(c)+"5= document.createElement('td');\n col"+str(c)+"1.innerHTML='"+str(content['billdetail'][c]['cdn'])+"';\n col"+str(c)+"2.innerHTML='"+str(content['billdetail'][c]['name'])+"';\n col"+str(c)+"3.innerHTML='"+str(content['billdetail'][c]['unitCost'])+"';\n col"+str(c)+"4.innerHTML='"+str(content['billdetail'][c]['qty'])+"';\n col"+str(c)+"5.innerHTML='"+str(content['billdetail'][c]['amount'])+"';\n row"+str(c)+".appendChild(col"+str(c)+"1);\n row"+str(c)+".appendChild(col"+str(c)+"2);\n row"+str(c)+".appendChild(col"+str(c)+"3);\n row"+str(c)+".appendChild(col"+str(c)+"4);\n row"+str(c)+".appendChild(col"+str(c)+"5);\n var tab"+str(c)+" = document.getElementById('tables');\n tab"+str(c)+".appendChild(row"+str(c)+");\n"
    c+=1
build=build+"\n var tab=document.getElementById('tables');\n var row=document.createElement('tr');\n var col1=document.createElement('td');\n var col2=document.createElement('td');\n var col3=document.createElement('td');\n var col4=document.createElement('td');\n var col5=document.createElement('td');\n col1.innerHTML='';\n col2.innerHTML='';\n col3.innerHTML='';\n col4.innerHTML='Subtotal';\n col5.innerHTML='"+str(total)+"';\n row.appendChild(col1);\n row.appendChild(col2);\n row.appendChild(col3);\n row.appendChild(col4);\n row.appendChild(col5);\n tab.appendChild(row);\n"
show1='</script>'
find1=temp.find(show1)
show2='</html>'
find2=temp.find(show2)
build=build+str(temp[find1:find2+len(show2)])
f2.write(build)
f.close()
f2.close()
f1.close()
