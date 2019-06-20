spam =['apples','bananas','tofu','cats']
a=''
#def list(spam):
for i in range(len(spam) - 1):
   a = a+','+spam[i]
#print (len(spam))
#print(spam[len(spam)])

print (a +' and '+spam[len(spam)-1])