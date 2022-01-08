FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./webScrapping.py" ]

# sudo docker build -t webscrapping .
# sudo docker run -it --rm --name webscrapping-app webscrapping
