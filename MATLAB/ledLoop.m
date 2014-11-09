%%  Loop für die LED Anzeige des Raspberry Pi
for i = 9:-1:0
    ledAnzeige(rpi,num2str(i));
    pause(0.655);
    ledAnzeige(rpi,'clear');
end