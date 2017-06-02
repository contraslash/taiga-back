FROM python:3.6-alpine
RUN apk update
RUN apk add --no-cache binutils
RUN apk add --no-cache gcc
RUN apk add --no-cache musl-dev
RUN apk add --no-cache autoconf
RUN apk add --no-cache flex
RUN apk add --no-cache bison
RUN apk add --no-cache jpeg-dev
RUN apk add --no-cache freetype-dev
RUN apk add --no-cache zlib-dev
RUN apk add --no-cache zeromq-dev
RUN apk add --no-cache gdbm-dev
RUN apk add --no-cache ncurses-dev
RUN apk add --no-cache automake
RUN apk add --no-cache libtool
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache curl
RUN apk add --no-cache git
RUN apk add --no-cache tmux
RUN apk add --no-cache gettext
RUN apk add --no-cache postgresql
RUN apk add --no-cache postgresql-contrib
RUN apk add --no-cache postgresql-client

RUN mkdir /code
WORKDIR /code
ADD settings/local.py.example /code/settings/local.py
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 8000

CMD ["python3" "manage.py" "runserver"]
