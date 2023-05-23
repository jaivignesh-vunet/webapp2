FROM alpine:3.14

RUN apk --no-cache add openjdk8-jre

EXPOSE 8080

COPY ./target/WebApp.war /usr/app/
WORKDIR /usr/app

ENTRYPOINT ["java", "-jar", "usr/app/*.war"]
