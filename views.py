import json
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from cartoview.app_manager.models import AppInstance, App
from cartoview.app_manager.views import StandardAppViews


class CMS(StandardAppViews):
    def __init__(self, app_name):
        super(StandardAppViews, self).__init__(app_name)

    def save(self, request, instance_id=None):
        user = request.user
        res_json = dict(success=False)
        data = json.loads(request.body)
        config = data.get('config', None)
        map_id = data.get('map', None)
        title = data.get('title', "")
        access = data.get('access', None)
        keywords = data.get('keywords', [])
        config.update(access=access, keywords=keywords)
        config = json.dumps(data.get('config', None))
        abstract = data.get('abstract', "")
        if instance_id is None:
            instance_obj = AppInstance()
            instance_obj.app = App.objects.get(name=self.app_name)
            instance_obj.owner = user
        else:
            instance_obj = AppInstance.objects.get(pk=instance_id)
            user = instance_obj.owner

        instance_obj.title = title
        instance_obj.config = config
        instance_obj.abstract = abstract
        instance_obj.map_id = map_id
        instance_obj.save()
        owner_permissions = [
            'view_resourcebase',
            'download_resourcebase',
            'change_resourcebase_metadata',
            'change_resourcebase',
            'delete_resourcebase',
            'change_resourcebase_permissions',
            'publish_resourcebase',
        ]
        permessions = {
            'users': {
                '{}'.format(request.user.username): owner_permissions,
            }
        }
        self.get_users_permissions(access, permessions, user.username)
        instance_obj.set_permissions(permessions)
        if hasattr(instance_obj, 'keywords') and keywords:
            new_keywords = [
                k for k in keywords if k not in instance_obj.keyword_list()
            ]
            instance_obj.keywords.add(*new_keywords)

        res_json.update(dict(success=True, id=instance_obj.id))
        return redirect('/apps/cartoview_cms/')


APP_NAME = os.path.basename(os.path.dirname(__file__))
cms = CMS(APP_NAME)
