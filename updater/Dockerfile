FROM consul:latest
WORKDIR /updater
RUN apk add --no-cache ca-certificates python3 py-pip
RUN pip install requests
COPY . /updater
COPY entrypoint.sh /
#ENTRYPOINT /entrypoint.sh
