# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from sellt.models import ThreeDModel
from sellt.models import App_3DModel_List
# Create your views here.
from django.core import serializers

import urllib
import urllib2
import json
import types


def ThreeDModelUpdate(request):
    form_data = {'mid': '219', 'page': '1', 'perCounts': '100'}
    form_data_urlencode = urllib.urlencode(form_data)
    requrl = "http://www.51hi3d.com/mobile/mobilePhone/showModelInfo"
    req = urllib2.Request(url=requrl, data=form_data_urlencode)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    # print  json.loads(res_data)
    j = json.loads(res)
    print len(j['data'])
    print j['data'][0]
    # print json_to_python('data’)

    print ThreeDModel.objects.all()

    return HttpResponse(res)


def App3DModelList(request):
    tmpurl = 'http://inter.jingzhi3d.com/CameraParameters/mli/'
    # m_Dic_List = App_3DModel_List.objects.values('tname','threeDModel__mid','threeDModel__mpath')
    m_Dic_List = App_3DModel_List.objects.values('tname', 'threeDModel__mid', 'threeDModel__mpath', 'threeDModel__id',
                                                 'threeDModel__bgImageName1', 'threeDModel__bgImageName2')
    lst = list()
    for m_Dic in m_Dic_List:
        print m_Dic
        dic = {'id': m_Dic['threeDModel__id'], 'mpath': m_Dic['threeDModel__mpath'], 'mid': m_Dic['threeDModel__mid'],
               'img1': tmpurl + m_Dic['threeDModel__bgImageName1'], 'img2': tmpurl + m_Dic['threeDModel__bgImageName2']}
        lst.append(dic)
    rDic = {'data': lst}
    j = json.dumps(rDic)
    return HttpResponse(j)


def ReloadData(request):
    form_data = {'mid': '219', 'page': '1', 'perCounts': '100'}
    form_data_urlencode = urllib.urlencode(form_data)
    requrl = "http://www.51hi3d.com/mobile/mobilePhone/showModelInfo"
    req = urllib2.Request(url=requrl, data=form_data_urlencode)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    j = json.loads(res)

    mInfoList = j['data']
    for mInfo in mInfoList:
        tmpM = ThreeDModel.objects.get_or_create(id=int(mInfo['id']))[0]

        if tmpM.id == 211:

            tmpM.bgImageName1 = 'm1b.jpg'
            tmpM.bgImageName2 = 'm1n.png'
            print '---------------' + "fqfqfwf"

        elif tmpM.id == 213:
            tmpM.bgImageName1 = 'm2b.jpg'
            tmpM.bgImageName2 = 'm2n.png'

        elif tmpM.id == 214:
            tmpM.bgImageName1 = 'm4b.jpg'
            tmpM.bgImageName2 = 'm4n.png'

        elif tmpM.id == 215:
            tmpM.bgImageName1 = 'm5b.jpg'
            tmpM.bgImageName2 = 'm5n.png'


        elif tmpM.id == 216:
            tmpM.bgImageName1 = 'm3b.jpg'
            tmpM.bgImageName2 = 'm3n.png'
        elif tmpM.id == 223:
            tmpM.bgImageName1 = 'm6b.jpg'
            tmpM.bgImageName2 = 'm6n.png'

        tmpM.mid = mInfo['mid'] if mInfo['mid'] else ' '
        tmpM.account = mInfo['account'] if mInfo['account'] else ' '
        tmpM.mname = mInfo['mname'] if mInfo['mname'] else ' '
        tmpM.thumbnail = mInfo['thumbnail'] if mInfo['thumbnail']  else ' '
        tmpM.tid = mInfo['tid'] if mInfo['tid'] else ' '
        tmpM.mpath = mInfo['mpath'] if mInfo['mpath'] else ' '
        tmpM.authoity = mInfo['authoity'] if mInfo['authoity'] else ' '
        tmpM.md5 = mInfo['md5'] if mInfo['md5'] else ' '
        tmpM.rmid = mInfo['rmid'] if mInfo['rmid'] else ' '
        tmpM.mdesc = mInfo['mdesc'] if mInfo['mdesc'] else ' '
        tmpM.likecoun = mInfo['likecoun'] if mInfo['likecoun'] else ' '
        tmpM.downcoun = mInfo['downcoun'] if mInfo['downcoun'] else ' '
        tmpM.updtime = mInfo['updtime'] if mInfo['updtime'] else ' '
        tmpM.addtime = mInfo['addtime'] if mInfo['addtime'] else ' '
        tmpM.ext_1 = mInfo['ext_1'] if mInfo['ext_1'] else ' '
        tmpM.colimage = mInfo['colimage'] if mInfo['colimage'] else ' '
        tmpM.qrimage1 = mInfo['qrimage1'] if mInfo['qrimage1']  else ' '
        '''
		tmpM.audioname1 = mInfo['audioname1']
		tmpM.audioname2 = mInfo['audioname2']
		tmpM.audioname3 = mInfo['audioname3']
		tmpM.coldesc = mInfo['coldesc']
		tmpM.qrimage2 = mInfo['qrimage2']
		tmpM.htmlpage = mInfo['htmlpage']
		tmpM.age_c = mInfo['age_c']
		tmpM.age_e = mInfo['age_e']
		tmpM.intro_c = mInfo['intro_c']
		tmpM.intro_e = mInfo['intro_e']
		tmpM.name_c = mInfo['name_c']
		tmpM.name_e = mInfo['name_e']
		#tmpM.high_c = mInfo['hight_c']
		#tmpM.high_e = mInfo['hight_e']
		tmpM.wide_c = mInfo['wide_c']
		tmpM.wide_e = mInfo['wide_e']
		tmpM.material_c = mInfo['material_c']
		tmpM.material_e = mInfo['material_e']
		'''
        tmpM.save()

    # for mInfo in mInfoList:
    # tmpM = ThreeDModel.objects.get_or_create(id = mInfo['id'])
    # tmpM.mname = mInfo['mname']
    return HttpResponse('aaa')
