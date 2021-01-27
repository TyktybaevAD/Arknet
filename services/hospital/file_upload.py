from django.templatetags.static import static
from django.contrib.staticfiles import finders
from django.conf import settings
from django.core import exceptions
from hospital.models import temp_oper,temp_sluch
from okb2.models import Pers,Pacient,F008,Inf_Z_sl,V012,V014,Inf_Sl,Ksg_kpg
from django.db import connection
from dbfread import DBF
from pprint import pprint
import os,time,datetime,uuid


rez = list()
OPER = None
SLUCH = None
def hospital_file_upload_1c(request):
    global rez,OPER,SLUCH
    rez.clear()
    # 1 - oper
    # 2 - sluch

    from hospital.models import Load_1c
    f_oper,f_sluch = list(Load_1c.objects.values_list('oper','sluch').filter(user = request.user.id))[0]


    dir_oper = settings.MEDIA_ROOT +'/'+ f_oper
    dir_sluch = settings.MEDIA_ROOT +'/'+ f_sluch
    
    insert_hospital(dir_oper,request,1)
    insert_hospital(dir_sluch,request,2)
    rez.append(OPER)
    rez.append(SLUCH)
    
    if (OPER == True) and (SLUCH == True):
        insert_to_models()

    return rez    

def insert_hospital(file,request,tip_file):
    global OPER,SLUCH
    print('request.user.id,',request.user.id)
    if tip_file == 1:
        OPER = False
        temp_oper.objects.filter(user=request.user.id).all().delete()
        for rec in DBF(file,char_decode_errors="ignore", encoding="cp866", lowernames=True):
            dict_rec_r = dict(rec)
            # Так не работает :(

            # rez_str = list()
            # for k,v in dict_rec_r.items():
            #     rez_str.append(k+'='+"'"+str(v)+"'")
            # rez_str.append('user'+'='+str(request.user.id))
            # rez.append(True)
            # temp_oper.objects.create(','.join(rez_str))
            # break

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
                                            kodan=dict_rec_r['kodan'],
                                            pr_osob=dict_rec_r['pr_osob'],
                                            k_mm=dict_rec_r['k_mm'],
                                            nib=dict_rec_r['nib'],
                                            user=request.user.id
                                        )
                OPER = True
            except KeyError:
                # rez.append(False)
                # OPER = False
                break
        # else:
        #     rez.append(True)
            

    else:
        SLUCH = False
        temp_sluch.objects.filter(user=request.user.id).all().delete()
        for rec in DBF(file,char_decode_errors="ignore", encoding="cp866", lowernames=True):
            dict_rec_r = dict(rec) 
            try:
                temp_sluch.objects.create(
                                            fam = dict_rec_r['fam'],
                                            im = dict_rec_r['im'],
                                            ot = dict_rec_r['ot'],
                                            pol = dict_rec_r['pol'],
                                            datr = dict_rec_r['datr'],
                                            udl = dict_rec_r['udl'],
                                            s_pasp = dict_rec_r['s_pasp'],
                                            n_pasp = dict_rec_r['n_pasp'],
                                            ss = dict_rec_r['ss'],
                                            c_oksm = dict_rec_r['c_oksm'],
                                            adr = dict_rec_r['adr'],
                                            m_roj = dict_rec_r['m_roj'],
                                            cod_adr = dict_rec_r['cod_adr'],
                                            cj = dict_rec_r['cj'],
                                            v_lgoty = dict_rec_r['v_lgoty'],
                                            in_t = dict_rec_r['in_t'],
                                            rab = dict_rec_r['rab'],
                                            r_n = dict_rec_r['r_n'],
                                            prof = dict_rec_r['prof'],
                                            vec = dict_rec_r['vec'],
                                            nib = dict_rec_r['nib'],
                                            datp = dict_rec_r['datp'],
                                            datv = dict_rec_r['datv'],
                                            goc = dict_rec_r['goc'],
                                            prpg = dict_rec_r['prpg'],
                                            vrez = dict_rec_r['vrez'],
                                            lpy = dict_rec_r['lpy'],
                                            ws = dict_rec_r['ws'],
                                            tm_otd = dict_rec_r['tm_otd'],
                                            otd = dict_rec_r['otd'],
                                            prof_k = dict_rec_r['prof_k'],
                                            icx = dict_rec_r['icx'],
                                            dsny = dict_rec_r['dsny'],
                                            dsk = dict_rec_r['dsk'],
                                            dskz = dict_rec_r['dskz'],
                                            dsc = dict_rec_r['dsc'],
                                            ds_osl = dict_rec_r['ds_osl'],
                                            dson = dict_rec_r['dson'],
                                            ksg_osn = dict_rec_r['ksg_osn'],
                                            ksg_sop = dict_rec_r['ksg_sop'],
                                            vid_hmp = dict_rec_r['vid_hmp'],
                                            metod_hmp = dict_rec_r['metod_hmp'],
                                            trs = dict_rec_r['trs'],
                                            tm_let = dict_rec_r['tm_let'],
                                            pri = dict_rec_r['pri'],
                                            ds_let = dict_rec_r['ds_let'],
                                            wskr = dict_rec_r['wskr'],
                                            dspat = dict_rec_r['dspat'],
                                            rasxp = dict_rec_r['rasxp'],
                                            otd_y = dict_rec_r['otd_y'],
                                            vds = dict_rec_r['vds'],
                                            sctp = dict_rec_r['sctp'],
                                            nctp = dict_rec_r['nctp'],
                                            t_pol = dict_rec_r['t_pol'],
                                            ctkom = dict_rec_r['ctkom'],
                                            ksg_ts = dict_rec_r['ksg_ts'],
                                            t_trv = dict_rec_r['t_trv'],
                                            details = dict_rec_r['details'],
                                            trav_ns = dict_rec_r['trav_ns'],
                                            pmg = dict_rec_r['pmg'],
                                            user=request.user.id
                                        )
                SLUCH = True
            except KeyError:
                # rez.append(False)
                # SLUCH = False
                break
        # else:
        #     rez.append(True)


def insert_to_models():
    Inf_Sl.objects.all().delete()
    Pers.objects.all().delete()
    Pacient.objects.all().delete()
    Inf_Z_sl.objects.all().delete()
    Ksg_kpg.objects.all().delete()

    YEAR = datetime.datetime.now()
    ICX = dict()
    ICX[1]=101
    ICX[2]=303
    ICX[3]=203
    ICX[4]=305
    s_ts = temp_sluch.objects.values('fam','im','ot','pol','datr','udl','s_pasp','n_pasp','ss','cod_adr','c_oksm','adr','m_roj','cj','v_lgoty','in_t','rab','r_n','prof',
                                    't_pol','sctp','nctp','ctkom','vec','pmg',
                                    'goc','lpy','datp','datv','icx','vds','ksg_ts',
                                    'vid_hmp','metod_hmp','otd','prof_k','nib','datp','datv','dsk','dsc','ds_osl','prpg','vrez','ws','tm_otd','dsny','dsk','dskz','dson','trs','tm_let','pri','ds_let','wskr','dspat','rasxp','otd_y','t_trv','details','trav_ns',
                                    'ksg_osn','ksg_sop').all()

    for s in range(len(s_ts)):
        UUID = uuid.uuid1()
        if len(Inf_Sl.objects.filter(nhistory=s_ts[s]['nib'],date_1__icontains=YEAR.year).all()[:1])==0:
        
            try:
                if len(s_ts[s]['datr'])>0:
                    date = str(s_ts[s]['datr']).replace(".","-")
                    date = datetime.datetime.strptime(date,"%d-%m-%Y").date()
                else:
                    date = None

                Pers.objects.create(
                                    id_pac=UUID,
                                    fam=s_ts[s]['fam'],
                                    im=s_ts[s]['im'],
                                    ot=s_ts[s]['ot'],
                                    w=s_ts[s]['pol'],
                                    dr=date,
                                    doctype=s_ts[s]['udl'],
                                    docser=s_ts[s]['s_pasp'],
                                    docnum=s_ts[s]['n_pasp'],
                                    snils=s_ts[s]['ss'],
                                    okatop=s_ts[s]['cod_adr']
                )
                
            except exceptions.ValidationError:
                continue
            
            pers_id = Pers.objects.filter(id_pac=UUID).values_list('id')[0][0]
            get_pers = Pers.objects.get(pk=pers_id)

            if len(s_ts[s]['t_pol'])>0:
                get_id_vpolis = F008.objects.get(id_tip=s_ts[s]['t_pol'])
            else:
                get_id_vpolis = None

            try:
                Pacient.objects.create(
                                        id_pac=UUID,
                                        id_pers=get_pers,
                                        vpolis=get_id_vpolis,
                                        spolis=s_ts[s]['sctp'],
                                        npolis=s_ts[s]['nctp'],
                                        smo=s_ts[s]['ctkom'],
                                        vnov_d=s_ts[s]['vec'],
                                        pmg=s_ts[s]['pmg']
                                        )
            except Exception as e:
                print(e)
                print('Pacient')
            
            try:
                try:
                    id_tip_v014 = int(str(s_ts[s]['goc']).strip())
                    get_id_v014 = V014.objects.get(id_tip=id_tip_v014)
                except ValueError:
                    get_id_v014 = None
                
                if len(s_ts[s]['datp']) > 0:
                    date1 = str(s_ts[s]['datp']).replace(".","-")
                    date1 = datetime.datetime.strptime(date1,"%d-%m-%Y").date()
                else:
                    date1 = None
                
                if len(s_ts[s]['datv'])>0:
                    date2 = str(s_ts[s]['datv']).replace(".","-")
                    date2 = datetime.datetime.strptime(date2,"%d-%m-%Y").date()
                else:
                    date2 = None
                
                if len(s_ts[s]['icx'])>0:
                    try:
                        id_iz = ICX[int(s_ts[s]['icx'])]
                        get_id_ishod = V012.objects.get(id_iz=id_iz)
                    except (ValueError,KeyError):
                        get_id_ishod = None
                else:
                    get_id_ishod = None

                Inf_Z_sl.objects.create(id_pac=UUID,
                                        for_pom=get_id_v014,
                                        lpu=s_ts[s]['lpy'],
                                        date_z_1=date1,
                                        date_z_2=date2,
                                        ishod=get_id_ishod,
                                        vds=s_ts[s]['vds'],
                                        ksg_ts=s_ts[s]['ksg_ts']
                                        )

                get_inf_z_sl = Inf_Z_sl.objects.get(id_pac=UUID)
                get_pacient = Pacient.objects.get(id_pac=UUID)
                # get_pacient.id_inf_z_sl.add(get_inf_z_sl)
                
            except Exception as e:
                print(e)
                print(UUID)
                


            try:
                # Нудно связать поля по ключам не забыть это сделать
                Inf_Sl.objects.create(
                    id_pac=UUID,
                    vid_hmp=s_ts[s]['vid_hmp'],
                    metod_hmp=s_ts[s]['metod_hmp'],
                    # podr Поле должно содержать id но из 1с буквы и цыфры нужно понять к чему они 
                    # podr=s_ts[s]['otd'],
                    # profil_k=s_ts[s]['prof_k'],
                    nhistory=s_ts[s]['nib'],
                    date_1=date1,
                    date_2=date2,
                    ds1=s_ts[s]['dsk'],
                    ds2=s_ts[s]['dsc'],
                    ds3=s_ts[s]['ds_osl'],
                    prpg=s_ts[s]['prpg'],
                    vrez=s_ts[s]['vrez'],
                    ws=s_ts[s]['ws'],
                    tm_otd=s_ts[s]['tm_otd'],
                    dsny=s_ts[s]['dsny'],
                    dsk=s_ts[s]['dsk'],
                    dskz=s_ts[s]['dskz'],
                    dson=s_ts[s]['dson'],
                    trs=s_ts[s]['trs'],
                    tm_let=s_ts[s]['tm_let'],
                    pri=s_ts[s]['pri'],
                    ds_let=s_ts[s]['ds_let'],
                    wskr=s_ts[s]['wskr'], 
                    dspat=s_ts[s]['dspat'], 
                    rasxp=s_ts[s]['rasxp'], 
                    otd_y=s_ts[s]['otd_y'],
                    t_trv=s_ts[s]['t_trv'],
                    details=s_ts[s]['details'], 
                    trav_ns=s_ts[s]['trav_ns']
                )
                get_inf_sl = Inf_Sl.objects.get(id_pac=UUID)
                get_inf_z_sl.id_inf_sl.add(get_inf_sl)
            except Exception as e:
                print(e)


            try:
                Ksg_kpg.objects.create(
                    id_pac=UUID,
                    ksg_osn=s_ts[s]['ksg_osn'],
                    ksg_sop=s_ts[s]['ksg_osn']
                )
                get_ksg_kpg = Ksg_kpg.objects.get(id_pac=UUID)
                get_inf_sl.id_ksg_kpg.add(get_ksg_kpg)
            except Exception as e:
                print(e)
        else:
            continue
        
    
  

        


#Inf_Sl.objects.filter(nhistory='0242129',date_1__icontains='2021').all()[:1]