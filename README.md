# Nano-backpack for NAO robot
Nano-backpack is an open hardware add-on for the humanoid robot NAO. It adds
a Nvidia Jetson Nano development board to the robot and thereby enhances the com-
putational capabilities of the system. The corresponding software architecture includes
a webapp to control the robot and allows an easy start into the development of further
applications.
This project was part of the Robotics Practical class (MScTI_ROBP) in summer term 2020 @ Heidelberg University.

## Setup:
<details><summary><b>Install and setup linux-wifi-hotspot on Jetson Nano</b></summary>

1. Install depencendiecs:

    ```sh
    sudo apt install -y libgtk-3-dev build-essential gcc g++ pkg-config make hostapd
    ```
2. Clone repo and build:

    ```sh
    git clone https://github.com/lakinduakash/linux-wifi-hotspot
    cd linux-wifi-hotspot

    # build binaries
    make

    # install
    sudo make install
    ```
3. Open application and create hotspot with `rndis0` preset
4. Run linux-wifi-hotspot on every startup:
    ```sh
    systemctl enable create_ap
    ```
</details>
<details><summary><b>Clone this repo and build Docker Image:</b></summary>
</details>

## TODO:
- [ ] Docu
   - [x] Simplify Layout - Alex frist page - abstract and contents, header
    - [x] Abstract
    - [X] Introduction - Alex / Royden
    - [x] Related works Backpack - Alex
    - [X] Related works Monocular - Royden 
    - [ ] Related Works optional: linux-wifi-hotstpot ? - Royden
    - [ ] Instructions for Peter - Peter how to - Alex
        - [x] pw user on Nano
        - [x] pw wlan nano-bp
        - [x] ip ssh
        - [x] standard ip NAO robot
        - [x] Table compatible Naoqi-SDKs (Offical: Python: no(not suitable for ARM), Javascript: qimessaging yes, qi2: yes, C++: not tested, Third-party: ROS: deprecated,   NodeJs~yorki: yes)
        - [ ] Development Environment Nano:
        - [x] how to use docker and python on Nano with NAO
   - [ ] Mechanical design - Royden
   - [ ] Remote control NAO ~ UI5 - Royden / Alex
   - [X] Depth estimation - python-decorator - single-frame <-> video - Royden
   - [ ] Conclusion: - Alex / Royden
      - [ ] benefit: easy start - dev env - UI for for testing
      - [ ] outlook: python base for depthestimation, JS base for more NAOqi-services
- [ ] App
   - [x] NAOs view - placeholder img of NAO - Alex
   - [X] ui5-datamodel ip, text params - Royden
   - [X] Import Error qimessaging - Royden
   - [ ] update readme, clean repo 
   - [X] Docker images - Royden
 
## ML Colab notebooks:
* monocular depth estimation: https://colab.research.google.com/drive/1gyQloTjFFWqocp1bS43dUadsRt_RBJK7?usp=sharing
* diagram for system overview: https://colab.research.google.com/drive/17LU7zdjKQaLcvlP8urdSHtBXtgi4b-lk?usp=sharing 
## Report
* Overleaf: https://www.overleaf.com/4935392816vjjswyvgnhcr
  * Note: link sharing is active

