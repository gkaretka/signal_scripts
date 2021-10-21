%data = [ 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1 ];
data = [ 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0 ];
V = 1;          % amplitude
N = 100;        % repelem 4*N vzorkov na jednu zmenu
filter_on = 1;  % filter on = 1; filter off = 0

%% filter setup - todo set frequency according to real values
fc = 15;        % cutoff
fs = 1000;      % sample freq.
[b,a] = butter(6, fc/(fs/2)); %coef.

%dataOut = filter(b, a, dataIn);

%% data preparation
nrz_l_data = nrz_l(data, V);
nrz_m_data = nrz_m(data, V);
bipolar_rz_data = bipolar_rz(data, V); % 2 vzorky na bit
rz_ami_data = rz_ami(data, V); % 4 vzorky na bit
bi_phi_l_data = bi_phi_l(data, V); % 2 vzorky na bit
bi_phi_s_data = bi_phi_s(data, V); % 2 vzorky na bit
dicode_nrz_data = dicode_nrz(data, V);

% zarovnanie na 4 vzorky na bit pre vsetky kody

nrz_l_data = repelem(repelem(nrz_l_data, 4), N);
nrz_m_data = repelem(repelem(nrz_m_data, 4), N);
bipolar_rz_data = repelem(repelem(bipolar_rz_data, 2), N);
rz_ami_data = repelem(rz_ami_data, N);
bi_phi_l_data = repelem(repelem(bi_phi_l_data, 2), N);
bi_phi_s_data = repelem(repelem(bi_phi_s_data, 2), N);
dicode_nrz_data = repelem(repelem(dicode_nrz_data, 4), N);

if filter_on == 1
    nrz_l_data = filter(b, a, nrz_l_data);
    nrz_m_data = filter(b, a, nrz_m_data);
    bipolar_rz_data = filter(b, a, bipolar_rz_data);
    rz_ami_data = filter(b, a, rz_ami_data);
    bi_phi_l_data = filter(b, a, bi_phi_l_data);
    bi_phi_s_data = filter(b, a, bi_phi_s_data);
    dicode_nrz_data = filter(b, a, dicode_nrz_data);
end

% check if length is matched
fprintf("Lengths should match %d, %d, %d, %d, %d, %d, %d", ...
        length(nrz_l_data), length(nrz_m_data), length(bipolar_rz_data),...
        length(rz_ami_data), length(bi_phi_l_data), length(bi_phi_s_data),...
        length(dicode_nrz_data));

periods = linspace(0, length(data)/2, length(data)*4*N);

%% fig 1
figure(1);
subplot(4, 1, 1);
plot(periods, repelem(data, 4*N))
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("original data")

subplot(4, 1, 2);
plot(periods, nrz_l_data)
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("nrz-l")

subplot(4, 1, 3);
plot(periods, nrz_m_data)
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("nrz-m")

subplot(4, 1, 4);
plot(periods, bipolar_rz_data)
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("bipolar-rz")

%% fig 2
figure(2);
subplot(4, 1, 1);
plot(periods, repelem(data, 4*N))
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("original data")

subplot(4, 1, 2);
plot(periods, rz_ami_data)
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("rz-ami")

subplot(4, 1, 3);
plot(periods, bi_phi_l_data)
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("bi-phi-l")

subplot(4, 1, 4);
plot(periods, bi_phi_s_data)
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("bi-phi-s")

%% fig 3
figure(3);
subplot(2, 1, 1);
plot(periods, repelem(data, 4*N))
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("original data")

subplot(2, 1, 2);
plot(periods, dicode_nrz_data)
xticks(0:0.5:length(data)/2)
grid on
xlim([0 length(data)/2])
legend("dicode-nrz")

%% funkcie

function [y] = nrz_l(x, V)
    y = x - 0.5;
    y = y.*2';
    y = y.*V;
end

function [y] = nrz_m(x, V)
    y = zeros(1, length(x));
    y(1) = x(1);
    for index = 2:length(x)
        if x(index) == 1
            if y(index - 1) == 0
                y(index) = 1;
            else
                y(index) = 0;
            end
        else
            y(index) = y(index - 1);
        end
    end
    y = nrz_l(y, V);
end

function y = bipolar_rz(x, V)
    y = zeros(1, length(x)*2);
    for index = 1:2:length(x)*2
        y(index) = x((index-1)/2 + 1);
        y(index) = (y(index) - 0.5)*2*V;
    end
end

function y = rz_ami(x, V)
    y = zeros(1, 4*length(x));
    prev_peak = 0;
    for index = 1:length(x)
        if x(index) == 1
            if prev_peak == 0
                y((index - 1) * 4 + 2) = 1;
                y((index - 1) * 4 + 3) = 1;
                prev_peak = 1;
            else
                y((index - 1) * 4 + 2) = -1;
                y((index - 1) * 4 + 3) = -1;
                prev_peak = 0;
            end
        end
    end
    y = y.*V;
end

function y = bi_phi_l(x, V)
    y = zeros(1, 2*length(x));
    for index = 1:length(x)
        if x(index) == 1
            y((index - 1)*2 + 1) = 1;
            y((index - 1)*2 + 2) = -1;
        else
            y((index - 1)*2 + 1) = -1;
            y((index - 1)*2 + 2) = 1;
        end
    end
    y = y .* V;
end

function y = bi_phi_s(x, V)
    y = zeros(1, 2*length(x));
    if x(1) == 1
        y(1) = -1;
        y(2) = -1;
    else
        y(1) = -1;
        y(2) = 1;
    end
    for index = 2:length(x)
        if x(index) == 1
            y((index - 1)*2 + 1) = - y((index - 1)*2);
            y((index - 1)*2 + 2) = - y((index - 1)*2);
        else
            y((index - 1)*2 + 1) = - y((index - 1)*2);
            y((index - 1)*2 + 2) = y((index - 1)*2);
        end
    end
    y = y .* V;
end

function y = dicode_nrz(x, V)
    y = zeros(1, length(x));
    if x(1) == 1
        y(1) = -1;
    else
        y(1) = 1;
    end
    for index = 2:length(x)
        if x(index - 1) == x(index)
            y(index) = 0;
        else
            if x(index) == 1
                y(index) = -1;
            else
                y(index) = 1;
            end
        end
    end
    y = y .* V;
end