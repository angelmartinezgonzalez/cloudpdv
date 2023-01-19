import os
import sys
import site

# Add the site-packages where is the site-packages caould be with or witout virtualenv to work with
site.addsitedir('C:/Python37/lib/site-packages/')

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/dev/sitiosweb/cloudpdv/src/cloudpdv')
sys.path.append('C:/dev/sitiosweb//cloudpdv/src/cloudpdv/cloudpdv')


os.environ['DJANGO_SETTINGS_MODULE'] = 'cloudpdv.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cloudpdv.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()