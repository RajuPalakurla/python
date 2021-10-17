from collections import OrderedDict,Counter

def collectionsfunction(text,dictionary1,key1,val1,deduct,list1):
    wordcount={}
    for word in text.split(" "):
        if word in wordcount.keys():
            wordcount[word]+=1
        else:
            wordcount[word]=1
    orderwords={word:wordcount[word] for word in sorted(wordcount.keys())}
    print(orderwords)

    counterobj=Counter(dictionary1)
    counterobj2=Counter(deduct)
    counterobj.subtract(counterobj2)
    print(dict(counterobj))

    orderData=OrderedDict(zip(key1,val1))
    del orderData[key1[1]]
    orderData[key1[1]]=val1[1]
    print(dict(orderData))

    dfltdict={}
    evenlist=[]
    oddlist=[]
    for val in list1:
        if val %2==0:
            evenlist.append(val)
        else:
            oddlist.append(val)
    if len(oddlist) > 0:
        dfltdict['odd']=oddlist
    if len(evenlist) > 0:
        dfltdict['even']=evenlist
    print(dfltdict)

if __name__ == "__main__":
    text="tamil nadu tamil, is one of the 28 states of india. its capital and largest city is chennai. tamil nadu lies in the southernmost part of the indian subcontinent and is bordered by the union territory of puducherry and the south indian states of kerala, karnataka, and andhra pradesh"
    dictionary1 ={1:3,2:4,12:2,14:6}
    deduct ={1:0,14:2}
    key1 = ['a','b','c']
    val1=[1,2,3]

    list1=[1,3,5,7,9,10]
    collectionsfunction(text,dictionary1,key1,val1,deduct,list1)