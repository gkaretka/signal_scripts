f0 = 100;
fc = 1000;
fs = 20000;

t = 0:1/fs:5*1/f0;
s1 = cos(2*pi*f0.*t);
s2 = zeros(1, length(t));

for i = 1: length(t)
    if s1(i) >= 0
        s2(i) = 1;
    else
        s2(i) = 0;
    end
end


sc = cos(2*pi*fc.*t);

sm1 = s1 .* sc;
sm2 = s2 .* sc;

figure (1);
subplot(4, 1, 1);
plot(t, s1);
subplot(4, 1, 2);
plot(t, sc);
subplot(4, 1, 3);
plot(t, sm1);
subplot(4, 1, 4);
plot(t, sm2);