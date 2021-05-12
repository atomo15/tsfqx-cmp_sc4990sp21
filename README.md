# CMP_SC 4990 Undergraduate Research in Computer Science /Spring 2021 / University of Missouri 
## Instructor: Dr. Dale Musser
#### The Spot from Boston Dynamics / Thunnathorne Synhiranakkrakul ( TSFQX ) [14351543]

### **Spot Camera:**
![spot_body](https://user-images.githubusercontent.com/49804761/117091110-eacfa400-ad1f-11eb-9dbb-e38d3e4c62f7.jpeg)

### Spot Cam (PTZ):
![spot_cam](https://user-images.githubusercontent.com/49804761/117091165-0c309000-ad20-11eb-9555-f0053f610bef.jpeg)




### **Motivations**
- Nowadays, people keep the smartphone with them all the time, In order to Control the Spots without using the main controller, this project is a prototype of creating a controller using the keyboard to control the camera of spots and spot cam which is Ptz camera. if we can switch the view of body camera of spot, adjust the perspective of Ptz camera like turn the Spot CAM to be left-right, up-down, and zoom in-out by button on the keyboard. moreover, hit the return on the keyboard to capture both images. we would have more mobility to uses both cameras and switching control by press 1 or 2 to switch mode between body camera and Ptz spot cam. the result from this research could be adapted to control both cameras with the transform from keyboard to another platform that can use to be a controller such as iOS or Android, in the future to make more mobility to control the spots and can carry your controller with them all the time, easy to charge controller. finally, all of this research could be used with detecting the object from the camera by changing the view of both cameras in order to easy to observe. 


### Objectives:
- Learn about how to set up, install and use the Spot
- Learn about how to control the robot from the program and controller
- Understand how the spots work
- Understand the library and structure of Boston Dynamics Stuff
- Understand how to adapt the Boston Dynamics to python programing 
- Learn how to switch camera and capture images from body of spot by program
- Learn how to control the angle and capture images from Ptz Spot Cam by program

### Backgrounds:
- The problem is when we want to control the spot, we need to control it by the main controller which is big like a PSP( PlayStation Portable) or Nintendo switch with a big Android screen and not easy to carry. if we could transform the controller into Mobile Application in order to have more mobility caused by today people always keep the phone with them all the time. moreover, in order to detect objects using the camera for analyzing the data such as Images Processing, Machine Learning, and Deep Learning. all of these might need to observe around the spots that need to explore more dimensions, more perspective view for better analysis that why we need to understand how to use the equipment of Boston Dynamics which is spots in terms of coding and solve all of these problems.

### Diagram:

### Normal Install Spots First-time Diagram:
![Install_Spot_Diagram](https://user-images.githubusercontent.com/49804761/117063358-539c2980-acea-11eb-8e15-ffaea315e7af.jpg)


### Work on Spots Diagram:
![Run_Spot_Diagram](https://user-images.githubusercontent.com/49804761/117063418-6ca4da80-acea-11eb-9705-064c116ab8a0.jpg)


### Overview Tsfqx Project Diagram: Algorithm in Program
![Tsfqx_SpotProject_Diagram](https://user-images.githubusercontent.com/49804761/117382573-6d816c00-aea4-11eb-84c2-6dc6a4256f82.jpg)


### Setup Spot Process Diagram: Tsfqx Program
![Setup_robot](https://user-images.githubusercontent.com/49804761/117382454-2bf0c100-aea4-11eb-831e-cde155a3f3a9.jpg)


### Spot | Body Camera Process Diagram: Tsfqx Program
![Image_Diagram](https://user-images.githubusercontent.com/49804761/117373041-2b4e2f80-ae90-11eb-97b3-ec4527f42a46.jpg)


### Spot CAM | Ptz Process Diagram: Tsfqx Program
![Ptz_Diagram](https://user-images.githubusercontent.com/49804761/117374042-08bd1600-ae92-11eb-8daf-ba4cfe33f556.jpg)


### Implementations:
- My implement is consist of 4 parts:
  1. Initial Spot → Install the spots in program
  2. Detect Input → Detecting input from the users
  3. Body Camera Spot → Controlling the Body Camera of the spot
  4. Ptz → Controlling the Spot CAM Ptz 

#### Initial Spot Part:
- [x] Import Libraries:
  - [x] import bosdyn.client
- [x] Install SDK:
  - [x] sdk = bosdyn.client.create_standard_sdk('spot')
- [x] Register Spot CAM SDK: Used for Ptz
  - [x] spot_cam.register_all_service_clients(sdk)
- [x] Create Robot Instance:
  - [x] robot = sdk.create_robot('$SPOTIP')
- [x] Authenticated Spot:
  - [x] robot.authenticate('$username', '$password')

#### Detect Input Part:
- [x] Import Libraries:
  - [x] from pynput import keyboard
  - [x] from pynput.keyboard import Key 
- [x] Detecting Input from Keyboard:
  - [x] with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
- [x] Create an condition to separate control between the body cam and ptz cam:
  - [x] Using def on_press(key): #Detecting the button that user press on keyboard 
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
- [x] Import the library for using Camera Spot:
  - [x] from bosdyn.client.image import ImageClient #operate spot camera
  - [x] from PIL import Image #open image file
  - [x] import io
- [x] Create Image instance: To use the camera
  - [x] image_client = robot.ensure_client(ImageClient.default_service_name)
- [x] Switching the camera view by pressing button 
  - [x] camera = image_source[c_index]  #Increase or Decrease c_index to change camera view 
- [x] Pressing Enter to Capture the picture
  - [x] image_response = image_client.get_image_from_sources([camera])[0]

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
  - [x] ptz_position = ptz_client.set_ptz_position(ptz_desc,pan,tilt,zoom)
- [x] Synchronize the Ptz with the keyboard command
- [ ] Calling get Image od Ptz (spot cam)


### Experimental results:

  #### Detect Input Part:
  - Obstacle:
    - Find the area to put condition
    - Handle error with listening keyboard function
  - Success:
    - [x] Detecting the input from keyboard and condition 
    - [x] Separate function between Body cam and Ptz cam 
    - [x] Memorized current pan, tilt, zoom and the position of camera spot during switch Body cam and Ptz cam
 
  #### Body Camera Part:
  - Obstacle:
    - Capture over 5 photos continously without program crashes 
  - Success:
    - [x] Import the Image library  
    - [x] Create Image instance
    - [x] Change Camera View
    - [x] Get Images from these camera

  #### Ptz Part:
  - Obstacle:
    -  Calling Methods of Ptz's instance and passing the parameter
    -  Register the ptz package
   
  - Success:
    -  [x] Import the ptz library   
    -  [x] Register the ptz module   
    -  [x] Create Ptz instance
    -  [x] Calling Set Position Method of Ptz  

### Result Video:


### Conclusions:
- For this project, we would like to focus on how to control the spots by creating the program from python to control the spots by using a keyboard instead of the main controller for the prototype, and further, we might transform it into Moblie Application after we figure it out how to control it by coding with Boston Dynamics Library
