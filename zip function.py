names=("sid","aman","anjali","atharva")
comps=('hp','dell','apple','oneplus')
zipped1=dict(zip(names,comps))
zipped2=list(zip(names,comps))
zipped3=zip(names,comps)

print(zipped1)
print(zipped2)

for (a,b) in zipped3:
    print((a,b))