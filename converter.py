import os
from tensorflow.keras.models import load_model

input_dir = "./models/DL_models"
output_dir = "./models/converted_DL_models"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".h5"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace(".h5", ".keras"))
        try:
            model = load_model(input_path, compile=False)
            model.save(output_path, save_format="keras_v3")
            print(f"✅ Converted: {filename}")
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")
