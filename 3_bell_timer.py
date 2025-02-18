# 
# 3分タイマー(『Pythonでつくるデスクトップアプリ』(クジラ飛行机．2024．ソシム)に掲載)を改変
#   https://github.com/kujirahand/book-desktop-python-sample/blob/main/src/ch2/timer3min.py

import datetime
import TkEasyGUI as sg
import pygame
import time

# functions
def play_bell(n=1):
    pygame.mixer.music.play()
    for i in range(n-1):
        time.sleep(0.5)
        pygame.mixer.music.play()

def input_timer_sec(timer, wind, window):
    input = timer
    try:
        input = eval(sg.popup_input('Input number in second. eg: 10 * 60 + 30'))
        window[wind].update('0' + str(datetime.timedelta(seconds=input)))
    except Exception as e:
        sg.popup('Input number')
    return input

# default time in sec
BELL = '\U0001F514' # to see in python: print('\U0001F514')
timer_sec_1 = 10.0 * 60
timer_sec_2 = 12.0 * 60
timer_sec_3 = 14.5 * 60
accumulated_time = datetime.timedelta(0)
start_time = None

input_1 = timer_sec_1
input_2 = timer_sec_2
input_3 = timer_sec_3

FONT_SISE_TIME = 200
FONT_SISE_SETTING = 30
FONT_SISE_BUTTON = 30

# sound setting
SOUND_FILE = '3_bell_timer_bell.mp3' # sound file for bell
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)

# layout
layout = [
    [sg.Text('00:00:00', key='-output-', font=('Helvetica', FONT_SISE_TIME))],
    [
        sg.Push(), sg.Push(),
        sg.Text(BELL + ' * 1'             , font=('Helvetica', FONT_SISE_SETTING), expand_x=True),
        sg.Text('00:00:00', key='-time_1-', font=('Helvetica', FONT_SISE_SETTING), expand_x=True),
        sg.Button('setting', key='-set_1-' , font=('Helvetica', FONT_SISE_BUTTON ), expand_x=True),
        sg.Push(), sg.Push()
    ],
    [
        sg.Push(), sg.Push(),
        sg.Text(BELL + ' * 2'             , font=('Helvetica', FONT_SISE_SETTING), expand_x=True),
        sg.Text('00:00:00', key='-time_2-', font=('Helvetica', FONT_SISE_SETTING), expand_x=True),
        sg.Button('setting', key='-set_2-' , font=('Helvetica', FONT_SISE_BUTTON ), expand_x=True),
        sg.Push(), sg.Push()
    ],
    [
        sg.Push(), sg.Push(),
        sg.Text(BELL + ' * 3'             , font=('Helvetica', FONT_SISE_SETTING), expand_x=True),
        sg.Text('00:00:00', key='-time_3-', font=('Helvetica', FONT_SISE_SETTING), expand_x=True),
        sg.Button('setting', key='-set_3-', font=('Helvetica', FONT_SISE_BUTTON ), expand_x=True),
        sg.Push(), sg.Push()
    ],
    [
        sg.Push(),
        sg.Button('START',   key='-start-', font=('Helvetica', FONT_SISE_BUTTON), expand_x=True),
        sg.Push(),
        sg.Button(BELL   ,   key='-bell-' , font=('Helvetica', FONT_SISE_BUTTON), expand_x=True),
        sg.Push(),
        sg.Button('RESET',   key='-reset-', font=('Helvetica', FONT_SISE_BUTTON), expand_x=True),
        sg.Push()
    ],
    [
        sg.Push(),
        sg.Button('STOP',     key='-stop-', font=('Helvetica', FONT_SISE_BUTTON), disabled=True),
        sg.Push(),
    ]
]

# create window
window = sg.Window('3-BELL TIMER', layout)

# update timer_sec_1,2,3
window['-time_1-'].update('0' + str(datetime.timedelta(seconds=timer_sec_1)))
window['-time_2-'].update('0' + str(datetime.timedelta(seconds=timer_sec_2)))
window['-time_3-'].update('0' + str(datetime.timedelta(seconds=timer_sec_3)))

# Event loop
while True: 
    event, _ = window.read(timeout=400)
    if event == sg.WINDOW_CLOSED:
        break
    if event == '-set_1-':
        input_1 = input_timer_sec(timer=timer_sec_1, wind='-time_1-', window=window)
        timer_sec_1 = input_1
    if event == '-set_2-':
        input_2 = input_timer_sec(timer=timer_sec_2, wind='-time_2-', window=window)
        timer_sec_2 = input_2
    if event == '-set_3-':
        input_3 = input_timer_sec(timer=timer_sec_3, wind='-time_3-', window=window)
        timer_sec_3 = input_3
    if event == '-start-':
        start_time = datetime.datetime.now()
        window['-set_1-'].update(disabled=True)
        window['-set_2-'].update(disabled=True)
        window['-set_3-'].update(disabled=True)
        window['-start-'].update(disabled=True)
        window['-reset-'].update(disabled=True)
        window['-stop-' ].update(disabled=False)
    if event == '-reset-':
        start_time = None
        timer_sec_1 = input_1 # refresh timer_sec
        timer_sec_2 = input_2
        timer_sec_3 = input_3
        window['-output-'].update('00:00:00')
        window['-set_1-' ].update(disabled=False)
        window['-set_2-' ].update(disabled=False)
        window['-set_3-' ].update(disabled=False)
        window['-start-' ].update(disabled=False)
        window['-reset-' ].update(disabled=False)
        window['-stop-'  ].update(disabled=True)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        continue
    if event == '-stop-':
        if window['-stop-'].text=='STOP':                 # from 'STOP' to 'RESTART'
            window['-stop-' ].update(text='RESTART')
            window['-start-'].update(disabled=True)
            window['-reset-'].update(disabled=False)
            accumulated_time = lapsed_time
            while True:        
                ev, _ = window.read(timeout=400)
                if ev == '-stop-':
                    window['-stop-' ].update(text='STOP') # from 'RESTART' to 'STOP' 
                    window['-start-'].update(disabled=True)
                    window['-reset-'].update(disabled=True)
                    start_time = datetime.datetime.now()
                    break
                if ev == '-reset-':
                    start_time = None
                    timer_sec_1 = input_1 # refresh timer_sec
                    timer_sec_2 = input_2
                    timer_sec_3 = input_3
                    accumulated_time = datetime.timedelta(0)
                    start_time = None
                    window['-stop-' ].update(text='STOP') # from 'RESTART' to 'STOP'
                    window['-output-'].update('00:00:00')
                    window['-set_1-' ].update(disabled=False)
                    window['-set_2-' ].update(disabled=False)
                    window['-set_3-' ].update(disabled=False)
                    window['-start-' ].update(disabled=False)
                    window['-reset-' ].update(disabled=False)
                    window['-stop-'  ].update(disabled=True)
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    break
                else:
                    continue
    if event == '-bell-':
        play_bell(1)
    if start_time is not None:
        lapsed_time = datetime.datetime.now() - start_time + accumulated_time
        window['-output-'].update('0' + str(datetime.timedelta(seconds=lapsed_time.seconds)))
        if lapsed_time.seconds >= timer_sec_1: # first bell
            timer_sec_1 = 999999
            play_bell(n=1)
            continue
        if lapsed_time.seconds >= timer_sec_2: # second bell
            timer_sec_2 = 9999999
            play_bell(n=2)
            continue
        if lapsed_time.seconds >= timer_sec_3: # third bell
            timer_sec_3 = 9999999
            play_bell(n=3)
            continue

window.close()
