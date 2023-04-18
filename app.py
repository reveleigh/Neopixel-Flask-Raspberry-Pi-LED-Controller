from flask import Flask, render_template, request
import board
import neopixel
import time
import threading

# On a Raspberry pi, use this instead, not all pins are supported
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 12

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

pixels.fill((0, 0, 0))
pixels.show()

def rainbow_cycle(stop_event):
    while not stop_event.is_set():
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(0.001)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

#Creating an event object to control thread termination.
stop_event = threading.Event()

#Creating a new thread object that will execute the rainbow_cycle function
# and passing the stop_event object as an argument to enable termination of the thread.
rainbow_thread = threading.Thread(target=rainbow_cycle, args=(stop_event,))

app = Flask(__name__, static_url_path='/static')

# Define routes for turning on the RGB lights
@app.route('/red')
def turn_on_red():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((255, 0, 0))
    pixels.show()
    return 'Red light turned on'

@app.route('/orange')
def turn_on_orange():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((255, 165, 0))
    pixels.show()
    return 'Orange light turned on'

@app.route('/yellow')
def turn_on_yellow():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((255, 255, 0))
    pixels.show()
    return 'Yellow light turned on'

@app.route('/green-yellow')
def turn_on_green_yellow():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((173, 255, 47))
    pixels.show()
    return 'Green - Yellow light turned on'

@app.route('/green')
def turn_on_green():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((0, 128, 0))
    pixels.show()
    return 'Green light turned on'

@app.route('/green-cyan')
def turn_on_green_cyan():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((0, 255, 255))
    pixels.show()
    return 'Green - Cyan light turned on'

@app.route('/cyan')
def turn_on_cyan():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((0, 191, 255))
    pixels.show()
    return 'Cyan - Yellow light turned on'

@app.route('/blue-cyan')
def turn_on_bluie_cyan():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((0, 139, 139))
    pixels.show()
    return 'Blue/Cyan light turned on'

@app.route('/blue')
def turn_on_blue():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((0, 0, 255))
    pixels.show()
    return 'Blue light turned on'

@app.route('/blue-magenta')
def turn_on_blue_magenta():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((139, 0, 139))
    pixels.show()
    return 'Blue/magenta - Yellow light turned on'

@app.route('/magenta')
def turn_on_magenta():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((255, 0, 255))
    pixels.show()
    return 'Magenta light turned on'

@app.route('/red-magenta')
def turn_on_red_magenta():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((255, 20, 147))
    pixels.show()
    return 'Red/magenta light turned on'

@app.route('/white')
def turn_on_white():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((255, 255, 255))
    pixels.show()
    return 'White light turned on'

@app.route('/warm-white')
def turn_on_warm_white():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((245, 222, 179))
    pixels.show()
    return 'Warm white light turned on'

@app.route('/cool-white')
def turn_on_cool_white():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((173, 216, 230))
    pixels.show()
    return 'Cool white light turned on'

@app.route('/black')
def turn_on_black():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    pixels.fill((0, 0, 0))
    pixels.show()
    return 'Lights off'


@app.route('/rainbow')
def turn_on_rainbow():
    global stop_event, rainbow_thread
    stop_event.clear()
    if not rainbow_thread.is_alive():
        rainbow_thread = threading.Thread(target=rainbow_cycle, args=(stop_event,))
        rainbow_thread.start()
    pixels.fill((0, 0, 0))
    pixels.show()
    return 'Rainbow on'

@app.route('/rgb', methods=['POST'])
def rgb():
    global pixels, stop_event, rainbow_thread
    if rainbow_thread.is_alive():
        stop_event.set()
        rainbow_thread.join()
    r = int(request.form['red'])
    g = int(request.form['green'])
    b = int(request.form['blue'])
    print('RGB: ({}, {}, {})'.format(r, g, b))

    pixels.fill((r, g, b))
    pixels.show()

    return render_template('index.html')



# Define the main route to display the HTML template
@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)