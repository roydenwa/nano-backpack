# robotics_practical
Codebase for robotics practical (MScTI_ROBP) in summer term 2020, Heidelberg University

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

## TODO
* Milestones aktuell halten
* etc.

## Milestones:
- [ ] test development env for ROS (in docker?)
- [ ] try nao/ naoqi with ROS: http://wiki.ros.org/nao
- [ ] use DenseDepth as basemodel for depth estimation: https://arxiv.org/pdf/1812.11941v2.pdf
- [ ] try to change basemodel of DensDepth to MobileNet V1/V2 to increase speed
- [ ] create nodes for CV in ROS (Python - opencv, tf/torch)
- [ ] try to convert depth images to point clouds via: http://wiki.ros.org/depth_image_proc
- [ ] implement functions in ROS nodes to check if navigation in certain direction is possible based on point cloud of surroundings
