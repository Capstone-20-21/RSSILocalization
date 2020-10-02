% 
% (c) 2019 Takahiro Hashimoto
% 

% pkg load signal;
% pkg load optim;

fname = './ReceivedPowers.csv';
data = csvread(fname, 1, 0);

figure();
plot(data(:,1), data(:,4));
% pbaspect([3 1]);
grid on;
xlabel('Distance between Tx-Rx [m]');
ylabel('Received Power [dB]');
