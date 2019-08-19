FROM golang:latest

COPY ./app /go/src/app
WORKDIR /go/src/app

RUN go install

CMD ["app"]
