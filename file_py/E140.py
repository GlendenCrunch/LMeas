# -*- coding: utf-8 -*-
_th440 = Reset()
if self.cvar1.get() or self.cvar3.get() or self.cvar4.get() == 1:
    _th502 = Message('Подключите провода к калибратору для измерения напряжения')
if self.cvar1.get() == 1:
    # dc 10V
    _th140 = Message('Подключите провода к калибратору для измерения напряжения')           
    _th140 = Callpar(20.0, '0000')
    _th140 = Call('dc', 10.0, 9.9, 'OUT 9.9 V', 'b01', 'c01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, 2.0, 'OUT 2.0 V', 'd01', 'e01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, 0.4, 'OUT 0.4 V', 'f01', 'g01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, 0.08, 'OUT 0.08 V', 'h01', 'i01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, 0.02, 'OUT 0.02 V', 'j01', 'k01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, -0.02, 'OUT -0.02 V', 'l01', 'm01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, -0.08, 'OUT -0.08 V', 'n01', 'o01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, -0.4, 'OUT -0.4 V', 'p01', 'q01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, -2.0, 'OUT -2.0 V', 'r01', 's01', 'A65', 0.05)
    _th140 = Call('dc', 10.0, -9.9, 'OUT -9.9 V', 't01', 'u01', 'A65', 0.05)
    # dc 2.5V
    _th140 = Callpar(20.0, '0000')
    _th140 = Call('dc', 2.5, 2.5, 'OUT 2.5 V', 'b17', 'c17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, 0.5, 'OUT 0.5 V', 'd17', 'e17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, 0.1, 'OUT 0.1 V', 'f17', 'g17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, 0.02, 'OUT 0.02 V', 'h17', 'i17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, 0.005, 'OUT 0.005 V', 'j17', 'k17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, -0.005, 'OUT -0.005 V', 'l17', 'm17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, -0.02, 'OUT -0.02 V', 'n17', 'o17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, -0.1, 'OUT -0.1 V', 'p17', 'q17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, -0.5, 'OUT -0.5 V', 'r17', 's17', 'A65', 0.05)
    _th140 = Call('dc', 2.5, -2.5, 'OUT -2.5 V', 't17', 'u17', 'A65', 0.05)
    # dc 0.625V
    _th140 = Callpar(20.0, '0000')
    _th140 = Call('dc', 0.625, 0.6, 'OUT 0.6 V', 'b33', 'c33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, 0.2, 'OUT 0.2 V', 'd33', 'e33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, 0.05, 'OUT 0.05 V', 'f33', 'g33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, 0.01, 'OUT 0.01 V', 'h33', 'i33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, 0.002, 'OUT 0.002 V', 'j33', 'k33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, -0.002, 'OUT -0.002 V', 'l33', 'm33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, -0.01, 'OUT -0.05 V', 'n33', 'o33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, -0.05, 'OUT -0.05 V', 'p33', 'q33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, -0.2, 'OUT -0.2 V', 'r33', 's33', 'A65', 0.1)
    _th140 = Call('dc', 0.625, -0.6, 'OUT -0.6 V', 't33', 'u33', 'A65', 0.1)
    # dc 0.1562V
    _th140 = Callpar(20.0, '0000')
    _th140 = Call('dc', 0.1562, 0.150, 'OUT 0.150 V', 'b49', 'c49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, 0.08, 'OUT 0.08 V', 'd49', 'e49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, 0.02, 'OUT 0.02 V', 'f49', 'g49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, 0.005, 'OUT 0.005 V', 'h49', 'i49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, 0.001, 'OUT 0.001 V', 'j49', 'k49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, -0.001, 'OUT -0.001 V', 'l49', 'm49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, -0.005, 'OUT -0.005 V', 'n49', 'o49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, -0.02, 'OUT -0.02 V', 'p49', 'q49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, -0.08, 'OUT -0.08 V', 'r49', 's49', 'A65', 0.5)
    _th140 = Call('dc', 0.1562, -0.150, 'OUT -0.150 V', 't49', 'u49', 'A65', 0.5)            
# ac0
if self.cvar3.get() == 1:
    # 20kHz 10B --------------------------------------------------------------------
    _th140 = Callpar(20.0, '0000')
    _th140 = Call('ac0', 10.0, 0.35, 'OUT 0.35 V, 0.1 kHz', 'd65', 'e65', '', 0.15)
    _th140 = Call('ac0', 10.0, 0.35, 'OUT 0.35 V, 9.0 kHz', 'd66', 'e66', '', 0.15)
    _th140 = Call('ac0', 10.0, 1.4, 'OUT 1.4 V, 0.1 kHz', 'f65', 'g65', '', 0.15)
    _th140 = Call('ac0', 10.0, 1.4, 'OUT 1.4 V, 9.0 kHz', 'f66', 'g66', '', 0.15)
    _th140 = Call('ac0', 10.0, 2.8, 'OUT 2.8 V, 0.1 kHz', 'h65', 'i65', '', 0.15)
    _th140 = Call('ac0', 10.0, 2.8, 'OUT 2.8 V, 9.0 kHz', 'h66', 'i66', '', 0.15)
    _th140 = Call('ac0', 10.0, 4.9, 'OUT 4.9 V, 0.1 kHz', 'j65', 'k65', '', 0.15)
    _th140 = Call('ac0', 10.0, 4.9, 'OUT 4.9 V, 9.0 kHz', 'j66', 'k66', '', 0.15)
    _th140 = Call('ac0', 10.0, 6.7, 'OUT 6.7 V, 0.1 kHz', 'l65', 'm65', '', 0.15)
    _th140 = Call('ac0', 10.0, 6.7, 'OUT 6.7 V, 9.0 kHz', 'l66', 'm66', '', 0.15)
    # 20kHz 2.5B
    _th140 = Callpar(20.0, '0100')
    _th140 = Call('ac0', 2.5, 0.085, 'OUT 0.085 V, 0.1 kHz', 'n65', 'o65', '', 0.15)
    _th140 = Call('ac0', 2.5, 0.085, 'OUT 0.085 V, 9.0 kHz', 'n66', 'o66', '', 0.15)
    _th140 = Call('ac0', 2.5, 0.35, 'OUT 0.35 V, 0.1 kHz', 'p65', 'q65', '', 0.15)
    _th140 = Call('ac0', 2.5, 0.35, 'OUT 0.35 V, 9.0 kHz', 'p66', 'q66', '', 0.15)
    _th140 = Call('ac0', 2.5, 0.7, 'OUT 0.7 V, 0.1 kHz', 'r65', 's65', '', 0.15)
    _th140 = Call('ac0', 2.5, 0.7, 'OUT 0.7 V, 9.0 kHz', 'r66', 's66', '', 0.15)
    _th140 = Call('ac0', 2.5, 1.2, 'OUT 1.2 V, 0.1 kHz', 't65', 'u65', '', 0.15)
    _th140 = Call('ac0', 2.5, 1.2, 'OUT 1.2 V, 9.0 kHz', 't66', 'u66', '', 0.15)
    _th140 = Call('ac0', 2.5, 1.6, 'OUT 1.6 V, 0.1 kHz', 'v65', 'w65', '', 0.15)
    _th140 = Call('ac0', 2.5, 1.6, 'OUT 1.6 V, 9.0 kHz', 'v66', 'w66', '', 0.15)
    # 20kHz 0.625B
    _thread = Callpar(20.0, '1000')
    _th140 = Call('ac0', 0.625, 0.02, 'OUT 0.02 V, 0.1 kHz', 'd71', 'e71', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.02, 'OUT 0.02 V, 9.0 kHz', 'd72', 'e72', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.085, 'OUT 0.085 V, 0.1 kHz', 'f71', 'g71', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.085, 'OUT 0.085 V, 9.0 kHz', 'f72', 'g72', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.17, 'OUT 0.17 V, 0.1 kHz', 'h71', 'i71', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.17, 'OUT 0.17 V, 9.0 kHz', 'h72', 'i72', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.29, 'OUT 0.29 V, 0.1 kHz', 'j71', 'k71', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.29, 'OUT 0.29 V, 9.0 kHz', 'j72', 'k72', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.4, 'OUT 0.4 V, 0.1 kHz', 'l71', 'm71', '', 0.15)
    _th140 = Call('ac0', 0.625, 0.4, 'OUT 0.4 V, 9.0 kHz', 'l72', 'm72', '', 0.15)
    # 20kHz 0.1562B
    _th140 = Callpar(20.0, '1100')
    #_th140 = Call('ac0', 0.1562, 0.001, 'OUT 0.001 V, 0.1 kHz', 'n71', 'o71', '', 0.5)
    #_th140 = Call('ac0', 0.1562, 0.001, 'OUT 0.001 V, 9.0 kHz', 'n72', 'o72', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.005, 'OUT 0.005 V, 0.1 kHz', 'p71', 'q71', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.005, 'OUT 0.005 V, 9.0 kHz', 'p72', 'q72', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.022, 'OUT 0.022 V, 0.1 kHz', 'r71', 's71', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.022, 'OUT 0.022 V, 9.0 kHz', 'r72', 's72', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.045, 'OUT 0.045 V, 0.1 kHz', 't71', 'u71', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.045, 'OUT 0.045 V, 9.0 kHz', 't72', 'u72', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.07, 'OUT 0.07 V, 0.1 kHz', 'v71', 'w71', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.07, 'OUT 0.07 V, 9.0 kHz', 'v72', 'w72', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.1, 'OUT 0.1 V, 0.1 kHz', 'x71', 'y71', '', 0.5)
    _th140 = Call('ac0', 0.1562, 0.1, 'OUT 0.1 V, 9.0 kHz', 'x72', 'y72', '', 0.5)
    # 100kHz 10B ---------------------------------------------------------------------
    _th140 = Callpar(100.0, '0000')
    _th140 = Call('ac0', 10.0, 0.35, 'OUT 0.35 V, 1.0 kHz', 'd67', 'e67', '', 1.0)
    _th140 = Call('ac0', 10.0, 0.35, 'OUT 0.35 V, 49.0 kHz', 'd68', 'e68', '', 1.0)
    _th140 = Call('ac0', 10.0, 1.4, 'OUT 1.4 V, 1.0 kHz', 'f67', 'g67', '', 1.0)
    _th140 = Call('ac0', 10.0, 1.4, 'OUT 1.4 V, 49.0 kHz', 'f68', 'g68', '', 1.0)
    _th140 = Call('ac0', 10.0, 2.8, 'OUT 2.8 V, 1.0 kHz', 'h67', 'i67', '', 1.0)
    _th140 = Call('ac0', 10.0, 2.8, 'OUT 2.8 V, 49.0 kHz', 'h68', 'i68', '', 1.0)
    _th140 = Call('ac0', 10.0, 4.9, 'OUT 4.9 V, 1.0 kHz', 'j67', 'k67', '', 1.0)
    _th140 = Call('ac0', 10.0, 4.9, 'OUT 4.9 V, 49.0 kHz', 'j68', 'k68', '', 1.0)
    _th140 = Call('ac0', 10.0, 6.7, 'OUT 6.7 V, 1.0 kHz', 'l67', 'm67', '', 1.0)
    _th140 = Call('ac0', 10.0, 6.7, 'OUT 6.7 V, 49.0 kHz', 'l68', 'm68', '', 1.0)
    # 100kHz 2.5B
    _th140 = Callpar(100.0, '0100')
    _th140 = Call('ac0', 2.5, 0.085, 'OUT 0.085 V, 1.0 kHz', 'n67', 'o67', '', 1.0)
    _th140 = Call('ac0', 2.5, 0.085, 'OUT 0.085 V, 49.0 kHz', 'n68', 'o68', '', 1.0)
    _th140 = Call('ac0', 2.5, 0.35, 'OUT 0.35 V, 1.0 kHz', 'p67', 'q67', '', 1.0)
    _th140 = Call('ac0', 2.5, 0.35, 'OUT 0.35 V, 49.0 kHz', 'p68', 'q68', '', 1.0)
    _th140 = Call('ac0', 2.5, 0.7, 'OUT 0.7 V, 1.0 kHz', 'r67', 's67', '', 1.0)
    _th140 = Call('ac0', 2.5, 0.7, 'OUT 0.7 V, 49.0 kHz', 'r68', 's68', '', 1.0)
    _th140 = Call('ac0', 2.5, 1.2, 'OUT 1.2 V, 1.0 kHz', 't67', 'u67', '', 1.0)
    _th140 = Call('ac0', 2.5, 1.2, 'OUT 1.2 V, 49.0 kHz', 't68', 'u68', '', 1.0)
    _th140 = Call('ac0', 2.5, 1.6, 'OUT 1.6 V, 1.0 kHz', 'v67', 'w67', '', 1.0)
    _th140 = Call('ac0', 2.5, 1.6, 'OUT 1.6 V, 49.0 kHz', 'v68', 'w68', '', 1.0)
    # 100kHz 0.625B
    _th140 = Callpar(100.0, '1000')
    _th140 = Call('ac0', 0.625, 0.02, 'OUT 0.02 V, 1.0 kHz', 'd73', 'e73', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.02, 'OUT 0.02 V, 49.0 kHz', 'd74', 'e74', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.085, 'OUT 0.085 V, 1.0 kHz', 'f73', 'g73', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.085, 'OUT 0.085 V, 49.0 kHz', 'f74', 'g74', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.17, 'OUT 0.17 V, 1.0 kHz', 'h73', 'i73', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.17, 'OUT 0.17 V, 49.0 kHz', 'h74', 'i74', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.29, 'OUT 0.29 V, 1.0 kHz', 'j73', 'k73', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.29, 'OUT 0.29 V, 49.0 kHz', 'j74', 'k74', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.4, 'OUT 0.4 V, 1.0 kHz', 'l73', 'm73', '', 1.0)
    _th140 = Call('ac0', 0.625, 0.4, 'OUT 0.4 V, 49.0 kHz', 'l74', 'm74', '', 1.0)
    # 100kHz 0.1562B
    _th140 = Callpar(100.0, '1100')
    #_th140 = Call('ac0', 0.1562, 0.001, 'OUT 0.001 V, 1.0 kHz', 'n73', 'o73', '', 10.0)
    #_th140 = Call('ac0', 0.1562, 0.001, 'OUT 0.001 V, 49.0 kHz', 'n74', 'o74', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.005, 'OUT 0.005 V, 1.0 kHz', 'p73', 'q73', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.005, 'OUT 0.005 V, 49.0 kHz', 'p74', 'q74', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.022, 'OUT 0.022 V, 1.0 kHz', 'r73', 's73', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.022, 'OUT 0.022 V, 49.0 kHz', 'r74', 's74', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.045, 'OUT 0.045 V, 1.0 kHz', 't73', 'u73', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.045, 'OUT 0.045 V, 49.0 kHz', 't74', 'u74', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.07, 'OUT 0.07 V, 1.0 kHz', 'v73', 'w73', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.07, 'OUT 0.07 V, 49.0 kHz', 'v74', 'w74', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.1, 'OUT 0.1 V, 1.0 kHz', 'x73', 'y73', '', 10.0)
    _th140 = Call('ac0', 0.1562, 0.1, 'OUT 0.1 V, 49.0 kHz', 'x74', 'y74', '', 10.0)
    # 200kHz 10B --------------------------------------------------------------------
    _th140 = Callpar(200.0, '0000')
    _th140 = Call('ac0', 10.0, 0.35, 'OUT 0.35 V, 1.0 kHz', 'd69', 'e69', '', 3.0)
    _th140 = Call('ac0', 10.0, 0.35, 'OUT 0.35 V, 99.0 kHz', 'd70', 'e70', '', 3.0)
    _th140 = Call('ac0', 10.0, 1.4, 'OUT 1.4 V, 1.0 kHz', 'f69', 'g69', '', 3.0)
    _th140 = Call('ac0', 10.0, 1.4, 'OUT 1.4 V, 99.0 kHz', 'f70', 'g70', '', 3.0)
    _th140 = Call('ac0', 10.0, 2.8, 'OUT 2.8 V, 1.0 kHz', 'h69', 'i69', '', 3.0)
    _th140 = Call('ac0', 10.0, 2.8, 'OUT 2.8 V, 99.0 kHz', 'h70', 'i70', '', 3.0)
    _th140 = Call('ac0', 10.0, 4.9, 'OUT 4.9 V, 1.0 kHz', 'j69', 'k69', '', 3.0)
    _th140 = Call('ac0', 10.0, 4.9, 'OUT 4.9 V, 99.0 kHz', 'j70', 'k70', '', 3.0)
    _th140 = Call('ac0', 10.0, 6.7, 'OUT 6.7 V, 1.0 kHz', 'l69', 'm69', '', 3.0)
    _th140 = Call('ac0', 10.0, 6.7, 'OUT 6.7 V, 99.0 kHz', 'l70', 'm70', '', 3.0)
    # 200kHz 2.5B
    _th140 = Callpar(200.0, '0100')
    _th140 = Call('ac0', 2.5, 0.085, 'OUT 0.085 V, 1.0 kHz', 'n69', 'o69', '', 3.0)
    _th140 = Call('ac0', 2.5, 0.085, 'OUT 0.085 V, 99.0 kHz', 'n70', 'o70', '', 3.0)
    _th140 = Call('ac0', 2.5, 0.35, 'OUT 0.35 V, 1.0 kHz', 'p69', 'q69', '', 3.0)
    _th140 = Call('ac0', 2.5, 0.35, 'OUT 0.35 V, 99.0 kHz', 'p70', 'q70', '', 3.0)
    _th140 = Call('ac0', 2.5, 0.7, 'OUT 0.7 V, 1.0 kHz', 'r69', 's69', '', 3.0)
    _th140 = Call('ac0', 2.5, 0.7, 'OUT 0.7 V, 99.0 kHz', 'r70', 's70', '', 3.0)
    _th140 = Call('ac0', 2.5, 1.2, 'OUT 1.2 V, 1.0 kHz', 't69', 'u69', '', 3.0)
    _th140 = Call('ac0', 2.5, 1.2, 'OUT 1.2 V, 99.0 kHz', 't70', 'u70', '', 3.0)
    _th140 = Call('ac0', 2.5, 1.6, 'OUT 1.6 V, 1.0 kHz', 'v69', 'w69', '', 3.0)
    _th140 = Call('ac0', 2.5, 1.6, 'OUT 1.6 V, 99.0 kHz', 'v70', 'w70', '', 3.0)
    # 200kHz 0.625B
    _th140 = Callpar(200.0, '1000')
    _th140 = Call('ac0', 0.625, 0.02, 'OUT 0.02 V, 1.0 kHz', 'd75', 'e75', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.02, 'OUT 0.02 V, 99.0 kHz', 'd76', 'e76', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.085, 'OUT 0.085 V, 1.0 kHz', 'f75', 'g75', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.085, 'OUT 0.085 V, 99.0 kHz', 'f76', 'g76', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.17, 'OUT 0.17 V, 1.0 kHz', 'h75', 'i75', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.17, 'OUT 0.17 V, 99.0 kHz', 'h76', 'i76', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.29, 'OUT 0.29 V, 1.0 kHz', 'j75', 'k75', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.29, 'OUT 0.29 V, 99.0 kHz', 'j76', 'k76', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.4, 'OUT 0.4 V, 1.0 kHz', 'l75', 'm75', '', 3.0)
    _th140 = Call('ac0', 0.625, 0.4, 'OUT 0.4 V, 99.0 kHz', 'l76', 'm76', '', 3.0)
    # 200kHz 0.1562B
    _th140 = Callpar(200.0, '1100')
    #_th140 = Call('ac0', 0.1562, 0.0005, 'OUT 0.0005 V, 1.0 kHz', 'n75', 'o75', '', 100.0)
    #_th140 = Call('ac0', 0.1562, 0.0005, 'OUT 0.0005 V, 99.0 kHz', 'n76', 'o76', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.005, 'OUT 0.005 V, 1.0 kHz', 'p75', 'q75', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.005, 'OUT 0.005 V, 99.0 kHz', 'p76', 'q76', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.022, 'OUT 0.022 V, 1.0 kHz', 'r75', 's75', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.022, 'OUT 0.022 V, 99.0 kHz', 'r76', 's76', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.045, 'OUT 0.045 V, 1.0 kHz', 't75', 'u75', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.045, 'OUT 0.045 V, 99.0 kHz', 't76', 'u76', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.07, 'OUT 0.07 V, 1.0 kHz', 'v75', 'w75', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.07, 'OUT 0.07 V, 99.0 kHz', 'v76', 'w76', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.1, 'OUT 0.1 V, 1.0 kHz', 'x75', 'y75', '', 100.0)
    _th140 = Call('ac0', 0.1562, 0.1, 'OUT 0.1 V, 99.0 kHz', 'x76', 'y76', '', 100.0)  
# ac
if self.cvar4.get() == 1: 
    # 20kHz 10B -----------------------------------------------------------------
    _th140 = Callpar(20.0, '0000')
    _th140 = Call('ac', 10.0, 0.35, 'OUT 0.35 V, 0.02 kHz', 'd77', 'e77', '', 0.15)
    _th140 = Call('ac', 10.0, 0.35, 'OUT 0.35 V, 0.5001 kHz', 'd93', 'e93', '', 0.15)
    _th140 = Call('ac', 10.0, 1.4, 'OUT 1.4 V, 0.02 kHz', 'f77', 'g77', '', 0.15)
    _th140 = Call('ac', 10.0, 1.4, 'OUT 1.4 V, 0.5001 kHz', 'f93', 'g93', '', 0.15)
    _th140 = Call('ac', 10.0, 2.8, 'OUT 2.8 V, 0.02 kHz', 'h77', 'i77', '', 0.15)
    _th140 = Call('ac', 10.0, 2.8, 'OUT 2.8 V, 0.501 kHz', 'h93', 'i93', '', 0.15)
    _th140 = Call('ac', 10.0, 4.9, 'OUT 4.9 V, 0.02 kHz', 'j77', 'k77', '', 0.15)
    _th140 = Call('ac', 10.0, 4.9, 'OUT 4.9 V, 0.501 kHz', 'j93', 'k93', '', 0.15)
    _th140 = Call('ac', 10.0, 6.7, 'OUT 6.7 V, 0.02 kHz', 'l77', 'm77', '', 0.15)
    _th140 = Call('ac', 10.0, 6.7, 'OUT 6.7 V, 0.501 kHz', 'l93', 'm93', '', 0.15)
    # 20kHz 2.5B
    _th140 = Callpar(20.0, '0100')
    _th140 = Call('ac', 2.5, 0.085, 'OUT 0.085 V, 0.02 kHz', 'n77', 'o77', '', 0.15)
    _th140 = Call('ac', 2.5, 0.085, 'OUT 0.085 V, 0.501 kHz', 'n93', 'o93', '', 0.15)
    _th140 = Call('ac', 2.5, 0.35, 'OUT 0.35 V, 0.02 kHz', 'p77', 'q77', '', 0.15)
    _th140 = Call('ac', 2.5, 0.35, 'OUT 0.35 V, 0.501 kHz', 'p93', 'q93', '', 0.15)
    _th140 = Call('ac', 2.5, 0.7, 'OUT 0.7 V, 0.02 kHz', 'r77', 's77', '', 0.15)
    _th140 = Call('ac', 2.5, 0.7, 'OUT 0.7 V, 0.501 kHz', 'r93', 's93', '', 0.15)
    _th140 = Call('ac', 2.5, 1.2, 'OUT 1.2 V, 0.02 kHz', 't77', 'u77', '', 0.15)
    _th140 = Call('ac', 2.5, 1.2, 'OUT 1.2 V, 0.501 kHz', 't93', 'u93', '', 0.15)
    _th140 = Call('ac', 2.5, 1.6, 'OUT 1.6 V, 0.02 kHz', 'v77', 'w77', '', 0.15)
    _th140 = Call('ac', 2.5, 1.6, 'OUT 1.6 V, 0.501 kHz', 'v93', 'w93', '', 0.15)            
    # 20kHz 0.625B
    _th140 = Callpar(20.0, '1000')
    _th140 = Call('ac', 0.625, 0.02, 'OUT 0.02 V, 0.02 kHz', 'd109', 'd109', '', 0.15)
    _th140 = Call('ac', 0.625, 0.02, 'OUT 0.02 V, 0.501 kHz', 'd125', 'e125', '', 0.15)
    _th140 = Call('ac', 0.625, 0.085, 'OUT 0.085 V, 0.02 kHz', 'f109', 'g109', '', 0.15)
    _th140 = Call('ac', 0.625, 0.085, 'OUT 0.085 V, 0.501 kHz', 'f125', 'g125', '', 0.15)
    _th140 = Call('ac', 0.625, 0.17, 'OUT 0.17 V, 0.02 kHz', 'h109', 'i109', '', 0.15)
    _th140 = Call('ac', 0.625, 0.17, 'OUT 0.17 V, 0.501 kHz', 'h125', 'i125', '', 0.15)
    _th140 = Call('ac', 0.625, 0.29, 'OUT 0.29 V, 0.02 kHz', 'j109', 'k109', '', 0.15)
    _th140 = Call('ac', 0.625, 0.29, 'OUT 0.29 V, 0.501 kHz', 'j125', 'k125', '', 0.15)
    _th140 = Call('ac', 0.625, 0.4, 'OUT 0.4 V, 0.02 kHz', 'l109', 'm109', '', 0.15)
    _th140 = Call('ac', 0.625, 0.4, 'OUT 0.4 V, 0.501 kHz', 'l125', 'm125', '', 0.15)
    # 20kHz 0.1562B
    _th140 = Callpar(20.0, '1100')
    #_th140 = Call('ac', 0.1562, 0.001, 'OUT 0.001 V, 0.02 kHz', 'n109', 'o109', '', 0.5)
    #_th140 = Call('ac', 0.1562, 0.001, 'OUT 0.001 V, 0.501 kHz', 'n125', 'o125', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.005, 'OUT 0.005 V, 0.02 kHz', 'p109', 'q109', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.005, 'OUT 0.005 V, 0.501 kHz', 'p125', 'q125', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.022, 'OUT 0.022 V, 0.02 kHz', 'r109', 's109', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.022, 'OUT 0.022 V, 0.501 kHz', 'r125', 's125', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.045, 'OUT 0.045 V, 0.02 kHz', 't109', 'u109', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.045, 'OUT 0.045 V, 0.501 kHz', 't125', 'u125', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.07, 'OUT 0.07 V, 0.02 kHz', 'v109', 'w109', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.07, 'OUT 0.07 V, 0.501 kHz', 'v125', 'w125', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.1, 'OUT 0.1 V, 0.02 kHz', 'x109', 'y109', '', 0.5)
    _th140 = Call('ac', 0.1562, 0.1, 'OUT 0.1 V, 0.501 kHz', 'x125', 'y125', '', 0.5)
    # 100kHz 10B -----------------------------------------------------------------
    _th140 = Callpar(100.0, '0000')
    _th140 = Call('ac', 10.0, 0.35, 'OUT 0.35 V, 0.02 kHz', 'd141', 'e141', '', 1.0)
    _th140 = Call('ac', 10.0, 0.35, 'OUT 0.35 V, 3.0 kHz', 'd157', 'e157', '', 1.0)
    _th140 = Call('ac', 10.0, 1.4, 'OUT 1.4 V, 0.02 kHz', 'f141', 'g141', '', 1.0)
    _th140 = Call('ac', 10.0, 1.4, 'OUT 1.4 V, 3.0 kHz', 'f157', 'g157', '', 1.0)
    _th140 = Call('ac', 10.0, 2.8, 'OUT 2.8 V, 0.02 kHz', 'h141', 'i141', '', 1.0)
    _th140 = Call('ac', 10.0, 2.8, 'OUT 2.8 V, 3.0 kHz', 'h157', 'i157', '', 1.0)
    _th140 = Call('ac', 10.0, 4.9, 'OUT 4.9 V, 0.02 kHz', 'j141', 'k141', '', 1.0)
    _th140 = Call('ac', 10.0, 4.9, 'OUT 4.9 V, 3.0 kHz', 'j157', 'k157', '', 1.0)
    _th140 = Call('ac', 10.0, 6.7, 'OUT 6.7 V, 0.02 kHz', 'l141', 'm141', '', 1.0)
    _th140 = Call('ac', 10.0, 6.7, 'OUT 6.7 V, 3.0 kHz', 'l157', 'm157', '', 1.0)
    # 100kHz 2.5B
    _th140 = Callpar(100.0, '0100')
    _th140 = Call('ac', 2.5, 0.085, 'OUT 0.085 V, 0.02 kHz', 'n141', 'o141', '', 1.0)
    _th140 = Call('ac', 2.5, 0.085, 'OUT 0.085 V, 3.0 kHz', 'n157', 'o157', '', 1.0)
    _th140 = Call('ac', 2.5, 0.35, 'OUT 0.35 V, 0.02 kHz', 'p141', 'q141', '', 1.0)
    _th140 = Call('ac', 2.5, 0.35, 'OUT 0.35 V, 3.0 kHz', 'p157', 'q157', '', 1.0)
    _th140 = Call('ac', 2.5, 0.7, 'OUT 0.7 V, 0.02 kHz', 'r141', 's141', '', 1.0)
    _th140 = Call('ac', 2.5, 0.7, 'OUT 0.7 V, 3.0 kHz', 'r157', 's157', '', 1.0)
    _th140 = Call('ac', 2.5, 1.2, 'OUT 1.2 V, 0.02 kHz', 't141', 'u141', '', 1.0)
    _th140 = Call('ac', 2.5, 1.2, 'OUT 1.2 V, 3.0 kHz', 't157', 'u157', '', 1.0)
    _th140 = Call('ac', 2.5, 1.6, 'OUT 1.6 V, 0.02 kHz', 'v141', 'w41', '', 1.0)
    _th140 = Call('ac', 2.5, 1.6, 'OUT 1.6 V, 3.0 kHz', 'v157', 'w157', '', 1.0)
    # 100kHz 0.625B
    _th140 = Callpar(100.0, '1000')
    _th140 = Call('ac', 0.625, 0.02, 'OUT 0.02 V, 0.02 kHz', 'd173', 'e173', '', 1.0)
    _th140 = Call('ac', 0.625, 0.02, 'OUT 0.02 V, 3.0 kHz', 'd189', 'e189', '', 1.0)
    _th140 = Call('ac', 0.625, 0.085, 'OUT 0.085 V, 0.02 kHz', 'f173', 'g173', '', 1.0)
    _th140 = Call('ac', 0.625, 0.085, 'OUT 0.085 V, 3.0 kHz', 'f189', 'g189', '', 1.0)
    _th140 = Call('ac', 0.625, 0.17, 'OUT 0.17 V, 0.02 kHz', 'h173', 'i173', '', 1.0)
    _th140 = Call('ac', 0.625, 0.17, 'OUT 0.17 V, 3.0 kHz', 'h189', 'i189', '', 1.0)
    _th140 = Call('ac', 0.625, 0.29, 'OUT 0.29 V, 0.02 kHz', 'j173', 'k173', '', 1.0)
    _th140 = Call('ac', 0.625, 0.29, 'OUT 0.29 V, 3.0 kHz', 'j189', 'k189', '', 1.0)
    _th140 = Call('ac', 0.625, 0.4, 'OUT 0.4 V, 0.02 kHz', 'l173', 'm173', '', 1.0)
    _th140 = Call('ac', 0.625, 0.4, 'OUT 0.4 V, 3.0 kHz', 'l189', 'm189', '', 1.0)
    # 100kHz 0.1562B
    _th140 = Callpar(100.0, '1100')
    #_th140 = Call('ac', 0.1562, 0.001, 'OUT 0.001 V, 0.02 kHz', 'n173', 'o173', '', 10.0)
    #_th140 = Call('ac', 0.1562, 0.001, 'OUT 0.001 V, 3.0 kHz', 'n189', 'o189', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.005, 'OUT 0.005 V, 0.02 kHz', 'p173', 'q173', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.005, 'OUT 0.005 V, 30 kHz', 'p189', 'q189', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.022, 'OUT 0.022 V, 0.02 kHz', 'r173', 's173', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.022, 'OUT 0.022 V, 3.0 kHz', 'r189', 's189', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.045, 'OUT 0.045 V, 0.02 kHz', 't173', 'u173', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.045, 'OUT 0.045 V, 3.0 kHz', 't189', 'u189', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.07, 'OUT 0.07 V, 0.02 kHz', 'v173', 'w173', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.07, 'OUT 0.07 V, 3.0 kHz', 'v189', 'w189', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.1, 'OUT 0.1 V, 0.02 kHz', 'x173', 'y173', '', 10.0)
    _th140 = Call('ac', 0.1562, 0.1, 'OUT 0.1 V, 3.0 kHz', 'x189', 'y189', '', 10.0)
    # 200kHz 10B --------------------------------------------------------------------
    _th140 = Callpar(200.0, '0000')
    _th140 = Call('ac', 10.0, 0.35, 'OUT 0.35 V, 0.02 kHz', 'd205', 'e205', '', 3.0)
    _th140 = Call('ac', 10.0, 0.35, 'OUT 0.35 V, 6.0 kHz', 'd221', 'e221', '', 3.0)
    _th140 = Call('ac', 10.0, 1.4, 'OUT 1.4 V, 0.02 kHz', 'f205', 'g205', '', 3.0)
    _th140 = Call('ac', 10.0, 1.4, 'OUT 1.4 V, 6.0 kHz', 'f221', 'g221', '', 3.0)
    _th140 = Call('ac', 10.0, 2.8, 'OUT 2.8 V, 0.02 kHz', 'h205', 'i205', '', 3.0)
    _th140 = Call('ac', 10.0, 2.8, 'OUT 2.8 V, 6.0 kHz', 'h221', 'i221', '', 3.0)
    _th140 = Call('ac', 10.0, 4.9, 'OUT 4.9 V, 0.02 kHz', 'j205', 'k205', '', 3.0)
    _th140 = Call('ac', 10.0, 4.9, 'OUT 4.9 V, 6.0 kHz', 'j221', 'k221', '', 3.0)
    _th140 = Call('ac', 10.0, 6.7, 'OUT 6.7 V, 0.02 kHz', 'l205', 'm205', '', 3.0)
    _th140 = Call('ac', 10.0, 6.7, 'OUT 6.7 V, 6.0 kHz', 'l221', 'm221', '', 3.0)
    # 200kHz 2.5B
    _th140 = Callpar(200.0, '0100')
    _th140 = Call('ac', 2.5, 0.085, 'OUT 0.085 V, 0.02 kHz', 'n205', 'o205', '', 3.0)
    _th140 = Call('ac', 2.5, 0.085, 'OUT 0.085 V, 6.0 kHz', 'n221', 'o221', '', 3.0)
    _th140 = Call('ac', 2.5, 0.35, 'OUT 0.35 V, 0.02 kHz', 'p205', 'q205', '', 3.0)
    _th140 = Call('ac', 2.5, 0.35, 'OUT 0.35 V, 6.0 kHz', 'p221', 'q221', '', 3.0)
    _th140 = Call('ac', 2.5, 0.7, 'OUT 0.7 V, 0.02 kHz', 'r205', 's205', '', 3.0)
    _th140 = Call('ac', 2.5, 0.7, 'OUT 0.7 V, 6.0 kHz', 'r221', 's221', '', 3.0)
    _th140 = Call('ac', 2.5, 1.2, 'OUT 1.2 V, 0.02 kHz', 't205', 'u205', '', 3.0)
    _th140 = Call('ac', 2.5, 1.2, 'OUT 1.2 V, 6.0 kHz', 't221', 'u221', '', 3.0)
    _th140 = Call('ac', 2.5, 1.6, 'OUT 1.6 V, 0.02 kHz', 'v205', 'w205', '', 3.0)
    _th140 = Call('ac', 2.5, 1.6, 'OUT 1.6 V, 6.0 kHz', 'v221', 'w221', '', 3.0)
    # 200kHz 0.625B
    _th140 = Callpar(200.0, '1000')
    _th140 = Call('ac', 0.625, 0.02, 'OUT 0.02 V, 0.02 kHz', 'd237', 'e237', '', 3.0)
    _th140 = Call('ac', 0.625, 0.02, 'OUT 0.02 V, 6.0 kHz', 'd253', 'e253', '', 3.0)
    _th140 = Call('ac', 0.625, 0.085, 'OUT 0.085 V, 0.02 kHz', 'f237', 'g237', '', 3.0)
    _th140 = Call('ac', 0.625, 0.085, 'OUT 0.085 V, 6.0 kHz', 'f253', 'g253', '', 3.0)
    _th140 = Call('ac', 0.625, 0.17, 'OUT 0.17 V, 0.02 kHz', 'h237', 'i237', '', 3.0)
    _th140 = Call('ac', 0.625, 0.17, 'OUT 0.17 V, 6.0 kHz', 'h253', 'i253', '', 3.0)
    _th140 = Call('ac', 0.625, 0.29, 'OUT 0.29 V, 0.02 kHz', 'j237', 'k237', '', 3.0)
    _th140 = Call('ac', 0.625, 0.29, 'OUT 0.29 V, 6.0 kHz', 'j253', 'k253', '', 3.0)
    _th140 = Call('ac', 0.625, 0.4, 'OUT 0.4 V, 0.02 kHz', 'l237', 'm237', '', 3.0)
    _th140 = Call('ac', 0.625, 0.4, 'OUT 0.4 V, 6.0 kHz', 'l253', 'm253', '', 3.0)
    # 200kHz 0.1562B
    _th140 = Callpar(200.0, '1100')
    #_th140 = Call('ac', 0.1562, 0.001, 'OUT 0.001 V, 0.02 kHz', 'n237', 'o237', '', 100.0)
    #_th140 = Call('ac', 0.1562, 0.001, 'OUT 0.001 V, 6.0 kHz', 'n253', 'o253', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.005, 'OUT 0.005 V, 0.02 kHz', 'p237', 'q237', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.005, 'OUT 0.005 V, 6.0 kHz', 'p253', 'q253', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.022, 'OUT 0.022 V, 0.02 kHz', 'r237', 's237', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.022, 'OUT 0.022 V, 6.0 kHz', 'r253', 's253', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.045, 'OUT 0.045 V, 0.02 kHz', 't237', 'u237', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.045, 'OUT 0.045 V, 6.0 kHz', 't253', 'u253', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.07, 'OUT 0.07 V, 0.02 kHz', 'v237', 'w237', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.07, 'OUT 0.07 V, 6.0 kHz', 'v253', 'w253', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.1, 'OUT 0.1 V, 0.02 kHz', 'x237', 'y237', '', 100.0)
    _th140 = Call('ac', 0.1562, 0.1, 'OUT 0.1 V, 6.0 kHz', 'x253', 'y253', '', 100.0)         

if self.dac == 1:
    # DAC1
    if self.cvar5.get() == 1:               
        _th140 = Message('Подключите выход ЦАП1 к мультиметру')
        _th140 = Callpar(20.0, '0000')              
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', 4750.0, 'DET:BAND 20', 3.0, 'b267', 'c267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', 2000.0, 'DET:BAND 20', 3.0, 'd267', 'e267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', 1000.0, 'DET:BAND 20', 3.0, 'f267', 'g267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', 250.0, 'DET:BAND 20', 3.0, 'h267', 'i267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', 3.0, 'DET:BAND 20', 3.0, 'j267', 'k267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', -3.0, 'DET:BAND 20', 3.0, 'l267', 'm267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', -250.0, 'DET:BAND 20', 3.0, 'n267', 'o267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', -1000.0, 'DET:BAND 20', 3.0, 'p267', 'q267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', -2000.0, 'DET:BAND 20', 3.0, 'r267', 's267', 0.3)
        _th140 = Ldac(0, 'CONF:VOLT:DC 10', -4750.0, 'DET:BAND 20', 3.0, 't267', 'u267', 0.3)
    # DAC2
    if self.cvar6.get() == 1:               
        _th140 = Message('Подключите выход ЦАП2 к мультиметру')
        _th140 = Callpar(20.0, '0000')
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', 4750.0, 'DET:BAND 20', 3.0, 'b268', 'c268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', 2000.0, 'DET:BAND 20', 3.0, 'd268', 'e268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', 1000.0, 'DET:BAND 20', 3.0, 'f268', 'g268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', 250.0, 'DET:BAND 20', 3.0, 'h268', 'i268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', 3.0, 'DET:BAND 20', 3.0, 'j268', 'k268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', -3.0, 'DET:BAND 20', 3.0, 'l268', 'm268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', -250.0, 'DET:BAND 20', 3.0, 'n268', 'o268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', -1000.0, 'DET:BAND 20', 3.0, 'p268', 'q268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', -2000.0, 'DET:BAND 20', 3.0, 'r268', 's268', 0.3)
        _th140 = Ldac(1, 'CONF:VOLT:DC 10', -4750.0, 'DET:BAND 20', 3.0, 't268', 'u440', 0.3)                   
_th = Reset()
_th = Message('Калибровка завершена')
