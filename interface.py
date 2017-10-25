from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput  import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from socket_server import SocketServer


def sendmessage():
    print(ed.text)


def on_client_active(checkbox, value):
    if value:
        isServer.active = False
        ed.hint_text = 'digite a mensagem a ser enviada'
        bt.height = 60
        bt.disabled = False

def on_server_active(checkbox, value):
    if value:
        isClient.active = False
        ed.hint_text = 'aguardando mensagem'
        bt.disabled = True
        SocketServer().start_socket()

def build():
    layout = FloatLayout()
    global isClient
    isClient = CheckBox()
    isClient.size_hint = None, None
    isClient.width = 50
    isClient.height  = 30
    isClient.x = 300
    isClient.y  =650
    isClient.bind(active=on_client_active)
    layout.add_widget(isClient)
    global  isServer
    isServer = CheckBox()
    isServer.size_hint = None, None
    isServer.width = 50
    isServer.height  = 30
    isServer.x = 30
    isServer.y  =650
    isServer.bind(active=on_server_active)
    layout.add_widget(isServer)
    ed = TextInput(hint_text='digite a mensagem a ser enviada')
    global ed
    ed.size_hint = None, None
    ed.height = 500
    ed.width = 400
    ed.y = 100
    layout.add_widget(ed)
    global bt
    bt = Button ( text= 'send')
    bt.size_hint= None, None
    bt.width = 400
    bt.height = 60
    bt.y = 20
    bt.on_press = sendmessage
    layout.add_widget(bt)
    return layout

janela = App()
Window.size = 400,700
janela.build = build
janela.run()
