# Docker for my Flask app  :
FROM python:3.6.1-alpine
RUN apk --update add bash nano
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
