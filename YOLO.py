from ultralytics import YOLO
import yaml

#YOLO 실행 함수
def YOLO_predict(path,img):
    
    #모델은 best.pt,실행하는 동작은 data.yaml이 판단한다. img는 jpg파일로(png도 받을 수 있게 수정 요망) 
    model_path = f'{path}/best.pt'
    yaml_path = f'{path}/data.yaml'

    model = YOLO(model_path)

    with open(yaml_path, 'r') as f:
        face_yaml = yaml.safe_load(f)

    #img를 모델에 돌린다.
    result = model.predict(source=img)

    #result에서 boxes의 x,y 좌표들을 구해본다.
    for r in result:
        coordinate = r.boxes.xyxy

    #좌표값 받아오기
    x1, y1, x2, y2 = map(int, coordinate[0])

    cropped_image = img[y1:y2, x1:x2]

    return cropped_image
