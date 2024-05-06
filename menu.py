import PySimpleGUI as sg
import blackjackgui

# Maximum value for the slider
money = 1000
gambled = 0

def Menu_window():
    sg.theme("neonyellow1")
    layout = [
        [sg.Text(
            "Casino",
            font="franklin 30")
        ],
        [sg.Text("Money Owned:", font="franklin 15", pad=((10, 100), (50, 10))), sg.Text("Money Wagered:", font="franklin 15", pad=((10, 10), (50, 10)))],
        [sg.Text("$ 1000", key='-MONEY_OWNED-', font="franklin 20", pad=((10, 170), (10, 10))), sg.Text("$ 0", key='-MONEY_WAGERED-', font="franklin 20", pad=((10, 10), (10, 10)))],
        [sg.Text(
            "Gamble Money:",
            font="franklin 20",
            key="-TEXT-",
            pad=((10, 10), (40, 10)))
        ],
        [sg.Slider((1, money), default_value=100, orientation='h', key='-MONEY-SLIDER-', visible=False)],
        [sg.Button("Set $", size=(12, 2), visible=False)],
        [sg.Button("Wager", size=(12, 2), pad=((10, 10), (10, 100)))],
        [sg.Button("Blackjack", size=(15, 20), visible=False)],
    ]
    return sg.Window("Menu", layout, size=(500, 600), element_justification='c')

def menu_funk():
    window = Menu_window()

    while True:
        global money
        global gambled
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
            
        if event == "Wager":
            money = money + gambled
            window["Wager"].update(visible=False)
            window["-MONEY-SLIDER-"].update(visible=True)
            window["Set $"].update(visible=True)
            
        if event == "Set $":
            gambled = values['-MONEY-SLIDER-']
            money = money - gambled
            window["Set $"].update(visible=False)
            window["-MONEY-SLIDER-"].update(visible=False)
            window["Wager"].update(visible=True)
            window['-MONEY_WAGERED-'].update(gambled)  
            window['-MONEY_OWNED-'].update(money)
            window["Blackjack"].update(visible=True)
            
        if event == "Blackjack":
            window.close()
            window = blackjackgui.blackjack_funk()

    window.close()