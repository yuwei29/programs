function y=f1(x)
    t=x+3;
    y=f3(t);
end

function y=f2(x)
    y=-x;
end

function y=f3(x)
    x=2*x;
    y=f2(x);
end

% f1(7) = f3(10) = f2(20) = -20 