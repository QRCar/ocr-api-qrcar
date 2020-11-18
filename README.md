# User Api for QRCar
> cbarange | 17th November 2020
---

## Get Started

```bash
python3 --version # 3.8.5
sudo docker build -t openalpr https://github.com/openalpr/openalpr.git
pip3 install -r requirements.txt
chmod +x ./openalpr_docker.py
mkdir -p /var/www/uploads
nohup ./openalpr_docker.py &
# [POST] localhost:5000/ocr [BODY:{picture_car:car_plate_0211.png}] -> STRING_LICENSE_PLATE_NUMBER
``` 

## Develop

```bash
pip3 install pipenv
pipenv --three
pipenv install flask
pipenv install marshmallow
pipenv run pip3 freeze > requirements.txt
./bootstrap.sh
```

