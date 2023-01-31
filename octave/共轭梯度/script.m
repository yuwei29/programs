clear;
clc;
a=[3 -2;-2 2];
b=[2;0];
x=[0;0;];
[xt,yt]=cg(a,b,x);
disp(xt);
disp(yt);
