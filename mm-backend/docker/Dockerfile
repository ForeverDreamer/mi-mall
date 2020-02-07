FROM doerlee/mod_wsgi

COPY . /app

# COPY my_conf/httpd.conf /usr/local/apache/conf

RUN python src/manage.py collectstatic