# 보드세팅

## 하드웨어 세팅

### 배터리팩 제작
![그림1](https://github.com/HJW1250/Medication-management-aids/assets/114561883/515f3ee0-6618-45ba-b7dc-d7b446ee790e)
BMS 보호회로에 각 맞는 리튬이온배터리 단자를 연결해줍니다.
알맞은 입출력단자에 QC3.0 출력단자와 C타입 입력단자를 연결합니다.

### LCD, 카메라, IR 근접센서, LED 모듈 고정
![그림4](https://github.com/HJW1250/Medication-management-aids/assets/114561883/66ed320b-54e0-4a31-bd3d-a182dcf1ded5)
기존 가공된 외관에 LCD와 카메라, IR 근접센서, LED를 글루건이나 본드로 고정해줍니다.

### 핀 연결
![그림5](https://github.com/HJW1250/Medication-management-aids/assets/114561883/b43892e2-e552-4e40-892f-e5b9502fe7de)
핀 맵을 참고하여 라즈베리파이에 핀을 연결해줍니다.

### 스피커와 배터리 모듈 연결
![그림6](https://github.com/HJW1250/Medication-management-aids/assets/114561883/6f3c42f9-b619-4fe9-9469-9d531ae2a3ff)
스피커는 라즈베리파이 USB단자에 연결합니다.
배터리팩은 라즈베리파이 C타입전원 단자에 연결합니다.

### 완성본
![그림7](https://github.com/HJW1250/Medication-management-aids/assets/114561883/7dd99541-a89d-416d-9971-ce6ac35b1773)

## 라즈베리파이 내부 세팅

### Raspberry Pi OS 라즈비안 설치
https://www.raspberrypi.com/software/
접속하여서 OS 소프트웨어를 다운받습니다.
OS로 라즈비안 64-Bit를 선택합니다.

![noname01](https://github.com/HJW1250/Medication-management-aids/assets/114561883/07aac3b4-4273-4d0e-bcc2-6fad2f4578ed)
고급옵션(밑의 톱니바퀴)을 선택하여 SSH 사용과 무선 LAN을 설정해줍니다.
SSH 사용 => 비밀번호 인증 사용 => 사용자 이름 및 비밀번호 설정 => 무선 LAN 설정 => locale 설정 지정

### 라즈베리파이 초기 설정
윈도우 cmd창에서 nmap으로 라즈베리파이의 IP주소를 찾습니다.
```
$ nmap -sn 192.168.0.0/24
```
putty를 실행하여 라즈베리파이에 접속하여 업데이트를 진행해줍니다.
```
$ sudo apt update
```
```
$ sudo apt upgrade
```
/etc/dhcpcd.conf 파일 열어서 라즈베리파이에 고정 IP를 설정합니다
```
$ sudo apt install vim
```
```
$ sudo vim /etc/dhcpcd.conf
```
파일 맨 아래에 아래의 내용을 추가해줍니다.
```
interface wlan0
static ip_address = 
static routers =
```
networking service 재시작해준 이후 reboot해줍니다.
```
$ sudo /etc/init.d/networking restart
```
```
$ sudo reboot
```

### 라즈베리파이 원격 GUI 접속
xrdp를 설치해줍니다.
```
$ sudo apt install xrdp
```
이후 원격접속을 설정해줍니다.
```
$ sudo raspi-config
```
Interface Options => VNC => enable 하기
접속이 안될경우
아래 코드로 원격접속화면을 생성해줍니다.
```
$ vncserver-virtual
$ vncserver-virtual –geometry 1280x1024
```
https://www.realvnc.com/en/connect/download/viewer/
접속하여서 VNC Viewer를 설치합니다.

### 카메라 설정하기
```
$ sudo raspi-config
```
Interface Options => Legacy Camera => enable 하기 => reboot
