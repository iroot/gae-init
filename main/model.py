# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
from uuid import uuid4
import os
import modelx


# The timestamp of the currently deployed version
TIMESTAMP = long(os.environ.get('CURRENT_VERSION_ID').split('.')[1]) >> 28


class Base(ndb.Model, modelx.BaseX):
  created = ndb.DateTimeProperty(auto_now_add=True)
  modified = ndb.DateTimeProperty(auto_now=True)
  version = ndb.IntegerProperty(default=TIMESTAMP)
  _PROPERTIES = set([
      'key',
      'id',
      'version',
      'created',
      'modified',
    ])


class Config(Base, modelx.ConfigX):
  analytics_id = ndb.StringProperty(default='')
  announcement_html = ndb.StringProperty(default='')
  announcement_type = ndb.StringProperty(default='info', choices=[
      'info', 'warning', 'success', 'danger',
    ])
  brand_name = ndb.StringProperty(default='gae-init')
  bucket_name = ndb.StringProperty(default='')
  facebook_app_id = ndb.StringProperty(default='')
  facebook_app_secret = ndb.StringProperty(default='')
  feedback_email = ndb.StringProperty(default='')
  flask_secret_key = ndb.StringProperty(default=str(uuid4()).replace('-', ''))
  locale = ndb.StringProperty(default='en')
  twitter_consumer_key = ndb.StringProperty(default='')
  twitter_consumer_secret = ndb.StringProperty(default='')

  _PROPERTIES = Base._PROPERTIES.union(set([
      'analytics_id',
      'announcement_html',
      'announcement_type',
      'brand_name',
      'bucket_name',
      'facebook_app_id',
      'facebook_app_secret',
      'feedback_email',
      'flask_secret_key',
      'locale',
      'twitter_consumer_key',
      'twitter_consumer_secret',
    ]))


class User(Base, modelx.UserX):
  name = ndb.StringProperty(indexed=True, required=True)
  username = ndb.StringProperty(indexed=True, required=True)
  email = ndb.StringProperty(indexed=True, default='')
  locale = ndb.StringProperty(default='')

  active = ndb.BooleanProperty(default=True)
  admin = ndb.BooleanProperty(default=False)

  federated_id = ndb.StringProperty(indexed=True, default='')
  facebook_id = ndb.StringProperty(indexed=True, default='')
  twitter_id = ndb.StringProperty(indexed=True, default='')

  _PROPERTIES = Base._PROPERTIES.union(set([
      'name',
      'username',
      'avatar_url',
      'locale',
    ]))


class Resource(Base, modelx.ResourceX):
  user_key = ndb.KeyProperty(kind=User, required=True)
  blob_key = ndb.BlobKeyProperty(required=True)
  name = ndb.StringProperty(indexed=True, required=True)
  bucket_name = ndb.StringProperty()
  image_url = ndb.StringProperty(default='')
  content_type = ndb.StringProperty(indexed=True, default='')
  size = ndb.IntegerProperty(indexed=True, default=0)

  _PROPERTIES = Base._PROPERTIES.union(set([
      'name',
      'bucket_name',
      'image_url',
      'content_type',
      'size',
      'size_human',
      'download_url',
      'view_url',
      'serve_url',
    ]))
