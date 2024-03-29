![tmp4o5usx_i](https://user-images.githubusercontent.com/49804761/118060916-7c12cc00-b359-11eb-98a3-c1aefe756891.jpg)

# CMP_SC 4990 Undergraduate Research in Computer Science /Spring 2021 / University of Missouri 
## Instructor: Dr. Dale Musser
#### The Spot from Boston Dynamics / Thunnathorne Synhiranakkrakul ( TSFQX ) [14351543]

### **Spot Camera:**
![spot](https://user-images.githubusercontent.com/49804761/118058251-613d5900-b353-11eb-8e56-b0d68c8d3f03.gif)


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

## Diagram:

### Normal Install Spots First-time Diagram:
![Install_Spot_Diagram](https://user-images.githubusercontent.com/49804761/117063358-539c2980-acea-11eb-8e15-ffaea315e7af.jpg)


### Work on Spots Diagram:
![Run_Spot_Diagram](https://user-images.githubusercontent.com/49804761/117063418-6ca4da80-acea-11eb-9705-064c116ab8a0.jpg)


### Overview Tsfqx Project Diagram: Algorithm in Program
![Tsfqx_SpotProject_Diagram](https://user-images.githubusercontent.com/49804761/118049651-a6598f00-b343-11eb-9d24-93c043a5bc5e.jpg)


### Setup Spot Process Diagram: Tsfqx Program
![Setup_robot](https://user-images.githubusercontent.com/49804761/117382454-2bf0c100-aea4-11eb-831e-cde155a3f3a9.jpg)


### Spot | Body Camera Process Diagram: Tsfqx Program
![Image_Diagram](https://user-images.githubusercontent.com/49804761/117373041-2b4e2f80-ae90-11eb-97b3-ec4527f42a46.jpg)


### Spot CAM | Ptz Process Diagram: Tsfqx Program
![Ptz_Diagram](https://user-images.githubusercontent.com/49804761/117374042-08bd1600-ae92-11eb-8daf-ba4cfe33f556.jpg)


## Implementations:
- My implement is consist of 4 parts:
  1. Initial Spot → Install the spots in program
  2. Detect Input → Detecting input from the users
  3. Body Camera Spot → Controlling the Body Camera of the spot
  4. Ptz → Controlling the Spot CAM Ptz 
  5. MediaLog  → Capturing Images from Spot CAM Ptz

#### Initial Spot Part:
- [x] Import Libraries:
```python 
  import bosdyn.client
```
- [x] Install SDK:
```python 
  sdk = bosdyn.client.create_standard_sdk('spot')
```
- [x] Register Spot CAM SDK: Used for Ptz
```python 
  spot_cam.register_all_service_clients(sdk)
```
- [x] Create Robot Instance:
```python 
  robot = sdk.create_robot('$SPOTIP')
```
- [x] Authenticated Spot:
```python 
  robot.authenticate('$username', '$password')
```

#### Detect Input Part:
- [x] Import Libraries:
```python 
  from pynput import keyboard
  from pynput.keyboard import Key 
```
- [x] Detecting Input from Keyboard:
```python 
  with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
```
- [x] Create an condition to separate control between the body cam and ptz cam:
  - [x] Using Function below to detect input:
      ```python 
          def on_press(key): #Detecting the button that user press on keyboard 
      ```
    - [x] Press 1 for controlling body cam or Press 2 for controlling Ptz cam:
      - [x] Press 1 for Control Spot Body Cam condition: 
        ```python 
        if key.char == '1':
          camera = image_source[0]
          select_menu = " Image"
        ```
      - [x] Press 2 for Control Spot Cam Ptz condition: 
        ```python 
        if key.char == '2':
          select_menu = " Ptz" 
        ```
  - [x] For Press 1 (Control Body Cam): 
    ```python 
    if select_menu == " Image":
    ```
    - [x] Using Left-arrow button ( ← ) [previous camera view] and Right-arrow button ( → ) [next camera view] to switch the camera view
      - [x] For Left-arrow button ( ← ):
        ```python 
        elif key == Key.left:
          c_index = c_index - 1               # Decrease Index of Camera View 
          if c_index <0:                      # Check Index is not lower than zero after subtracted
            c_index = 0                       # If the result lower than zero assign zero instead of the result
            camera = image_source[c_index]    # Save Current Camera View
        ```
      - [x] For Right-arrow button ( → ):
        ```python 
        elif key == Key.right:
          c_index = c_index + 1               # Increase Index of Camera View 
          if c_index == len(image_source):    # Check Index out of range or not after add index
            c_index = 0                       # If the result higher than the max index assign zero instead of the result
            camera = image_source[c_index]    # Save Current Camera View
        ```
       - [x] While using buttons, save the position of camera in variable
    - [x] Using return button ( ↩ ) to Capture the picture from camera on each view that the user choose and save to local storage 
     ```python 
       image_response = image_client.get_image_from_sources([camera])[0]
     ```

  - [x] For Press 2 (Control Spot Cam, PTZ):
    ```python 
      if select_menu == " Ptz":
    ```
    - [x] Set default Pan, tilt, Zoom in global:
    ```python 
      horizontal  = int(0)
      vertical    = int(0)
      zoom        = int(0)
    ```
    - [x] Using Left-arrow button ( ← ) and Right-arrow button ( → ) to switch the camera view in horizontal (Hold value in variable)
      - [x] For Left-arrow button ( ← ):
        ```python 
          if x>0:
            x-=1
            ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
            c = True #Show current position on main display
        ```
      - [x] For Right-arrow button ( → ):
        ```python 
          if x >= 0 and x <=360:
              x+=1
              ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
              c = True #Show current position on main display
        ```
    - [x] Using Up-arrow button ( ↑ ) and Down-arrow button ( ↓ ) to switch the camera view in Vertical (Hold value in variable)
        - [x] For Up-arrow button ( ↑ ):
           ```python 
              if key == Key.up:
                  if select_menu == " Ptz":
                      if y >-90 and y <90:
                          y+=1
                          ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                          c = True
           ```
        - [x] For Down-arrow button ( ↓ ):
           ```python 
              elif key == Key.down:
                  if select_menu == " Ptz":
                      if y>-90:
                          y-=1
                          ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                          c = True
           ```
    - [x] Using = and - to zoom in and out respectively (Hold value in variable)
      - [x] For = : Zoom in
          ```python 
            if key.char == '=':
            if select_menu == " Ptz":
                ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                z+=1
                c = True
          ```
      - [x] For - : Zoom out
          ```python
            elif key.char == '-':
              if select_menu == " Ptz":
                  if z>0:
                      ptz_position = ptz_client.set_ptz_position(ptz_desc,x,y,z)
                      z-=1
                      c = True
          ```
#### Camera Spot Part:
- [x] Import the library for using Camera Spot:
  ```python 
    from bosdyn.client.image import ImageClient #operate spot camera
    from PIL import Image #open image file
    import io
  ```
- [x] Create Image instance: To use the camera
  ```python 
    image_client = robot.ensure_client(ImageClient.default_service_name)
  ```
- [x] Switching the camera view by pressing button 
  ```python 
    camera = image_source[c_index]  #Increase or Decrease c_index to change camera view 
  ```
- [x] Pressing Enter to Capture the picture
  ```python 
    image_response = image_client.get_image_from_sources([camera])[0]
  ```

#### Ptz Part:
- [x] Import the library for using Spot CAM (Ptz):
  - [x] Control the Ptz Spot CAM:
    ```python 
    from bosdyn.client.spot_cam.ptz import PtzClient
    from bosdyn.client import spot_cam
    from bosdyn.api.spot_cam import ptz_pb2
    ```
  - [x] Capture Image from the Ptz Spot CAM:
    ```python 
        from bosdyn.client.spot_cam.media_log import MediaLogClient
        from bosdyn.api import image_pb2
        from bosdyn.api.spot_cam import logging_pb2, camera_pb2
        import tempfile
        import shutil
        import os
        class Namespace:
          def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    ```
- [x] Register Spot Cam (Ptz):
  ```python 
    spot_cam.register_all_service_clients(sdk)
  ```
- [x] Create Ptz instance:
  ```python 
    ptz_client = robot.ensure_client(PtzClient.default_service_name)
  ```
- [x] Calling set position medthod of Ptz (spot cam)
  ```python 
    option_name = "mech"
    ptz_desc = ptz_pb2.PtzDescription(name=option_name)
    ptz_position = ptz_client.set_ptz_position(ptz_desc,pan,tilt,zoom)
  ``` 
- [x] Synchronize the Ptz with the keyboard command
- [x] Create Medialog instance: for Capture Image From Ptz
  ```python 
    medialog_client = robot.ensure_client(MediaLogClient.default_service_name)
    args = (camera_pb2.Camera(name="ptz"),logging_pb2.Logpoint.STILLIMAGE)
  ```
- [x] Capture Image From Ptz:   
  ```python 
      global args          
      lp = medialog_client.store(*args)
                
      while lp.status != logging_pb2.Logpoint.COMPLETE:
        lp = medialog_client.get_status(lp)
              
      options = Namespace(camera_name='ptz', command='media_log', dst=None, hostname='192.168.80.3', media_log_command='store_retrieve', password='$PASSWORD',save_as_rgb24=False, stitching=True, username='$USERNAME',verbose=False)
            
      ir_flag = hasattr(options, 'camera_name') and options.camera_name == 'ir'
                
      if options.stitching or ir_flag:
        lp, img = robot.ensure_client(MediaLogClient.default_service_name).retrieve(lp)
      else:
        lp, img = robot.ensure_client(MediaLogClient.default_service_name).retrieve_raw_data(lp)
                    
      with tempfile.NamedTemporaryFile(delete=False) as img_file:
        img_file.write(img)
        src_filename = img_file.name
                
      dst_filename = os.path.basename(src_filename)
                
      if lp.image_params.height == 4800 or (lp.image_params.width == 640 and lp.image_params.height == 512):
        shutil.move(src_filename, '{}.jpg'.format(dst_filename))
      else:
        target_filename = '{}-{}x{}.rgb24'.format(dst_filename, lp.image_params.width, lp.image_params.height)
        shutil.move(src_filename, target_filename)
        if not options.save_as_rgb24:
          with open(target_filename, mode='rb') as fd:
            data = fd.read()
          mode = 'RGB'
          image = Image.frombuffer(mode, (lp.image_params.width, lp.image_params.height), data, 'raw', mode, 0, 1)
          image.save('{}.jpg'.format(dst_filename))
          os.remove(target_filename)
  ```

## Experimental results:

  #### Detect Input Part:
  - Obstacle:
    - Find the area to put condition
    - Handle error with listening keyboard function
  - Success:
    - [x] Detecting the input from keyboard and condition 
    - [x] Separate function between Body cam and Ptz cam 
    - [x] Memorized current pan, tilt, zoom and the position of camera spot during switch Body cam and Ptz cam
    - [x] Swithing between Image and Ptz mode smoothly with save previous value
 
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
    -  Calling methods of Medialog's instance and passing the parameter
    -  Save Image from Ptz
   
  - Success:
    -  [x] Import the ptz library   
    -  [x] Register the ptz module   
    -  [x] Create Ptz instance
    -  [x] Calling Set Position Method of Ptz  
    -  [x] Adjust Angle of Ptz camera
    -  [x] Import the medialog library
    -  [x] Capture Image from return button
    -  [x] Save image from Ptz camera into local storage 

## Result Video:

[![My Project](http://img.youtube.com/vi/h1B-MOwWQ7g/0.jpg)](http://www.youtube.com/watch?v=h1B-MOwWQ7g "Youtube")

## Example: Result From Ptz Spot CAM:
![video_ptz](https://user-images.githubusercontent.com/49804761/118060789-33f3a980-b359-11eb-8c5d-b8d395945ff2.jpg)

## Example: Result From Body Spot camera:
![result](https://user-images.githubusercontent.com/49804761/118061294-4f12e900-b35a-11eb-89e3-d7fe6d08eece.png)

## Conclusions:
- For this project, I learn how to install the spot SDK, the restriction with connecting to the spot technically, how to run the code from laptop to spot, know how the spot works such as when we turn on the spot with blue button, it does not mean we power on the spot, it means the brain or CPU inside of spot waiting for the command from controller or program that we wrote, the spot cannot move until we press the button next to the power button which is red, this button will unlock all of the joint of the Spot. if we turn the blue button, it will consume energy lower than we turn on the blue button with the red button because the joint will consume the power a lot. the CPU, which is the brain of the spots, is intelligent because even we try to command whatever it is, the spot will think about what he can do it or not, if he can do it, your command will work. on the other hand, if not, he will deny and it will show up as an error on the terminal. from my research, I learn more about how to connect the spot with my own program, how to detect input from the keyboard, how to switch the camera and capture an image with the body cam, how to adjust the angle, and capture images from Ptz Spot cam. moreover, I would like to focus on how to control the spots by creating the program from python to control the spots by using a keyboard instead of the main controller for the prototype, and further, I might transform it into Moblie Application after we figure it out how to control it by coding with Boston Dynamics Library or using for Machine Learning, Deep Learning that using Ptz Spot cam by expanding the perspective view, finally, all of the objective and implementation on this project are successfully that can command body cam and Ptz spot cam in terms of the program and also demo video result will obviously visualize the result from this course. 
