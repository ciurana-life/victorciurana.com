# Pull base image
FROM python:3.9-alpine

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stder
ENV PYTHONUNBUFFERED 1
# Poetry
ENV POETRY_HOME="/opt/poetry"
ENV VENV_PATH="/opt/pysetup/.venv"
# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
# Prevent no python found
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
# Prevent runtime error
COPY poetry.lock pyproject.toml ./

# Install Pillow dependencies (fuck_you!)
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev curl

# Install dependencies
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN poetry config virtualenvs.create false
# RUN poetry install --no-dev
RUN poetry install

# Copy entrypoint.sh
COPY ./entrypoint.sh .

# Copy project
COPY . .

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
