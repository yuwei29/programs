function [x,y] = cg(a,b,x)
    x1s=[x(1)];
    x2s=[x(2)];
    y=f(a,b,x);
    ys=[y];
    preg=1;
    g=b-a*x;
    e=0.001;
    n=2;
    d=g;
    for i=1:n
        if norm(g,2)<e
            paint(x1s,x2s,ys,i);
            return
        end
        if i>1
            beta=g'*g/(preg'*preg);
            d=g+beta*d;
        end
        alpha=g'*g/(d'*a*d);
        x=x+alpha*d;
        y=f(a,b,x);
        x1s(end+1)=x(1);
        x2s(end+1)=x(2);
        ys(end+1)=y;
        preg=g;
        g=g-alpha*a*d;
    end
    paint(x1s,x2s,ys,n+1);
end

function y = f(a,b,x)
    y=0.5*x'*a*x-x'*b;
end

function paint(x1s,x2s,ys,i)
    base=1:i;
    figure(1);
    plot(base,ys);
    figure(2);
    plot(x1s,x2s);
    hold on;
    x1 = -0.5:0.01:4.5;
    x2 = -0.5:0.01:4.5;
    [X1,X2]=meshgrid(x1,x2);
    Y = 1.5*X1.*X1-2*X1.*X2+X2.*X2-2*X1;
    v = -1.8:0.3:0.3;
    contour(X1,X2,Y,v);
    hold off;
end
