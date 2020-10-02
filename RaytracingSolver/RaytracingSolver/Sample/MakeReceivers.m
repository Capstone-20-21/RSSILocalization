% 
% (c) 2019 Takahiro Hashimoto
% 

p0 = [1;  1; 1.5];
p1 = [50; 1; 1.5];
nx = 99;

filename = 'ReceiverPositions.dat';
fid = fopen(filename, 'w');

fprintf(fid, 'receiver positions\n')
fprintf(fid, '%d\n', nx);
for i=1:nx
	pos = p0 + (p1-p0)/(nx-1)*(i-1);
	fprintf(fid, ' %d %d %d\n', pos(1), pos(2), pos(3));
end
fclose(fid);