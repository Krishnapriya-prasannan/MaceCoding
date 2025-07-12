n=int(input())
st=[]
q=0
k=1
ins=['']*(n)
while(q!=n):
    ins[q]=input()
    q+=1
q=0
while(q!=n+1):
    if ins[q].startswith('PUSH'):
        s=ins[q]
        st.append(int(s[5:]))
        q+=1
    elif ins[q].startswith('STORE'):
        reg=st[-1]
        st.pop()
        q+=1
    elif ins[q].startswith('LOAD'):
        st.append(reg)
        q+=1
    elif ins[q].startswith('PLUS'):
        if st:
            m=st[-1]
            st.pop()
        
        if st:
            g=st[-1]
            st.pop()
            st.append(m+g)
        q+=1
    elif ins[q].startswith('TIMES'):
        if st:
            m=st[-1]
            st.pop()
        
        if st:
            g=st[-1]
            st.pop()
            st.append(m*g)
        q+=1
    elif ins[q].startswith('IFZERO'):
        if st[-1]!=0:
            st.pop()
            q+=1
        else:
            st.pop()
            s=ins[q]
            q=int(s[7:])
    else:

        print(st[-1])
        break

            
