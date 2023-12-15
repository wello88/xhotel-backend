"""
WSGI config for xhotel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xhotel.settings')





application = get_wsgi_application()

# server {
#     listen 80;
#     server_name your_domain.com;

#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /static/ {
#         root /path/to/your/django/project;
#     }

#     location / {
#         include proxy_params;
#         proxy_pass http://127.0.0.1:8000;  # Assuming Gunicorn is running on localhost:8000
#     }
# }
