import time
from datetime import datetime
import simpleaudio as sa
import threading
from tkinter import *

click_normal = sa.WaveObject.from_wave_file("metronome-85688.wav")


# Get beats per minute value
def get_bpm(*args):
    try:
        bpm_value = int(text_bpm.get())
        return bpm_value
    except ValueError:
        print("INVALID")
        return 0


def more_than_2_threads():
    return len(threading.enumerate()) > 2


def tick(tick_enabled):
    bpm_value = get_bpm()
    print('BPM Value: ' + str(bpm_value))

    # Print('{}, {}'.format(bpm_value, tick_enabled))
    t0 = datetime.now()
    num_of_ticks = 0

    if bpm_value == 0:
        return
    time_per_beat = 60 / bpm_value  # Time in [s]

    while tick_enabled:
        # Print(bpm_value)
        if more_than_2_threads():
            break

        else:
            start = time.time()
            play_click_normal = click_normal.play()  # Plays 0.02s
            play_click_normal.wait_done()
            num_of_ticks += 1
            end = time.time()
            delay = end - start
            # Print(delay)
            if more_than_2_threads():
                break
            time.sleep(time_per_beat - delay)


    if tick_enabled:
        t1 = datetime.now()
        t_delta = t1 - t0
        print("\n\n")
        print("Number of ticks: " + str(num_of_ticks))
        print("Time passed: " + str(t_delta))
        print("\n\n")

def tick_threaded(enabled):
    if get_bpm() < 15:
        text_bpm.set(15)
    if get_bpm() > 450:
        text_bpm.set(450)

    num_of_ticks = 0
    thread = threading.Thread(target=tick, args=(enabled,))
    thread.start()
    num_of_ticks += 1
    if more_than_2_threads():
        # Print(threading.get_ident())
        threading.enumerate()[1].join()

    # Print(thread.getName())
    # Print(thread.name)

    print(threading.enumerate())


window = Tk()
window.title("Metronome")

window.geometry("450x300+1100+100")

# Beats per minute label
lab_bpm = Label(window,
                text="BPM value", font=("Sans Serif", 16))
lab_bpm.place(bordermode=INSIDE, relx=0.05, rely=0.05,
              relwidth=0.24, relheight=0.15)

# Beats per minute entry
text_bpm = StringVar()
ent_set_bpm = Entry(window, textvariable=text_bpm,
                    font=("Sans Serif", 16, "bold"))
ent_set_bpm.insert(0, text_bpm.get())
ent_set_bpm.place(relx=0.05, rely=0.20,
                  relwidth=0.24, relheight=0.15)
default_bpm = "120"
text_bpm.set(default_bpm)
text_bpm.trace('w', get_bpm)

# Start button
but_start = Button(window, text="START", font=("Sans Serif", 16, "bold"),
                  command=lambda: tick_threaded(True))
but_start.place(relx=0.5, rely=0.8, relwidth=0.24, relheight=0.15)

# Stop button
but_stop = Button(window, text="STOP", font=("Sans Serif", 16, "bold"),
                  command=lambda: tick_threaded(False))
but_stop.place(relx=0.75, rely=0.8, relwidth=0.24, relheight=0.15)

window.mainloop()

print("away from mainloop")
