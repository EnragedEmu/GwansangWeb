from ultralytics import YOLO
import yaml

#YOLO 실행 함수
def YOLO_predict(path):
    #모델은 best.pt,실행하는 동작은 data.yaml이 판단한다. img는 jpg파일로(png도 받을 수 있게 수정 요망) 
    model_path = f'{path}/best.pt'
    image_path = f'{path}/img.jpg'
    yaml_path = f'{path}/data.yaml'

    model = YOLO(model_path)

    with open(yaml_path, 'r') as f:
        face_yaml = yaml.safe_load(f)

    result = model.predict(source=image_path, save=True,save_crop=True)

    return result

path='실제 path 넣으시오'
YOLO_predict(path)
