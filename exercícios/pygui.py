import PySimpleGUI as pg
#theme
#pg.theme("DarkAmber")
#layout
layout = [
    [pg.Text("Enter name")],
    [pg.InputText()],
    [pg.Button("Ok"), pg.Button("Cancel")]
]
#window
window = pg.Window("Form", layout)
#event loop
while True:
    event, values = window.read()
    if event == "Cancel" or event == pg.WIN_CLOSED:
        break
    print(values[0])
 
# close window
window.close()
    