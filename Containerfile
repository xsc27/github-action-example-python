FROM docker.io/python:3.11-alpine as build
# COPY --chmod=444 requirements.txt /opt/app/
# COPY --chmod=555 *.py /opt/app/
COPY ** /opt/src/
# RUN pip install --no-cache-dir -r /tmp/src/requirements.txt
ARG PSEUDO_VERSION=1
# RUN apk add git
# RUN SETUPTOOLS_SCM_PRETEND_VERSION=${PSEUDO_VERSION} pip install --progress-bar off --root-user-action ignore -c /opt/src/requirements.txt /opt/src
# RUN --mount=type=bind,source=.,target=/opt/src,rw,z \
RUN set -eux && \
  pip config --global set global.progress_bar off && \
  pip config --global set global.root_user_action ignore && \
  SETUPTOOLS_SCM_PRETEND_VERSION=${PSEUDO_VERSION} \
    pip install --compile --target /opt/app --constraint /opt/src/requirements.txt /opt/src
# RUN --mount=source=.,target=/opt/src/,type=bind pip install /opt/src
# RUN --mount=source=.git,target=/opt/src/.git,type=bind pip install /opt/src


FROM docker.io/python:3.11-alpine
COPY --from=build /opt/app/ /opt/app/
USER guest
ENV PYTHONPATH=/opt/app/
ENTRYPOINT ["/opt/app/bin/httpcat"]
