# Docker for my Flask app  :
from alpine:latest
RUN apk add --no-cache python3-dev \
      && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
#expose the port
EXPOSE 5000
#create the executable run always
ENTRYPOINT ["python3"]
CMD ["app.py"]