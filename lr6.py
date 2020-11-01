def printTble(tble):
    for i in range(0,5):
        print(tble[i])
    print("\n")
def dubbleLetter(bin_table,dbl_id):
    bin_table.append("")
    j=0
    for i in range(dbl_id,len(bin_table)):
        bin_table[len(bin_table)-j-1]=bin_table[len(bin_table)-j-2]
        j+=1
    bin_table[dbl_id]=bin_table[dbl_id+1][0]+"x";
    bin_table[dbl_id+1]="x"+bin_table[dbl_id+1][0];
    return bin_table
key=input("Input key : \n")
tabl=[['','','','',''],
    ['','','','',''],
    ['','','','',''],
    ['','','','',''],
    ['','','','','']]
alphabet = "abcdefghiklmnopqrstuvwxyz"
i=0
j=0
for k in range(len(key)):
    if j<5:
        if not key[k] in tabl[0] and not key[k] in tabl[1] and not key[k] in tabl[2] and not key[k] in tabl[3]and not key[k] in tabl[4]:
            tabl[i][j]=key[k]
            j+=1
    else:
        i+=1
        j=1
        if not key[k] in tabl[0] and not key[k] in tabl[1] and not key[k] in tabl[2] and not key[k] in tabl[3]and not key[k] in tabl[4]:
            tabl[i][0]=key[k]
for k in range(len(alphabet)):
    if j<5:
        if not alphabet[k] in tabl[0] and not alphabet[k] in tabl[1] and not alphabet[k] in tabl[2] and not alphabet[k] in tabl[3]and not alphabet[k] in tabl[4]:
                tabl[i][j]=alphabet[k]
                j+=1
    else:
        i+=1
        j=1
        if not alphabet[k] in tabl[0] and not alphabet[k] in tabl[1] and not alphabet[k] in tabl[2] and not alphabet[k] in tabl[3]and not alphabet[k] in tabl[4]:
            tabl[i][0]=alphabet[k]
f=open('text.txt')
text=f.read()
f.close()
text=text.replace(' ', '')
text=text.replace('\n', '')
text_bin=[]
for i in range(len(text)):
    if (i+1)%2==0:
        text_bin.append(text[i-1:i+1])
if (len(text))%2!=0:
    text_bin.append(text[len(text)-1]+'x')
code_text=[]
for i in range(len(text_bin)):
    if text_bin[i][0]==text_bin[i][1]:
        text_bin=dubbleLetter(text_bin,i)
if text_bin[len(text_bin)-1][0]==text_bin[len(text_bin)-1][1]:
    text_bin=dubbleLetter(text_bin,len(text_bin)-1)
def findLetter(tble,letr):
    if letr in tble[0]:
        return 0,tble[0].index(letr)
    if letr in tble[1]:
        return 1,tble[1].index(letr)
    if letr in tble[2]:
        return 2,tble[2].index(letr)
    if letr in tble[3]:
        return 3,tble[3].index(letr)
    if letr in tble[4]:
        return 4,tble[4].index(letr)
for i in range(len(text_bin)):
    code_bin=""
    ltr1_x,ltr1_y=findLetter(tabl,text_bin[i][0])
    ltr2_x,ltr2_y=findLetter(tabl,text_bin[i][1])
    if ltr1_x==ltr2_x:
        code_bin=tabl[ltr1_x][(ltr1_y+1)%5]+tabl[ltr1_x][(ltr2_y+1)%5]
    if ltr1_y==ltr2_y:
        code_bin=tabl[(ltr1_x+1)%5][ltr1_y]+tabl[(ltr1_x+1)%5][ltr1_y]
    if ltr1_y!=ltr2_y and ltr1_x!=ltr2_x:
        code_bin=tabl[ltr1_x][ltr2_y]+tabl[ltr2_x][ltr1_y]
    code_text.append(code_bin)
f=open("code.txt","w")
f.write(''.join(code_text))
f.close()
