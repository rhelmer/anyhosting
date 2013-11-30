import string

from celery import Celery
import nginx
from shipper import Shipper

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def generate_config(sitename):
    c = nginx.Conf()
    u = nginx.Upstream('php',
        nginx.Key('server', 'unix://tmp/php-fcgi.socket')
    )
    c.add(u)
    s = nginx.Server()
    s.add(
        nginx.Key('listen', '80'),
        nginx.Key('root', '/var/www/%s/htdocs' % sitename),
        nginx.Key('index', 'index.php'),
        nginx.Location('= /robots.txt',
             nginx.Key('allow', 'all'),
             nginx.Key('log_not_found', 'off'),
             nginx.Key('access_log', 'off')
        ),
        nginx.Location('~ \.php$',
             nginx.Key('include', 'fastcgi.conf'),
             nginx.Key('fastcgi_intercept_errors', 'on'),
             nginx.Key('fastcgi_pass', 'php')
        )
    )
    c.add(s)
    return nginx.dumpf(c, '%s.conf' % string.replace(sitename, '.', '_'))

@app.task
def build_container(tag, path):
    s = Shipper()
    s.build(tag=tag, path=path)

@app.task
def start_container(image, command, ports=None):
    s = Shipper()
    s.run(image, command, ports=ports, once=True)

@app.task
def stop_container(image=None):
    s = Shipper()
    s.stop(*s.containers(image=image, running=True))
