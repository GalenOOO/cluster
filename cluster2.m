
load('julei2.txt');
x = julei2;
[RD,CD,order] = optics(x,60);
savetxt('RD60.txt',RD');
savetxt('order60.txt',order');

