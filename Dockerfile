FROM debian:buster-slim

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install -y --no-install-recommends uwsgi uwsgi-plugin-python3 python3 python3-pip

COPY . /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 9876
RUN chmod +x custom-start.sh
CMD ["/usr/src/app/custom-start.sh"]
