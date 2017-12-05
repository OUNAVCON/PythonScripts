close;
clear;
clc;

R0 = 10000;
T0 = 25+273;
beta = 3435;
R_lower = 10e3; //+/- 5%
Vs = 3.3;
ADC_RES = 2^12;

T_MIN = -15;
T_MAX = 100;
NUM_POINTS = 16;
T_Delta = (T_MAX-T_MIN)/NUM_POINTS;
disp(T_Delta)

t = T_MIN:T_Delta:T_MAX

for i = 1:length(t)
    T=t(i)+273;
    R(i) = R0 * exp(-beta * (1/T0 - 1/T));
    Vout(i) = (ADC_RES*R_lower)/(R(i) + R_lower);
end

subplot(2,1,1);
plot(t,R);
subplot(2,1,2);
plot(t,Vout, '-*')

data = [];
for i = 1:length(Vout)-1
    m(i) = (t(i+1) - t(i))/(Vout(i+1)-Vout(i))
    y0(i) = t(i)
    data($+1,:) = [int(Vout(i)), m(i), -y0(i)];
end

disp(data)

adc = 3030;
point = 10;
m = data(point,2);
x0 = data(point,1);
y0 = data(point,3);

Tout = (adc-x0)*m - y0
disp(Tout)

