ARG PYTHON_BASE=3.13-slim
# build stage
FROM python:$PYTHON_BASE AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# install PDM
RUN pip install -U pdm
ENV PDM_CHECK_UPDATE=false

COPY . /app/
WORKDIR /app
RUN pdm install --check --prod --no-editable

# run stage
FROM python:$PYTHON_BASE

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# retrieve packages from build stage
COPY --from=builder /app/ /app
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app
ENTRYPOINT ["/bin/sh", "-c" , "./manage.py runserver 0.0.0.0:8000"]