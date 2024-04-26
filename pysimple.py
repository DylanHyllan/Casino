import PySimpleGUI as sg

def blackjack_window():
    layout = [
        [sg.Button("Hit"), sg.Button("Stand"), sg.Button("Double")]
    ]
    window = sg.Window("blackjack", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

    window.close()

blackjack_window() 