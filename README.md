# smartmirror
since 2022.11

## front - PyQt5
- 버튼 누를 경우 url 방문 기능
- 버튼 누를 경우 내장 exe 파일 실행 
- 현재 경로의 exe 파일 실행 기능
- exe파일 폴더에서 exe파일들 경로 가져와서 실행기능
- image파일 폴더에서 png파일들 경로 가져와서 이미지 띄우는 기능

## back - opencv, open pose skeleton
- 5가지 포즈를 감지하여 front로 적절한 변수를 전달하여 해당 포즈에 해당하는 프로그램을 실행시킨다. (사진은 좌우 반전)
  - 상단 오른쪽으로 팔 뻗기
  
  ![스크린샷 2023-02-02 오후 7 46 34](https://user-images.githubusercontent.com/94885018/216304241-e5fd7366-5f54-4acf-a42e-01cb96d9a06c.png)
  - 상단 왼쪽으로 팔 뻗기
  
  ![스크린샷 2023-02-02 오후 7 37 27](https://user-images.githubusercontent.com/94885018/216303083-939f31e1-674d-4717-9772-7fc3a47579b1.png)
  - 하단 오른쪽으로 팔 뻗기

  ![스크린샷 2023-02-02 오후 7 37 59](https://user-images.githubusercontent.com/94885018/216303628-4cb02ea1-245f-44c2-afe6-82fb8f0ab569.png)  
  - 하단 왼쪽으로 팔 뻗기
 
  ![스크린샷 2023-02-02 오후 7 38 20](https://user-images.githubusercontent.com/94885018/216303468-376839d7-bc8e-4c8c-97b2-e001ebce3bfb.png)
  - 오른쪽 손목을 흉부로 접기
  
  ![스크린샷 2023-02-02 오후 7 38 31](https://user-images.githubusercontent.com/94885018/216302764-bb92f852-55e5-4ca7-9955-86223fd9b870.png)
 

  
## UI 
![스크린샷 2023-02-02 오후 7 32 49](https://user-images.githubusercontent.com/94885018/216302588-e8e3bad0-e328-47d9-aaef-1697dbcdd33e.png)
페이지를 넘길 시 다른 실행 아이콘을 가져옴
![스크린샷 2023-02-02 오후 7 38 49](https://user-images.githubusercontent.com/94885018/216302601-26f89982-eabf-4536-8d32-33f8f7bc747f.png)

