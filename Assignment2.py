st=input("Enter any word: ")
d={}
for i in st:
    d[i] = st.count(i)

for i,j in d.items():
    print(f'{i} : {j}')