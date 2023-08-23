from ultralytics import YOLO
import yaml

def YOLO_predict(path):
    model_path = f'{path}/best.pt'
    image_path = f'{path}/img.jpg'
    yaml_path = f'{path}/data.yaml'

    model = YOLO(model_path)

    with open(yaml_path, 'r') as f:
        face_yaml = yaml.safe_load(f)

    result = model.predict(source=image_path, save=True,save_crop=True)

    return result

path='D:/pycharm project/my project/faceMBTI/practice'
YOLO_predict(path)