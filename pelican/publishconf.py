#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os

AUTHOR = '40323107'
SITENAME = '2015FALL CADP 課程'
SITEURL = 'http://40323107.github.io/2015fallcadpa/'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('2015 CADP 課程網頁', 'http://wordpress-2015course.rhcloud.com/'),
         ('2015 FALL CADPA 作業主頁','http://2015fallhw.github.io/2015fallcadpa/'),('Github','https://github.com/2015fallhw/2015fallcadpa/wiki'),('Vimeo','https://vimeo.com/user24079973/videos'),('40323107 作業主頁','http://2015fallhw.github.io/2015fallcadpa/user/40323107/'),('My Github','https://github.com/40323107/2015fallcadpa/tree/gh-pages'),('My Vimeo','https://vimeo.com/home/myvideos'),('My Copy','https://www.copy.com/browse/a:dd7adaa;z:copy;b:myfiles'),('My WordPress','http://wordpress-40323107.rhcloud.com/'),('G2 作業主頁','http://2015fallhw.github.io/2015fallcadpa/category/g2.html'),('G2 Github','https://github.com/40323107/2015cadpa_g2/tree/gh-pages'),('Python', 'http://python.org/'))

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/ametaireau'),
          ('Github', 'https://github.com/'),('OpenShift','https://openshift.redhat.com/app/login?then=%2Fapp%2Fconsole%2Fapplications'),('Bitbucket','https://bitbucket.org/'),('Vimeo','https://vimeo.com/home/myvideos'),('Copy','https://www.copy.com/page/home;section:landing'))
          
DEFAULT_PAGINATION = 10

SITEURL = 'http://40323107.github.io/2015fallcadpa/'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
DISQUS_SITENAME = "2015fallcadp"
#GOOGLE_ANALYTICS = ""

# 必須絕對目錄或相對於設定檔案所在目錄
PLUGIN_PATHS = ['./../plugin']
PLUGINS = ['liquid_tags.notebook']
# 目錄設定相對於 reveal 下的 content 目錄
NOTEBOOK_DIR = 'notebook'
'''
if not os.path.exists('_nb_header.html'):     
    import warnings 
    warnings.warn("_nb_header.html not found.") 
else: 
    EXTRA_HEADER = open('_nb_header.html', encoding="utf-8").read()
'''

