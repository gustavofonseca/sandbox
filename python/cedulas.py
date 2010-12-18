#coding: utf-8

valor = int(input("Digite o valor a pagar:"))
cedulas = 0
cedula_atual = 50
a_pagar = valor

#iterar sobre os tipos de cédulas e verificar se é suficiente para saldar a dívida.
while True:
    if cedula_atual <= a_pagar:
        a_pagar -= cedula_atual
        cedulas += 1
    else:
        if cedulas: print("%d cédula(s) de R$%d" % (cedulas, cedula_atual))
        
        if a_pagar == 0:
            break
            
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual =5
        elif cedula_atual == 5:
            cedula_atual = 1
            
        cedulas = 0
            