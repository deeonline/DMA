clear ; close all; clc

%% ==================== Part 1: Basic Function ====================
% Complete warmUpExercise.m 
fprintf('Running warmUpExercise ... \n');
fprintf('5x5 Identity Matrix: \n');
%warmUpExercise()

fprintf('Program paused. Press enter to continue.\n');
%pause;


%% ======================= Part 2: Plotting =======================
fprintf('Plotting Data ...\n')
data = csvread('gapminder.csv');
%X = data(:, 1); y = data(:, 2);
%m = length(y); % number of training examples

%%csvread is not able to account for strings in quotation. 
%% Eg. Korea, North
%% Therefore, all those rows are left shifted once

rows = [43, 44, 85, 101, 102, 114, 115, 127, 212];
data(rows,:) = [data(rows,[2:end]),zeros(length(rows),1)];

data(0==data) = nan;

co2emissions = data(:,6);
oilperperson = data(:,11);
relectric = data(:,13);
urbanrate = data(:,16);


% Plot Data
% Note: You have to complete the code in plotData.m
%plotData(co2emissions, urbanrate);

figure; % open a new figure window

%plot (round(urbanrate/10), round(relectric/1000) ,'rx', 'MarkerSize', 10);
xlabel ('Urbanrate(in %)');
ylabel('Oil/person');

%clear; close all; clc
plot(oilperperson,'rx');
%fprintf('Program paused. Press enter to continue.\n');
