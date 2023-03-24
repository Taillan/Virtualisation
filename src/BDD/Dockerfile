FROM mysql:latest

ENV PACKAGES openssh-server openssh-client
ENV MYSQL_ROOT_PASSWORD="rootroot"
ENV MYSQL_DATABASE="QuizzDB"

COPY ./init_db.sql /docker-entrypoint-initdb.d/init_db.sql

EXPOSE 3306