l1=[40,23,20,12]
l2=[40,56,87,34]
ls=['Vignesh','Priya','Privika']
s='The quick brown fox jumps over the lazy dog'

## Create list with elements present in l1 but not in l2
l3=[ each_element for each_element in l1 if each_element not in l2]
print('l1:',l1)
print('l2:',l2)
print('l3:',l3)

## Create common elements present in both l1 and l2
l4=[ each_element for each_element in l1 if each_element  in l2]
print('l4:',l4)

l5= [ each_element[0] for each_element in ls]
print('l5:',l5)

words=s.split()
print('words:',words)
l6=[[each_element.upper(),len(each_element)] for each_element in words ]
print('l6:',l6)
