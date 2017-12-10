# GUIGoPiGo

GUIGoPiGo is a system that allows a user to navigate the Raspberry Pi powered GoPiGo robot, along a given maze. The maze is a whiteboard, with black electrical tape representing edges. When given nodes, represented by the blue buttons, the robot will calculate the shortest path using the A* pathfinding algorithm. The progress of the robot along the path is represented by blue lines, and a image of the robot moving to each respective node.

Additionally, the user can choose put an obstacle on an edge by clicking on any edge on the map, which will highlight red. The robot will take this into account during it's calculation, and attempt to find a different path. If there is no valid path to traverse, the robot will not move. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run the software, you'll need:

*A GoPiGO3 robot kit

*Raspberry Pi, running Raspbian for Robots (equpped with Wi-Fi dongle or onboard Wi-Fi)

*Python 3.4+ installed on the robot

*Pip

*tornado and GoPiGo modules

*A computer

*Any modern web browser (NOTE: The webpage has only been tested with Google Chrome, Mozilla Firefox, Internet Explorer/Microsoft Edge, and Chromium. Any other browsers, such as the browser that is included with the Raspberry Pi are NOT guaranteed to display the webpage properly/support websockets.)

### Installing

1. Click the "Clone or Download" button on GitHub to clone a copy of the repository. Download it as a zip file, and extract the contents to a USB stick.
2. Transfer the files into the desired directory on the Raspberry Pi.
3. Open the terminal, and ensure that you have the correct Python version (3.4+), and the modules tornado and GoPiGO installed. If not you can check your Python version and modules by entering these commands, and install the correct versions:
```
pip install tornado
```
```
python -V
```

## Running the Robot
1. Open the file titled "MasterControlProgram.py". This will bring up the
2. Open the file called "wepage.html". It is located in the path ```GUIGoPiGo/GUI/src/webpage.html``` .
3. Enter the IP address of your robot. You can also enter "localhost" if your robot is not connected to the internet.
4. Select the desired waypoints and/or blocked edges.
5. Place the rover on n1, facing the n2 node.
6. Click start.
7. Watch the robot go!! 

### Tips for Good Performance

Ensure the room that you plan to test in has adequate lighting. The line sensor is extremely sensitive, and lack of adequate lighting will cause the robot to deviate from it's path.

Make sure that the surface is clean and white, and the lines are black. The robot works by detecting raw values from the surface and converting them into absolute values (1 for black, and 0 for white). Smudges and dirt will negatively impact performance.

Check the charge the battery pack before EVERY SINGLE RUN. When the voltage goes below 10.00 volts, the line sensor and motors ecome subject to unpredictable behavior, making path traversal difficult. At 6.00 volts, the Raspberry PI will enter into safe mode, and there is a risk of corrupting all of the files on the memory card. 

## Contributors

* **Jason Jayatissa**- Documentation, GUI
* **Jeffrey Johnson**- Readme, GUI
* **Nathan O' Leary**- GUI
* **Charles Matthews**- Robot Controller
* **James Spagnola**- Pathfinding, Robot Controller
* **Sergio Valoy**- Documentation
* **Bastian Tenbergen**- Project Lead and Stakeholder 

## License
Copyright (c) 2017 by the principle investigator and contributors.

This project is licensed under the Creative Commons BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including the rights to use, copy, modify, merge,
publish, and/or distribute copies of the Software for non-commercial purposes,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments

* Dexter Industries
* CPS Rover
* Dr. Bastian Tenbergen
