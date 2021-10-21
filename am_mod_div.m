f0 = 100;
fc = 1000;
fs = 20000;
S0 = 1;

m1 = 1;
m2 = 0.5;
m3 = 0.25;

t = 0:1/fs:5*1/f0;
n = @(t) cos(2*pi*f0*t);

s1 = S0*(1 + m1*n(t)) .* cos(2*pi*fc.*t);
s2 = S0*(1 + m2*n(t)) .* cos(2*pi*fc.*t);
s3 = S0*(1 + m3*n(t)) .* cos(2*pi*fc.*t);

figure(1)
subplot(3, 1, 1)
plot(t, s1)
subplot(3, 1, 2)
plot(t, s2)
subplot(3, 1, 3)
plot(t, s3)

fft1 = abs(fft(s1))/length(s1);
fft2 = abs(fft(s2))/length(s2);
fft3 = abs(fft(s3))/length(s3);

fft1 = fftshift(fft1);
fft2 = fftshift(fft2);
fft3 = fftshift(fft3);

f = linspace(-fs/2, fs/2, length(fft1));

figure(2)
subplot(3, 1, 1);
plot(f, fft1)
subplot(3, 1, 2);
plot(f, fft2)
subplot(3, 1, 3);
plot(f, fft3)