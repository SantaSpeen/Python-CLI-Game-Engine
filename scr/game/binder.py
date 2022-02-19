from pynput import keyboard


def on_press(key):

    Key = keyboard.Key

    match key:
        case Key.up:
            Store.last_key = 0
        case Key.down:
            Store.last_key = 1
        case Key.left:
            Store.last_key = 2
        case Key.right:
            Store.last_key = 3
        case Key.esc:
            Store.last_key = 4
        case Key.enter:
            Store.last_key = 5


def get_listener() -> keyboard.Listener:
    Store.last_key = None
    return keyboard.Listener(on_press=on_press)
