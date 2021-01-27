from django.templatetags.static import static
from django.contrib.staticfiles import finders
from django.conf import settings
from django.core import exceptions
from hospital.models import *
from okb2.models import *
from dbfread import DBF
import os
import time
import datetime
import uuid


class InsertHospital:
    def __init__(self, request):
        self.rez = list()
        self.OPER = None
        self.SLUCH = None
        self.__hospital_file_upload_1c(request)

    def __hospital_file_upload_1c(self, request):
        self.rez.clear()
        from hospital.models import Load_1c
        f_oper, f_sluch = list(Load_1c.objects.values_list(
            'oper', 'sluch').filter(user=request.user.id))[0]
        dir_oper = settings.MEDIA_ROOT + '/' + f_oper
        dir_sluch = settings.MEDIA_ROOT + '/' + f_sluch
        self.__insert_hospital(dir_oper, request, 1)
        self.__insert_hospital(dir_sluch, request, 2)
        self.rez.append(self.OPER)
        self.rez.append(self.SLUCH)

        if (self.OPER == True) and (self.SLUCH == True):
            self.__insert_to_models()

    def __insert_hospital(self, file, request, tip_file):
        if tip_file == 1:
            self.OPER = False
            temp_oper.objects.filter(user=request.user.id).all().delete()
            for rec in DBF(file, char_decode_errors="ignore", encoding="utf-8", lowernames=True):
                dict_rec_r = dict(rec)
                kodan = str(dict_rec_r['kodan']).strip(' ')
                kodan = ''.join(kodan)
                try:
                    temp_oper.objects.create(
                        kod_op=dict_rec_r['kod_op'],
                        dato=dict_rec_r['dato'],
                        goc_o=dict_rec_r['goc_o'],
                        py=dict_rec_r['py'],
                        kodx=dict_rec_r['kodx'],
                        kodxa=dict_rec_r['kodxa'],
                        kodxa1=dict_rec_r['kodxa1'],
                        obz=dict_rec_r['obz'],
                        kodan=kodan,
                        pr_osob=dict_rec_r['pr_osob'],
                        k_mm=dict_rec_r['k_mm'],
                        nib=dict_rec_r['nib'],
                        user=request.user.id
                    )
                    self.OPER = True
                except KeyError:
                    pass
        else:
            self.SLUCH = False
            temp_sluch.objects.filter(user=request.user.id).all().delete()
            for rec in DBF(file, char_decode_errors="ignore", encoding="cp866", lowernames=True):
                dict_rec_r = dict(rec)
                try:
                    tm_let = dict_rec_r['tm_let'] if dict_rec_r['tm_let'] != '' else None
                    temp_sluch.objects.create(
                        fam=dict_rec_r['fam'],
                        im=dict_rec_r['im'],
                        ot=dict_rec_r['ot'],
                        pol=dict_rec_r['pol'],
                        datr=dict_rec_r['datr'],
                        udl=dict_rec_r['udl'],
                        s_pasp=dict_rec_r['s_pasp'],
                        n_pasp=dict_rec_r['n_pasp'],
                        ss=dict_rec_r['ss'],
                        c_oksm=dict_rec_r['c_oksm'],
                        adr=dict_rec_r['adr'],
                        m_roj=dict_rec_r['m_roj'],
                        cod_adr=dict_rec_r['cod_adr'],
                        cj=dict_rec_r['cj'],
                        v_lgoty=dict_rec_r['v_lgoty'],
                        in_t=dict_rec_r['in_t'],
                        rab=dict_rec_r['rab'],
                        r_n=dict_rec_r['r_n'],
                        prof=dict_rec_r['prof'],
                        vec=dict_rec_r['vec'],
                        nib=dict_rec_r['nib'],
                        datp=dict_rec_r['datp'],
                        datv=dict_rec_r['datv'],
                        goc=dict_rec_r['goc'],
                        prpg=dict_rec_r['prpg'],
                        vrez=dict_rec_r['vrez'],
                        lpy=dict_rec_r['lpy'],
                        ws=dict_rec_r['ws'],
                        tm_otd=dict_rec_r['tm_otd'],
                        otd=dict_rec_r['otd'],
                        prof_k=dict_rec_r['prof_k'],
                        icx=dict_rec_r['icx'],
                        dsny=dict_rec_r['dsny'],
                        dsk=dict_rec_r['dsk'],
                        dskz=dict_rec_r['dskz'],
                        dsc=dict_rec_r['dsc'],
                        ds_osl=dict_rec_r['ds_osl'],
                        dson=dict_rec_r['dson'],
                        ksg_osn=dict_rec_r['ksg_osn'],
                        ksg_sop=dict_rec_r['ksg_sop'],
                        vid_hmp=dict_rec_r['vid_hmp'],
                        metod_hmp=dict_rec_r['metod_hmp'],
                        trs=dict_rec_r['trs'],
                        tm_let=tm_let,
                        pri=dict_rec_r['pri'],
                        ds_let=dict_rec_r['ds_let'],
                        wskr=dict_rec_r['wskr'],
                        dspat=dict_rec_r['dspat'],
                        rasxp=dict_rec_r['rasxp'],
                        otd_y=dict_rec_r['otd_y'],
                        vds=dict_rec_r['vds'],
                        sctp=dict_rec_r['sctp'],
                        nctp=dict_rec_r['nctp'],
                        t_pol=dict_rec_r['t_pol'],
                        ctkom=dict_rec_r['ctkom'],
                        ksg_ts=dict_rec_r['ksg_ts'],
                        t_trv=dict_rec_r['t_trv'],
                        details=dict_rec_r['details'],
                        trav_ns=dict_rec_r['trav_ns'],
                        pmg=dict_rec_r['pmg'],
                        user=request.user.id
                    )
                    self.SLUCH = True
                except KeyError:
                    continue

    def get_rez(self):
        return self.rez

    def _jon(self, s):
        l = str(s).split()
        j = ''.join(l)
        return j

    def __insert_to_models(self):
        Sluchay.objects.all().delete()
        Vb_s.objects.all().delete()
        Vds.objects.all().delete()
        Le_Vr.objects.all().delete()
        Le_trv.objects.all().delete()
        Oper.objects.all().delete()
        Oslo.objects.all().delete()
        Manpy.objects.all().delete()
        Disability.objects.all().delete()
        Patient_P.objects.all().delete()
        Patient.objects.all().delete()

        YEAR = datetime.datetime.now()
        ICX = dict()
        ICX[1] = 101
        ICX[2] = 303
        ICX[3] = 203
        ICX[4] = 305
    #     get_vidpow = V008.objects.get(id_tip=302)

        s_ts = temp_sluch.objects.values('fam', 'im', 'ot', 'pol', 'datr', 'udl', 's_pasp', 'n_pasp', 'ss', 'c_oksm', 'adr',
                                         'm_roj', 'cod_adr', 'cj', 'v_lgoty', 'in_t', 'rab', 'r_n', 'prof', 'vec', 'nib', 'datp',
                                         'datv', 'goc', 'prpg', 'vrez', 'lpy', 'ws', 'tm_otd', 'otd', 'prof_k', 'icx', 'dsny',
                                         'dsk', 'dskz', 'dsc', 'ds_osl', 'dson', 'ksg_osn', 'ksg_sop', 'vid_hmp', 'metod_hmp', 'trs',
                                         'tm_let', 'pri', 'ds_let', 'wskr', 'dspat', 'rasxp', 'otd_y', 'vds', 'sctp', 'nctp', 't_pol',
                                         'ctkom', 'ksg_ts', 't_trv', 'details', 'trav_ns', 'pmg').all()

        for s in range(len(s_ts)):
            if len(Sluchay.objects.filter(nib=s_ts[s]['nib'], datp__icontains=YEAR.year).all()[:1]) == 0:
                UUID = uuid.uuid1()

                # Oper

                o_st = temp_oper.objects.values('kod_op', 'dato', 'goc_o', 'py', 'kodx', 'kodxa',
                                                'kodxa1', 'obz', 'kodan', 'pr_osob', 'k_mm', 'nib').filter(nib=s_ts[s]['nib'])
         
                for o in range(len(o_st)):
                    if o_st[o]['kod_op'] != '':
                        try:
                            id_kod_op = V001.objects.get(kod=o_st[o]['kod_op'])
                        except V001.DoesNotExist:
                            id_kod_op = None
                    else:
                        id_kod_op = None
                    
                    if o_st[o]['obz'] != '':
                        try:
                            id_obz = V001.objects.get(kod=o_st[o]['obz'])
                        except V001.DoesNotExist:
                            id_obz = None
                    else:
                        id_obz = None
        
                    if len(o_st[o]['dato']) > 0:
                        date = str(o_st[o]['dato']).replace(".", "-")
                        date = datetime.datetime.strptime(
                            date, "%d-%m-%Y").date()
                    else:
                        date = None

                    if o_st[o]['py'] != '':
                        try:
                            id_py = PY.objects.get(kod=o_st[o]['py'])
                        except PY.DoesNotExist:
                            id_py = None
                    else:
                        id_py = None

                    if o_st[o]['kodx'] != '':
                        try:
                            kodx = self._jon(o_st[o]['kodx'])
                            top_1 = Vra.objects.filter(
                                kod=kodx).values_list('id')[:1]
                            try:
                                id_kodx = Vra.objects.get(id=top_1[0][0])
                            except IndexError:
                                id_kodx = None
                        except Vra.DoesNotExist:
                            id_kodx = None

                    else:
                        id_kodx = None

                    if o_st[o]['kodxa'] != '':
                        try:
                            kodxa = self._jon(o_st[o]['kodxa'])
                            top_1 = Vra.objects.filter(
                                kod=kodxa).values_list('id')[:1]
                            try:
                                id_kodxa = Vra.objects.get(id=top_1[0][0])
                            except IndexError:
                                id_kodxa = None
                        except Vra.DoesNotExist:
                            id_kodxa = None

                    else:
                        id_kodxa = None

                    if o_st[o]['kodxa1'] != '':
                        try:
                            kodxa1 = self._jon(o_st[o]['kodxa1'])
                            top_1 = Vra.objects.filter(
                                kod=kodxa1).values_list('id')[:1]
                            try:
                                id_kodxa1 = Vra.objects.get(id=top_1[0][0])
                            except IndexError:
                                id_kodxa1 = None
                        except Vra.DoesNotExist:
                            id_kodxa1 = None
                    else:
                        id_kodxa1 = None

                    if o_st[o]['kodan'] != '':
                        try:
                            kodan = self._jon(o_st[o]['kodan'])
                            top_1 = Vra.objects.filter(
                                kod=kodan).values_list('id')[:1]
                            try:
                                id_kodan = Vra.objects.get(id=top_1[0][0])
                            except IndexError:
                                id_kodan = None
                        except Vra.DoesNotExist:
                            id_kodan = None
                    else:
                        id_kodan = None

                    if o_st[o]['goc_o'] != '':
                        try:
                            id_goc = V014.objects.get(id_tip=o_st[o]['goc_o'])
                        except V014.DoesNotExist:
                            id_goc = None
                    else:
                        id_goc = None

                    Oper.objects.create(
                        id_pac=UUID,
                        kod_op=id_kod_op,
                        dato=date,
                        py=id_py,
                        kodx=id_kodx,
                        kodxa=id_kodxa,
                        kodxa1=id_kodxa1,
                        obz=id_obz,
                        kodan=id_kodan,
                        goc=id_goc
                    )
                
                

                # Sluchay
                if s_ts[s]['pmg'] != '':
                    try:
                        id_pmg = F003.objects.get(kod=s_ts[s]['pmg'])
                    except F003.DoesNotExist:
                        id_pmg = None
                else:
                    id_pmg = None

                if s_ts[s]['lpy'] != '':
                    try:
                        id_lpy = F003.objects.get(kod=s_ts[s]['lpy'])
                    except:
                        id_lpy = None
                else:
                    id_lpy = None

                if len(s_ts[s]['datp']) > 0:
                    date1 = str(s_ts[s]['datp']).replace(".", "-")
                    date1 = datetime.datetime.strptime(
                        date1, "%d-%m-%Y").date()
                else:
                    date1 = None

                if len(s_ts[s]['datv']) > 0:
                    date2 = str(s_ts[s]['datv']).replace(".", "-")
                    date2 = datetime.datetime.strptime(
                        date2, "%d-%m-%Y").date()
                else:
                    date2 = None

                # if s_ts[s]['prpg'] != '':
                #     try:
                #         id_prpg = Prpg.objects.get(kod=s_ts[s]['prpg'])
                #     except Prpg.DoesNotExist:
                #         id_prpg = None
                # else:
                #     id_prpg = None

                if s_ts[s]['vrez'] != '':
                    try:
                        id_vrez = Vrzb.objects.get(kod=s_ts[s]['vrez'])
                    except Vrzb.DoesNotExist:
                        id_vrez = None
                else:
                    id_vrez = None

                if s_ts[s]['ws'] != '':
                    try:
                        id_ws = Ws.objects.get(kod=s_ts[s]['ws'])
                    except Ws.DoesNotExist:
                        id_ws = None
                else:
                    id_vrez = None

                if s_ts[s]['otd'] != '':
                    try:
                        id_otd = otde.objects.get(kod=s_ts[s]['otd'])
                    except otde.DoesNotExist:
                        id_otd = None
                else:
                    id_otd = None

                # if s_ts[s]['prof_k'] != '':
                #     try:
                #         id_prof_k = V020.objects.get(idk_pr=s_ts[s]['prof_k'])
                #     except V020.DoesNotExist:
                #         id_prof_k = None
                # else:
                #     id_prof_k = None

                if len(s_ts[s]['icx']) > 0:
                    try:
                        id_iz = ICX[int(s_ts[s]['icx'])]
                        get_id_ishod = V012.objects.get(id_iz=id_iz)
                    except (V012.DoesNotExist, KeyError):
                        get_id_ishod = None
                else:
                    get_id_ishod = None

                if s_ts[s]['dsny'] != '':
                    try:
                        id_dsny = Ds.objects.get(kod=s_ts[s]['dsny'])
                    except Ds.DoesNotExist:
                        id_dsny = None
                else:
                    id_dsny = None

                if s_ts[s]['dsk'] != '':
                    try:
                        id_dsk = Ds.objects.get(kod=s_ts[s]['dsk'])
                    except Ds.DoesNotExist:
                        id_dsk = None
                else:
                    id_dsk = None

                if s_ts[s]['dskz'] != '':
                    try:
                        id_dskz = Ds.objects.get(kod=s_ts[s]['dskz'])
                    except Ds.DoesNotExist:
                        id_dskz = None
                else:
                    id_dskz = None

                if s_ts[s]['dsc'] != '':
                    try:
                        id_dsc = Ds.objects.get(kod=s_ts[s]['dsc'])
                    except Ds.DoesNotExist:
                        id_dsc = None
                else:
                    id_dsc = None

                if s_ts[s]['ds_osl'] != '':
                    try:
                        id_ds_osl = Ds.objects.get(kod=s_ts[s]['ds_osl'])
                    except Ds.DoesNotExist:
                        id_ds_osl = None
                else:
                    id_ds_osl = None

                if s_ts[s]['dson'] != '':
                    try:
                        id_dson = Ds.objects.get(kod=s_ts[s]['dson'])
                    except Ds.DoesNotExist:
                        id_dson = None
                else:
                    id_dson = None

                if s_ts[s]['ksg_osn'] != '':
                    try:
                        id_ksg_osn = T006.objects.get(
                            code_usl=s_ts[s]['ksg_osn'])
                    except T006.DoesNotExist:
                        id_ksg_osn = None
                else:
                    id_ksg_osn = None

                if s_ts[s]['ksg_sop'] != '':
                    try:
                        id_ksg_sop = T006.objects.get(
                            code_usl=s_ts[s]['ksg_sop'])
                    except T006.DoesNotExist:
                        id_ksg_sop = None
                else:
                    id_ksg_sop = None
                

                if s_ts[s]['goc'] != '':
                    try:
                        id_goc = V014.objects.get(id_tip=s_ts[s]['goc'])
                    except V014.DoesNotExist:
                        id_goc = None
                else:
                    id_goc = None

                if s_ts[s]['trs'] != '':
                    try:
                        id_trs = Trs.objects.get(kod=s_ts[s]['trs'])
                    except Trs.DoesNotExist:
                        id_trs = None
                else:
                    id_trs = None
                
                if s_ts[s]['ds_let'] !='':
                    try:
                        id_ds_let = Ds.objects.get(kod=s_ts[s]['ds_let'])
                    except Ds.DoesNotExist:
                        id_ds_let = None
                else:
                    id_ds_let = None

                if s_ts[s]['dspat'] !='':
                    try:
                        id_dspat = Ds.objects.get(kod=s_ts[s]['dspat'])
                    except Ds.DoesNotExist:
                        id_dspat = None
                else:
                    id_dspat = None
                
                if s_ts[s]['otd_y'] != '':
                    try:
                        id_otd_y = otde.objects.get(kod=s_ts[s]['otd_y'])
                    except otde.DoesNotExist:
                        id_otd_y = None
                else:
                    id_otd_y = None

                    

                Sluchay.objects.create(
                    id_pac=UUID,
                    pmg=id_pmg,
                    lpy=id_lpy,
                    nib=s_ts[s]['nib'],
                    datp=date1,
                    datv=date2,
                    # prpg=id_prpg,
                    vrez=id_vrez,
                    ws=id_ws,
                    tm_otd=s_ts[s]['tm_otd'],
                    otd=id_otd,
                    icx=get_id_ishod,
                    dsny=id_dsny,
                    dsk=id_dsk,
                    dskz=id_dskz,
                    dsc=id_dsc,
                    ds_osl=id_ds_osl,
                    dson=id_dson,
                    ksg_osn=id_ksg_osn,
                    ksg_sop=id_ksg_sop,
                    vid_hmp=s_ts[s]['vid_hmp'],
                    metod_hmp=s_ts[s]['metod_hmp'],
                    tm_let=s_ts[s]['tm_let'],

                    # pri=s_ts[s]['pri'],

                    ds_let=id_ds_let,
                    wskr=s_ts[s]['wskr'],
                    dspat=id_dspat,
                    rasxp=s_ts[s]['rasxp'],
                    otd_y=id_otd_y,
                    goc=id_goc,
                    trs=id_trs
                )

                # Vds

                if s_ts[s]['t_pol'] != '':
                    try:
                        id_t_pol = F008.objects.get(id_tip=s_ts[s]['t_pol'])
                    except F008.DoesNotExist:
                        id_t_pol = None
                else:
                    id_t_pol = None

                if s_ts[s]['vds'] != '':
                    try:
                        id_vds = V010.objects.get(spname=s_ts[s]['vds'])
                    except V010.DoesNotExist:
                        id_vds = None
                else:
                    id_vds = None

                if s_ts[s]['ctkom'] != '':
                    try:
                        id_ctkom = Skom.objects.get(kod=s_ts[s]['ctkom'])
                    except Skom.DoesNotExist:
                        id_ctkom = None
                else:
                    id_ctkom = None

                if s_ts[s]['ksg_ts'] != '':
                    try:
                        id_ksg_ts = T003.objects.get(kod=s_ts[s]['ksg_ts'])
                    except T003.DoesNotExist:
                        id_ksg_ts = None
                else:
                    id_ksg_ts = None

                Vds.objects.create(
                    id_pac=UUID,
                    t_pol=id_t_pol,
                    vds=id_vds,
                    ctkom=id_ctkom,
                    sctp=s_ts[s]['sctp'],
                    nctp=s_ts[s]['nctp'],
                    ksg_ts=id_ksg_ts
                )

                # Le_trv

                if s_ts[s]['t_trv'] != '':
                    try:
                        id_t_trv = Ds.objects.get(kod=s_ts[s]['t_trv'])
                    except Ds.DoesNotExist:
                        id_t_trv = None
                else:
                    id_t_trv = None

                if s_ts[s]['details'] != '':
                    try:
                        id_details = Ds.objects.get(kod=s_ts[s]['details'])
                    except Ds.DoesNotExist:
                        id_details = None
                else:
                    id_details = None

                if s_ts[s]['trav_ns'] != '':
                    try:
                        id_trav_ns = Trv.objects.get(kod=s_ts[s]['trav_ns'])
                    except Trv.DoesNotExist:
                        id_trav_ns = None
                else:
                    id_trav_ns = None

                Le_trv.objects.create(
                    id_pac=UUID,
                    t_trv=id_t_trv,
                    details=id_details,
                    # trav_ns=id_trav_ns
                )


                #le_vr

                if s_ts[s]['prof_k'] != '':
                    try:
                        id_prof_k = V020.objects.get(idk_pr=s_ts[s]['prof_k'])
                    except V020.DoesNotExist:
                        id_prof_k = None
                else:
                    id_prof_k = None

                Le_Vr.objects.create(
                    id_pac=UUID,
                    prof_k=id_prof_k
                )

                # Patient
                if len(s_ts[s]['datr']) > 0:
                    date = str(s_ts[s]['datr']).replace(".", "-")
                    date = datetime.datetime.strptime(date, "%d-%m-%Y").date()
                else:
                    date = None

                if date != None:
                    if YEAR.year > date.year:
                        vs = YEAR.year - date.year
                        nvs = 'Л'
                    elif YEAR.year == date.year:
                        if int(date.month) < int(YEAR.month):
                            vs = YEAR.month - date.month
                            nvs = 'М'
                        else:
                            vs = YEAR.day - date.day
                            nvs = 'Д'
                    else:
                        vs = None
                        nvs = None
                else:
                    vs = None
                    nvs = None
                try:
                    id_pol = V005.objects.get(id_pol=s_ts[s]['pol'])
                except V005.DoesNotExist:
                    id_pol = None

                if s_ts[s]['udl'] != '':
                    try:
                        id_udl = F011.objects.get(id_doc=s_ts[s]['udl'])
                    except F011.DoesNotExist:
                        id_udl = None
                else:
                    id_udl = None

                if s_ts[s]['c_oksm'] != '':
                    try:
                        id_c_oksm = Oksm.objects.get(kod=s_ts[s]['c_oksm'])
                    except Oksm.DoesNotExist:
                        id_c_oksm = None
                else:
                    id_c_oksm = None

                if s_ts[s]['cj'] != '':
                    try:
                        id_cj = CJ.objects.get(kod=s_ts[s]['cj'])
                    except CJ.DoesNotExist:
                        id_cj = None
                else:
                    id_cj = None

                if s_ts[s]['v_lgoty'] != '':
                    try:
                        id_v_lgoty = V_LGOTY.objects.get(
                            kod=s_ts[s]['v_lgoty'])
                    except V_LGOTY.DoesNotExist:
                        id_v_lgoty = None
                else:
                    id_v_lgoty = None

                if s_ts[s]['in_t'] != '':
                    try:
                        id_in_t = T004.objects.get(kod=s_ts[s]['in_t'])
                    except T004.DoesNotExist:
                        id_in_t = None
                else:
                    id_in_t = None

                if s_ts[s]['r_n'] != '':
                    try:
                        id_r_n = Rab_Ner.objects.get(kod=s_ts[s]['r_n'])
                    except Rab_Ner.DoesNotExist:
                        id_r_n = None
                else:
                    id_r_n = None

                if s_ts[s]['vec'] == '':
                    vec = 0
                else:
                    vec = s_ts[s]['vec']
                #new
                # if s_ts[s]['trs'] != '':
                #     try:
                #         id_trs = Trs.objects.get(kod=s_ts[s]['trs'])
                #     except Trs.DoesNotExist:
                #         id_trs = None
                # else:
                #     id_trs = None
                


                Patient.objects.create(
                    id_pac=UUID,
                    fam=s_ts[s]['fam'],
                    im=s_ts[s]['im'],
                    ot=s_ts[s]['ot'],
                    pol=id_pol,
                    datr=date,
                    vs=vs,
                    nvs=nvs,
                    udl=id_udl,
                    s_pasp=s_ts[s]['s_pasp'],
                    n_pasp=s_ts[s]['n_pasp'],
                    ss=s_ts[s]['ss'],
                    cod_adr=s_ts[s]['cod_adr'],
                    c_oksm=id_c_oksm,
                    adr=s_ts[s]['adr'],
                    m_roj=s_ts[s]['m_roj'],
                    cj=id_cj,
                    v_lgoty=id_v_lgoty,
                    in_t=id_in_t,
                    rab=s_ts[s]['rab'],
                    r_n=id_r_n,
                    prof=s_ts[s]['prof'],
                    vec=vec,
                    #new
                    # trs=id_trs,
                )

                patient = Patient.objects.get(id_pac=UUID)
                sluchay = Sluchay.objects.get(id_pac=UUID)
                patient.sluchay.add(sluchay)

                vds = Vds.objects.get(id_pac=UUID)
                # patient.vds.add(vds)
                sluchay.vds.add(vds)
                le_trv = Le_trv.objects.get(id_pac=UUID)
                # patient.le_trv.add(le_trv)
                sluchay.le_trv.add(le_trv)
                le_vr = Le_Vr.objects.get(id_pac=UUID)
                # patient.le_vr.add(le_vr)
                sluchay.le_vr.add(le_vr)

                try:
                    oper_list = list(map(lambda r: r[0], Oper.objects.filter(id_pac=UUID).values_list('id')))
                    for oper in range(len(oper_list)):
                        id_oper = Oper.objects.get(id=oper_list[oper])
                        # patient.oper.add(id_oper)
                        sluchay.oper.add(id_oper)
                except:
                    pass
                
            else:
                continue
