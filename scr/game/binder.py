from pynput import keyboard


def on_press(key):

    Key = keyboard.Key

    match key:
        case Key.up:
            print("\r   Up", end='')
        case Key.down:
            print("\r Down", end='')
        case Key.left:
            print("\r Left", end='')
        case Key.right:
            print("\rRight", end='')
        case Key.esc:
            return False


def get_listener() -> keyboard.Listener:
    return keyboard.Listener(on_press=on_press)
