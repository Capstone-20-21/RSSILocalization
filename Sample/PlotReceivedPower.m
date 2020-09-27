% 
% (c) 2019 Takahiro Hashimoto
% 

% pkg load signal;
% pkg load optim;

fname = './ReceivedPowers.csv';
data = csvread(fname, 1, 0);

figure(1);
plot3(data(:,1), data(:,2), data(:,4));

x = data(:,1);
y = data(:,2);
power = data(:,4);
xv = linspace(min(x), max(x), 101);
yv = linspace(min(y), max(y), 7);
[X,Y] = meshgrid(xv, yv);
power = griddata(x,y,power,X,Y);

figure(2);
surf(X, Y, power);

% pbaspect([3 1]);
grid on;
xlabel('Distance between Tx-Rx [m]');
ylabel('Received Power [dB]');
