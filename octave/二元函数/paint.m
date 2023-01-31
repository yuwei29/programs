function paint
  x=-1:0.01:1;
  y=-1:0.01:1;
  [X,Y]=meshgrid(x,y);
  Z = f(X,Y);
  mesh(X,Y,Z);
end

function z = f(x,y)
   z=cos(2*pi*x).*cos(2*pi*y).*exp(-(x.*x+y.*y)/10);
end


