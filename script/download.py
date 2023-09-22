import gdown
import os

os.mkdir("./external_model_params")
os.mkdir("./model_trained")
os.mkdir("./dataset_info_ctrlhair")

url = "https://drive.google.com/drive/folders/1X0y82o7-JB6nGYIWdbbJa4MTFbtV9bei"
gdown.download_folder(url, quiet=True, use_cookies=False)

url = "https://drive.google.com/drive/folders/1opQhmc7ckS3J8qdLii_EMqmxYCcBLznO"
gdown.download_folder(url, quiet=True, use_cookies=False)

url = "https://drive.google.com/file/d/17iRY9zkQk7_qq2MdAyJBE54nlEHzA04R/view?usp=sharing"
output_path = './dataset_info_ctrlhair/hsv_stat_dict.pkl'
gdown.download(url, output_path, quiet=False,fuzzy=True)
