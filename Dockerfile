FROM adoptopenjdk:11-jre-hotspot

EXPOSE 8080

COPY ./target/WebApp.war /usr/app/
WORKDIR /usr/app

ENTRYPOINT ["java", "-jar", "WebApp.war"]
