import os, mimetypes

from django.shortcuts import render, HttpResponse
from django.template import RequestContext, loader

from webpanel import settings
from files.models import Docroot

def index(request, path=''):
    # TODO get from model
    user = 'example'
    # TODO get from model
    docroot = 'testfiles/www/example.com/htdocs'

    # FIXME need auth check

    link_path = '/files'

    if path != '':
        # validate path info
        path = path.strip('/')
        path = path.replace('\0', '')

        link_path += '/%s' % path
        abs_path = os.path.join(settings.BASE_DIR, docroot, path)
        if os.path.isfile(abs_path):
            with open(abs_path) as f:
                return HttpResponse(f.read(),
                                    mimetype='application/octet-stream')
        elif os.path.isdir(abs_path):
            pass
        else:
            print 'Unknown filetype for entry %s, not listing' % abs_path

    abs_docroot = os.path.join(settings.BASE_DIR, docroot, path)

    files = []
    dirs = []
    for entry in os.listdir(abs_docroot):
        abs_entry = os.path.join(abs_docroot, entry)
        if os.path.isfile(abs_entry):
            files.append(entry)
        elif os.path.isdir(abs_entry):
            dirs.append(entry)
        else:
            print 'Unknown filetype for entry %s, not listing' % entry

    template = loader.get_template('files/index.html')
    context = RequestContext(request, {
        'user': user,
        'path': path,
        'link_path': link_path,
        'files': files,
        'dirs': dirs,
    })
    return HttpResponse(template.render(context))
