import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow import keras
import cv2
from PIL import Image

model = keras.models.load_model("D:\E drive copy\REC\Projects\Final Year Project\Phase 2\Python code\model.h5")
path = "D:\\E drive copy\\REC\\Projects\\Final Year Project\Phase 2\\Python code\\20220330_161247.jpg"

vid = cv2.VideoCapture(0)

def predict(input_img):
    
    img = image.load_img(input_img, color_mode="rgb", target_size=(150, 150), interpolation="nearest")
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img/255
    
    images = np.vstack([img])
    classes = model.predict(images, batch_size=1)
    #predict_result = []
    predict_result = ""
    
    max = np.amax(classes[0])
    if np.where(classes[0] == max)[0] == 0:
      predict_result = 'Normal Lemon'
    elif np.where(classes[0] == max)[0] == 1:
      predict_result = 'Defective Lemon'
    
    print(predict_result)
    
    plt.figure(figsize=(5, 5))
    plt.imshow(image.load_img(path, color_mode="rgb", target_size=(1080, 1080), interpolation="nearest"))
    title = f"predict: {predict_result} ({round(float(max)*100, 2)}%)"
    plt.title(title, color='black')
    plt.axis('off')
    plt.show()
    
    return predict_result
    
def start():
    count=0
    while(vid.isOpened()):
        ret, frame = vid.read();
        frame = frame[100:500, 100:500]
        count = count+1
          
        if count == 10:
            cv2.imwrite(path, frame);
            result = predict(path);
            cv2.imshow(result, frame)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            
            break
    
    return result
            
if __name__=="__main__":
    start()
