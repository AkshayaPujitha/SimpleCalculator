from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def operand(a):
    l=['1','2','3','4','5','6','7','8','9']
    if a in l:
        return 1
    else:
        return 0
def operator(a):
    l=['+','-','*','/']
    if a in l:
        return 1
    else:
        return 0

l=[]
l2=[]
ans=[]
def operation(l,l3):
    l3.pop(0)
    if l[0]=="+" or l[0]=="-" or l[0]=="*" or l[0]=="/":
        i=1
        u=len(ans)
        sum=""
        l2=[]
        print(ans[u-1])
        l2.append(ans[u-1])
        m=l[0]
    else:
        i=0
        sum=0
        m=0
        l2=[]
    length=len(l)
    num=""
    
   
    while i<length:
        if operand(l[i]):
            num=num+l[i]
            i=i+1
        else:
            if m==0:
                m=l[i]
                l2.append(num)
                num=""
                i=i+1
            else:
                if m=="+":
                    sum=(float(num))+(float(l2[0]))
                if m=="-":
                    sum=-(float(num))+(float(l2[0]))
                if m=="*":
                    sum=(float(num))*(float(l2[0]))
                if m=="/":
                    sum=(float(l2[0]))/(float(num))

                l2=[]
                l2.append(sum)
                num=""
                
                m=l[i]
                i=i+1
    print(sum,num,l2,m)
    if l2!=[]:
        if m=="+":
            sum=(float(num))+(float(l2[0]))
        if m=="-":
            sum=-(float(num))+(float(l2[0]))
        if m=="*":
            sum=(float(num))*(float(l2[0]))
        if m=="/":
            sum=(float(l2[0]))/(float(num))

        
    else:
        if m=="+":
            sum=sum+(float(num))
        if m=="-":
            sum=sum-(float(num))
        if m=="*":
            sum=sum*float(num)
        if m=="/":
            sum=sum/float(num)

    
            
    #print(sum,l)
    for i in range(0,length):
        l.remove(l[0])
    ans.append(sum)
    return sum

def text(l2):
    if l2[0]=="+" or l2[0]=="-" or l2[0]=="*" or l2[0]=="/":
        sum=""
        u=len(ans)
        l2.insert(0,str(ans[u-1]))
        print(l2)
    else:
        sum=""
    length=len(l2)
    for i in l2:
        sum=sum+i
    for i in range(0,length):
        l2.remove(l2[0])
    l2.append(sum)
    print(l2)
    return sum

def calc(request):
    if request.method=='POST':
        a=request.POST.get('num')
        print(a)
        if a=="c":
            le=len(l2)
            le1=len(l)
            while le>0:
                m=l2[0]
                l2.remove(m)
                le-=1
            while le1>0:
                m=l[0]
                l.remove(m)
                le1-=1

        elif operand(a):
            l2.append(a)
            l.append(a)
        elif operator(a):
            l2.append(a)
            l.append(a)
        elif a=='=':
            print(l)
            sum=operation(l,l2)
            print(sum,l2)
            return render(request,'home.html',{'sum':sum})
        i=len(l)
        if len(l2)!=0:
            sum=text(l2)
        else:
            sum=" "
        return render(request,'home.html',{'sum':sum})
        

    return render(request,'home.html')
