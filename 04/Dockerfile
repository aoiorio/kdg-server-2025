FROM golang:1.24.3 AS builder

WORKDIR /app

COPY /hello.go .

RUN go build -o hello hello.go


FROM alpine:3.22.0

WORKDIR /root/

COPY --from=builder /app ./

CMD ["./hello"]
