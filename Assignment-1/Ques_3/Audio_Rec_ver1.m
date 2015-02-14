% Manoj Gulati
% PhD-1327
% Wireless System Implementation
% Task-3: Record and playbcak audio + Option to save raw data
% Reference: https://nf.nci.org.au/facilities/software/Matlab/techdoc/ref/audiorecorder.html

clear all;
close all; 

display('Define a recorder object');
recObj = audiorecorder(48000,16,1,0);

disp('Start speaking.')
recordblocking(recObj, 10);
disp('End of Recording.');

%%

display('Playback the recorded object');
play(recObj);

%%

y = getaudiodata(recObj);
% plot recorded frame in time domain
plot(1:1:length(y),y);

% Dump recorded file in float format
csvwrite('Test1.csv',y);
%%

% Plot spectrogram of recorded voice
y = getaudiodata(recObj);
spectrogram(y, ones(1, 512),127,512, 8192, 'yaxis')

