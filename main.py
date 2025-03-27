from fastapi import FastAPI
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image  # Add this import
import numpy as np  

app = FastAPI()

hello = "Om"

@app.get("/")
def home():
    return {"key": hello}

model = load_model("cat_dog_classifier.keras")

@app.get("/predict")
def predict(img_path: str):  # Fixed function name and parameter
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    prediction = model.predict(img_array)
    confidence = prediction[0][0]
    
    if confidence > 0.5:
        result = "Dog"
    else:
        result = "Cat"
        
    return {"prediction": result, "confidence": float(confidence)}

img = input("Enter the image path: ")
print(predict(img))