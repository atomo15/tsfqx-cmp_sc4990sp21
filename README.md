# CMP_SC 4990 Undergraduate Research in Computer Science /Spring 2021 / University of Missouri 
## Instructor: Dr. Dale Musser
#### The Spot from Boston Dynamics / Thunnathorne Synhiranakkrakul ( TSFQX ) [14351543]

### **Spot Camera:**
![spot_body](https://user-images.githubusercontent.com/49804761/117091110-eacfa400-ad1f-11eb-9dbb-e38d3e4c62f7.jpeg)

### Spot Cam (PTZ):
![spot_cam](https://user-images.githubusercontent.com/49804761/117091165-0c309000-ad20-11eb-9555-f0053f610bef.jpeg)




### **Motivations**
- Nowadays people keep the smart phone with them all the time, In order to Control the Spots without using the main controller, this project is a prototype of creating a controller using the keyboard to control spots, future works, this project might be adapted to ios or android os in the future to make more mobility to control the spots and can carry your controller with them all the time, easy to charge controller.


### Objectives:
- Learn about how to set up, install and use the Spot 
- Learn about how to control the robot from program and controller
- Understand about how the spots work
- Understand the library and structure of Boston Dynamics Stuff

### Backgrounds:
- The problem is when we want to control the spot, we need to control it by the main controller which is big like a PSP with a big Android screen and not easy to carry. if we could transform the controller into Mobile Application in order to have more mobility caused by today people always keep the phone with them all the time. for this project, we would like to focus on how to control the spots by creating the program from python to control the spots by using a keyboard instead of the main controller for the prototype, and further, we might transform it into Moblie Application after we figure it out how to control it by coding with Boston Dynamics Library.

###Diagram:

### Install Spots Diagram:
![Install_Spot_Diagram](https://user-images.githubusercontent.com/49804761/117063358-539c2980-acea-11eb-8e15-ffaea315e7af.jpg)


### Work on Spots Diagram:
![Run_Spot_Diagram](https://user-images.githubusercontent.com/49804761/117063418-6ca4da80-acea-11eb-9705-064c116ab8a0.jpg)



### Overview Tsfqx Project Diagram:
![Tsfqx_SpotProject_Diagram](https://user-images.githubusercontent.com/49804761/117087850-57de3c00-ad16-11eb-9857-64dad4b07eda.jpg)

### Body Camera Diagram Process:
![Image_Diagram](https://user-images.githubusercontent.com/49804761/117349743-5b3a0a80-ae71-11eb-982e-c29486cc963b.jpg)



### Implementations:


#### Detect Input Part:
- [x] Import Libraries:
  - [x] from pynput import keyboard
  - [x] from pynput.keyboard import Key 
- [x] Detecting Input from Keyboard:
  - [x] with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
- [x] Create an condition to separate control between the body cam and ptz cam
- [x] Using def on_press(key): this Method including below elements
  - [x] Press 1 for controlling body cam or Press 2 for controlling Ptz cam:
    - [x] Press 1 for Control Spot Body Cam condition: 
      - [x] if key.char == '1':
      - [x] camera = image_source[0]
      - [x] select_menu = " Image"
    - [x] Press 2 for Control Spot Cam Ptz condition: 
      - [x] if key.char == '2':
      - [x] select_menu = " Ptz" 
- [x] For Press 1 (Control Body Cam): 
  - [x] if select_menu == " Image":
  - [x] Using Left-arrow button ( ← ) [previous camera view] and Right-arrow button ( → ) [next camera view] to switch the camera view
  - [x] While using buttons, save the position of camera in variable
    - [x] For Left-arrow button ( ← ):
      - [x] c_index = c_index - 1             # Decrease Index of Camera View 
      - [x] if c_index <0:                    # Check Index is not lower than zero after subtracted
      - [x] c_index = 0                       # If the result lower than zero assign zero instead of the result
      - [x] camera = image_source[c_index]    # Save Current Camera View
    - [x] For Right-arrow button ( → ):
      - [x] c_index = c_index + 1             # Increase Index of Camera View 
      - [x] if c_index == len(image_source):  # Check Index out of range or not after add index
      - [x] c_index = 0                       # If the result higher than the max index assign zero instead of the result
      - [x] camera = image_source[c_index]    # Save Current Camera View
  - [x] Using return button ( ↩ ) to Capture the picture from camera on each view that the user choose and save to local storage 
     - [x] image_response = image_client.get_image_from_sources([camera])[0]
     
- [x] For Press 2 (Control Spot Cam, PTZ):
  - [x] if select_menu == " Ptz":
  - [x] Using Left-arrow button ( ← ) and Right-arrow button ( → ) to switch the camera view in horizontal (Hold value in variable)
  - [x] Using Up-arrow button ( ↑ ) and Down-arrow button ( ↓ ) to switch the camera view in Vertical (Hold value in variable)
  - [x] Using = and - to zoom in and out respectively (Hold value in variable)

#### Camera Spot Part:
- [x] Creating intance that import from "from bosdyn.client.image import ImageClient" and calling robot.ensure_client method to make image client instance
- [x] Calling get image method
- [ ] Sync the button to the camera of spot
- [ ] Switching the camera view by pressing button 
- [ ] Pressing Enter to Capture the picture

#### Ptz Part:
- [x] Import the library for using Spot CAM (Ptz):
  - [x] from bosdyn.client.spot_cam.ptz import PtzClient
  - [x] from bosdyn.client import spot_cam
  - [x] from bosdyn.api.spot_cam import ptz_pb2
- [x] Register Spot Cam (Ptz):
  - [x] spot_cam.register_all_service_clients(sdk)
- [x] Create Ptz instance:
  - [x] ptz_client = robot.ensure_client(PtzClient.default_service_name)
- [x] Calling set position medthod of Ptz (spot cam)
  - [x] option_name = "mech"
  - [x] ptz_desc = ptz_pb2.PtzDescription(name=option_name)
  - [x] ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
- [x] Sync the Ptz with the keyboard command
- [ ] Calling get Image od Ptz (spot cam)


### Experimental results:

  #### Detect Input Part:
  - Obstacle:
    - Find the area to put condition
  - Progress:
    - Detecting the input from keyboard and condition is works
    - Separate function between Body cam and Ptz cam is works
 
  #### Body Camera Part:
  - Obstacle:
    - Capture in real time
  - Progress:
    - Image instance which is control body camera is work and can get images from these camera
    - Trying to select, switch the camera and capture image from the keyboard 

  #### Ptz Part:
  - Obstacle:
    -  Calling Methods of Ptz's instance and passing the parameter
    -  Register the ptz package
   
  - Progress:
    -  [x] Import the ptz library successfully  
    -  [x] Register the ptz module successfully  
    -  [x] Calling Set Position Method of Ptz successfully 


### Conclusions:

