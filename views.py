import json
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from cartoview.app_manager.models import AppInstance
from cartoview.app_manager.views import StandardAppViews


class CMS(StandardAppViews):
    def __init__(self, app_name):
        super(StandardAppViews, self).__init__(app_name)

    @method_decorator(login_required)
    def new(self, request, template=None, context={}, *args, **kwargs):
        return redirect('/apps/cartoview_cms/admin/pages/2/add_subpage/')

    @staticmethod
    def view(request, instanceid):
        temp_app_instance = AppInstance.objects.get(id=instanceid)
        config = json.loads(temp_app_instance.config);
        if config['url'] is not None:
            return redirect(config['url'])
        else:
            return redirect("/")

    def edit(self, request, instanceid):
        temp_app_instance = AppInstance.objects.get(id=instanceid)
        config = json.loads(temp_app_instance.config);
        if config['id'] is not None:
            return redirect("/apps/cartoview_cms/admin/pages/%s/edit/" % config['id'])
        else:
            return redirect("/")


APP_NAME = os.path.basename(os.path.dirname(__file__))
cms = CMS(APP_NAME)
