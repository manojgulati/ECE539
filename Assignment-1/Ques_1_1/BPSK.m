% Manoj Gulati
% PhD-1327
% Wireless System Implementation
% Task-1_1: Generate BPSK modulated wave with randomly generated input
% binary sequence

close all;
clear all;

b_seq=0;
% Required no. of binary numbers
n=10;
% generate 100 binary numbers
b_seq=round(rand(1,n));
% Making the seq. bilateral from unitlateral
b=2*b_seq-1;

% Bit duration in sec
T=1; 
% This will result in unit amplitude waveforms
Eb=T/2; 
% Carrier frequency
fc=3/T; 
% discrete time sequence between 0 and n*T (1000 samples)
t=linspace(0,n,1000);
% Number of time samples
N=length(t); 
% Number of samples per bit
Nsb=N/length(b_seq); 

% Replicate and tile each bit Nsb times
dd=repmat(b_seq',1,Nsb); 
bb=repmat(b',1,Nsb); 
% Transpose the replicated matrix
dw=dd'; 
bw=bb';
% Convert dw to a column vector (colum by column) and convert to a row vector
dw=dw(:)'; 
bw=bw(:)'; 
% Data sequence samples
w=sqrt(2*Eb/T)*(cos(2*pi*fc*t)); % carrier waveform
bpsk_w=bw.*w; % modulated waveform

% plot for actual bit stream, bipolar bit stream, carrier waveform and BPSK
% modulated wave

subplot(4,1,1);
plot(t,dw,'r--');
axis([0 n -1.5 1.5]);
title('Input Bit Stream');

subplot(4,1,2);
plot(t,bw,'b-'); 
axis([0 n -1.5 1.5]);
title('Bipolar Bit Stream');

subplot(4,1,3);
plot(t,w,'r'); 
axis([0 n -1.5 1.5]);
title('Carrier Waveform');

subplot(4,1,4);
plot(t,bpsk_w,'.'); 
axis([0 n -1.5 1.5]);
title('BPSK Modulated Wave');
xlabel('time')

%% Generate BPSK Modulated wave using pskmod function

% Using Input binary sequence generated previously i.e. b_seq

Bpsk_mod = pskmod(b_seq,2);

% Plot constellation scatter plot

plot(real(Bpsk_mod),imag(Bpsk_mod),'b*');
axis([-1.5 1.5 -1.5 1.5]);
xlabel('Inphase');
ylabel('Quadrature');
title('Scatterplot');
grid on;







