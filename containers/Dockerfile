FROM ibmcom/db2express-c:10.5.0.5-3.10.0

ADD init-db.sh /db2/init-db.sh

WORKDIR db2

RUN bash ./init-db.sh
