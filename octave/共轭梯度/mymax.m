%{
def f(x,a,b):
    e=0.001
    preg=1
    g=vsub(b,axmul(a,x))
    n=2
    d=g
    for i in range(n):
        if l2(g)<e:
            return x
        if i>0:
            beta= -vdot(g,g)/vdot(preg,preg)
            d=vsub(g,ax(beta,d))
        alpha = vdot(g,g)/vdot(d,axmul(a,d))
        x = vsub(x,ax(-alpha,d))
        preg = g
        g = vsub(g,ax(alpha,axmul(a,d)) )
    return x
%}

function max = mymax(n1, n2, n3, n4, n5)

    %This function calculates the maximum of the 
    
    % five numbers given as input
    
    max =  n1;
    
    if(n2 > max)
    
       max = n2;
    
    end
    
    if(n3 > max)
    
       max = n3;
    
    end
    
    if(n4 > max)
    
       max = n4;
    
    end
    
    if(n5 > max)
    
       max = n5;
    
    end
end
function  s = a(w,h)
    s = w*h;
    disp(['area=',num2str(s)]);
end
a(2,3)
function b(x)
    disp(x)
    disp(x+3)
    disp(x+10)
    disp(x*10)
end
b(2)
b(5)
function s = h(x,y)
    disp(x+y)
    s = x*x+y*y-2*x*y 
end
h(2,5)
h(7,2)
s=mymax(5,6,7,3,2)
