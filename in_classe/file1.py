file = './in_classe/a/a.txt'
#file = 'C:/Users/marco/Dropbox/Documenti/DIDATTICA/fondamenti di programmazione (MN)/in_classe/a/a.txt'
with open(file) as f:
    s = f.read()
print(s)