# -*- coding: utf-8 -*-
Reset()
if self.vardict_boo['cvar1'].get() or self.vardict_boo['cvar3'].get() or self.vardict_boo['cvar4'].get() == 1:
    Message('Подключите провода к калибратору для измерения напряжения')
if self.vardict_boo['cvar1'].get() == 1:
    # dc 10V
    Callpar(20, '0000')
    Call('dcv', 10, '9.9 V', 'b1', 'c1', 0.05)
    Call('dcv', 10, '7 V', 'd1', 'e1', 0.05)
    Call('dcv', 10, '4 V', 'f1', 'g1', 0.05)
    Call('dcv', 10,'2 V','h1','i1', 0.05)
    Call('dcv', 10,'0.5 V','j1','k1', 0.05)
    Call('dcv', 10,'-0.5 V','l1','m1', 0.05)
    Call('dcv', 10,'-2 V','n1','o1', 0.05)
    Call('dcv', 10,'-4 V','p1','q1', 0.05)
    Call('dcv', 10,'-7 V','r1','s1', 0.05)
    Call('dcv', 10, '-9.9 V','t1','u1', 0.05)
    # dc 2.5V
    Callpar(20, '0100')
    Call('dcv', 2.5, '2.475 V','b17','c17', 0.05)
    Call('dcv', 2.5, '1.75 V','d17','e17', 0.05)
    Call('dcv', 2.5, '1 V','f17','g17', 0.05)
    Call('dcv', 2.5, '0.5 V','h17','i17', 0.05)
    Call('dcv', 2.5, '0.15 V','j17','k17', 0.05)
    Call('dcv', 2.5, '-0.15 V','l17','m17', 0.05)
    Call('dcv', 2.5, '-0.5 V','n17','o17', 0.05)
    Call('dcv', 2.5, '-1 V','p17','q17', 0.05)
    Call('dcv', 2.5, '-1.75 V','r17','s17', 0.05)
    Call('dcv', 2.5, '-2.475 V','t17','u17', 0.05)
    # dc 0.625V
    Callpar(20, '1000')
    Call('dcv', 0.625, '0.6 V','b33','c33', 0.1)
    Call('dcv', 0.625, '0.42 V','d33','e33', 0.1)
    Call('dcv', 0.625, '0.24 V','f33','g33', 0.1)
    Call('dcv', 0.625, '0.12 V','h33','i33', 0.1)
    Call('dcv', 0.625, '0.03 V','j33','k33', 0.1)
    Call('dcv', 0.625, '-0.03 V','l33','m33', 0.1)
    Call('dcv', 0.625, '-0.12 V','n33','o33', 0.1)
    Call('dcv', 0.625, '-0.24 V','p33','q33', 0.1)
    Call('dcv', 0.625, '-0.42 V','r33','s33', 0.1)
    Call('dcv', 0.625, '-0.6 V','t33','u33', 0.1)
    # dc 0.1562V
    Callpar(20, '1100')
    Call('dcv', 0.1562, '0.15 V','b49','c49', 0.5)
    Call('dcv', 0.1562, '0.105 V','d49','e49', 0.5)
    Call('dcv', 0.1562, '0.06 V','f49','g49', 0.5)
    Call('dcv', 0.1562, '0.03 V','h49','i49', 0.5)
    Call('dcv', 0.1562, '0.01 V','j49','k49', 0.5)
    Call('dcv', 0.1562, '0.005 V','l49','m49', 0.5)
    Call('dcv', 0.1562, '-0.005 V','n49','o49', 0.5)
    Call('dcv', 0.1562, '-0.01 V','p49','q49', 0.5)
    Call('dcv', 0.1562, '-0.03 V','r49','s49', 0.5)
    Call('dcv', 0.1562, '-0.06 V','t49','u49', 0.5)
    Call('dcv', 0.1562, '-0.105 V','v49','w49', 0.5)
    Call('dcv', 0.1562, '-0.15 V','x49','y49', 0.5)
# ac0
if self.vardict_boo['cvar3'].get() == 1:
    # 20kHz 10B --------------------------------------------------------------------
    Callpar(20, '0000')
    Call('ac0', 10, '0.35 V, 0.1 kHz', 'd69', 'e69', 0.15)
    Call('ac0', 10, '0.35 V, 9.0 kHz', 'd70', 'e70', 0.15)
    Call('ac0', 10, '1.4 V, 0.1 kHz', 'f69', 'g69', 0.15)
    Call('ac0', 10, '1.4 V, 9.0 kHz', 'f70', 'g70', 0.15)
    Call('ac0', 10, '2.8 V, 0.1 kHz', 'h69', 'i69', 0.15)
    Call('ac0', 10, '2.8 V, 9.0 kHz', 'h70', 'i70', 0.15)
    Call('ac0', 10, '4.9 V, 0.1 kHz', 'j69', 'k69', 0.15)
    Call('ac0', 10, '4.9 V, 9.0 kHz', 'j70', 'k70', 0.15)
    Call('ac0', 10, '6.7 V, 0.1 kHz', 'l69', 'm69', 0.15)
    Call('ac0', 10, '6.7 V, 9.0 kHz', 'l70', 'm70', 0.15)
    # 20kHz 2.5B
    Callpar(20, '0100')
    Call('ac0', 2.5, '0.085 V, 0.1 kHz', 'n69', 'o69', 0.15)
    Call('ac0', 2.5, '0.085 V, 9.0 kHz', 'n70', 'o70', 0.15)
    Call('ac0', 2.5, '0.35 V, 0.1 kHz', 'p69', 'q69', 0.15)
    Call('ac0', 2.5, '0.35 V, 9.0 kHz', 'p70', 'q70', 0.15)
    Call('ac0', 2.5, '0.7 V, 0.1 kHz', 'r69', 's69', 0.15)
    Call('ac0', 2.5, '0.7 V, 9.0 kHz', 'r70', 's70', 0.15)
    Call('ac0', 2.5, '1.2 V, 0.1 kHz', 't69', 'u69', 0.15)
    Call('ac0', 2.5, '1.2 V, 9.0 kHz', 't70', 'u70', 0.15)
    Call('ac0', 2.5, '1.6 V, 0.1 kHz', 'v69', 'w69', 0.15)
    Call('ac0', 2.5, '1.6 V, 9.0 kHz', 'v70', 'w70', 0.15)
    # 20kHz 0.625B
    Callpar(20, '1000')
    Call('ac0', 0.625, '0.02 V, 0.1 kHz', 'd77', 'e77', 0.15)
    Call('ac0', 0.625, '0.02 V, 9.0 kHz', 'd78', 'e78', 0.15)
    Call('ac0', 0.625, '0.085 V, 0.1 kHz', 'f77', 'g77', 0.15)
    Call('ac0', 0.625, '0.085 V, 9.0 kHz', 'f78', 'g78', 0.15)
    Call('ac0', 0.625, '0.17 V, 0.1 kHz', 'h77', 'i77', 0.15)
    Call('ac0', 0.625, '0.17 V, 9.0 kHz', 'h78', 'i78', 0.15)
    Call('ac0', 0.625, '0.29 V, 0.1 kHz', 'j77', 'k77', 0.15)
    Call('ac0', 0.625, '0.29 V, 9.0 kHz', 'j78', 'k78', 0.15)
    Call('ac0', 0.625, '0.4 V, 0.1 kHz', 'l77', 'm77', 0.15)
    Call('ac0', 0.625, '0.4 V, 9.0 kHz', 'l78', 'm78', 0.15)
    # 20kHz 0.1562B
    Callpar(20, '1100')
    #Call('ac0', 0.1562, '0.0005 V, 0.1 kHz', 'n77', 'o77', 0.5)
    #Call('ac0', 0.1562, '0.0005 V, 9.0 kHz', 'n78', 'o78', 0.5)
    Call('ac0', 0.1562, '0.005 V, 0.1 kHz', 'p77', 'q77', 0.5)
    Call('ac0', 0.1562, '0.005 V, 9.0 kHz', 'p78', 'q78', 0.5)
    Call('ac0', 0.1562, '0.022 V, 0.1 kHz', 'r77', 's77', 0.5)
    Call('ac0', 0.1562, '0.022 V, 9.0 kHz', 'r78', 's78', 0.5)
    Call('ac0', 0.1562, '0.045 V, 0.1 kHz', 't77', 'u77', 0.5)
    Call('ac0', 0.1562, '0.045 V, 9.0 kHz', 't78', 'u78', 0.5)
    Call('ac0', 0.1562, '0.07 V, 0.1 kHz', 'v77', 'w77', 0.5)
    Call('ac0', 0.1562, '0.07 V, 9.0 kHz', 'v78', 'w78', 0.5)
    Call('ac0', 0.1562, '0.1 V, 0.1 kHz', 'x77', 'y77', 0.5)
    Call('ac0', 0.1562, '0.1 V, 9.0 kHz', 'x78', 'y78', 0.5)
    # 100kHz 10B ---------------------------------------------------------------------
    Callpar(100, '0000')
    Call('ac0', 10, '0.35 V, 1.0 kHz', 'd71', 'e71', 1)
    Call('ac0', 10, '0.35 V, 49.0 kHz', 'd72', 'e72', 1)
    Call('ac0', 10, '1.4 V, 1.0 kHz', 'f71', 'g71', 1)
    Call('ac0', 10, '1.4 V, 49.0 kHz', 'f72', 'g72', 1)
    Call('ac0', 10, '2.8 V, 1.0 kHz', 'h71', 'i71', 1)
    Call('ac0', 10, '2.8 V, 49.0 kHz', 'h72', 'i72', 1)
    Call('ac0', 10, '4.9 V, 1.0 kHz', 'j71', 'k71', 1)
    Call('ac0', 10, '4.9 V, 49.0 kHz', 'j72', 'k72', 1)
    Call('ac0', 10, '6.7 V, 1.0 kHz', 'l71', 'm71', 1)
    Call('ac0', 10, '6.7 V, 49.0 kHz', 'l72', 'm72', 1)
    # 100kHz 2.5B
    Callpar(100, '0100')
    Call('ac0', 2.5, '0.085 V, 1.0 kHz', 'n71', 'o71', 1)
    Call('ac0', 2.5, '0.085 V, 49.0 kHz', 'n72', 'o72', 1)
    Call('ac0', 2.5, '0.35 V, 1.0 kHz', 'p71', 'q71', 1)
    Call('ac0', 2.5, '0.35 V, 49.0 kHz', 'p72', 'q72', 1)
    Call('ac0', 2.5, '0.7 V, 1.0 kHz', 'r71', 's71', 1)
    Call('ac0', 2.5, '0.7 V, 49.0 kHz', 'r72', 's72', 1)
    Call('ac0', 2.5, '1.2 V, 1.0 kHz', 't71', 'u71', 1)
    Call('ac0', 2.5, '1.2 V, 49.0 kHz', 't72', 'u72', 1)
    Call('ac0', 2.5, '1.6 V, 1.0 kHz', 'v71', 'w71', 1)
    Call('ac0', 2.5, '1.6 V, 49.0 kHz', 'v72', 'w72', 1)
    # 100kHz 0.625B
    Callpar(100, '1000')
    Call('ac0', 0.625, '0.02 V, 1.0 kHz', 'd79', 'e79', 1)
    Call('ac0', 0.625, '0.02 V, 49.0 kHz', 'd80', 'e80', 1)
    Call('ac0', 0.625, '0.085 V, 1.0 kHz', 'f79', 'g79', 1)
    Call('ac0', 0.625, '0.085 V, 49.0 kHz', 'f80', 'g80', 1)
    Call('ac0', 0.625, '0.17 V, 1.0 kHz', 'h79', 'i79', 1)
    Call('ac0', 0.625, '0.17 V, 49.0 kHz', 'h80', 'i80', 1)
    Call('ac0', 0.625, '0.29 V, 1.0 kHz', 'j79', 'k79', 1)
    Call('ac0', 0.625, '0.29 V, 49.0 kHz', 'j80', 'k80', 1)
    Call('ac0', 0.625, '0.4 V, 1.0 kHz', 'l79', 'm79', 1)
    Call('ac0', 0.625, '0.4 V, 49.0 kHz', 'l80', 'm80', 1)
    # 100kHz 0.1562B
    Callpar(100, '1100')
    #Call('ac0', 0.1562, '0.0005 V, 1.0 kHz', 'n79', 'o79', 10)
    #Call('ac0', 0.1562, '0.0005 V, 49.0 kHz', 'n80', 'o80', 10)
    Call('ac0', 0.1562, '0.005 V, 1.0 kHz', 'p79', 'q79', 10)
    Call('ac0', 0.1562, '0.005 V, 49.0 kHz', 'p80', 'q80', 10)
    Call('ac0', 0.1562, '0.022 V, 1.0 kHz', 'r79', 's79', 10)
    Call('ac0', 0.1562, '0.022 V, 49.0 kHz', 'r80', 's80', 10)
    Call('ac0', 0.1562, '0.045 V, 1.0 kHz', 't79', 'u79', 10)
    Call('ac0', 0.1562, '0.045 V, 49.0 kHz', 't80', 'u80', 10)
    Call('ac0', 0.1562, '0.07 V, 1.0 kHz', 'v79', 'w79', 10)
    Call('ac0', 0.1562, '0.07 V, 49.0 kHz', 'v80', 'w80', 10)
    Call('ac0', 0.1562, '0.1 V, 1.0 kHz', 'x79', 'y79', 10)
    Call('ac0', 0.1562, '0.1 V, 49.0 kHz', 'x80', 'y80', 10)
    # 200kHz 10B --------------------------------------------------------------------
    Callpar(200, '0000')
    Call('ac0', 10, '0.35 V, 1.0 kHz', 'd73', 'e73', 3)
    Call('ac0', 10, '0.35 V, 99.0 kHz', 'd74', 'e74', 3)
    Call('ac0', 10, '1.4 V, 1.0 kHz', 'f73', 'g73', 3)
    Call('ac0', 10, '1.4 V, 99.0 kHz', 'f74', 'g74', 3)
    Call('ac0', 10, '2.8 V, 1.0 kHz', 'h73', 'i73', 3)
    Call('ac0', 10, '2.8 V, 99.0 kHz', 'h74', 'i74', 3)
    Call('ac0', 10, '4.9 V, 1.0 kHz', 'j73', 'k73', 3)
    Call('ac0', 10, '4.9 V, 99.0 kHz', 'j74', 'k74', 3)
    Call('ac0', 10, '6.7 V, 1.0 kHz', 'l73', 'm73', 3)
    Call('ac0', 10, '6.7 V, 99.0 kHz', 'l74', 'm74', 3)
    # 200kHz 2.5B
    Callpar(200, '0100')
    Call('ac0', 2.5, '0.085 V, 1.0 kHz', 'n73', 'o73', 3)
    Call('ac0', 2.5, '0.085 V, 99.0 kHz', 'n74', 'o74', 3)
    Call('ac0', 2.5, '0.35 V, 1.0 kHz', 'p73', 'q73', 3)
    Call('ac0', 2.5, '0.35 V, 99.0 kHz', 'p74', 'q74', 3)
    Call('ac0', 2.5, '0.7 V, 1.0 kHz', 'r73', 's73', 3)
    Call('ac0', 2.5, '0.7 V, 99.0 kHz', 'r74', 's74', 3)
    Call('ac0', 2.5, '1.2 V, 1.0 kHz', 't73', 'u73', 3)
    Call('ac0', 2.5, '1.2 V, 99.0 kHz', 't74', 'u74', 3)
    Call('ac0', 2.5, '1.6 V, 1.0 kHz', 'v73', 'w73', 3)
    Call('ac0', 2.5, '1.6 V, 99.0 kHz', 'v74', 'w74', 3)
    # 200kHz 0.625B
    Callpar(200, '1000')
    Call('ac0', 0.625, '0.02 V, 1.0 kHz', 'd81', 'e81', 3)
    Call('ac0', 0.625, '0.02 V, 99.0 kHz', 'd82', 'e82', 3)
    Call('ac0', 0.625, '0.085 V, 1.0 kHz', 'f81', 'g81', 3)
    Call('ac0', 0.625, '0.085 V, 99.0 kHz', 'f82', 'g82', 3)
    Call('ac0', 0.625, '0.17 V, 1.0 kHz', 'h81', 'i81', 3)
    Call('ac0', 0.625, '0.17 V, 99.0 kHz', 'h82', 'i82', 3)
    Call('ac0', 0.625, '0.29 V, 1.0 kHz', 'j81', 'k81', 3)
    Call('ac0', 0.625, '0.29 V, 99.0 kHz', 'j82', 'k82', 3)
    Call('ac0', 0.625, '0.4 V, 1.0 kHz', 'l81', 'm81', 3)
    Call('ac0', 0.625, '0.4 V, 99.0 kHz', 'l82', 'm82', 3)
    # 200kHz 0.1562B
    Callpar(200, '1100')
    #Call('ac0', 0.1562, '0.0005 V, 1.0 kHz', 'n81', 'o81', 100)
    #Call('ac0', 0.1562, '0.0005 V, 99.0 kHz', 'n82', 'o82', 100)
    Call('ac0', 0.1562, '0.005 V, 1.0 kHz', 'p81', 'q81', 100)
    Call('ac0', 0.1562, '0.005 V, 99.0 kHz', 'p82', 'q82', 100)
    Call('ac0', 0.1562, '0.022 V, 1.0 kHz', 'r81', 's81', 100)
    Call('ac0', 0.1562, '0.022 V, 99.0 kHz', 'r82', 's82', 100)
    Call('ac0', 0.1562, '0.045 V, 1.0 kHz', 't81', 'u81', 100)
    Call('ac0', 0.1562, '0.045 V, 99.0 kHz', 't82', 'u82', 100)
    Call('ac0', 0.1562, '0.07 V, 1.0 kHz', 'v81', 'w81', 100)
    Call('ac0', 0.1562, '0.07 V, 99.0 kHz', 'v82', 'w82', 100)
    Call('ac0', 0.1562, '0.1 V, 1.0 kHz', 'x81', 'y81', 100)
    Call('ac0', 0.1562, '0.1 V, 99.0 kHz', 'x82', 'y82', 100)
    # 400kHz 10B ----------------------------------------------------------------------
    Callpar(400, '0000')
    Call('ac0', 10, '0.35 V, 1.0 kHz', 'd75', 'e75', 5)
    Call('ac0', 10, '0.35 V, 199.0 kHz', 'd76', 'e76', 5)
    Call('ac0', 10, '1.4 V, 1.0 kHz', 'f75', 'g75', 5)
    Call('ac0', 10, '1.4 V, 199.0 kHz', 'f76', 'g76', 5)
    Call('ac0', 10, '2.8 V, 1.0 kHz', 'h75', 'i75', 5)
    Call('ac0', 10, '2.8 V, 199.0 kHz', 'h76', 'i76', 5)
    Call('ac0', 10, '4.9 V, 1.0 kHz', 'j75', 'k75', 5)
    Call('ac0', 10, '4.9 V, 199.0 kHz', 'j76', 'k76', 5)
    Call('ac0', 10, '6.7 V, 1.0 kHz', 'l75', 'm75', 5)
    Call('ac0', 10, '6.7 V, 199.0 kHz', 'l76', 'm76', 5)
    # 400kHz 2.5B
    Callpar(400, '0100')
    Call('ac0', 2.5, '0.085 V, 1.0 kHz', 'n75', 'o75', 5)
    Call('ac0', 2.5, '0.085 V, 199.0 kHz', 'n76', 'o76', 5)
    Call('ac0', 2.5, '0.35 V, 1.0 kHz', 'p75', 'q75', 5)
    Call('ac0', 2.5, '0.35 V, 199.0 kHz', 'p76', 'q76', 5)
    Call('ac0', 2.5, '0.7 V, 1.0 kHz', 'r75', 's75', 5)
    Call('ac0', 2.5, '0.7 V, 199.0 kHz', 'r76', 's76', 5)
    Call('ac0', 2.5, '1.2 V, 1.0 kHz', 't75', 'u75', 5)
    Call('ac0', 2.5, '1.2 V, 199.0 kHz', 't76', 'u76', 5)
    Call('ac0', 2.5, '1.6 V, 1.0 kHz', 'v75', 'w75', 5)
    Call('ac0', 2.5, '1.6 V, 199.0 kHz', 'v76', 'w76', 5)
    # 400kHz 0.625B
    Callpar(400, '1000')
    Call('ac0', 0.625, '0.02 V, 1.0 kHz', 'd83', 'e83', 10)
    Call('ac0', 0.625, '0.02 V, 199.0 kHz', 'd84', 'e84', 10)
    Call('ac0', 0.625, '0.085 V, 1.0 kHz', 'f83', 'g83', 10)
    Call('ac0', 0.625, '0.085 V, 199.0 kHz', 'f84', 'g84', 10)
    Call('ac0', 0.625, '0.17 V, 1.0 kHz', 'h83', 'i83', 10)
    Call('ac0', 0.625, '0.17 V, 199.0 kHz', 'h84', 'i84', 10)
    Call('ac0', 0.625, '0.29 V, 1.0 kHz', 'j83', 'k83', 10)
    Call('ac0', 0.625, '0.29 V, 199.0 kHz', 'j84', 'k84', 10)
    Call('ac0', 0.625, '0.4 V, 1.0 kHz', 'l83', 'm83', 10)
    Call('ac0', 0.625, '0.4 V, 199.0 kHz', 'l84', 'm84', 10)
    # 400kHz 0.1562B
    Callpar(400, '1100')
    #Call('ac0', 0.156, '0.0005 V, 1.0 kHz', 'n83', 'o83', 100)
    #Call('ac0', 0.1562, '0.0005 V, 199.0 kHz', 'n84', 'o84', 100)
    Call('ac0', 0.1562, '0.005 V, 1.0 kHz', 'p83', 'q83', 100)
    Call('ac0', 0.1562, '0.005 V, 199.0 kHz', 'p84', 'q84', 100)
    Call('ac0', 0.1562, '0.022 V, 1.0 kHz', 'r83', 's83', 100)
    Call('ac0', 0.1562, '0.022 V, 199.0 kHz', 'r84', 's84', 100)
    Call('ac0', 0.1562, '0.045 V, 1.0 kHz', 't83', 'u83', 100)
    Call('ac0', 0.1562, '0.045 V, 199.0 kHz', 't84', 'u84', 100)
    Call('ac0', 0.1562, '0.07 V, 1.0 kHz', 'v83', 'w83', 100)
    Call('ac0', 0.1562, '0.07 V, 199.0 kHz', 'v84', 'w84', 100)
    Call('ac0', 0.1562, '0.1 V, 1.0 kHz', 'x83', 'y83', 100)
    Call('ac0', 0.1562, '0.1 V, 199.0 kHz', 'x84', 'y84', 100)
# ac
if self.vardict_boo['cvar4'].get() == 1:
    # 20kHz 10B -----------------------------------------------------------------
    Callpar(20, '0000')
    Call('acv', 10, '0.35 V, 0.02 kHz', 'd85', 'e85', 0.15)
    Call('acv', 10, '0.35 V, 0.5001 kHz', 'd101', 'e101', 0.15)
    Call('acv', 10, '1.4 V, 0.02 kHz', 'f85', 'g85', 0.15)
    Call('acv', 10, '1.4 V, 0.5001 kHz', 'f101', 'g101', 0.15)
    Call('acv', 10, '2.8 V, 0.02 kHz', 'h85', 'i85', 0.15)
    Call('acv', 10, '2.8 V, 0.501 kHz', 'h101', 'i101', 0.15)
    Call('acv', 10, '4.9 V, 0.02 kHz', 'j85', 'k85', 0.15)
    Call('acv', 10, '4.9 V, 0.501 kHz', 'j101', 'k101', 0.15)
    Call('acv', 10, '6.7 V, 0.02 kHz', 'l85', 'm85', 0.15)
    Call('acv', 10, '6.7 V, 0.501 kHz', 'l101', 'm101', 0.15)
    # 20kHz 2.5B
    Callpar(20, '0100')
    Call('acv', 2.5, '0.085 V, 0.02 kHz', 'n85', 'o85', 0.15)
    Call('acv', 2.5, '0.085 V, 0.501 kHz', 'n101', 'o101', 0.15)
    Call('acv', 2.5, '0.35 V, 0.02 kHz', 'p85', 'q85', 0.15)
    Call('acv', 2.5, '0.35 V, 0.501 kHz', 'p101', 'q101', 0.15)
    Call('acv', 2.5, '0.7 V, 0.02 kHz', 'r85', 's85', 0.15)
    Call('acv', 2.5, '0.7 V, 0.501 kHz', 'r101', 's101', 0.15)
    Call('acv', 2.5, '1.2 V, 0.02 kHz', 't85', 'u85', 0.15)
    Call('acv', 2.5, '1.2 V, 0.501 kHz', 't101', 'u101', 0.15)
    Call('acv', 2.5, '1.6 V, 0.02 kHz', 'v85', 'w85', 0.15)
    Call('acv', 2.5, '1.6 V, 0.501 kHz', 'v101', 'w101', 0.15)
    # 20kHz 0.625B
    Callpar(20, '1000')
    Call('acv', 0.625, '0.02 V, 0.02 kHz', 'd117', 'e117', 0.15)
    Call('acv', 0.625, '0.02 V, 0.501 kHz', 'd133', 'e133', 0.15)
    Call('acv', 0.625, '0.085 V, 0.02 kHz', 'f117', 'g117', 0.15)
    Call('acv', 0.625, '0.085 V, 0.501 kHz', 'f133', 'g133', 0.15)
    Call('acv', 0.625, '0.17 V, 0.02 kHz', 'h117', 'i117', 0.15)
    Call('acv', 0.625, '0.17 V, 0.501 kHz', 'h133', 'i133', 0.15)
    Call('acv', 0.625, '0.29 V, 0.02 kHz', 'j117', 'k117', 0.15)
    Call('acv', 0.625, '0.29 V, 0.501 kHz', 'j133', 'k133', 0.15)
    Call('acv', 0.625, '0.4 V, 0.02 kHz', 'l117', 'm117', 0.15)
    Call('acv', 0.625, '0.4 V, 0.501 kHz', 'l133', 'm133', 0.15)
    # 20kHz 0.1562B
    Callpar(20, '1100')
    #Call('acv', 0.1562, '0.0005 V, 0.02 kHz', 'n117', 'o117', 0.5)
    #Call('acv', 0.1562, '0.0005 V, 0.501 kHz', 'n133', 'o133', 0.5)
    Call('acv', 0.1562, '0.005 V, 0.02 kHz', 'p117', 'q117', 0.5)
    Call('acv', 0.1562, '0.005 V, 0.501 kHz', 'p133', 'q133', 0.5)
    Call('acv', 0.1562, '0.022 V, 0.02 kHz', 'r117', 's117', 0.5)
    Call('acv', 0.1562, '0.022 V, 0.501 kHz', 'r133', 's133', 0.5)
    Call('acv', 0.1562, '0.045 V, 0.02 kHz', 't117', 'u117', 0.5)
    Call('acv', 0.1562, '0.045 V, 0.501 kHz', 't133', 'u133', 0.5)
    Call('acv', 0.1562, '0.07 V, 0.02 kHz', 'v117', 'w117', 0.5)
    Call('acv', 0.1562, '0.07 V, 0.501 kHz', 'v133', 'w133', 0.5)
    Call('acv', 0.1562, '0.1 V, 0.02 kHz', 'x117', 'y117', 0.5)
    Call('acv', 0.1562, '0.1 V, 0.501 kHz', 'x133', 'y133', 0.5)
    # 100kHz 10B -----------------------------------------------------------------
    Callpar(100, '0000')
    Call('acv', 10, '0.35 V, 0.02 kHz', 'd149', 'e149', 1)
    Call('acv', 10, '0.35 V, 3.0 kHz', 'd165', 'e165', 1)
    Call('acv', 10, '1.4 V, 0.02 kHz', 'f149', 'g149', 1)
    Call('acv', 10, '1.4 V, 3.0 kHz', 'f165', 'g165', 1)
    Call('acv', 10, '2.8 V, 0.02 kHz', 'h149', 'i149', 1)
    Call('acv', 10, '2.8 V, 3.0 kHz', 'h165', 'i165', 1)
    Call('acv', 10, '4.9 V, 0.02 kHz', 'j149', 'k149', 1)
    Call('acv', 10, '4.9 V, 3.0 kHz', 'j165', 'k165', 1)
    Call('acv', 10, '6.7 V, 0.02 kHz', 'l149', 'm149', 1)
    Call('acv', 10, '6.7 V, 3.0 kHz', 'l165', 'm165', 1)
    # 100kHz 2.5B
    Callpar(100, '0100')
    Call('acv', 2.5, '0.085 V, 0.02 kHz', 'n149', 'o149', 1)
    Call('acv', 2.5, '0.085 V, 3.0 kHz', 'n165', 'o165', 1)
    Call('acv', 2.5, '0.35 V, 0.02 kHz', 'p149', 'q149', 1)
    Call('acv', 2.5, '0.35 V, 3.0 kHz', 'p165', 'q165', 1)
    Call('acv', 2.5, '0.7 V, 0.02 kHz', 'r149', 's149', 1)
    Call('acv', 2.5, '0.7 V, 3.0 kHz', 'r165', 's165', 1)
    Call('acv', 2.5, '1.2 V, 0.02 kHz', 't149', 'u149', 1)
    Call('acv', 2.5, '1.2 V, 3.0 kHz', 't165', 'u165', 1)
    Call('acv', 2.5, '1.6 V, 0.02 kHz', 'v149', 'w149', 1)
    Call('acv', 2.5, '1.6 V, 3.0 kHz', 'v165', 'w165', 1)
    # 100kHz 0.625B
    Callpar(100, '1000')
    Call('acv', 0.625, '0.02 V, 0.02 kHz', 'd181', 'e181', 1)
    Call('acv', 0.625, '0.02 V, 3.0 kHz', 'd197', 'e197', 1)
    Call('acv', 0.625, '0.085 V, 0.02 kHz', 'f181', 'g181', 1)
    Call('acv', 0.625, '0.085 V, 3.0 kHz', 'f197', 'g197', 1)
    Call('acv', 0.625, '0.17 V, 0.02 kHz', 'h181', 'i181', 1)
    Call('acv', 0.625, '0.17 V, 3.0 kHz', 'h197', 'i197', 1)
    Call('acv', 0.625, '0.29 V, 0.02 kHz', 'j181', 'k181', 1)
    Call('acv', 0.625, '0.29 V, 3.0 kHz', 'j197', 'k197', 1)
    Call('acv', 0.625, '0.4 V, 0.02 kHz', 'l181', 'm181', 1)
    Call('acv', 0.625, '0.4 V, 3.0 kHz', 'l197', 'm197', 1)
    # 100kHz 0.1562B
    Callpar(100, '1100')
    #Call('acv', 0.1562, '0.0005 V, 0.02 kHz', 'n181', 'o181', 10)
    #Call('acv', 0.1562, '0.0005 V, 3.0 kHz', 'n197', 'o197', 10)
    Call('acv', 0.1562, '0.005 V, 0.02 kHz', 'p181', 'q181', 10)
    Call('acv', 0.1562, '0.005 V, 30 kHz', 'p197', 'q197', 10)
    Call('acv', 0.1562, '0.022 V, 0.02 kHz', 'r181', 's181', 10)
    Call('acv', 0.1562, '0.022 V, 3.0 kHz', 'r197', 's197', 10)
    Call('acv', 0.1562, '0.045 V, 0.02 kHz', 't181', 'u181', 10)
    Call('acv', 0.1562, '0.045 V, 3.0 kHz', 't197', 'u197', 10)
    Call('acv', 0.1562, '0.07 V, 0.02 kHz', 'v181', 'w181', 10)
    Call('acv', 0.1562, '0.07 V, 3.0 kHz', 'v197', 'w197', 10)
    Call('acv', 0.1562, '0.1 V, 0.02 kHz', 'x181', 'y181', 10)
    Call('acv', 0.1562, '0.1 V, 3.0 kHz', 'x197', 'y197', 10)
    # 200kHz 10B --------------------------------------------------------------------
    Callpar(200, '0000')
    Call('acv', 10, '0.35 V, 0.02 kHz', 'd213', 'e213', 3)
    Call('acv', 10, '0.35 V, 6.0 kHz', 'd229', 'e229', 3)
    Call('acv', 10, '1.4 V, 0.02 kHz', 'f213', 'g213', 3)
    Call('acv', 10, '1.4 V, 6.0 kHz', 'f229', 'g229', 3)
    Call('acv', 10, '2.8 V, 0.02 kHz', 'h213', 'i213', 3)
    Call('acv', 10, '2.8 V, 6.0 kHz', 'h229', 'i229', 3)
    Call('acv', 10, '4.9 V, 0.02 kHz', 'j213', 'k213', 3)
    Call('acv', 10, '4.9 V, 6.0 kHz', 'j229', 'k229', 3)
    Call('acv', 10, '6.7 V, 0.02 kHz', 'l213', 'm213', 3)
    Call('acv', 10, '6.7 V, 6.0 kHz', 'l229', 'm229', 3)
    # 200kHz 2.5B
    Callpar(200, '0100')
    Call('acv', 2.5, '0.085 V, 0.02 kHz', 'n213', 'o213', 3)
    Call('acv', 2.5, '0.085 V, 6.0 kHz', 'n229', 'o229', 3)
    Call('acv', 2.5, '0.35 V, 0.02 kHz', 'p213', 'q213', 3)
    Call('acv', 2.5, '0.35 V, 6.0 kHz', 'p229', 'q229', 3)
    Call('acv', 2.5, '0.7 V, 0.02 kHz', 'r213', 's213', 3)
    Call('acv', 2.5, '0.7 V, 6.0 kHz', 'r229', 's229', 3)
    Call('acv', 2.5, '1.2 V, 0.02 kHz', 't213', 'u213', 3)
    Call('acv', 2.5, '1.2 V, 6.0 kHz', 't229', 'u229', 3)
    Call('acv', 2.5, '1.6 V, 0.02 kHz', 'v213', 'w213', 3)
    Call('acv', 2.5, '1.6 V, 6.0 kHz', 'v229', 'w229', 3)
    # 200kHz 0.625B
    Callpar(200, '1000')
    Call('acv', 0.625, '0.02 V, 0.02 kHz', 'd245', 'e245', 3)
    Call('acv', 0.625, '0.02 V, 6.0 kHz', 'd261', 'e261', 3)
    Call('acv', 0.625, '0.085 V, 0.02 kHz', 'f245', 'g245', 3)
    Call('acv', 0.625, '0.085 V, 6.0 kHz', 'f261', 'g261', 3)
    Call('acv', 0.625, '0.17 V, 0.02 kHz', 'h245', 'i245', 3)
    Call('acv', 0.625, '0.17 V, 6.0 kHz', 'h261', 'i261', 3)
    Call('acv', 0.625, '0.29 V, 0.02 kHz', 'j245', 'k245', 3)
    Call('acv', 0.625, '0.29 V, 6.0 kHz', 'j261', 'k261', 3)
    Call('acv', 0.625, '0.4 V, 0.02 kHz', 'l245', 'm245', 3)
    Call('acv', 0.625, '0.4 V, 6.0 kHz', 'l261', 'm261', 3)
    # 200kHz 0.1562B
    Callpar(200, '1100')
    #Call('acv', 0.1562, '0.0005 V, 0.02 kHz', 'n245', 'o245', 100)
    #Call('acv', 0.1562, '0.0005 V, 6.0 kHz', 'n261', 'o261', 100)
    Call('acv', 0.1562, '0.005 V, 0.02 kHz', 'p245', 'q245', 100)
    Call('acv', 0.1562, '0.005 V, 6.0 kHz', 'p261', 'q261', 100)
    Call('acv', 0.1562, '0.022 V, 0.02 kHz', 'r245', 's245', 100)
    Call('acv', 0.1562, '0.022 V, 6.0 kHz', 'r261', 's261', 100)
    Call('acv', 0.1562, '0.045 V, 0.02 kHz', 't245', 'u245', 100)
    Call('acv', 0.1562, '0.045 V, 6.0 kHz', 't261', 'u261', 100)
    Call('acv', 0.1562, '0.07 V, 0.02 kHz', 'v245', 'w245', 100)
    Call('acv', 0.1562, '0.07 V, 6.0 kHz', 'v261', 'w261', 100)
    Call('acv', 0.1562, '0.1 V, 0.02 kHz', 'x245', 'y245', 100)
    Call('acv', 0.1562, '0.1 V, 6.0 kHz', 'x261', 'y261', 100)
    # 400kHz 10B ----------------------------------------------------------------------
    Callpar(400, '0000')
    Call('acv', 10, '0.35 V, 0.02 kHz', 'd277', 'e277', 5)
    Call('acv', 10, '0.35 V, 12.0 kHz', 'd293', 'e293', 5)
    Call('acv', 10, '1.4 V, 0.02 kHz', 'f277', 'g277', 5)
    Call('acv', 10, '1.4 V, 12.0 kHz', 'f293', 'g293', 5)
    Call('acv', 10, '2.8 V, 0.02 kHz', 'h277', 'i277', 5)
    Call('acv', 10, '2.8 V, 12.0 kHz', 'h293', 'i293', 5)
    Call('acv', 10, '4.9 V, 0.02 kHz', 'j277', 'k277', 5)
    Call('acv', 10, '4.9 V, 12.0 kHz', 'j293', 'k293', 5)
    Call('acv', 10, '6.7 V, 0.02 kHz', 'l277', 'm277', 5)
    Call('acv', 10, '6.7 V, 12.0 kHz', 'l293', 'm293', 5)
    # 400kHz 2.5B
    Callpar(400, '0100')
    Call('acv', 2.5, '0.085 V, 0.02 kHz', 'n277', 'o277', 5)
    Call('acv', 2.5, '0.085 V, 12.0 kHz', 'n293', 'o293', 5)
    Call('acv', 2.5, '0.35 V, 0.02 kHz', 'p277', 'q277', 5)
    Call('acv', 2.5, '0.35 V, 12.0 kHz', 'p293', 'q293', 5)
    Call('acv', 2.5, '0.7 V, 0.02 kHz', 'r277', 's277', 5)
    Call('acv', 2.5, '0.7 V, 12.0 kHz', 'r293', 's293', 5)
    Call('acv', 2.5, '1.2 V, 0.02 kHz', 't277', 'u277', 5)
    Call('acv', 2.5, '1.2 V, 12.0 kHz', 't293', 'u293', 5)
    Call('acv', 2.5, '1.6 V, 0.02 kHz', 'v277', 'w277', 5)
    Call('acv', 2.5, '1.6 V, 12.0 kHz', 'v293', 'w293', 5)
    # 400kHz 0.625B
    Callpar(400, '1000')
    Call('acv', 0.625, '0.02 V, 0.02 kHz', 'd309', 'e309', 10)
    Call('acv', 0.625, '0.02 V, 12.0 kHz', 'd325', 'e325', 10)
    Call('acv', 0.625, '0.085 V, 0.02 kHz', 'f309', 'g309', 10)
    Call('acv', 0.625, '0.085 V, 12.0 kHz', 'f325', 'g325', 10)
    Call('acv', 0.625, '0.17 V, 0.02 kHz', 'h309', 'i309', 10)
    Call('acv', 0.625, '0.17 V, 12.0 kHz', 'h325', 'i325', 10)
    Call('acv', 0.625, '0.29 V, 0.02 kHz', 'j309', 'k309', 10)
    Call('acv', 0.625, '0.29 V, 12.0 kHz', 'j325', 'k325', 10)
    Call('acv', 0.625, '0.4 V, 0.02 kHz', 'l309', 'm309', 10)
    Call('acv', 0.625, '0.4 V, 12.0 kHz', 'l325', 'm325', 10)
    # 400kHz 0.1562B
    Callpar(400, '1100')
    #Call('acv', 0.1562, '0.0005 V, 0.02 kHz', 'n309', 'o309', 100)
    #Call('acv', 0.1562, '0.0005 V, 12.0 kHz', 'n325', 'o325', 100)
    Call('acv', 0.1562, '0.005 V, 0.02 kHz', 'p309', 'q309', 100)
    Call('acv', 0.1562, '0.005 V, 12.0 kHz', 'p325', 'q325', 100)
    Call('acv', 0.1562, '0.022 V, 0.02 kHz', 'r309', 's309', 100)
    Call('acv', 0.1562, '0.022 V, 12.0 kHz', 'r325', 's325', 100)
    Call('acv', 0.1562, '0.045 V, 0.02 kHz', 't309', 'u309', 100)
    Call('acv', 0.1562, '0.045 V, 12.0 kHz', 't325', 'u325', 100)
    Call('acv', 0.1562, '0.07 V, 0.02 kHz', 'v309', 'w309', 100)
    Call('acv', 0.1562, '0.07 V, 12.0 kHz', 'v325', 'w325', 100)
    Call('acv', 0.1562, '0.1 V, 0.02 kHz', 'x309', 'y309', 100)
    Call('acv', 0.1562, '0.1 V, 12.0 kHz', 'x325', 'y325', 100)
# kz
if self.vardict_boo['cvar2'].get() == 1:
    Message('Подключите заглушку')
    Callpar(20, '0000')
    Call('acz', 10, '', 'f65', 'f65', 0.05)
    Callpar(20, '0100')
    Call('acz', 2.5, '', 'f66','f66', 0.05)
    Callpar(20, '1000')
    Call('acz', 0.625, '', 'f67','f67', 0.1)
    Callpar(20, '1100')
    Call('acz', 0.1562, '', 'f68','f68', 0.5)

if self.dac == 1:
    # DAC1
    if self.vardict_boo['cvar5'].get() == 1:
        Message('Подключите выход ЦАП1 к мультиметру')
        Callpar(20, '0000')
        Ldac('0 DC', 4750, 'b341', 'c341', 0.3)
        Ldac('0 DC', 4000, 'd341', 'e341', 0.3)
        Ldac('0 DC', 2000, 'f341', 'g341', 0.3)
        Ldac('0 DC', 1000, 'h341', 'i341', 0.3)
        Ldac('0 DC', 250, 'j341', 'k341', 0.3)
        Ldac('0 DC', 0.5, 'l341', 'm341', 0.3)
        Ldac('0 DC', -0.5, 'n341', 'o341', 0.3)
        Ldac('0 DC', -250, 'p341', 'q341', 0.3)
        Ldac('0 DC', -1000, 'r341', 's341', 0.3)
        Ldac('0 DC', -2000, 't341', 'u341', 0.3)
        Ldac('0 DC', -4000, 'v341', 'w341', 0.3)
        Ldac('0 DC', -4750, 'x341', 'y341', 0.3)
    # DAC2
    if self.vardict_boo['cvar6'].get() == 1:
        Message('Подключите выход ЦАП2 к мультиметру')
        Callpar(20, '0000')
        Ldac('1 DC', 4750, 'b342', 'c342', 0.3)
        Ldac('1 DC', 4000, 'd342', 'e342', 0.3)
        Ldac('1 DC', 2000, 'f342', 'g342', 0.3)
        Ldac('1 DC', 1000, 'h342', 'i342', 0.3)
        Ldac('1 DC', 250, 'j342', 'k342', 0.3)
        Ldac('1 DC', 0.5, 'l342', 'm342', 0.3)
        Ldac('1 DC', -0.5, 'n342', 'o342', 0.3)
        Ldac('1 DC', -250, 'p342', 'q342', 0.3)
        Ldac('1 DC', -1000, 'r342', 's342', 0.3)
        Ldac('1 DC', -2000, 't342', 'u342', 0.3)
        Ldac('1 DC', -4000, 'v342', 'w342', 0.3)
        Ldac('1 DC', -4750, 'x342', 'y342', 0.3)
Reset()
Message('Калибровка завершена')
