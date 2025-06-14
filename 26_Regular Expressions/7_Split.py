import re

str='a7b@k9 zA.aacaaaa'
splitPattern='[.@ ]'
target_list=re.split(splitPattern,str)

print(target_list)