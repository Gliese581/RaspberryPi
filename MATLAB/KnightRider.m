%%  Knightrider
%

gpio = 20:27;
for i = 1:10
    for j = 1:8
        writeDigitalPin(rpi, gpio(:,j), 0);
        pause(0.02);
        if j < 8
            writeDigitalPin(rpi, gpio(:,j+1), 0);
        end
        pause(0.02);
        writeDigitalPin(rpi, gpio(:,j), 1);
    end
    for j = 8:-1:1
        writeDigitalPin(rpi, gpio(:,j), 0);
        pause(0.02);
        if j > 1
            writeDigitalPin(rpi, gpio(:,j-1), 0);
        end
        pause(0.02);
        writeDigitalPin(rpi, gpio(:,j), 1);
    end
end