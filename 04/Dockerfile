FROM golang:1.24.3 AS builder

WORKDIR /app

COPY /hello.go .

RUN go build -o hello hello.go


FROM alpine:latest

WORKDIR /root/

COPY --from=builder /app ./

CMD ["./hello"]
