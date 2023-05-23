FROM alpine:3.14

RUN apk --no-cache add openjdk8-jre

EXPOSE 8080

COPY ./target/*.jar /usr/app/
WORKDIR /usr/app

ENTRYPOINT ["java", "-jar", "usr/app/*.jar"]
