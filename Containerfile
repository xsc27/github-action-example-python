FROM docker.io/python:3.11-alpine as build
# COPY --chmod=444 requirements.txt /opt/app/
# COPY --chmod=555 *.py /opt/app/
# COPY ** /opt/src/
# RUN pip install --no-cache-dir -r /tmp/src/requirements.txt
ARG PSEUDO_VERSION=1
# RUN apk add git
# RUN SETUPTOOLS_SCM_PRETEND_VERSION=${PSEUDO_VERSION} pip install --progress-bar off --root-user-action ignore -c /opt/src/requirements.txt /opt/src
RUN --mount=type=bind,source=.,target=/opt/src/ \
  ls -al /opt/src
# RUN --mount=source=.,target=/opt/src/,type=bind pip install /opt/src
# RUN --mount=source=.git,target=/opt/src/.git,type=bind pip install /opt/src
USER guest
ENTRYPOINT ["python3", "/opt/app/cli.py"]
