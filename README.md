# TODO:

- [ ] Docu
 - [ ] Layout simplify - Alex frist page - abstract and contents, header
 - [ ] Related works Backpack - Alex
 - [ ] Related works Mooncular
 - [ ] Intructions for Peter - Peter how to - Alex
  - pw user on Nano
  - pw wlan nano-bp
  - ip ssh
  - standard ip NAO robot
  - Table compatible Naoqi-SDKs (Offical: Python: no(not suitable for ARM), Javascript: qimessaging yes, qi2: yes, C++: not tested, Third-party: ROS: deprecated,   NodeJs~yorki: yes)
  - Development Environment Nano:
   - how to use docker and python on Nano with NAO
 - [ ] Mechanical design - Royden
 - [ ] Remote control NAO ~ UI5 - Royden / Alex
 - [ ] Depthestiation - decorator -> single-frame <-> video - Royden
 - [ ] Conclusion: - Alex 
  - [ ] benefit: easy start - dev env - UI for for testing
  - [ ] outlook: python base for depthestimation, JS base for more NAOqi-services
- [ ] App
 - [ ] NAOs view - placeholder img of NAO - Alex
 - [ ] ui5-datamodel ip, text params - Royden
 - [ ] Import Error qimessaging - Royden
 - [ ] update readme, clean repo 
 - [ ] Docker images
 

# robotics_practical
Codebase for robotics practical (MScTI_ROBP) in summer term 2020, Heidelberg University

## ML Colab notebooks:
* monocular depth estimation: https://colab.research.google.com/drive/1gyQloTjFFWqocp1bS43dUadsRt_RBJK7?usp=sharing

## Daten:
* Bewerbungsfrist: 26.06.2020
  * abgeschickt: 10.06.2020
  * bestätigt: 17.06.2020
* Sicherheitsunterweisung: **30.06.2020, 14.00 Uhr**
* Ziel: **30.09.2020**
* Präsentation: Anfang Oktober
* Vorlesungsbeginn WS 2020/2021: 02.11.2020 &rarr; Puffer

## Orga
* Zugang:
  * 50 € Pfand
  * 1 Zugang &rarr; Alex
* peter.wittlinger@ziti.uni-heidelberg.de
* etc.

## How to build and run ROS Kinetic within a Docker Image and access the GUI via VNC
navigate into ROS folder,
build:
```bash
docker build -t "ros-vnc-py3.7" .
```
run:
```bash
docker run -it --rm -p 6080:80 "ros-vnc-py3.7"
# -it == interactive mode
# --rm == remove container after exit
# -p ... == port forwarding
```
browse: http://localhost:6080 or use VNC client

## TODO
* Milestones aktuell halten
* etc.

## Milestones:

# Testing and prep:
- [X] test development env for ROS (in docker?)
- [X] try nao/ naoqi with ROS: http://wiki.ros.org/nao
- [X] use DenseDepth as basemodel for depth estimation: https://arxiv.org/pdf/1812.11941v2.pdf
- [X] write test-funcs to showcase depth estimation model in realtime via your webcam

# Remote control NAO:
- [ ] construct NAO-nano-backpack
- [ ] write webapp to control NAO
- [ ] serve webapp with flask on nano

# Add depth estimation:
- [ ] use opencv to detect if dark blue colored objects are in the desired direction and decline movement if so
    - [ ] get desired direction and draw on depth image
    - [ ] use color picker to check if movement in chosen direction is possible (dark blue == not possible)
    - [ ] try to implement a color search algo in opencv similar to SSD (single shot detector)
- [ ] implement functions to check if navigation in certain direction is possible based on point cloud of surroundings
- [ ] optional: try to change basemodel of DensDepth to MobileNet V1/V2 to increase speed

# Diagram: 
- https://colab.research.google.com/drive/17LU7zdjKQaLcvlP8urdSHtBXtgi4b-lk?usp=sharing 
