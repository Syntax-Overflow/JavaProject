import FreeSimpleGUI as sg

# Layout
layout = [[sg.Text("Input Username")],
          [sg.Input(key='User')],
          [sg.Text("Input Password")],
          [sg.Input(key="Pass", password_char="*")]]

# Create login window
window = sg.Window('Login', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()