# Pull base image
FROM python:3.8.3-alpine

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stder
ENV PYTHONUNBUFFERED 1

# Install Pillow dependencies (fuck_you!)
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements/requirements_dev.txt requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh .

# Copy project
COPY . .

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
