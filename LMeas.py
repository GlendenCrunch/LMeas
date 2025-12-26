#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import os
import re
import time
from datetime import datetime
import array
import json
import ctypes
from struct import pack
import csv
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import threading
from threading import Thread
from openpyexcel import load_workbook
from openpyexcel.styles import PatternFill
import pyvisa
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import numpy as np
import usb1

sem = threading.Semaphore()
COUNT = 1

Size = ctypes.pointer(ctypes.c_ulong(1000000))
Data = ctypes.pointer(ctypes.c_ushort())
Sync = ctypes.pointer(ctypes.c_ulong())

class LMeasGUI():
    """class GUI"""
    def __init__(self, parent):
        self.parent = parent
        self.folder_1 = os.getcwd()
        self.rg1 = [number for number in range(0,16) if number % 1 == 0]
        self.rg2 = ['E14', 'E-502']
        self.rg3 = ['DC', 'AC']
        self.rg4 = ['400.0', '200.0', '100.0', '49.0']
        self.rg4_e502 = ['0', '1', '9', '99', '199']     # 2MHz / dRate + 1
        self.rg5 = {'10.0': '0000', '2.5': '0100', '0.625': '1000', '0.1562': '1100'}
        self.rg5_e502 = {'10.0': '0', '5': '1', '2': '2', '1': '3', '0.5': '4', '0.2': '5'}

        self.varlist_str = ['name_protokol','temp','humi','press','custom','pover','dac1','dac2','freq','adc0',
        'adc1','adc2','adc3','adc4','adc5','adc6','adc7','adc8','adc9','adc10','adc11','adc12','adc13','adc14','adc15']
        self.vardict_str = {self.var: tk.StringVar() for self.var in self.varlist_str}

        self.varlist_boo = ['cvar1','cvar2','cvar3','cvar4','cvar5','cvar6','kvar1','kvar2','kvar3','kvar4','kvar5','kvar6',
        'kvar7','kvar8','kvar9','kvar10','kvar11','kvar12','kvar13','kvar14','kvar15','kvar16','kvar17','kvar18','kvar19', 'MP2017']
        self.vardict_boo = {self.var: tk.BooleanVar() for self.var in self.varlist_boo}
        for self.var in self.varlist_boo[:22]:
            self.vardict_boo[self.var].set(1)

        self.ar10b = ('arial', 10, 'bold')
        self.ar12b = ('arial', 12, 'bold')
        self.img1 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\pan1.gif')
        self.img2 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\check.gif')
        self.img3 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\error.png')
        self.img4 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\refresh.png')

        with open(f'{self.folder_1}\\setting.json','r', encoding='utf-8') as file_json:
            self.sett_json = json.load(file_json)
        with open(f'{self.folder_1}\\theme.json','r', encoding='utf-8') as file_json:
            self.theme_json = json.load(file_json)

        self.theme = self.theme_json[self.sett_json['theme']]
        self.sign_pribor = self.sett_json['sign_pribor']

        self.bg_colour = self.theme['.']['bg_colour']
        self.fg_colour = self.theme['.']['fg_colour']
        self.bg_button = self.theme['.']['bg_button']

        self.style = ttk.Style()
        self.style.theme_create('theme', settings=self.theme)
        self.style.theme_use('theme')

        parent.title('LMeas')
        parent.geometry('1000x490')
        parent.iconbitmap(f'{self.folder_1}\\icon\\icon.ico')
        parent.resizable(width=False, height=False)

        main_menu = tk.Menu(parent)
        parent.config(menu=main_menu)
        fmenu = tk.Menu(main_menu, tearoff=False)
        fmenu.add_separator()
        fmenu.add_command(label='Закрыть', command=parent.destroy)

        fsetting = tk.Menu(main_menu, tearoff=False)
        fsetting.add_command(label='Калибровка/Поверка', command=self.setting_win)
        fsetting.add_command(label='Стили', command=self.set_style_win)

        main_menu.add_cascade(label='Файл', menu=fmenu)
        main_menu.add_cascade(label='Протокол', command=self.protokol)
        main_menu.add_cascade(label='Настройки', menu=fsetting)
        main_menu.add_cascade(label='О программе', command=self.about_win)

        self.tabframe = tk.Frame(parent)
        self.rightframe = tk.Frame(parent)
        self.statusframe = tk.Frame(parent)

        self.tabframe.grid(row=0, column=0, ipadx = 110, ipady = 210, sticky="nsew")
        self.rightframe.grid(row=0, column=1, sticky="ns")
        self.statusframe.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.sb = tk.Scrollbar(self.rightframe, orient='vertical')
        self.lb = tk.Listbox(self.rightframe, selectmode='extended', width=39, height=20, relief='ridge')
        self.sb['command'] = self.lb.yview
        self.lb['yscroll'] = self.sb.set
        self.sb.pack(side='right', fill='y')
        self.lb.pack(side='right', fill='y')

        self.tab_control = ttk.Notebook(self.tabframe)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Соединение")
        self.tab_control.add(self.tab2, text="Поверка/калибровка")
        self.tab_control.add(self.tab3, text="Сбор данных")
        self.tab_control.pack(expand=1, fill='both')

        self.statusbar = tk.Label(self.statusframe, text="Статус: ожидание...", background="gray80", anchor='w')
        self.statusbar.pack(side='left', fill='x', expand=True)
        self.statusbar_1 = tk.Label(self.statusframe, text="I T L ©", background="gray80", anchor='e')
        self.statusbar_1.pack(side='right', fill='x')

        self.tree = ttk.Treeview(self.tab1, columns=['1', '2', '3', '4'], height=5)
        self.tree.heading('#0', text="", anchor='center')
        self.tree.heading('1', text="Наименовение", anchor='center')
        self.tree.heading('2', text="Тип", anchor='center')
        self.tree.heading('3', text="Зав. №", anchor='center')
        self.tree.heading('4', text="IDN?", anchor='center')
        self.tree.column('#0', stretch=False, anchor='center', minwidth=30, width=30)
        self.tree.column('1', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree.column('2', stretch=False, anchor='center', minwidth=100, width=100)
        self.tree.column('3', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree.column('4', stretch=False, anchor='center', minwidth=360, width=360)
        self.tree.place(x=5, y=290)

        self.lbf1 = tk.LabelFrame(self.tab1, text='LCARD', width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf1.place(x=5, y=5)
        self.lbf2 = tk.LabelFrame(self.tab1, text='Калибратор', width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf2.place(x=205, y=5)
        self.lbf3 = tk.LabelFrame(self.tab1, text='Мультиметр', width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf3.place(x=405, y=5)
        self.lbf4 = tk.LabelFrame(self.tab2, text='Параметры поверки', width=200, height=390, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf4.place(x=5, y=5)
        self.lbf5 = tk.LabelFrame(self.tab3, text='АЦП', width=350, height=165, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf5.place(x=5, y=45)
        self.lbf6 = tk.LabelFrame(self.tab3, text='ЦАП, мВ', width=350, height=180, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf6.place(x=5, y=220)
        self.lbf7 = tk.LabelFrame(self.tab3, text='Каналы АЦП, мВ', width=200, height=385, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf7.place(x=370, y=0)
        self.lbf8 = tk.LabelFrame(self.tab3, text='График, U(t)', width=155, height=180, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf8.place(x=545, y=0)

        self.canvas_1 = tk.Canvas(self.lbf5, width=35, height=35, bg=self.bg_colour, highlightthickness=1, highlightbackground=self.bg_colour)
        self.canvas_1.place(x=250, y=50)
        self.oval_1 = self.canvas_1.create_oval(10, 10, 30, 30, fill="white")

        self.lc_on = tk.Button(self.lbf1, text='Подключить', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_lcard)
        self.lc_on.place(x=35, y=80)
        self.lc_off = tk.Button(self.lbf1, text='Отключить', state='disabled', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.close_lc)
        self.lc_off.place(x=35, y=130)
        self.fluk_on = tk.Button(self.lbf2, text='Подключить', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_fluke_5500)
        self.fluk_on.place(x=35, y=130)
        self.dmm_on = tk.Button(self.lbf3, text='Подключить', state='disabled', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_dmm)
        self.dmm_on.place(x=35, y=130)
        self.fresh = tk.Button(self.tab1, image=self.img4, fg='#fff', bg=self.bg_button, command=self.pribor)
        self.fresh.place(x=690, y=240)
        self.start_on = tk.Button(self.tab2, text='► Старт', state='disabled', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.start)
        self.start_on.place(x=210, y=20)
        self.paus_on = tk.Button(self.tab2, text='▌▌ Пауза', state='disabled', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b)
        self.paus_on.place(x=350, y=20)
        self.meas_on = tk.Button(self.lbf5, text='Измерить', state='disabled', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.measure_adc)
        self.meas_on.place(x=10,y=105)
        self.set_dac = tk.Button(self.lbf6, text='Задать', state='disabled', width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.measure_dac)
        self.set_dac.place(x=10,y=120)
        self.draw_on = tk.Button(self.lbf8, text='Построить', state='disabled', width=13, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.graphic_adc)
        self.draw_on.place(x=5,y=70)
        self.draw_csv_on = tk.Button(self.lbf8, text='Построить CSV', width=13, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.graphic_adc_csv)
        self.draw_csv_on.place(x=5,y=110)

        self.combo_lcard = ttk.Combobox(self.lbf1, value=self.rg2, state='readonly', height=5, width=25)
        self.combo_lcard.current(0)
        self.combo_lcard.place(x=15, y=10)
        self.combo_dmm = ttk.Combobox(self.lbf3, state='readonly', height=5, width=25)
        self.combo_dmm.place(x=15, y=10)
        self.combo_flu = ttk.Combobox(self.lbf2, state='readonly', height=5, width=25)
        self.combo_flu.place(x=15, y=10)
        self.combo_rez = ttk.Combobox(self.tab3, value=self.rg3, state='readonly', height=4, width=10)
        self.combo_rez.place(x=135,y=10)
        self.combo_rez.current(0)
        self.combo_frq = ttk.Combobox(self.lbf5, state='readonly', height=4, width=10)
        self.combo_frq.place(x=130,y=10)
        self.combo_amp = ttk.Combobox(self.lbf5, state='readonly', height=4, width=10)
        self.combo_amp.place(x=130,y=40)
        self.combo_ch = ttk.Combobox(self.lbf8, value=self.rg1, state='readonly', height=4, width=5)
        self.combo_ch.place(x=10,y=15)
        self.combo_ch.current(0)

        self.lab3 = tk.Label(self.tab2, text='Тип:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab3.place(x=10,y=30)
        self.lab4 = tk.Label(self.tab2, text='Зав.№:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab4.place(x=10,y=60)
        self.lab5 = tk.Label(self.tab2, text='Температура,°C:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab5.place(x=10,y=110)
        self.lab6 = tk.Label(self.tab2, text='Влажность,%:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab6.place(x=10,y=140)
        self.lab7 = tk.Label(self.tab2, text='Давление,кПа:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab7.place(x=10,y=170)
        self.lab8 = tk.Label(self.tab2, text='Заказчик:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab8.place(x=10,y=200)
        self.lab9 = tk.Label(self.tab2, text='Поверитель:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab9.place(x=10,y=230)
        self.lab10 = tk.Label(self.tab1, text='Название протокола:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab10.place(x=20,y=230)
        self.lab11 = tk.Label(self.tab3, text='Режим АЦП/ЦАП:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab11.place(x=15,y=10)
        self.lab12 = tk.Label(self.lbf5, text='Частота, кГц:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab12.place(x=10,y=10)
        self.lab13 = tk.Label(self.lbf5, text='Усиление:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab13.place(x=10,y=40)
        self.lab14 = tk.Label(self.lbf5, text='Кол-во циклов:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab14.place(x=10,y=70)
        self.lab15 = tk.Label(self.lbf8, text='канал', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab15.place(x=70,y=15)
        self.lab16 = tk.Label(self.lbf6, text='Частота, Гц:', bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab16.place(x=5,y=80)

        self.entry1 = ttk.Entry(self.tab1, textvariable=self.vardict_str['name_protokol'], width=55, font=self.ar10b)
        self.entry1.place(x=170, y=230)
        self.entry2 = ttk.Entry(self.tab2, textvariable=self.vardict_str['temp'], width=10, font='arial 8')
        self.entry2.place(x=130, y=110)
        self.entry3 = ttk.Entry(self.tab2, textvariable=self.vardict_str['humi'], width=10, font='arial 8')
        self.entry3.place(x=130, y=140)
        self.entry4 = ttk.Entry(self.tab2, textvariable=self.vardict_str['press'], width=10, font='arial 8')
        self.entry4.place(x=130, y=170)
        self.entry5 = ttk.Entry(self.tab2, textvariable=self.vardict_str['custom'], width=10, font='arial 8')
        self.entry5.place(x=130, y=200)
        self.entry6 = ttk.Entry(self.tab2, textvariable=self.vardict_str['pover'], width=10, font='arial 8')
        self.entry6.place(x=130, y=230)
        self.ent_loop = ttk.Entry(self.lbf5, width=11, font='arial 10')
        self.ent_loop.insert(tk.END, 10)
        self.ent_loop.place(x=130,y=70)
        self.ent_dac1 = ttk.Entry(self.lbf6, textvariable=self.vardict_str['dac1'], width=10, font='arial 9')
        self.ent_dac1.place(x=130,y=5)
        self.ent_dac2 = ttk.Entry(self.lbf6, textvariable=self.vardict_str['dac2'], width=10, font='arial 9')
        self.ent_dac2.place(x=130,y=45)
        self.ent_freq = ttk.Entry(self.lbf6, textvariable=self.vardict_str['freq'], width=10, font='arial 9')
        self.ent_freq.place(x=130,y=80)

        self.entry_widget(self.lbf7, 16, [self.vardict_str['adc0'],self.vardict_str['adc1'],self.vardict_str['adc2'],self.vardict_str['adc3'],
        self.vardict_str['adc4'],self.vardict_str['adc5'],self.vardict_str['adc6'],self.vardict_str['adc7'],self.vardict_str['adc8'],
        self.vardict_str['adc9'],self.vardict_str['adc10'],self.vardict_str['adc11'],self.vardict_str['adc12'],self.vardict_str['adc13'],self.vardict_str['adc14'],self.vardict_str['adc15']])

        self.checkbut_widget(self.lbf7, 16, ["0 канал: ","1 канал: ","2 канал: ","3 канал: ","4 канал: ","5 канал: ",
            "6 канал: ", "7 канал: ", "8 канал: ", "9 канал: ", "10 канал: ", "11 канал: ", "12 канал: ", "13 канал: ",
            "14 канал: ", "15 канал: "], [self.vardict_boo['kvar1'],self.vardict_boo['kvar2'],self.vardict_boo['kvar3'],self.vardict_boo['kvar4'],
            self.vardict_boo['kvar5'],self.vardict_boo['kvar6'],self.vardict_boo['kvar7'],self.vardict_boo['kvar8'],self.vardict_boo['kvar9'],
            self.vardict_boo['kvar10'],self.vardict_boo['kvar11'],self.vardict_boo['kvar12'],self.vardict_boo['kvar13'],self.vardict_boo['kvar14'],self.vardict_boo['kvar15'],self.vardict_boo['kvar16']])

        self.chkbtn_1 = tk.Checkbutton(self.lbf1, bg="#848a98", activebackground="#848a98", text="МП 2017", variable=self.vardict_boo['MP2017'], onvalue=1, offvalue=0, font=self.ar10b)
        tk.Checkbutton(self.lbf6, text="ЦАП 1:", variable=self.vardict_boo['kvar17'], onvalue=1, offvalue=0, bg=self.bg_colour, activebackground=self.bg_colour).place(x=5,y=5)
        tk.Checkbutton(self.lbf6, text="ЦАП 2:", variable=self.vardict_boo['kvar18'], onvalue=1, offvalue=0, bg=self.bg_colour, activebackground=self.bg_colour).place(x=5,y=45)
        tk.Checkbutton(self.lbf5, text="Запись в CSV", variable=self.vardict_boo['kvar19'], onvalue=1, offvalue=0, bg=self.bg_colour, activebackground=self.bg_colour).place(x=230,y=10)

        self.lb2 = tk.Listbox(self.tab2, selectmode='extended', width=47, height=3, relief='ridge', fg='blue', font=("Arial", 15, 'bold'))
        self.lb2.place(x=210, y=70)

        self.progress1 = ttk.Progressbar(self.tab2, orient='horizontal', mode='determinate', length=730, value=0)
        self.progress1.place(x=5, y=395)

    def date_time(self):
        today = datetime.today()
        self.data_today = today.strftime('%d-%m-%Y,%H-%M-%S')

    def protokol(self):
        rep = filedialog.askopenfilenames(parent=self.parent, initialdir=f'{self.folder_1}\\Protocol\\',
                                          initialfile='',
                                          filetypes=[("xlsx", "*.xlsx"),("All files", "*")])
        try:
            os.startfile(rep[0])
        except IndexError:
            self.lb.insert('end', 'Файл протокола не выбран')

    def win_one(self, name_win, size_win):
        self.top = tk.Toplevel(self.parent)
        self.top.title(name_win)
        self.top.iconbitmap(f'{self.folder_1}\\icon\\icon.ico')
        self.top.resizable(0, 0)
        w = self.top.winfo_screenwidth()
        h = self.top.winfo_screenheight()
        w = w // 3
        h = h // 2
        w = w - 200
        h = h - 200
        self.top.geometry(size_win.format(w, h))

    def about_win(self):
        self.win_one('О программе', '500x300+{}+{}')
        text1 = ('LMeas v1.14\rDate: 2022-12-02\rAutor: g1enden (I T L)')
        text2 = ('Поддерживаемые L-CARD:\rE14-440\rE14-440D\rE-502')

        top_1 = tk.Frame(self.top, height=70, relief="raise")
        top_1.pack(side='top', fill='x')
        top_2 = tk.Frame(self.top, height=30, relief="raise")
        top_2.pack(side='top', fill='x')

        img_about = tk.Label(top_1, image=self.img1)
        img_about.place(x=10,y=10)
        autor = tk.Label(top_1, justify='left', text=text1, font=self.ar10b, foreground='deepskyblue4')
        autor.place(x=260,y=5)
        support = tk.Label(top_2, justify='center', text=text2, font=self.ar10b, foreground='deepskyblue4')
        support.grid(row=0, column=0)
        _button = tk.Button(self.top, text='OK', width=10, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.top.destroy)
        _button.place(x=200,y=250)

    def checkbut_widget(self, frm, rng_i, ch_text, ch_var):
        for i in range(rng_i):
            tk.Checkbutton(frm, text=ch_text[i], variable=ch_var[i], onvalue=1, offvalue=0, bg=self.bg_colour, activebackground=self.bg_colour).grid(row=i, column=0, sticky="w")

    def entry_widget(self, frm, rng_i, ch_text):
        for i in range(rng_i):
            ttk.Entry(frm, textvariable=ch_text[i], state='readonly', width=10, font='arial 9').grid(row=i, column=1, sticky="w")

    def setting_win(self):
        self.win_one('Настройки', '220x250+{}+{}')
        try:
            self.checkbut_widget(self.top, 6, ["DC","Заглушка","AC: 0 канал","AC","ЦАП1","ЦАП2"],
                [self.vardict_boo['cvar1'],self.vardict_boo['cvar2'],self.vardict_boo['cvar3'],self.vardict_boo['cvar4'],self.vardict_boo['cvar5'],self.vardict_boo['cvar6']])
        except AttributeError:
            clab = tk.Label(self.top, text='Прибор не определён', font='arial 13', foreground='deepskyblue4')
            clab.pack(anchor='w')

        _button = tk.Button(self.top, text="OK", width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.top.destroy)
        _button.place(x=40,y=210)

    def set_style_win(self):
        self.win_one('Стили', '350x300+{}+{}')
        lab_style = tk.Label(self.top, text='Цветовая тема:', font=self.ar10b)
        lab_style.place(x=20,y=15)
        combo_style = ttk.Combobox(self.top, state='readonly', values=['Dark', 'Light'], height=5, width=25)
        combo_style.current(0)
        combo_style.place(x=150, y=15)
        lab_lang = tk.Label(self.top, text='Язык:', font=self.ar10b)
        lab_lang.place(x=20,y=45)
        combo_lang = ttk.Combobox(self.top, state='readonly', values=['Russia', 'English'], height=5, width=25)
        combo_lang.current(0)
        combo_lang.place(x=150, y=45)

        def set_ok():
            self.sett_json['language'] = combo_lang.get()
            self.sett_json['theme'] = combo_style.get()

            with open(f'{self.folder_1}\\setting.json', 'w', encoding='utf-8') as file_json:
                json.dump(self.sett_json, file_json, ensure_ascii=False, indent=4, sort_keys=True)

            self.parent.destroy()
            try:
                self.inst_dmm.close()
                self.inst_fluke.close()
            except AttributeError:
                print ('Стиль изменён')
            os.system(f'{self.folder_1}\\LMeas.py')

        _button = tk.Button(self.top, text="Применить", width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=set_ok)
        _button.place(x=120,y=250)

    def cnt(self):
        e440_1 = sum(1 for line in open(f'{self.folder_1}\\file_py\\e440d.py', encoding='utf-8') if line.lstrip().startswith('Call('))
        e440_2 = sum(1 for line in open(f'{self.folder_1}\\file_py\\e440d.py', encoding='utf-8') if line.lstrip().startswith('Ldac('))
        e440_3 = e440_1 + e440_2
        e140_1 = sum(1 for line in open(f'{self.folder_1}\\file_py\\e140.py', encoding='utf-8') if line.lstrip().startswith('Call('))
        e140_2 = sum(1 for line in open(f'{self.folder_1}\\file_py\\e140.py', encoding='utf-8') if line.lstrip().startswith('Ldac('))
        e140_3 = e140_1 + e140_2
        e502_1 = sum(1 for line in open(f'{self.folder_1}\\file_py\\e502.py', encoding='utf-8') if line.lstrip().startswith('Call('))
        e502_2 = sum(1 for line in open(f'{self.folder_1}\\file_py\\e502.py', encoding='utf-8') if line.lstrip().startswith('Ldac('))
        e502_3 = e502_1 + e502_2
        return {'E440':e440_1, 'E440D':e440_3, 'E140':e140_1, 'E140D':e140_3,'E502':e502_3}

    def visa_search(self):
        #self.rm = pyvisa.ResourceManager(visa_library='C:/Program Files/IVI Foundation/VISA/Win64/agvisa/agbin/visa32.dll')
        self.rm = pyvisa.ResourceManager()
        self.rm_list = list(self.rm.list_resources())
        return self.rm_list

    def decay_cycle(self, rm):
        for j, _ in enumerate(self.sign_pribor):
            if re.search(list(self.sign_pribor.keys())[j], rm):
                rm = list(self.sign_pribor.values())[j]
        return rm

    def adres_cycle(self, combo_dmm, rm):
        for j, _ in enumerate(self.sign_pribor):
            if combo_dmm == list(self.sign_pribor.values())[j]:
                adres = list(filter(lambda rmt: list(self.sign_pribor.keys())[j] in rmt, rm))
                if len(adres) > 0:
                    return adres

        if combo_dmm[:4] in ('ASRL', 'USB0', 'TCPI'):
            return [combo_dmm]

    def pribor(self):
        self.lb.delete(0, 'end')
        self.lb.insert('end', 'Обнаруженные приборы и порты:')
        self.lb.itemconfig('end', bg='light cyan')
        self.visa_search()
        decay_list = list(map(self.decay_cycle, self.rm_list))
        self.lb.insert('end', *decay_list)
        self.combo_dmm.configure(values=decay_list)
        #self.combo_dmm.current(0)
        self.combo_flu.configure(values=decay_list)
        #self.combo_flu.current(0)
        self.tree.delete(*self.tree.get_children())
        self.chkbtn_1.place(x=0,y=240)

    def connect_lcard(self):
        if self.combo_lcard.get() == 'E14':
            self.connect_lcard_e14()
        elif self.combo_lcard.get() == 'E-502':
            self.connect_lcard_e502()

    def connect_lcard_e14(self):
        self.wl = ctypes.CDLL('libr\\wlcomp.dll')
        #self.wl = ctypes.cdll.wlcomp
        hDll = ctypes.pointer(ctypes.c_ulong(self.wl.LoadAPIDLL('libr\\lcomp.dll'.encode('ascii'))))
        hErr = ctypes.pointer(ctypes.c_ulong())
        self.hIfc = ctypes.pointer(ctypes.c_ulong(self.wl.CallCreateInstance(hDll, 0, hErr)))
        print ('hDll', hDll.contents.value)
        print ('hIfc', self.hIfc.contents.value)
        print ('hErr', hErr.contents.value)

        Open = ctypes.pointer(ctypes.c_ulonglong(self.wl.OpenLDevice(self.hIfc)))
        print ('Open', Open.contents.value)

        Bios = ctypes.pointer(ctypes.c_ulong(self.wl.LoadBios(self.hIfc, 'libr\\E440')))
        print ('Bios', Bios.contents.value)

        Test = ctypes.pointer(ctypes.c_ulong(self.wl.PlataTest(self.hIfc)))
        print ('Test', Test.contents.value)

        sl = ctypes.pointer(Slot())
        self.wl.GetSlotParam(self.hIfc, sl)
        print ('Slot', hex(sl.contents.BoardType))

        pd = ctypes.pointer(Read())
        print ('ReadPlataDescr', self.wl.ReadPlataDescr(self.hIfc, pd))
        self.bn = pd.contents.BrdName.decode('utf-8')
        self.sn = pd.contents.SerNum.decode('utf-8')
        self.dac = ord(pd.contents.IsDacPresent)

        self.wl.RequestBufferStream(self.hIfc, Size, 1)     # L_STREAM_ADC = 1
        print ('Allocated memory size(word):', Size[0])
        self.combo_frq.configure(value=self.rg4)
        self.combo_frq.current(0)
        self.combo_amp.configure(value=list(self.rg5.keys()))
        self.combo_amp.current(0)
        if self.dac == 1:
            self.bn = self.bn + 'D'
            self.set_dac.configure(state='normal')
            self.dmm_on.configure(state='normal')
        else:
            self.set_dac.configure(state='disabled')
        self.connect_lcard_set(self.bn, self.sn)
        self.draw_on.configure(state='normal')
        self.chkbtn_1.place(x=10,y=40)

    def close_lc(self):
        try:
            if self.bn in ('E440', 'E440D'):
                print ('StopDevice', self.wl.StopLDevice(self.hIfc))
                print ('CloseDevice', self.wl.CloseLDevice(self.hIfc))
            elif self.bn == 'E502':
                self.context.close()
        except AttributeError:
            pass
        self.lc_on.configure(state='normal')
        self.lc_off.configure(state='disabled')
        self.dmm_on.configure(state='disabled')
        self.start_on.configure(state='disabled')

    def exit_lmeas(self):
        self.close_lc()
        self.parent.destroy()

    def connect_lcard_e502(self):
        pp = ctypes.pointer(Read_x502())
        pp2 = ctypes.pointer(t_x502_info())
        self.lib = ctypes.cdll.LoadLibrary('libr\\e502api.dll')
        self.lib2 = ctypes.cdll.LoadLibrary('libr\\x502api.dll')
        self.Create = self.lib2.X502_Create()
        Open = self.lib.E502_OpenUsb(self.Create, 0)
        self.lib2.X502_Close(self.Create)
        # ------------------------------------------
        self.context = usb1.USBContext()
        self.handle = self.context.openByVendorIDAndProductID(0x2A52,0xE502)
        self.handle.claimInterface(0)
        info_e502_0 = self.handle.controlRead(0xC0, 0x80, 0, 0, 80)
        info_e502_1 = info_e502_0.decode('UTF-8')
        self.bn = info_e502_1[0:4]
        self.sn = info_e502_1[32:40]
        self.combo_frq.configure(value=self.rg4_e502)
        self.combo_frq.current(0)
        self.combo_amp.configure(value=list(self.rg5_e502.keys()))
        self.combo_amp.current(0)
        self.set_dac.configure(state='normal')
        self.dmm_on.configure(state='normal')
        self.connect_lcard_set(self.bn, self.sn)

    def connect_lcard_set(self, bord_name, ser_num):
        print(f'Тип: {bord_name}')
        print(f'Зав.№: {ser_num}')
        self.date_time()
        self.vardict_str['name_protokol'].set(f'{self.data_today},{bord_name},{ser_num}.xlsx')
        self.b14 = f'LCARD {bord_name} №{ser_num} подключена'
        self.tree.insert('', 'end', text='', image=self.img2, values=('LCARD', bord_name, ser_num, ''))
        self.lab3['text'] = f'Тип: {bord_name}'
        self.lab4['text'] = f'Зав.№: {ser_num}'
        self.lb.insert('end', self.b14)
        self.lb.see('end')
        self.lb.itemconfig('end', bg = 'light cyan')
        self.lc_on.configure(state='disabled')
        self.lc_off.configure(state='normal')
        self.start_on.configure(state='normal')
        self.meas_on.configure(state='normal')

    def connect_dmm(self):
        self.inst_dmm = self.rm.open_resource(self.adres_cycle(self.combo_dmm.get(), self.rm_list)[0])
        if self.combo_dmm.get()[:4] in ('ASRL', 'USB0', 'TCPI'):
            self.inst_dmm.write('SYST:REM')
            time.sleep(1)

        self.data_0 = self.inst_dmm.query("*IDN?")
        self.connect_pribor_set('Мультиметр', 'light cyan')

    def connect_fluke_5500(self):
        try:
            self.inst_fluke = self.rm.open_resource(self.combo_flu.get(), baud_rate=9600, data_bits=8, write_termination='\r', read_termination='\r')
            time.sleep(1)
            self.inst_fluke.write('*IDN?')
            self.data_0 = self.inst_fluke.read()
            self.connect_pribor_set('Калибратор', 'light cyan')
            if self.b1[1] == 'N4-56':
                self.calbr = self.sett_json['N4-56']
            elif self.b1[1] in ('5522A', '5500E'):
                self.calbr = self.sett_json['5522A']
        except:
            self.lb.insert('end', 'Ошибка: Калибратор не определён')
            self.lb.itemconfig('end', bg='salmon')

    def connect_pribor_set(self, name_pribor, color):
        self.b1 = self.data_0.split(',')
        self.b10 = f'{name_pribor} {self.b1[1]} подключен'
        self.lb.insert('end', self.b10)
        self.lb.see('end')
        self.lb.itemconfig('end', bg = color)
        self.tree.insert('', 'end', text='', image=self.img2, values=(self.b10.split(' ')[0], self.b1[1], self.b1[2], self.data_0))

    def change_rows(self, cel_1, data_1, cel_2, data_accur, numb_accur):
        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == cel_1:
                    cell.value = data_1
                if cell.value == cel_2:
                    cell.value = data_accur
                    colour = PatternFill(start_color='FFFFDAB9', end_color='FFFFDAB9', fill_type='solid')
                    if data_accur > numb_accur or data_accur < -numb_accur:
                        cell.fill = colour

    def border_cell(self):
        self.wb.save('{}\\Protocol\\{}'.format(self.folder_1,self.vardict_str['name_protokol'].get()))
        time.sleep(1)
        self.progress1.step(1)

    def start(self):
        if self.vardict_boo['gost'].get() == 1:
            self.bn = 'E440_2017'
        self.progress1.configure(maximum = self.cnt()[self.bn])
        self.lb.insert('end', f'Время начала: {self.data_today[11:]}')
        self.wb = load_workbook(f'{self.folder_1}\\shablon\\{self.bn}.xlsx')
        self.ws = self.wb.active
        with open(f'{self.folder_1}\\file_py\\{self.bn}.py', encoding='utf-8') as lc_file:
            exec(lc_file.read())

    def graphic_adc(self):
        fig = figure(1)
        ax1 = fig.add_subplot(211)
        ax1.plot(y2[int(self.combo_ch.get())], x2[int(self.combo_ch.get())])
        ax1.grid(True)
        #ax1.set_xlim((0, 0.5))
        ax1.set_ylabel('U, V')
        l1=ax1.set_title('t, sec')
        l1.set_color('g')
        l1.set_fontsize('large')
        show()

    def graphic_adc_csv(self):
        data_plot = np.genfromtxt(f'{self.folder_1}\\csv\\lcard_phase.csv', delimiter=',', names=['phase1', 'phase2', 'phase3', 'time_phase'])
        plt.plot(data_plot['time_phase'], data_plot['phase1'], data_plot['time_phase'], data_plot['phase2'], data_plot['time_phase'], data_plot['phase3'])
        plt.title('L-CARD graph from csv')
        plt.ylabel('Voltage, mV')
        plt.xlabel('time, sec')
        #plt.xlim(0, 0.02)
        #plt.ylim(0, 2.5)
        plt.show()

    def measure_adc(self):
        if self.bn in ('E440', 'E440D', 'E440_2017'):
            Callpar(float(self.combo_frq.get()), self.rg5.get(self.combo_amp.get()))
            Meas_adc(float(self.combo_amp.get()), int(self.ent_loop.get()))
        elif self.bn == 'E502':
            Callpar(int(self.combo_frq.get()), int(self.rg5_e502.get(self.combo_amp.get())))
            Meas_adc(float(self.combo_amp.get()), int(self.ent_loop.get()))

    def measure_dac(self):
        if self.bn == 'E440D':
            if self.vardict_boo['kvar17'].get() == 1:
                Meas_dac('0 DC', float(self.ent_dac1.get()))
            if self.vardict_boo['kvar18'].get() == 1:
                Meas_dac('1 DC', float(self.ent_dac2.get()))
        elif self.bn == 'E502':
            if self.combo_rez.get() == 'DC':
                if self.vardict_boo['kvar17'].get() == 1:
                    Meas_dac('16 DC', float(self.ent_dac1.get()))
                if self.vardict_boo['kvar18'].get() == 1:
                    Meas_dac('32 DC', float(self.ent_dac2.get()))
            if self.combo_rez.get() == 'AC':
                if self.vardict_boo['kvar17'].get() == 1:
                    Meas_dac('16 AC', float(self.ent_dac1.get()), float(my_gui.ent_freq.get()))
                if self.vardict_boo['kvar18'].get() == 1:
                    Meas_dac('32 AC', float(self.ent_dac2.get()), float(my_gui.ent_freq.get()))
# ====================================================================================
class Callpar(Thread):
    def __init__(self, dRate, Amp):
        Thread.__init__(self)
        self.dRate = dRate
        self.Amp = Amp
        self.start()

    def callpar_e14(self):
        global fr
        global N
        pp = ctypes.pointer(Wadc_par_0())
        pp.contents.s_Type = 1          # L_ADC_PARAM = 1
        pp.contents.AutoInit = 1
        pp.contents.dRate = self.dRate  # задаём чаcтоту
        pp.contents.dKadr = 0.0
        pp.contents.dScale = 0.0
        pp.contents.SynchroType = 0
        pp.contents.SynchroSensitivity = 0
        pp.contents.SynchroMode = 0
        pp.contents.AdChannel = 0
        pp.contents.AdPorog = 0
        pp.contents.NCh = 16

        get_bin = lambda x, n: format(x, 'b').zfill(n)
        for p in range(16):
            j = get_bin(p, 4)           # перебор каналов
            k4 = int(self.Amp + j, 2)   # задаём усиление
            pp.contents.Chn[p] = k4

        pp.contents.FIFO = 4096
        pp.contents.IrqStep = 4096
        pp.contents.Pages = 32
        pp.contents.IrqEna = 1
        pp.contents.AdcEna = 1

        my_gui.wl.FillDAQparameters(my_gui.hIfc, pp, 2)

        my_gui.wl.SetParametersStream(my_gui.hIfc, pp, 2, Size,
                               ctypes.cast(ctypes.pointer(Data), ctypes.POINTER(ctypes.c_void_p)),
                               ctypes.cast(ctypes.pointer(Sync), ctypes.POINTER(ctypes.c_void_p)), 1)   # L_STREAM_ADC = 1

        fr = pp.contents.dRate * 1000   #Hz
        N = pp.contents.NCh

    def callpar_e502(self):
        global number_ch
        number_ch = 15
        data_ch_writ = my_gui.handle.controlWrite(0x40, 0x11, 0x200+0x100, 0, pack( "I", number_ch))    # кол-во каналов

        j = 8 * number_ch + self.Amp        # Amp - усиление (0:10V; 1:5V; 2:2V; 3:1V; 4:0,5V; 5:0,2V)
        for i in range(number_ch + 1):
            data_table_writ = my_gui.handle.controlWrite(0x40, 0x11, 512 + i, 0, pack( "I", j))         # таблица настроек 0x200+0x0
            j -= 8
                                                                        # делитель частоты (2MHz / self.dRate + 1)
        data_freq1_writ = my_gui.handle.controlWrite(0x40, 0x11, 0x200+0x102, 0, pack( "I", self.dRate))  # O_HARD
        data_freq2_writ = my_gui.handle.controlWrite(0x40, 0x11, 0x400+0x12, 0, pack( "I", self.dRate))   # IO_ARITH

    def run(self):
        sem.acquire()
        if my_gui.bn in ('E440', 'E440D', 'E440_2017'):
            self.callpar_e14()
        elif my_gui.bn == 'E502':
            self.callpar_e502()
        sem.release()
# ============================= Meas-E502-E14 =======================================================
class Meas_adc(Thread):
    def __init__(self, pred, nloop):
        Thread.__init__(self)
        self.pred = pred
        self.nloop = nloop
        self.start()

    def smooth(self, y, box_pts):
        box = np.ones(box_pts) / box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth

    def two2dec(self, s):
        if s[0] == '1':
            return -1 * (int(''.join('1' if x == '0' else '0' for x in s), 2) + 1)
        else:
            return int(s, 2)

    def start_meas_e502(self, pts, smooth_pts):
        thread_start = my_gui.handle.controlWrite(0x40, 0x12, 0, 0, pack( "I", 1))                 # запуск потока на ввод
        data_synch_writ = my_gui.handle.controlWrite(0x40, 0x11, 0x400+0x19, 0, pack( "I", 1))     # IN_STREAM_ENABLE
        data_preload_adc = my_gui.handle.controlWrite(0x40, 0x11, 0x200+0x10C, 0, pack( "I", 1))   # запись 1 в регистр 0x10C
        data_preload_adc = my_gui.handle.controlWrite(0x40, 0x11, 0x200+0x10C, 0, pack( "I", 1))   # запись 1 в регистр 0x10C
        data_syn_wrt = my_gui.handle.controlWrite(0x40, 0x11, 0x200+0x10A, 0, pack( "I", 1))       # запуск синхронного ввода-вывода

        self.point = pts
        self.smooth_pts = smooth_pts
        size_data_bulk = (4 * (number_ch + 1)) * 8      # 512
        buff = array.array('f', ())                     # общий буффер
        while len(buff) != self.point:
            data_read = my_gui.handle.bulkRead(0x1, size_data_bulk)
            #print (data_read)
            j = 0
            while j < len(data_read):
                x0 = bin(data_read[j])[2:].zfill(8)
                x1 = bin(data_read[j + 1])[2:].zfill(8)
                x2 = bin(data_read[j + 2])[2:].zfill(8)
                x3 = data_read[j + 3] - 192
                data_lc = ((self.two2dec(x2 + x1 + x0) / 6000000) * self.pred)
                buff.append(data_lc)
                j += 4

        data_syn_wrt = my_gui.handle.controlWrite(0x40, 0x11, 0x200+0x10A, 0, pack( "I", 0))       # остановка синхронного ввода-вывода
        thread_stop = my_gui.handle.controlWrite(0x40, 0x13, 0, 0, pack( "I", 1))                  # остановка потока на ввод

        x5 = array.array('f', ())
        self.x6 = [array.array('f', ()) for _ in range(number_ch + 1)]
        for k in range(number_ch + 1):
            j = k
            while j < self.point:
                x5.append(buff[j])
                j += number_ch + 1
            self.x6[k] = self.smooth(x5, self.smooth_pts)
            x5 = array.array('f', ())

    def start_meas_e14(self):
        global x2
        global y2
        my_gui.wl.EnableCorrection(my_gui.hIfc, 1)
        my_gui.wl.InitStartLDevice(my_gui.hIfc)
        my_gui.wl.StartLDevice(my_gui.hIfc)

        if my_gui.vardict_boo['kvar19'].get() == 1:
            fieldnames = ['phase1', 'phase2', 'phase3', 'time_phase']
            csvfile =  open(f'{my_gui.folder_1}\\csv\\lcard_phase.csv', 'w', newline='')
            write = csv.DictWriter(csvfile, fieldnames = fieldnames)
            write.writeheader()
            t1 = time.time()

        point = 32768
        V = self.nloop
        y = array.array('f', ())
        y2 = [array.array('f', ()) for _ in range(N)]
        x1 = array.array('f', ())
        x2 = [array.array('f', ()) for _ in range(N)]

        for _ in range(V):
            for k in range(N):
                i = k
                while i < point:
                    if Data[i] < 10000:
                        data_lc = Data[i] * (self.pred / 8000)
                    else:
                        data_lc = (Data[i] - 65536) * (self.pred / 8000)
                    x1.append(data_lc)
                    y.append(i / fr)
                    i += N
                x2[k] = x1
                y2[k] = y
                x1 = array.array('f', ())
                y = array.array('f', ())

            self.var_ent = array.array('f', ())
            for k in range(N):
                if my_gui.combo_rez.get() == 'DC':
                    data_adc = sum(x2[k]) / (point / N)
                if my_gui.combo_rez.get() == 'AC':
                    data_adc = (max(x2[k]) - min(x2[k])) / (1.4142135 * 2)
                data_adc = round(data_adc, 5)
                self.var_ent.append(data_adc * 1000)
                print ('Chn', k, data_adc)

            if my_gui.vardict_boo['kvar19'].get() == 1:
                t2 = time.time()
                write.writerow({'phase1': self.var_ent[1], 'phase2': self.var_ent[2], 'phase3': self.var_ent[15], 'time_phase': t2 - t1})

        my_gui.wl.StopLDevice(my_gui.hIfc)

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = 'Статус: измерение...'
        my_gui.meas_on.configure(state='disabled')
        my_gui.canvas_1.itemconfig(my_gui.oval_1, fill="green")

        if my_gui.bn in ('E440', 'E440D', 'E440_2017'):
            self.start_meas_e14()
        elif my_gui.bn == 'E502':
            self.start_meas_e502(8192*(number_ch + 1)*(16 - number_ch), 1)
            self.var_ent = array.array('f', ())
            for k in range(number_ch + 1):
                if my_gui.combo_rez.get() == 'DC':
                    data_adc = sum(self.x6[k]) / (self.point / (number_ch + 1))
                elif my_gui.combo_rez.get() == 'AC':
                    data_adc = (math.sqrt(sum(i*i for i in self.x6[k][819:]) / len(self.x6[k][819:])))
                self.var_ent.append(data_adc * 1000)
                print ('Chn', k, data_adc)
        
        for i in range(16):
            if my_gui.vardict_boo['kvar'+str(i+1)].get() == 1:
                my_gui.vardict_str['adc'+str(i)].set(str(self.var_ent[i]))

        my_gui.canvas_1.itemconfig(my_gui.oval_1, fill="white")
        my_gui.statusbar["text"] = 'Статус: ожидание...'
        my_gui.meas_on.configure(state='normal')
        sem.release()
# ============================= Callibration-E502-E14 ====================================
class Call(Meas_adc):
    def __init__(self, rez, pred, volt1, cell1, cell2, accurancy):
        Thread.__init__(self)
        self.rez = rez
        self.pred = pred
        self.volt1 = volt1
        self.cell1 = cell1
        self.cell2 = cell2
        self.accurancy = accurancy
        self.start()

    def call_e14(self):
        my_gui.wl.EnableCorrection(my_gui.hIfc, 1)
        my_gui.wl.InitStartLDevice(my_gui.hIfc)
        my_gui.wl.StartLDevice(my_gui.hIfc)
        time.sleep(2)

        point = 32768
        V = 20
        x1 = array.array('f', ())
        x2 = [array.array('f', ()) for _ in range(N)]

        for _ in range(V):
            for k in range(N):
                i = k
                while i < point:
                    if Data[i] < 10000:
                        data_lc = Data[i] * (self.pred / 8000)
                    elif Data[i] > 10000:
                        data_lc = (Data[i] - 65536) * (self.pred / 8000)
                    x1.append(data_lc)
                    i += N
                x2[k] = x1
                x1 = array.array('f', ())

        my_gui.wl.StopLDevice(my_gui.hIfc)

        for k in range(N):
            if self.rez == 'dcv':
                data_adc = sum(x2[k]) / (point / N)
            elif self.rez in ('acv', 'acz'):
                data_adc = ((max(x2[k]) - min(x2[k])) / (1.4142135 * 2))
            elif self.rez == 'ac0':
                data_adc = ((max(x2[0]) - min(x2[0])) / (1.4142135 * 2))

            data_adc = round(data_adc, 4)
            #print ('Chn', k, data_adc)

            if self.rez == 'acz':
                data_accur = 100 * (data_adc / self.pred) * math.sqrt(8192 / (8192 - 1))
            else:
                data_accur = ((data_adc - float(self.volt1.split(' ')[0])) / self.pred) * 100

            if self.rez in ('dcv', 'acv'):
                xi2 = self.xi[0] + str(int(self.xi[1:]) + k)
                yi2 = self.yi[0] + str(int(self.yi[1:]) + k)
            elif self.rez == 'acz':
                xi2 = chr(ord(self.xi[0]) + k) + str(int(self.xi[1:]))
                yi2 = chr(ord(self.yi[0]) + k) + str(int(self.yi[1:]))
            elif self.rez == 'ac0':
                xi2 = self.xi[0] + str(int(self.xi[1:]))
                yi2 = self.yi[0] + str(int(self.yi[1:]))

            my_gui.change_rows(xi2, data_adc * 1000, yi2, data_accur, self.accurancy)

    def call_e502(self):
        if self.rez in ('acv'):
            if float(self.volt1.split(' ')[2]) == 0.01:
                if float(self.volt1.split(' ')[0]) < 0.04:
                    self.start_meas_e502(10*8192*(number_ch + 1)*(16 - number_ch), 250)
                else:
                    self.start_meas_e502(10*8192*(number_ch + 1)*(16 - number_ch), 4)
            elif float(self.volt1.split(' ')[2]) == 1.0:
                if float(self.volt1.split(' ')[0]) < 0.041 or float(self.volt1.split(' ')[0]) > 0.021:
                    self.start_meas_e502(8192*(number_ch + 1)*(16 - number_ch), 3)
                elif float(self.volt1.split(' ')[0]) < 0.021 or float(self.volt1.split(' ')[0]) > 0.009:
                    self.start_meas_e502(8192*(number_ch + 1)*(16 - number_ch), 7)
            else:
                self.start_meas_e502(8192*(number_ch + 1)*(16 - number_ch), 1)

        else:
            self.start_meas_e502(8192*(number_ch + 1)*(16 - number_ch), 1)

        for k in range(number_ch + 1):
            if self.rez == 'dcv':
                data_adc = sum(self.x6[k]) / (self.point / (number_ch + 1))
                data_accur = ((data_adc - float(self.volt1.split(' ')[0])) / self.pred) * 100
            elif self.rez in ('acv', 'ac0'):
                data_adc = (math.sqrt(sum(i*i for i in self.x6[k][819:]) / len(self.x6[k][819:])))
                data_accur = ((data_adc - float(self.volt1.split(' ')[0])) / float(self.volt1.split(' ')[0])) * 100

            data_adc = round(data_adc, 4)
            #print ('Chn', k, data_adc)

            if self.rez in ('dcv', 'acv'):
                xi2 = self.xi[0] + str(int(self.xi[1:]) + k)
                yi2 = self.yi[0] + str(int(self.yi[1:]) + k)
            elif self.rez == 'ac0':
                xi2 = self.xi[0] + str(int(self.xi[1:]))
                yi2 = self.yi[0] + str(int(self.yi[1:]))

            if self.accurancy == ' ':
                xac = self.pred / math.sqrt(2)
                x = float(self.volt1.split(' ')[0])
                accurancy = 0.15 + 0.02 * ((xac / x) - 1)
                my_gui.change_rows(xi2, data_adc * 1000, yi2, data_accur, accurancy)
            else:
                my_gui.change_rows(xi2, data_adc * 1000, yi2, data_accur, self.accurancy)

    def run(self):
        sem.acquire()
        global COUNT
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {COUNT} из {my_gui.cnt()[my_gui.bn]}'
        time.sleep(1)
        my_gui.inst_fluke.write(my_gui.calbr[self.rez]+self.volt1)
        my_gui.lb2.delete(0, 'end')
        if self.rez == 'acz':
            my_gui.lb2.insert('end', 'Заглушка')
            my_gui.inst_fluke.write(my_gui.calbr['OFF'])
        else:
            my_gui.lb2.insert('end', f'Режим измерения: {self.rez.upper()}')
            my_gui.lb2.insert('end', 'Установлено: ' + self.volt1)
            my_gui.inst_fluke.write(my_gui.calbr['ON'])
        my_gui.lb2.see('end')
        time.sleep(4)
        self.xi = self.cell1
        self.yi = self.cell2

        if my_gui.bn in ('E440', 'E440D', 'E440_2017'):
            self.call_e14()
        elif my_gui.bn == 'E502':
            self.call_e502()

        my_gui.border_cell()
        COUNT += 1
        sem.release()
# ================================= DAC ==========================================
class Meas_dac(Thread):
    def __init__(self, rez, volt_dac, freq=None):
        Thread.__init__(self)
        self.rez = rez
        self.volt_dac = volt_dac
        self.freq = freq
        self.start()

    def dac_set_param_e502(self):
        my_gui.context.close()
        my_gui.lib.E502_OpenUsb(my_gui.Create, 0)

        if self.rez.split()[1] == 'DC':
            volt_dac = [(self.volt_dac * 30000) / 5000]
            self.size = 1
        elif self.rez.split()[1] == 'AC':
            volt_dac = array.array('f', ())
            self.size = 1000000

            for x in range(self.size):
                y_sin_analog = (self.volt_dac * (math.sin(x * 2 * math.pi * self.freq / self.size))) * math.sqrt(2) * (30000 / 5000)
                volt_dac.append(y_sin_analog)

        self.pyarr = (ctypes.c_double * len(volt_dac))(*volt_dac)
        self.volt_dac_ok = (ctypes.c_double * len(volt_dac))()
        my_gui.lib2.X502_SetOutFreq(my_gui.Create, ctypes.pointer(ctypes.c_double(self.size)))
        my_gui.lib2.X502_StreamsEnable(my_gui.Create, int(self.rez.split()[0]))
        my_gui.lib2.X502_PreloadStart(my_gui.Create)
        for _ in range(500):
            my_gui.lib2.X502_PrepareData(my_gui.Create, self.pyarr, self.pyarr, 'NULL', self.size, 0x0002, self.volt_dac_ok)
            my_gui.lib2.X502_Send(my_gui.Create, self.volt_dac_ok, self.size, 10)
            my_gui.lib2.X502_Configure(my_gui.Create, 0)
            my_gui.lib2.X502_StreamsStart(my_gui.Create)
        my_gui.lib2.X502_StreamsStop(my_gui.Create)
        my_gui.lib2.X502_Close(my_gui.Create)

    def dac_set_param_e14(self):
        pf = ctypes.pointer(AsyncParam())
        pf.contents.s_Type = 9    # L_ASYNC_DAC_OUT = 9
        pf.contents.Mode = int(self.rez.split()[0])

        my_gui.wl.InitStartLDevice(my_gui.hIfc)
        my_gui.wl.StartLDevice(my_gui.hIfc)
        my_gui.wl.EnableCorrection(my_gui.hIfc, 1)

        for _ in range(100):
            x = (self.volt_dac * 2048) / 5000
            pf.contents.Data[0] = int(round(x, 0))
            my_gui.wl.IoAsync(my_gui.hIfc, pf)

        my_gui.wl.StopLDevice(my_gui.hIfc)

    def select_dac(self):
        if my_gui.bn in ('E440', 'E440D', 'E440_2017'):
            self.dac_set_param_e14()
        elif my_gui.bn == 'E502':
            self.dac_set_param_e502()

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = 'Статус: установка ЦАП...'
        self.select_dac()
        my_gui.statusbar["text"] = 'Статус: ожидание...'
        sem.release()

class Ldac(Meas_dac):
    def __init__(self, rez, volt_dac, cell1, cell2, accur, freq=None):
        Thread.__init__(self)
        self.rez = rez
        self.volt_dac = volt_dac
        self.cell1 = cell1
        self.cell2 = cell2
        self.accur = accur
        self.freq = freq
        self.start()

    def run(self):
        sem.acquire()
        global COUNT
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {COUNT} из {my_gui.cnt()[my_gui.bn]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', f'ЦАП {self.rez}, напряжение {self.volt_dac} мВ')
        my_gui.lb2.see('end')
        time.sleep(1)

        if my_gui.bn in ('E440', 'E440D', 'E440_2017') or self.rez.split()[1] == 'DC':
            my_gui.inst_dmm.write('CONF:VOLT:DC 10')
            my_gui.inst_dmm.write('DET:BAND 20')
            time.sleep(1)
            self.select_dac()
            my_gui.inst_dmm.write('READ?')
            time.sleep(3)
            data_dac = float(my_gui.inst_dmm.read()) * 1000

        elif self.rez.split()[1] == 'AC':
            if self.rez.split()[2] == 'F':
                my_gui.inst_dmm.write('CONF:FREQ')
            else:
                my_gui.inst_dmm.write('CONF:VOLT:AC 10')
            if self.freq < 99:
                my_gui.inst_dmm.write('DET:BAND 3')
            else:
                my_gui.inst_dmm.write('DET:BAND 20')
            time.sleep(1)

            my_gui.context.close()
            my_gui.lib.E502_OpenUsb(my_gui.Create, 0)

            volt_dac = array.array('f', ())
            self.size = 1000000

            for x in range(self.size):
                y_sin_analog = (self.volt_dac * (math.sin(x * 2 * math.pi * self.freq / self.size))) * math.sqrt(2) * (30000 / 5000)
                volt_dac.append(y_sin_analog)

            self.pyarr = (ctypes.c_double * len(volt_dac))(*volt_dac)
            self.volt_dac_ok = (ctypes.c_double * len(volt_dac))()
            my_gui.lib2.X502_SetOutFreq(my_gui.Create, ctypes.pointer(ctypes.c_double(self.size)))
            my_gui.lib2.X502_StreamsEnable(my_gui.Create, int(self.rez.split()[0]))
            my_gui.lib2.X502_PreloadStart(my_gui.Create)
            for i in range(500):
                my_gui.lib2.X502_PrepareData(my_gui.Create, self.pyarr, self.pyarr, 'NULL', self.size, 0x0002, self.volt_dac_ok)
                my_gui.lib2.X502_Send(my_gui.Create, self.volt_dac_ok, self.size, 10)
                my_gui.lib2.X502_Configure(my_gui.Create, 0)
                my_gui.lib2.X502_StreamsStart(my_gui.Create)
                if i == 450:
                    if self.rez.split()[2] == 'F':
                        data_dac = float(my_gui.inst_dmm.query('MEAS:FREQ?'))
                    else:
                        my_gui.inst_dmm.write('READ?')
                        time.sleep(1)
                        data_dac = float(my_gui.inst_dmm.read()) * 1000
                    #print(data_dac)
            my_gui.lib2.X502_StreamsStop(my_gui.Create)
            my_gui.lib2.X502_Close(my_gui.Create)

        data_dac = round(data_dac, 2)
        if self.rez.split()[1] == 'DC':
            data_accur = ((data_dac - self.volt_dac) / 5000) * 100
        elif self.rez.split()[1] == 'AC':
            data_accur = ((data_dac - self.volt_dac) / self.volt_dac) * 100
            if self.rez.split()[2] == 'F':
                data_accur = ((data_dac - self.freq) / self.freq) * 100
                if self.freq in (100000, 300000):
                    data_dac = data_dac / 1000

        my_gui.change_rows(self.cell1, data_dac, self.cell2, data_accur, self.accur)
        my_gui.border_cell()
        COUNT += 1
        sem.release()
# ------------------------------ Structure e14 -------------------------------------
class Slot(ctypes.Structure):
    _fields_ = [('Base', ctypes.c_ulong),
                ('BaseL', ctypes.c_ulong),
                ('Base1', ctypes.c_ulong),
                ('BaseL1', ctypes.c_ulong),
                ('Mem', ctypes.c_ulong),
                ('MemL', ctypes.c_ulong),
                ('Mem1', ctypes.c_ulong),
                ('MemL1', ctypes.c_ulong),
                ('Irq', ctypes.c_ulong),
                ('BoardType', ctypes.c_ulong),
                ('DSPType', ctypes.c_ulong),
                ('Dma', ctypes.c_ulong),
                ('DmaDac', ctypes.c_ulong),
                ('DTA_REG', ctypes.c_ulong),
                ('IDMA_REG', ctypes.c_ulong),
                ('CMD_REG', ctypes.c_ulong),
                ('IRQ_RST', ctypes.c_ulong),
                ('DTA_ARRAY', ctypes.c_ulong),
                ('RDY_REG', ctypes.c_ulong),
                ('CFG_REG', ctypes.c_ulong)]

class Read(ctypes.Structure):
    _fields_ = [('SerNum', ctypes.c_char*9),
                ('BrdName', ctypes.c_char*7),
                ('Rev', ctypes.c_char),
                ('DspType', ctypes.c_char*5),
                ('IsDacPresent', ctypes.c_char),
                ('Quartz', ctypes.c_ulong),
                ('Reserv2', ctypes.c_char*13),
                ('KoefADC', ctypes.c_ushort*8),
                ('KoefDAC', ctypes.c_ushort*4),
                ('Custom', ctypes.c_ushort*32)]

class AsyncParam(ctypes.Structure):
    _fields_ = [('s_Type', ctypes.c_ulong),
                ('FIFO', ctypes.c_ulong),
                ('IrgStep', ctypes.c_ulong),
                ('Pages', ctypes.c_ulong),
                ('dRate', ctypes.c_double),
                ('Rate', ctypes.c_ulong),
                ('NCh', ctypes.c_ulong),
                ('Chn', ctypes.c_ulong * 128),
                ('Data', ctypes.c_ulong * 128),
                ('Mode', ctypes.c_ulong)]

class Wadc_par_0(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('s_Type', ctypes.c_ulong),
                ('FIFO', ctypes.c_ulong),
                ('IrqStep', ctypes.c_ulong),
                ('Pages', ctypes.c_ulong),
                ('AutoInit', ctypes.c_ulong),
                ('dRate', ctypes.c_double),
                ('dKadr', ctypes.c_double),
                ('dScale', ctypes.c_double),
                ('Rate', ctypes.c_ulong),
                ('Kadr', ctypes.c_ulong),
                ('Scale', ctypes.c_ulong),
                ('FPDelay', ctypes.c_ulong),
                ('SynchroType', ctypes.c_ulong),
                ('SynchroSensitivity', ctypes.c_ulong),
                ('SynchroMode', ctypes.c_ulong),
                ('AdChannel', ctypes.c_ulong),
                ('AdPorog', ctypes.c_ulong),
                ('NCh', ctypes.c_ulong),
                ('Chn', ctypes.c_ulong * 16),
                ('IrqEna', ctypes.c_ulong),
                ('AdcEna', ctypes.c_ulong)]
# ------------------------------ Structure e502 -------------------------------------
class Read_x502(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('arr', ctypes.c_uint32 * 1),
                ('devs', ctypes.c_uint32)]

class t_x502_cbr_coef(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('offs', ctypes.c_double),
                ('k', ctypes.c_double)]

class t_x502_cbr(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('adc', t_x502_cbr_coef*6),
                ('rez1', ctypes.c_uint32*64),
                ('dac', t_x502_cbr_coef*2),
                ('rez2', ctypes.c_uint32*20)]

class t_x502_info(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('BrdName', ctypes.c_char*32),
                ('SerNum', ctypes.c_char*32),
                ('devflags', ctypes.c_uint32),
                ('fpga_ver', ctypes.c_uint16),
                ('plda_ver', ctypes.c_uint8),
                ('board_rev', ctypes.c_uint8),
                ('mcu_firmware_ver', ctypes.c_uint32),
                ('factory_mac', ctypes.c_uint8*6),
                ('rezerv', ctypes.c_uint8*110),
                ('cbr', t_x502_cbr)]
# -----------------------------------------------------------------------------------
class Message(Thread):
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text
        self.start()

    def run(self):
        sem.acquire()
        messagebox.showinfo('ВНИМАНИЕ!', self.text)
        my_gui.inst_fluke.write(my_gui.calbr['OFF'])
        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == '_type':
                    cell.value = my_gui.bn
                if cell.value == '_numb':
                    cell.value = my_gui.sn
                if cell.value == '_customer':
                    cell.value = my_gui.vardict_str['custom'].get()
                if cell.value == '_temp':
                    cell.value = my_gui.vardict_str['temp'].get()
                if cell.value == '_hum':
                    cell.value = my_gui.vardict_str['humi'].get()
                if cell.value == '_pres':
                    cell.value = my_gui.vardict_str['press'].get()
                if cell.value == '_pov':
                    cell.value = my_gui.vardict_str['pover'].get()
                if cell.value == '_date':
                    cell.value = my_gui.data_today[:10]
        sem.release()

class Reset(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def merged_cells(self):
        for merged_cells in my_gui.ws.merged_cells.ranges:
            style = my_gui.ws.cell(merged_cells.min_row, merged_cells.min_col)._style
            for col in range(merged_cells.min_col, merged_cells.max_col + 1):
                for row in range(merged_cells.min_row, merged_cells.max_row + 1):
                    my_gui.ws.cell(row, col)._style = style

    def run(self):
        sem.acquire()
        time.sleep(1)
        my_gui.inst_fluke.write('*CLS')
        my_gui.inst_fluke.write('*RST')
        if my_gui.bn in ('E440', 'E440D', 'E440_2017'):
            if my_gui.dac == 1:
                my_gui.inst_dmm.write('*RST')
        elif my_gui.bn == 'E502':
            my_gui.inst_dmm.write('*RST')
        time.sleep(1)
        self.merged_cells()
        sem.release()


root = tk.Tk()
my_gui = LMeasGUI(root)
my_gui.cnt()
my_gui.pribor()
root.protocol('WM_DELETE_WINDOW', my_gui.exit_lmeas)
root.mainloop()
