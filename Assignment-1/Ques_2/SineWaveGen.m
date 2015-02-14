% Manoj Gulati
% PhD-1327
% Wireless System Implementation
% Task-2: Generate Sine Wave with User Defined Input

clear all;
close all;

prompt = 'Enter the frequency of sine wave?';
f = input(prompt);

prompt = 'Enter the phase of sine wave?';
phase = input(prompt);

prompt = 'Enter the amplitude of sine wave?';
amp = input(prompt);

prompt = 'Enter the number of samples to be visualized for sine wave?';
N = input(prompt);

% No of samples to be visualized
t=[1:1:N];
% Sampling frequency
fs=f*20;

% plot for visualization of generated sine wave
plot(amp*sin(2*pi*f/fs*t+phase),'b-*');
ylabel(strcat('Amplitude = ',int2str(max(t))))
xlabel(strcat('No. of samples is ', int2str(max(t)),'  (fs=',int2str(fs),'Hz)'));
legend(strcat('SineWave Freq = ',int2str(max(f)),' Phase = ',int2str(max(phase))));