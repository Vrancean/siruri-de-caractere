from re import A


s=str(input('introdu sirul:'))
s1=len([i for i in s if i=='A'])
print('a) numarul de aparitii ale caracterului (A) in sir:',s1)
s2=s.replace('A','*')
print('b) substituirea caracterului (A) cu (*):',s2)
s3=s.replace('B',' ')
print('c) stergerea caracterului (B) din sir:',s3)
s4=s.count('MA')
print('d) aparitia silabei (MA) in sir:',s4)
s5=s.replace('MA','TA')
print('e) subsituirea silabei (MA) prin silaba (TA):',s5)
s6=s.replace('TO',' ')
print('f) stergerea silabei (TO) din sir:',s6)
s7=s[::-1]
print('g) scrierea inversa a sirului:',s7)
