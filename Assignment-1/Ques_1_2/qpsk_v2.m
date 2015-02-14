% Manoj Gulati
% PhD-1327
% Wireless System Implementation
% Task-1_2: Generate QPSK modulated wave with randomly generated input
% binary sequence

close all;
clear all;

b_seq=0;
t=0;
% Required no. of binary numbers
n=20;
% generate 100 binary numbers
b_seq = round(rand(1,n));

% Cnverting unipolar to Bi-polar
bi_b_seq = 2*b_seq-1;

% Data sequence samples
% reshape to make pairs of 2
b_seq_res = reshape(bi_b_seq,2,n/2);

% Bit duration in sec
T=1; 
% This will result in unit amplitude waveforms
Eb=T/2; 
% Carrier frequency
fc=3/T; 

% discrete time sequence between 0 and n*T (100 samples)
% 100 samples per bit
t=linspace(0,1,100);
% carrier waveform
w1=sqrt(2*Eb/T)*(cos(2*pi*fc*t)); 
w2=sqrt(2*Eb/T)*(sin(2*pi*fc*t)); 

in_phase=[]
iq_phase=[]
qpsk_res=[]

for i=1:n/2
    % Generating in phase component by multiplying with cos(wc*t)
    i_phase = b_seq_res(1,i)*w1;
    % Generating out of phase component by multiplying with cos(wc*t)
    q_phase = b_seq_res(2,i)*w2;
    % concatenating in phase values
    in_phase = [in_phase i_phase]
    % concatenating out of phase values
    iq_phase = [iq_phase q_phase]
    % concatenating qpsk values
    qpsk_res = [qpsk_res i_phase+q_phase]
    
end

subplot(3,1,1);
plot(in_phase,'b-');
grid on;
title('Inphase Component');
xlabel('Time');
ylabel('Amplitude');
%
subplot(3,1,2);
plot(iq_phase,'r-');
grid on;
title('Quadrature Component');
xlabel('Time');
ylabel('Amplitude');
%
subplot(3,1,3);
plot(qpsk_res,'b');
grid on;
title('QPSK modulated Signal');
xlabel('Time');
ylabel('Amplitude');
%%
% plottting input binary sequence after pairing
subplot(2,1,1);
plot(b_seq_res(1,:),'b-');
grid on;
title('Input bit seq. in-phase');
xlabel('Time');
ylabel('Amplitude');
axis([1 5 -2 2])
%
subplot(2,1,2);
plot(b_seq_res(2,:),'r-');
grid on;
title('Input bit seq. out-phase');
xlabel('Time');
ylabel('Amplitude');
axis([1 5 -2 2])
%%

scatter(b_seq_res(1,:),b_seq_res(2,:),'r*');
grid on;
axis([-2 2 -2 2]);
title('QPSK Constellation Diagram');
