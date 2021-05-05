import bosdyn.client

from bosdyn.client.image import ImageClient #get ImageClient instance

from bosdyn.client.spot_cam.ptz import PtzClient

from PIL import Image #open image file
import io

import inspect

from pynput import keyboard
from pynput.keyboard import Key


#print(dir(PtzClient.get_ptz_position))

#print(inspect.getfullargspec(PtzClient.get_ptz_position))

horizontal = int(0)
default_menu = "1: Image | 2: Ptz"
select_menu = ""
vertical = int(0)
zoom = int(0)

image_source = ['back_depth', 'back_depth_in_visual_frame', 'back_fisheye_image', 'frontleft_depth', 'frontleft_depth_in_visual_frame', 'frontleft_fisheye_image', 'frontright_depth', 'frontright_depth_in_visual_frame', 'frontright_fisheye_image', 'left_depth', 'left_depth_in_visual_frame', 'left_fisheye_image', 'right_depth', 'right_depth_in_visual_frame', 'right_fisheye_image']

camera = ""
c_index = int(0)

print("Create Robot")
#sdk = bosdyn.client.create_standard_sdk('understanding-spot')
#
#robot = sdk.create_robot('192.168.80.3')
#
#id_client = robot.ensure_client('robot-id')
#
#print(id_client.get_id())
#
#fut = id_client.get_id_async()
#
#print(fut.result())
#
#robot.authenticate('atom', 'atom29589990')
#
#state_client = robot.ensure_client('robot-state')
#
#state_bot = state_client.get_robot_state()

#image_client = robot.ensure_client(ImageClient.default_service_name)
#sources = image_client.list_image_sources()
#[source.name for source in sources]
#['back_depth', 'back_depth_in_visual_frame', 'back_fisheye_image', 'frontleft_depth', 'frontleft_depth_in_visual_frame', 'frontleft_fisheye_image', 'frontright_depth', 'frontright_depth_in_visual_frame', 'frontright_fisheye_image', 'left_depth', 'left_depth_in_visual_frame', 'left_fisheye_image', 'right_depth', 'right_depth_in_visual_frame', 'right_fisheye_image']
#
#image_response = image_client.get_image_from_sources(["left_fisheye_image"])[0]
#
#image = Image.open(io.BytesIO(image_response.shot.image.data))
#image.show()


    #print(PtzClient)
    #ptz_client = robot.ensure_client(PtzClient.default_service_name)

    #print(ptz_client.get_ptz_position())


def save(x,y,z):
    global zoom
    global vertical
    global horizontal
    zoom = z
    vertical = y
    horizontal = x
    
def reset():
    global zoom
    global vertical
    global horizontal
    zoom = 0
    vertical = 0
    horizontal = 0

    
def get():
    global zoom
    global vertical
    global horizontal
    x = horizontal
    y = vertical
    z = zoom
    return x,y,z
    

def on_press(key):
    print('\033c')
    global default_menu
    global select_menu
    global camera
    global c_index
    global image_source
    print("Menu: ",default_menu)
    r = False
    c = False
    x,y,z = get()
    try:
        #print('Alphanumeric key pressed: {0} '.format(
        #    key.char))
        if key.char == '=':
            if select_menu == " Ptz":
                print("Zooming in")
                z+=1
                c = True
        elif key.char == '-':
            if select_menu == " Ptz":
                if z>0:
                    print("Zooming out")
                    z-=1
                    c = True
        elif key.char == 'w':
            print("Going forward")
        elif key.char == 'd':
            print("Going to the right")
        elif key.char == 'a':
            print("Going to the left")
        elif key.char == 's':
            print("Going backward")
        elif key.char == '1':
            camera = image_source[0]
            select_menu = " Image"
        elif key.char == '2':
            select_menu = " Ptz"
    except AttributeError:
        #print('special key pressed: {0}'.format(
        #    key))
        if key == Key.up:
            #print("Turn Spot-cam UP")
            if select_menu == " Ptz":
                if y >-90 and y <90:
                    y+=1
                    c = True
        elif key == Key.down:
            #print("Turn Spot-cam Down")
            if select_menu == " Ptz":
                if y>-90:
                    y-=1
                    c = True
        elif key == Key.left:
            #print("Turn Spot-cam left")
            if select_menu == " Ptz":
                if x>0:
                    x-=1
                    c = True
            elif select_menu == " Image":
                c_index = c_index - 1
                if c_index <0:
                    c_index = 0
                camera = image_source[c_index]
                print("previous camera view",camera)
                ###
        elif key == Key.right:
            #print("Turn Spot-cam right")
            if select_menu == " Ptz":
                if x >= 0 and x <=360:
                    x+=1
                    c = True
            elif select_menu == " Image":
                c_index = c_index + 1
                if c_index == len(image_source):
                    c_index = 0
                camera = image_source[c_index]
                print("next camera view",camera)
        elif key == Key.backspace:
            print("Turn Spot-cam Reset")
            reset()
            r = True
            c = True
        elif key == Key.enter:
            if select_menu == " Image":
                #global image_client
                #image_response = image_client.get_image_from_sources(["left_fisheye_image"])[0]
                print("Capture Image with",camera)
            elif select_menu == " Ptz":
                print("Capture Ptz")
    if r == False:
        save(x,y,z)
    if c == True:
        if select_menu == " Ptz":
            print("Command the spot-cam with ",horizontal,vertical,zoom)
        elif select_menu == " Image":
            print("Change Camera")
    #print("Result",horizontal,vertical,zoom)
    print("Status:",select_menu)

def on_release(key):
    #print('Key released: {0}'.format(
    #    key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # Collect events until released
    with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

main()
