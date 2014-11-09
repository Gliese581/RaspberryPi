%%  Raspberry und LCD-Display UC121902-TNARX-A
%   Pin 1 = 5V+
%   Pin 2 = GND
%   Pin 3 = CS      -> GPIO 10
%   Pin 4 = Clock   -> GPIO 11
%   Pin 5 = Data    -> GPIO 12
tic;
%%  Daten
data = [0 0 0 0 0 0 0 0 ... %1. Stelle (ganz rechts) c,x,d,b,g,a,e,f  x=nicht belegt/keine Auswirkung)
        1 0 0 1 0 0 0 0 ... %2. Stelle: 0 (als Beispiel)
        1 0 0 1 0 0 0 0 ... %3. Stelle: 1 
        1 0 0 1 0 0 0 0 ... %4. Stelle: 2 
        1 0 0 1 0 0 0 0 ... %5. Stelle: 3 
        1 0 0 1 0 0 0 0 ... %6. Stelle: 4
        0 0 0 0 1 ...       % Glocke,Schrägstich,MEM,CHAN,x 
        1 0 0 ...           % 1(DP),0(DQ),0(DR) - 1/2 duty, obere Segmente D54-D112 folgen)
              ...            %hier beginnt die obere Hälfte 
        1 0 0 1 0 0 0 0 ... %7. Stelle: 5 
        1 0 0 1 0 0 0 0 ... %8. Stelle: 6     
        1 0 0 1 0 0 0 0 ... %9. Stelle: 7  
        0 0 0 0 0 0 0 0 ... %10. Stelle: 8 
        0 0 0 0 0 0 0 0 ... %11. Stelle: 9 
        0 0 0 0 0 0 0 0 ... %12. Stelle: A 
        0 0 0 0 1 ...       % SEC,PROG,BAT(leer),BAT(voll),x
        0 0 1];             % x,x,1(DR) - Abschluss der oberen Segmente

%%  Senden
writeDigitalPin(rpi, 10, 1);            % setze CS auf 1
for i = 1:112
    writeDigitalPin(rpi, 11, 0);        % setze Clock auf 0
   % pause(0.2);                         % warte 0.4 Sekunden
    writeDigitalPin(rpi, 12, data(i));  % lade Datenbit
    writeDigitalPin(rpi, 11, 1);        % setze Clock auf 1 -> schreibe
    
    if (i == 56)
        writeDigitalPin(rpi, 10, 0);    % setze CS auf 0
       % pause(0.2)                        % 1 Sekunde warte
        writeDigitalPin(rpi, 10, 1);    % setze CS auf 1
    end
end
writeDigitalPin(rpi, 10, 0);            % setze CS auf 0
toc;