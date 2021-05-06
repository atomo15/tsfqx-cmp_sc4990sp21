
import bosdyn.client

from pynput import keyboard
from pynput.keyboard import Key
from pynput.keyboard import Listener

from bosdyn.client.image import ImageClient #get ImageClient instance

#register spot cam for Ptz
from bosdyn.client.spot_cam.ptz import PtzClient
from bosdyn.client import spot_cam
from bosdyn.api.spot_cam import ptz_pb2
#register spot cam for Ptz

#Ptz capture
from bosdyn.client.spot_cam.media_log import MediaLogClient
from bosdyn.api import image_pb2
from bosdyn.api.spot_cam import logging_pb2, camera_pb2
#Ptz capture

from PIL import Image #open image file
import io

import inspect




#print(dir(PtzClient.get_ptz_position))

#print(inspect.getfullargspec(PtzClient.get_ptz_position))

#Set main menu
default_menu = "1: Image | 2: Ptz"
select_menu = ""
#Set main menu




#set up choice for camera
image_source = ['back_depth', 'back_depth_in_visual_frame', 'back_fisheye_image', 'frontleft_depth', 'frontleft_depth_in_visual_frame', 'frontleft_fisheye_image', 'frontright_depth', 'frontright_depth_in_visual_frame', 'frontright_fisheye_image', 'left_depth', 'left_depth_in_visual_frame', 'left_fisheye_image', 'right_depth', 'right_depth_in_visual_frame', 'right_fisheye_image']
#set up choice for camera

#Set default camera and camera index
camera = "back_depth"
c_index = int(0)
#Set default camera and camera index

print("Create Robot")

sdk = bosdyn.client.create_standard_sdk('understanding-spot')

#register spot cam for Ptz
spot_cam.register_all_service_clients(sdk)
#register spot cam for Ptz

robot = sdk.create_robot('192.168.80.3')

id_client = robot.ensure_client('robot-id')

#print(id_client.get_id())

fut = id_client.get_id_async()

#print(fut.result())

robot.authenticate('atom', 'atom29589990')

state_client = robot.ensure_client('robot-state')

state_bot = state_client.get_robot_state()

print(state_bot)

#Set up image instance
image_client = robot.ensure_client(ImageClient.default_service_name)
sources = image_client.list_image_sources()
#Set up image instance

#Set up Ptz

#Store pan tilt zoom values
horizontal = int(0)
vertical = int(0)
zoom = int(0)
#Store pan tilt zoom values

option_name = "mech"
ptz_desc = ptz_pb2.PtzDescription(name=option_name)
ptz_client = robot.ensure_client(PtzClient.default_service_name)
#Set up Ptz

#Ptz capture
medialog_client = robot.ensure_client(MediaLogClient.default_service_name)
#options = Namespace(camera_name='ptz', command='media_log', dst=None, hostname='192.168.80.3', media_log_command='store_retrieve', password='atom29589990', save_as_rgb24=False, stitching=True, username='atom', verbose=False)
#options = [camera_name='ptz',command='media_log',dst=None,hostname='192.168.80.3',media_log_command='store_retrieve',password='atom29589990',save_as_rgb24=False,stitching=True,username='atom',verbose=False]
#
#args = (camera_pb2.Camera(name="ptz"), logging_pb2.Logpoint.STILLIMAGE)
#
#lp = client.store(*args)
#
#while lp.status != logging_pb2.Logpoint.COMPLETE:
#    lp = client.get_status(lp)
#
#lp = MediaLogRetrieveCommand.save_logpoint_as_image(robot, lp, options, dst_filename=None)

#Ptz capture




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
    global ptz_client
    global ptz_desc
    zoom = 0
    vertical = 0
    horizontal = 0
    ptz_position = ptz_client.set_ptz_position(ptz_desc,0,0,0)

    
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
    global ptz_desc
    global ptz_client
    print("Menu: ",default_menu)
    r = False
    c = False
    x,y,z = get()
    try:
        #print('Alphanumeric key pressed: {0} '.format(
        #    key.char))
        if key.char == '=':
            if select_menu == " Ptz":#print("Zooming in")
                ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                z+=1
                c = True
        elif key.char == '-':
            if select_menu == " Ptz":#print("Zooming out")
                if z>0:
                    ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
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
            if select_menu == " Ptz":#print("Turn Spot-cam UP")
                if y >-90 and y <90:
                    y+=1
                    ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                    c = True
        elif key == Key.down:
            if select_menu == " Ptz":#print("Turn Spot-cam Down")
                if y>-90:
                    y-=1
                    ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                    c = True
        elif key == Key.left:
            if select_menu == " Ptz":#print("Turn Spot-cam left")
                if x>0:
                    x-=1
                    ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                    c = True
            elif select_menu == " Image":
                c_index = c_index - 1
                if c_index <0:
                    c_index = 0
                camera = image_source[c_index]
                print("Camera View : ",camera)
                ###
        elif key == Key.right:
            if select_menu == " Ptz":#print("Turn Spot-cam right")
                if x >= 0 and x <=360:
                    x+=1
                    #global ptz_client
                    ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                    c = True
            elif select_menu == " Image":
                c_index = c_index + 1
                if c_index == len(image_source):
                    c_index = 0
                camera = image_source[c_index]
                print("Camera View : ",camera)
        elif key == Key.backspace:
            print("Turn Spot-cam Reset")
            reset()
            r = True
            c = True
        elif key == Key.enter:
            if select_menu == " Image":
                global image_client
                image_response = image_client.get_image_from_sources([camera])[0]
                print("Capture Image with",camera)
                image = Image.open(io.BytesIO(image_response.shot.image.data))
                image.show()
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
    print("Ready")
    with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

main()
