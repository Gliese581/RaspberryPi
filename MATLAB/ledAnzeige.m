function [led_Message] = ledAnzeige(pi_name,data)
%%  LED-Anzeige 7 Segmente + Punkt
%   Ansteuerung des Raspberry Pi B+
%   Funktion lieﬂt einen String
%   folgende Werte werden akzeptiert

cmd_list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'help', 'clear'};

if (isempty(data))
    error('String is empty');
end
if (exist('pi_name') == 0)
    error('Please connect to your Raspberry Pi');
end
if (any(strcmp(data,cmd_list)) == 1)
    switch data
        case 'help'
            disp('ledAnzeige(<PiName>,<String>) Strings are: 0 - 9, clear and help');
        case 'clear'
            writeDigitalPin(pi_name, 20, 1);
            writeDigitalPin(pi_name, 21, 1);
            writeDigitalPin(pi_name, 22, 1);
            writeDigitalPin(pi_name, 23, 1);
            writeDigitalPin(pi_name, 24, 1);
            writeDigitalPin(pi_name, 25, 1);
            writeDigitalPin(pi_name, 26, 1);
            writeDigitalPin(pi_name, 27, 1);
        case '0'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 23, 0);
            writeDigitalPin(pi_name, 24, 0);
            writeDigitalPin(pi_name, 25, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '1'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '2'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 22, 0);
            writeDigitalPin(pi_name, 24, 0);
            writeDigitalPin(pi_name, 25, 0);
        case '3'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 22, 0);
            writeDigitalPin(pi_name, 25, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '4'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 22, 0);
            writeDigitalPin(pi_name, 23, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '5'
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 22, 0);
            writeDigitalPin(pi_name, 23, 0);
            writeDigitalPin(pi_name, 25, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '6'
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 22, 0);
            writeDigitalPin(pi_name, 23, 0);
            writeDigitalPin(pi_name, 24, 0);
            writeDigitalPin(pi_name, 25, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '7'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '8'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 22, 0);
            writeDigitalPin(pi_name, 23, 0);
            writeDigitalPin(pi_name, 24, 0);
            writeDigitalPin(pi_name, 25, 0);
            writeDigitalPin(pi_name, 26, 0);
        case '9'
            writeDigitalPin(pi_name, 20, 0);
            writeDigitalPin(pi_name, 21, 0);
            writeDigitalPin(pi_name, 22, 0);
            writeDigitalPin(pi_name, 23, 0);
            writeDigitalPin(pi_name, 25, 0);
            writeDigitalPin(pi_name, 26, 0);
    end
end