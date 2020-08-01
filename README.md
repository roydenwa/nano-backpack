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
navigate into ROS folder
build:
```bash
docker build -t "ros-vnc-py3.7" .
```
run:
```bash
docker run -it --rm -p 6080:80 "ros-vnc-py3.7"
```
browse localhost:6080

## TODO
* Milestones aktuell halten
* etc.

## Milestones:
- [ ] test development env for ROS (in docker?)
- [ ] try nao/ naoqi with ROS: http://wiki.ros.org/nao
- [ ] use DenseDepth as basemodel for depth estimation: https://arxiv.org/pdf/1812.11941v2.pdf
- [ ] try to change basemodel of DensDepth to MobileNet V1/V2 to increase speed
- [ ] write test-funcs to showcase depth estimation model in realtime via your webcam
- [ ] create nodes for CV in ROS (Python - opencv, tf/torch)
- [ ] use opencv to detect if dark blue colored objects are in the desired direction and decline movement if so
    - [ ] get desired direction and draw on depth image
    - [ ] use color picker to check if movement in chosen direction is possible (dark blue == not possible)
    - [ ] try to implement a color search algo in opencv similar to SSD (single shot detector)
- [ ] optional: try to convert depth images to point clouds via: http://wiki.ros.org/depth_image_proc
- [ ] implement functions in ROS nodes to check if navigation in certain direction is possible based on point cloud of surroundings
