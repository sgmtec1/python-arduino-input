from pyfirmata import Arduino, util, OUTPUT

board=Arduino ('COM6')
board.digital[7].mode = OUTPUT

while True:
    estado = input('Digite 1 para ligar o LED ou 0 para desligar: ')
    board.digital[7].write(int(estado))