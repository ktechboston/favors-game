FROM amacneil/dbmate:v1.10.0

COPY ./db/migrations /db/migrations

ENTRYPOINT ["dbmate"]