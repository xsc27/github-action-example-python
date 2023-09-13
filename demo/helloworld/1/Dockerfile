ARG PY_VER=3
FROM docker.io/python:${PY_VER}-alpine
COPY --chmod=555 main.py /opt/app/
ENTRYPOINT ["/opt/app/main.py"]
LABEL org.opencontainers.image.authors="hire@carlosmeza.com"
