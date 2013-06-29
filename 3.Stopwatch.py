import simplegui

interval = 100
time = 0
win = 0
tries = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    d = t % 10
    c = (t // 10) % 10
    b = (t // 100) % 6
    a = t // 600
    time_format = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return time_format

def start():
    timer.start()
        
def stop():
    global d,win, tries
    if timer.is_running():
        timer.stop()
        if d == 0:
            win += 1
            tries += 1
        else:
            tries += 1

def reset():
    global time,win,tries
    time = 0
    timer.stop()
    win = 0
    tries = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1



def draw(canvas):
    global time
    canvas.draw_text(format(time), [200,100], 22, "White")
    canvas.draw_text(str(win) + "/" + str(tries),[365,25],22,"White")

    

frame = simplegui.create_frame("Stopwatch",400,200)
timer = simplegui.create_timer(interval,tick)

frame.set_draw_handler(draw)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)

frame.start()

