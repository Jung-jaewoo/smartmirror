import cv2
import sys
from pathlib import Path
import time
from time import sleep
from os import path
import os
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import union
pose_type = "SmartMirror"

# MPII에서 각 파트 번호, 선으로 연결될 POSE_PAIRS
BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                "Background": 15 }

POSE_PAIRS = [ ["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"] ]

# 각 파일 path
BASE_DIR = Path(__file__).resolve().parent
protoFile = str(BASE_DIR)+"/file/pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = str(BASE_DIR)+"/file/pose_iter_160000.caffemodel"

# 위의 path에 있는 network 모델 불러오기
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

# openCV의 좌표계는 좌측위가 (0,0)이다...
# 아래/오른쪽으로 갈수록 증가한다





##################################################
# 자세 체크 함수들

def check_right_up(points):
    while(True):
        if points[1] and points[2] and points[3] and points[4]:
            neck_x,neck_y=points[1] #목
            rs_x,rs_y=points[2] #오른쪽 어깨
            re_x,re_y=points[3] #오른쪽 팔꿈치
            rw_x,rw_y=points[4] #오른쪽 손목
            
            #어깨보다 팔꿈치가 위로 & 어깨 오른쪽에 팔꿈치
            if rs_y > re_y and re_x < rs_x:
            #목보다 오른쪽에 손목 & 목보다 위에 손목
                if rw_x < neck_x and neck_y > rw_y:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
def check_left_up(points):
    while(True):
        if points[1] and points[5] and points[6] and points[7]:
            neck_x,neck_y=points[1] #목
            ls_x,ls_y=points[5] #왼쪽 어깨
            le_x,le_y=points[6] #왼쪽 팔꿈치
            lw_x,lw_y=points[7] #왼쪽 손목
            
            #어깨보다 팔꿈치가 위로 & 어깨 왼쪽에 팔꿈치
            if ls_y > le_y and le_x > ls_x:
            #목보다 왼쪽에 손목 & 머리보다 위에 손목
                if lw_x > neck_x and neck_y > lw_y:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

        
def check_right_down(points):
    while(True):
        if points[2] and points[3] and points[4] and points[14]:
            rs_x,rs_y=points[2] #오른쪽 어깨
            re_x,re_y=points[3] #오른쪽 팔꿈치
            rw_x,rw_y=points[4] #오른쪽 손목
            c_x,c_y = points[14] #흉부
            
            #흉부보다 손목이 위로 올라감 & 흉부 오른쪽에 손목
            if c_y > rw_y and rw_x < c_x:
                #어깨 아래 팔꿈치 & 어깨 오른쪽 팔꿈치
                if re_y > rs_y and re_x < rs_x:
                    #팔꿈치 아래 손목 & 팔꿈치 오른쪽 손목
                    if rw_y > re_y and rw_x < re_x:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
def check_left_down(points):
    while(True):
        if points[5] and points[6] and points[7] and points[14]:
            ls_x,ls_y=points[5] #왼쪽 어깨
            le_x,le_y=points[6] #왼쪽 팔꿈치
            lw_x,lw_y=points[7] #왼쪽 손목
            c_x,c_y = points[14] #흉부
            
            #흉부보다 손목이 위로 올라감 & 흉부 왼쪽에 손목
            if c_y > lw_y and lw_x > c_x:
                #어깨 아래 팔꿈치 & 어깨 왼쪽 팔꿈치
                if le_y > ls_y and le_x > ls_x:
                    #팔꿈치 아래 손목 & 팔꿈치 왼쪽 손목
                    if lw_y > le_y and lw_x > le_x:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False



#################################################
# 결과를 반환하는 함수

def show_result(pose_type): #END/Again
    if pose_type=="l_up":
        print("왼쪽 위")
        return "A"
    elif pose_type == "r_up":
        print("오른쪽 위")
        return "B"
    elif pose_type == "l_down":
        print("왼쪽 아래")
        return "C"
    elif pose_type == "r_down":
        print("오른쪽 아래")
        return "D"
    else:
        print("자세를 취해주세요.") 
        return "Again"


def check_up(points):
    lu = check_left_up(points)
    ru = check_right_up(points)
    ld = check_left_down(points)
    rd = check_right_down(points)
    
    
    r = 0
    if lu:
        r = show_result("l_up")
        #time.sleep(2)
    if ru:
        r = show_result("r_up")
        #time.sleep(2)
    if ld:
        r = show_result("l_down")
        #time.sleep(2)
    if rd:
        r = show_result("r_down")
        #time.sleep(2)
    
    return r


    

def startCam():
    ###카메라랑 연결...?
    capture = cv2.VideoCapture(0) #카메라 정보 받아옴
    # capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #카메라 속성 설정
    # capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # width:너비, height: 높이

    inputWidth=320
    inputHeight=240
    inputScale=1.0/255

    path = str(BASE_DIR).replace("back","front") + "/exefiles/"
    file_list = os.listdir(path)
    file_list_exe = [file for file in file_list if file.endswith(".exe")]        

    #반복문을 통해 카메라에서 프레임을 지속적으로 받아옴
    while cv2.waitKey(1) <0:  #아무 키나 누르면 끝난다.
        #웹캠으로부터 영상 가져옴
        hasFrame, frame = capture.read()  
        
        #영상이 커서 느리면 사이즈를 줄이자
        #frame=cv2.resize(frame,dsize=(320,240),interpolation=cv2.INTER_AREA)
        
        #웹캠으로부터 영상을 가져올 수 없으면 웹캠 중지
        if not hasFrame:
            cv2.waitKey()
            break
        
        # 
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        
        inpBlob = cv2.dnn.blobFromImage(frame, inputScale, (inputWidth, inputHeight), (0, 0, 0), swapRB=False, crop=False)
        
        imgb=cv2.dnn.imagesFromBlob(inpBlob)
        #cv2.imshow("motion",(imgb[0]*255.0).astype(np.uint8))
        
        # network에 넣어주기
        net.setInput(inpBlob)

        # 결과 받아오기
        output = net.forward()


        # 키포인트 검출시 이미지에 그려줌
        points = []
        for i in range(0,15):
            # 해당 신체부위 신뢰도 얻음.
            probMap = output[0, i, :, :]
        
            # global 최대값 찾기
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

            # 원래 이미지에 맞게 점 위치 변경
            x = (frameWidth * point[0]) / output.shape[3]
            y = (frameHeight * point[1]) / output.shape[2]

            # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로    
            if prob > 0.1 :    
                cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 255), thickness=-1, lineType=cv2.FILLED) # circle(그릴곳, 원의 중심, 반지름, 색)
                cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, lineType=cv2.LINE_AA)
                points.append((int(x), int(y)))
            else :
                points.append(None)
        
        

        # 각 POSE_PAIRS별로 선 그어줌 (머리 - 목, 목 - 왼쪽어깨, ...)
        for pair in POSE_PAIRS:
            partA = pair[0]             # Head
            partA = BODY_PARTS[partA]   # 0
            partB = pair[1]             # Neck
            partB = BODY_PARTS[partB]   # 1
            
            #partA와 partB 사이에 선을 그어줌 (cv2.line)
            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (0, 255, 0), 2)
        
                
        cv2.imshow("Output-Keypoints",frame)
        
    
        ####################################################################    위는 기본적인 카메라 출력
        
        result = check_up(points)
        print(result)

        if result == 'A':
            os.system(file_list_exe[0])
            sleep(5)
        elif result == 'B':
            os.system(file_list_exe[1])
            sleep(5)
        elif result == 'C':
            os.system(file_list_exe[2])
            sleep(5)
        elif result == 'D':
            os.system(file_list_exe[3])
            sleep(5)

            
        ####### result 변수를 UI에 전달하면 어느정도 작동할 듯????

    capture.release()  #카메라 장치에서 받아온 메모리 해제
    cv2.destroyAllWindows() #모든 윈도우 창 닫음










