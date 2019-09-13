FROM consul:latest
WORKDIR /updater
RUN apk add --no-cache ca-certificates python3 py-pip bash
RUN pip install requests
COPY . /updater
