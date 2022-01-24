txt = "Company12"

x = txt.isalnum()

print(x)

import re

l2=["abc",12,6,"!","?","!^&"]

string_value ="alphanumeric@123__"

def rem_nonan(str):
    return(re.sub(r'[\W_]+', '', str))

s=re.sub(r'[\W_]+', '', string_value)
ss=rem_nonan(string_value)
print(s,ss)

l2=["abc","1g2","6e@ert5","!","?7aw$","!^vd21&"]
l4=rem_nonan(l2[0])
print(l4)
l4=rem_nonan(l2[1])
print(l4)
l4=rem_nonan(l2[2])
print(l4)
l4=rem_nonan(l2[3])
print(l4)
#l4=[for s in  l2,rem_nonam(s)]
l4=[rem_nonan(s) for s in l2]
#l4=list(filter(lambda s: s in l2 if not s.isalnum(), l2))
print(l4)