from okb2.models import *
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .validators import validate_file
# Create your models here.

## Загрузка Из 1С
class Load_1c(models.Model):
    oper = models.FileField(upload_to='documents/hospital/%Y/%m/%d',validators=[validate_file])
    sluch = models.FileField(upload_to='documents/hospital/%Y/%m/%d',validators=[validate_file])
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.oper.name + ' ' + self.sluch.name
    

@receiver(post_delete,sender=Load_1c)
def submission_delete(sender, instance, **kwargs):
    instance.oper.delete(False)
    instance.sluch.delete(False)

class temp_oper(models.Model):
    kod_op = models.CharField(max_length=30,blank=True,null=True)
    dato = models.CharField(max_length=10,blank=True,null=True)
    goc_o = models.CharField(max_length=10,blank=True,null=True)
    py = models.CharField(max_length=10,blank=True,null=True)
    kodx = models.CharField(max_length=10,blank=True,null=True)
    kodxa = models.CharField(max_length=10,blank=True,null=True)
    kodxa1 = models.CharField(max_length=10,blank=True,null=True)
    obz = models.CharField(max_length=10,blank=True,null=True)
    kodan = models.CharField(max_length=10,blank=True,null=True)
    pr_osob = models.CharField(max_length=10,blank=True,null=True)
    k_mm = models.CharField(max_length=10,blank=True,null=True)
    nib = models.CharField(max_length=30,blank=True,null=True)
    user = models.CharField(max_length=10,blank=True,null=True)

class temp_sluch(models.Model):
    fam = models.CharField(max_length=50,blank=True,null=True)
    im = models.CharField(max_length=50,blank=True,null=True)
    ot = models.CharField(max_length=50,blank=True,null=True)
    pol = models.CharField(max_length=1,blank=True,null=True)
    datr = models.CharField(max_length=10,blank=True,null=True)
    udl = models.CharField(max_length=50,blank=True,null=True)
    s_pasp = models.CharField(max_length=4,blank=True,null=True)
    n_pasp = models.CharField(max_length=6,blank=True,null=True)
    ss = models.CharField(max_length=14,blank=True,null=True)
    c_oksm = models.CharField(max_length=3,blank=True,null=True)
    adr = models.CharField(max_length=200,blank=True,null=True)
    m_roj = models.CharField(max_length=200,blank=True,null=True)
    cod_adr = models.CharField(max_length=50,blank=True,null=True)
    cj = models.CharField(max_length=1,blank=True,null=True)
    v_lgoty = models.CharField(max_length=1,blank=True,null=True)
    in_t = models.CharField(max_length=3,blank=True,null=True)
    rab = models.CharField(max_length=200,blank=True,null=True)
    r_n = models.CharField(max_length=20,blank=True,null=True)
    prof = models.CharField(max_length=150,blank=True,null=True)
    vec = models.CharField(max_length=5,blank=True,null=True)
    nib = models.CharField(max_length=15,blank=True,null=True)
    datp = models.CharField(max_length=10,blank=True,null=True)
    datv = models.CharField(max_length=10,blank=True,null=True)
    goc = models.CharField(max_length=1,blank=True,null=True)
    prpg = models.CharField(max_length=12,blank=True,null=True)
    vrez = models.CharField(max_length=20,blank=True,null=True)
    lpy = models.CharField(max_length=6,blank=True,null=True)
    ws = models.CharField(max_length=5,blank=True,null=True)
    tm_otd = models.CharField(max_length=6,blank=True,null=True)
    otd = models.CharField(max_length=10,blank=True,null=True)
    prof_k = models.CharField(max_length=50,blank=True,null=True)
    icx = models.CharField(max_length=1,blank=True,null=True)
    dsny = models.CharField(max_length=10,blank=True,null=True)
    dsk = models.CharField(max_length=10,blank=True,null=True)
    dskz = models.CharField(max_length=10,blank=True,null=True)
    dsc = models.CharField(max_length=10,blank=True,null=True)
    ds_osl = models.CharField(max_length=100,blank=True,null=True)
    dson = models.CharField(max_length=10,blank=True,null=True)
    ksg_osn = models.CharField(max_length=15,blank=True,null=True)
    ksg_sop = models.CharField(max_length=15,blank=True,null=True)
    vid_hmp = models.CharField(max_length=20,blank=True,null=True)
    metod_hmp = models.CharField(max_length=20,blank=True,null=True)
    trs = models.CharField(max_length=10,blank=True,null=True)
    tm_let = models.CharField(max_length=5,blank=True,null=True)
    pri = models.CharField(max_length=3,blank=True,null=True)
    ds_let = models.CharField(max_length=10,blank=True,null=True)
    wskr = models.CharField(max_length=1,blank=True,null=True)
    dspat = models.CharField(max_length=10,blank=True,null=True)
    rasxp = models.CharField(max_length=10,blank=True,null=True)
    otd_y = models.CharField(max_length=6,blank=True,null=True)
    vds = models.CharField(max_length=100,blank=True,null=True)
    sctp = models.CharField(max_length=16,blank=True,null=True)
    nctp = models.CharField(max_length=16,blank=True,null=True)
    t_pol = models.CharField(max_length=1,blank=True,null=True)
    ctkom = models.CharField(max_length=10,blank=True,null=True)
    ksg_ts = models.CharField(max_length=30,blank=True,null=True)
    t_trv = models.CharField(max_length=2,blank=True,null=True)
    details = models.CharField(max_length=6,blank=True,null=True)
    trav_ns = models.CharField(max_length=2,blank=True,null=True)
    pmg = models.CharField(max_length=10,blank=True,null=True)
    user = models.CharField(max_length=10,blank=True,null=True)

#####



class Vb_s(models.Model):
    #Сведения о переводах
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    kod_y = models.ForeignKey(F003,on_delete=models.SET_NULL,blank=True,null=True)
    pr_per = models.ForeignKey(PR_PER,on_delete=models.SET_NULL,blank=True,null=True)
    #Внутренний перевод
    potd = models.ForeignKey(otde,on_delete=models.SET_NULL,blank=True,null=True)
    dat_pe = models.DateField(blank=True,null=True)
    datv = models.DateField(blank=True,null=True)

class Vb_a(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    datv = models.DateField(blank=True,null=True)
    srber = models.IntegerField(blank=True,null=True)
    pra = models.BooleanField(blank=True,null=True)
    pria = models.ForeignKey(Tip_pb,on_delete=models.SET_NULL,blank=True,null=True)
    m_prer = models.ForeignKey(Met_pb,on_delete=models.SET_NULL,blank=True,null=True)
    n_ber = models.IntegerField(blank=True,null=True)


class Vds(models.Model):
    #сведения об оплате оказанной мед.помощи
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    vds = models.ForeignKey(Isfin,on_delete=models.SET_NULL,blank=True,null=True)
    sctp = models.CharField(max_length=30,blank=True,null=True)
    nctp = models.CharField(max_length=30,blank=True,null=True)
    t_pol = models.ForeignKey(F008,on_delete=models.SET_NULL,blank=True,null=True)
    ctkom = models.ForeignKey(Skom,on_delete=models.SET_NULL,blank=True,null=True)
    ksg_ts = models.ForeignKey(T003,on_delete=models.SET_NULL,blank=True,null=True)

class Le_Vr(models.Model):
    #Сведения о койко-днях
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    kod = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True)
    spec = models.ForeignKey(V021,on_delete=models.SET_NULL,blank=True,null=True)
    prof_k = models.ForeignKey(V020,on_delete=models.SET_NULL,blank=True,null=True)
    pea = models.IntegerField(blank=True,null=True)
    kat1 = models.IntegerField(blank=True,null=True)
    kat2 = models.IntegerField(blank=True,null=True)
    kat3 = models.IntegerField(blank=True,null=True)
    datv = models.DateField(blank=True,null=True)
    prk = models.CharField(max_length=10,blank=True,null=True)


class Le_trv(models.Model):
    # Заполняется при определенных диагнозах и 1с 
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    t_trv = models.ForeignKey(Trv,on_delete=models.SET_NULL,blank=True,null=True,related_name='Trv')
    details = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='details')
    trav_ns = models.BooleanField(blank=True,null=True)
    # trv_3 = models.BooleanField(default=None,blank=True,null=True)

class Oslo(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    osl = models.ForeignKey(Pope,on_delete=models.SET_NULL,blank=True,null=True)
    xosl = models.ForeignKey(Xosl,on_delete=models.SET_NULL,blank=True,null=True)
    posl = models.ForeignKey(Posl,on_delete=models.SET_NULL,blank=True,null=True)
    aosl = models.ForeignKey(Aosl,on_delete=models.SET_NULL,blank=True,null=True)
    datp = models.DateField(blank=True,null=True)
    dato = models.DateField(blank=True,null=True)
    kopr = models.CharField(max_length=5,blank=True,null=True)
    datv = models.DateField(blank=True,null=True)
    tnvr = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True)
    


class Oper(models.Model):
    #Операции
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    kodo = models.CharField(max_length=10,blank=True,null=True)
    kodx = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True,related_name='kodx')
    obz = models.ForeignKey(V001,on_delete=models.SET_NULL,blank=True,null=True,related_name='obz')
    koda = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True,related_name='koda')
    kods = models.IntegerField(blank=True,null=True)
    kodxa = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True,related_name='kodxa')
    kodxa1 = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True,related_name='kodxa1')
    kodan = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True,related_name='kodan')
    kopr = models.CharField(max_length=5,blank=True,null=True)
    datv = models.DateField(blank=True,null=True)
    goc = models.ForeignKey(V014,on_delete=models.SET_NULL,blank=True,null=True,related_name='goc_o')
    pop = models.BooleanField(default=False,blank=True,null=True)
    py = models.ForeignKey(PY,on_delete=models.SET_NULL,blank=True,null=True)
    kod_op = models.ForeignKey(V001,on_delete=models.SET_NULL,blank=True,null=True)
    pr_osob = models.ManyToManyField(PR_OSOB,blank=True)
    k_mm = models.DecimalField(decimal_places=2,max_digits=2,blank=True,null=True)
    metobz = models.CharField(max_length=5,blank=True,null=True)
    dato = models.DateField(blank=True,null=True)
    tm_o = models.TimeField(blank=True,null=True)
    oslo = models.ManyToManyField(Oslo,blank=True)




class Manpy(models.Model):
    #Сведения о манипуляциях
    PL_CHOICES = [
        ('0','Неизвестно'),
        ('1','Да'),
        ('2','Нет')
    ]
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    tnvr = models.ForeignKey(Vra,on_delete=models.SET_NULL,blank=True,null=True)
    kodmn = models.ForeignKey(Ab_Obsh,on_delete=models.SET_NULL,blank=True,null=True)
    kopr = models.CharField(max_length=15,blank=True,null=True)
    datm = models.DateField(blank=True,null=True)
    datv = models.DateField(blank=True,null=True)
    kol = models.IntegerField(blank=True,null=True)
    py = models.ForeignKey(PY,on_delete=models.SET_NULL,blank=True,null=True)
    pl = models.CharField(max_length=15,choices=PL_CHOICES,blank=True,null=True)

    
    def pl_display(self):
        return self.get_pl_display()


class Disability(models.Model):
    #Сведения о листе нетрудоспособности
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    dat_l1 = models.DateField(blank=True,null=True)
    dat_l2 = models.DateField(blank=True,null=True)
    ot_ln = models.BooleanField(blank=True,null=True)
    vs_bol = models.IntegerField(blank=True,null=True)
    sex_bol = models.ForeignKey(V005,on_delete=models.SET_NULL,blank=True,null=True)

class Napr(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    naprdate = models.DateField(blank=True,null=True)
    napr_mo = models.ForeignKey(F003,on_delete=models.SET_NULL,blank=True,null=True)
    napr_v = models.ForeignKey(V028,on_delete=models.SET_NULL,blank=True,null=True)
    napr_issl = models.ForeignKey(V029,on_delete=models.SET_NULL,blank=True,null=True)
    napr_usl = models.ForeignKey(V001,on_delete=models.SET_NULL,blank=True,null=True)
    

class Cons(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    pr_cons = models.ForeignKey(N019,on_delete=models.SET_NULL,blank=True,null=True)
    dt_cons = models.DateField(blank=True,null=True)

class Onk_sl(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    ds1_t = models.ForeignKey(N018,on_delete=models.SET_NULL,blank=True,null=True)
    stad = models.ForeignKey(N002,on_delete=models.SET_NULL,blank=True,null=True)
    onk_t = models.ForeignKey(N003,on_delete=models.SET_NULL,blank=True,null=True)
    onk_n = models.ForeignKey(N004,on_delete=models.SET_NULL,blank=True,null=True)
    onk_m = models.ForeignKey(N005,on_delete=models.SET_NULL,blank=True,null=True)
    mtstz = models.ForeignKey(V027,on_delete=models.SET_NULL,blank=True,null=True)

class B_diag(models.Model):
    DIAG_TIP_CHOICES = [
        ('1','Гистологический признак'),
        ('2','Маркёр (ИГХ)')
    ]
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    diag_date = models.DateField(blank=True,null=True)
    diag_tip = models.CharField(max_length=1,choices=DIAG_TIP_CHOICES,blank=True,null=True)
    diag_code = models.CharField(max_length=20,blank=True,null=True)
    diag_rslt = models.CharField(max_length=20,blank=True,null=True)
    rec_rslt = models.IntegerField(blank=True,null=True)
    
    def diag_tip_display(self):
        return self.get_diag_tip_display()

class B_prot(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    prot = models.ForeignKey(N001,on_delete=models.SET_NULL,blank=True,null=True)
    d_prot = models.DateField(blank=True,null=True)

class Onk_usl(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    usl_tip = models.ForeignKey(N013,on_delete=models.SET_NULL,blank=True,null=True)
    hir_tip = models.ForeignKey(N014,on_delete=models.SET_NULL,blank=True,null=True)

class Ksg_kpg(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    ksg_in = models.ForeignKey(V023,on_delete=models.SET_NULL,blank=True,null=True)
    ksg_ins = models.CharField(max_length=8,blank=True,null=True)

class Sluchay(models.Model):
    #Сведения о пребывании в стационаре (случай)
    TIP_WSK_CHOICES = [
        ('1','без вскрытия'),
        ('2','патологоанатом.'),
        ('3','судебное')
    ]
    RASX_CHOICES = [
        ('1','Да'),
        ('2','Нет')
    ]

    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    nib = models.CharField(max_length=20,blank=True,null=True)
    datp = models.DateField(blank=True,null=True)
    datv = models.DateField(blank=True,null=True)
    goc = models.ForeignKey(V014,on_delete=models.SET_NULL,blank=True,null=True)
    prpg = models.ForeignKey(Prpg,on_delete=models.SET_NULL,blank=True,null=True)
    vrez = models.ForeignKey(Vrzb,on_delete=models.SET_NULL,blank=True,null=True)
    lpy = models.ForeignKey(F003,on_delete=models.SET_NULL,blank=True,null=True,related_name='lpy')
    ws = models.ForeignKey(Ws,on_delete=models.SET_NULL,blank=True,null=True)
    tm_otd = models.TimeField(blank=True,null=True)
    iddokt = models.ForeignKey(Vra,on_delete = models.SET_NULL,blank=True,null=True,related_name='iddokt')
    otd = models.ForeignKey(otde,on_delete=models.SET_NULL,blank=T003,null=True)
    # prof_k = models.ForeignKey(V020,on_delete=models.SET_NULL,blank=True,null=True)
    icx = models.ForeignKey(V012,on_delete=models.SET_NULL,blank=True,null=True)
    pmg = models.ForeignKey(F003,on_delete=models.SET_NULL,blank=True,null=True,related_name='pmg')
    dsny = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='dsny')
    dsk = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='dsk')
    dskz = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='dskz')
    dsc = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='dsc')
    ds_osl = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='ds_osl')
    dson = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='dson')
    ksg_osn = models.ForeignKey(T006,on_delete=models.SET_NULL,blank=True,null=True,related_name='ksg_osn')
    ksg_sop = models.ForeignKey(T006,on_delete=models.SET_NULL,blank=True,null=True,related_name='ksg_sop')
    vid_hmp = models.CharField(max_length=30,blank=True,null=True)
    metod_hmp = models.CharField(max_length=30,blank=True,null=True)
    vb_s = models.ManyToManyField(Vb_s,blank=True)
    dspat = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='dspat')
    pri = models.ForeignKey(Prli,on_delete=models.SET_NULL,blank=True,null=True)
    trav = models.CharField(max_length=2,blank=True,null=True)
    le_vr = models.ManyToManyField(Le_Vr,blank=True)
    alg = models.CharField(max_length=1,blank=True,null=True)
    ps = models.CharField(max_length=1,blank=True,null=True)
    le_trv = models.ManyToManyField(Le_trv,blank=True)
    lv = models.IntegerField(blank=True,null=True)
    # oslo = models.ManyToManyField(Oslo,blank=True)
    oper = models.ManyToManyField(Oper,blank=True)
    manpy = models.ManyToManyField(Manpy,blank=True)
    disability = models.ForeignKey(Disability,on_delete=models.SET_NULL,blank=True,null=True)
    vds = models.ManyToManyField(Vds,blank=True)
    trs = models.ForeignKey(Trs,on_delete=models.SET_NULL,blank=True,null=True)
    rasx = models.CharField(max_length=1,choices=RASX_CHOICES,blank=True,null=True)
    tup = models.CharField(max_length=5,blank=True,null=True)
    dspo = models.CharField(max_length=60,blank=True,null=True)
    vr = models.CharField(max_length=5,blank=True,null=True)
    # dat_pe = models.DateField(blank=True,null=True)
    dat_s = models.DateField(blank=True,null=True)
    z_of = models.CharField(max_length=1,blank=True,null=True)
    otd_y = models.ForeignKey(otde,on_delete=models.SET_NULL,blank=True,null=True,related_name='otd_y')
    admt = models.CharField(max_length=2,blank=True,null=True)
    profz = models.CharField(max_length=3,blank=True,null=True)
    kod_otd = models.CharField(max_length=3,blank=True,null=True)
    osibka = models.CharField(max_length=1,blank=True,null=True)
    tipst = models.CharField(max_length=1,blank=True,null=True)
    tm = models.CharField(max_length=5,blank=True,null=True)
    wskr = models.CharField(max_length=1,choices=TIP_WSK_CHOICES,blank=True,null=True)
    rasxp = models.CharField(max_length=1,choices=RASX_CHOICES,blank=True,null=True)
    dat_ot = models.DateField(blank=True,null=True)
    tm_let = models.TimeField(blank=True,null=True)
    otm_tfoms = models.CharField(max_length=1,blank=True,null=True)
    otm_w = models.CharField(max_length=1,blank=True,null=True)
    dat_otd = models.DateField(blank=True,null=True)
    ds_oms = models.CharField(max_length=7,blank=True,null=True)
    check_tf = models.CharField(max_length=2,blank=True,null=True)
    dsc_r = models.CharField(max_length=7,blank=True,null=True)
    tnvr_r = models.CharField(max_length=5,blank=True,null=True)
    ds_let = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='ds_let')
    min_po = models.IntegerField(blank=True,null=True)
    n_ib = models.CharField(max_length=15,blank=True,null=True)
    npr_num = models.CharField(max_length=20,blank=True,null=True)
    npr_date = models.DateField(blank=True,null=True)
    ds_0 = models.ForeignKey(Ds,on_delete=models.SET_NULL,blank=True,null=True,related_name='ds_0')
    npl = models.CharField(max_length=1,blank=True,null=True)
    k_npl = models.DecimalField(decimal_places=4,max_digits=4,blank=True,null=True)
    nib_1c = models.CharField(max_length=20,blank=True,null=True)
    rslt = models.ForeignKey(V009,on_delete=models.SET_NULL,blank=True,null=True)
    p_per = models.CharField(max_length=1,blank=True,null=True)
    ds_onk = models.CharField(max_length=1,blank=True,null=True)
    onk_sl = models.OneToOneField(Onk_sl,on_delete=models.SET_NULL,blank=True,null=True)
    # ds1_t = models.CharField(max_length=2,blank=True,null=True)
    # stad = models.CharField(max_length=3,blank=True,null=True)
    # onk_t = models.CharField(max_length=3,blank=True,null=True)
    # onk_n = models.CharField(max_length=3,blank=True,null=True)
    # onk_m = models.CharField(max_length=3,blank=True,null=True)
    # mtstz = models.CharField(max_length=1,blank=True,null=True)
    b_diag = models.OneToOneField(B_diag,on_delete=models.SET_NULL,blank=True,null=True)
    # diag_tip = models.CharField(max_length=1,blank=True,null=True)
    # diag_code = models.CharField(max_length=20,blank=True,null=True)
    # diag_rslt = models.CharField(max_length=20,blank=True,null=True)
    b_prot = models.OneToOneField(B_prot,on_delete=models.SET_NULL,blank=True,null=True)
    # prot = models.CharField(max_length=20,blank=True,null=True)
    # d_prot = models.DateField(blank=True,null=True)
    cons = models.OneToOneField(Cons,on_delete=models.SET_NULL,blank=True,null=True)
    # dt_cons = models.DateField(blank=True,null=True)
    # pr_cons = models.CharField(max_length=20,blank=True,null=True)
    onk_usl = models.OneToOneField(Onk_usl,on_delete=models.SET_NULL,blank=True,null=True)
    # usl_tip = models.CharField(max_length=20,blank=True,null=True)
    # hir_tip = models.CharField(max_length=20,blank=True,null=True)
    c_zab = models.ForeignKey(V027,on_delete=models.SET_NULL,blank=True,null=True)
    sumv = models.DecimalField(decimal_places=13,max_digits=13,blank=True,null=True)
    onk_1_2 = models.CharField(max_length=1,blank=True,null=True)
    # diag_date = models.DateField(blank=True,null=True)
    gwf = models.IntegerField(blank=True,null=True)
    u_gwf = models.CharField(max_length=1,blank=True,null=True)
    sofa = models.CharField(max_length=1,blank=True,null=True)
    iwl = models.CharField(max_length=1,blank=True,null=True)
    ksg_kpg = models.ManyToManyField(Ksg_kpg,blank=True,null=True)
    # ksg_in = models.CharField(max_length=8,blank=True,null=True)
    # ksg_ins = models.CharField(max_length=8,blank=True,null=True)
    napr = models.OneToOneField(Napr,on_delete=models.SET_NULL,blank=True,null=True)
    # napr_mo = models.CharField(max_length=8,blank=True,null=True)
    # napr_v = models.CharField(max_length=1,blank=True,null=True)
    # napr_usl = models.CharField(max_length=20,blank=True,null=True)
    # napr_issl = models.CharField(max_length=2,blank=True,null=True)
    adr_fakt = models.CharField(max_length=100,blank=True,null=True)
    # docdate= models.DateField(blank=True,null=True)
    #docorg = models.CharField(max_length=100,blank=True,null=True)
    vb_a = models.OneToOneField(Vb_a,on_delete=models.SET_NULL,blank=True,null=True)

    def wskr_display(self):
        return self.get_wskr_display()
    
    def rasxp_display(self):
        return self.get_rasxp_display()

class Patient_P(models.Model):
    #Сведения о представителе пациента
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    fam_p = models.CharField(max_length=80,blank=True,null=True)
    im_p = models.CharField(max_length=80,blank=True,null=True)
    ot_p = models.CharField(max_length=80,blank=True,null=True)
    pol = models.ForeignKey(V005,on_delete=models.SET_NULL,blank=True,null=True)
    datr = models.DateField(blank=True,null=True)
    s_pasp = models.CharField(max_length=10,blank=True,null=True)
    n_pasp = models.CharField(max_length=20,blank=True,null=True)
    m_roj = models.CharField(max_length=200,blank=True,null=True)
    udl_p = models.ForeignKey(F011,on_delete=models.SET_NULL,blank=True,null=True)
    sp_pasp = models.CharField(max_length=10,blank=True,null=True)
    np_pasp = models.CharField(max_length=20,blank=True,null=True)
    skom_p = models.ForeignKey(Skom,on_delete=models.SET_NULL,blank=True,null=True)
    stat_p = models.ForeignKey(F008,on_delete=models.SET_NULL,blank=True,null=True)
    s_pol = models.CharField(max_length=25,blank=True,null=True)
    n_pol = models.CharField(max_length=25,blank=True,null=True)
    sex = models.CharField(max_length=1,blank=True,null=True)
    dr = models.DateField(blank=True,null=True)
    udl = models.CharField(max_length=2,blank=True,null=True)

class Patient(models.Model):
    #Сведения о пациенте
    RPR_CHOICES = [
        ('1','Центральный АО'),
        ('2','Ленинский АО'),
        ('3','Калининский АО'),
        ('4','Восточный АО')
    ]
    id = models.BigAutoField(primary_key=True)
    id_pac = models.CharField(max_length=50,blank=True,null=True,db_index=True)
    fam = models.CharField(max_length=80,blank=True,null=True)
    im = models.CharField(max_length=80,blank=True,null=True)
    ot = models.CharField(max_length=80,blank=True,null=True)
    pol = models.ForeignKey(V005,on_delete=models.SET_NULL,blank=True,null=True)
    datr = models.DateField(blank=True,null=True)
    vs = models.IntegerField(blank=True,null=True)
    nvs = models.CharField(max_length=1,blank=True,null=True)
    udl = models.ForeignKey(F011,on_delete=models.SET_NULL,blank=True,null=True)
    s_pasp = models.CharField(max_length=10,blank=True,null=True)
    n_pasp = models.CharField(max_length=20,blank=True,null=True)
    docdate= models.DateField(blank=True,null=True)
    docorg = models.CharField(max_length=100,blank=True,null=True)
    ss = models.CharField(max_length=14,blank=True,null=True)
    c_oksm = models.ForeignKey(Oksm,on_delete=models.SET_NULL,blank=True,null=True)
    adr = models.CharField(max_length=200,blank=True,null=True)
    # rai = models.CharField(max_length=1,blank=True,null=True)
    rkod = models.CharField(max_length=1,blank=True,null=True)
    ylc = models.CharField(max_length=25,blank=True,null=True)
    dom = models.CharField(max_length=7,blank=True,null=True)
    kv= models.CharField(max_length=7,blank=True,null=True)
    kp = models.CharField(max_length=10,blank=True,null=True)
    stro = models.CharField(max_length=10,blank=True,null=True)
    m_roj = models.CharField(max_length=200,blank=True,null=True)
    rai = models.CharField(max_length=1,choices=RPR_CHOICES,blank=True,null=True)
    cj = models.ForeignKey(CJ,on_delete=models.SET_NULL,blank=True,null=True)
    v_lgoty = models.ForeignKey(V_LGOTY,on_delete=models.SET_NULL,blank=True,null=True)
    in_t = models.ForeignKey(T004,on_delete=models.SET_NULL,blank=True,null=True)
    rab = models.CharField(max_length=200,blank=True,null=True)
    r_n = models.ForeignKey(Rab_Ner,on_delete=models.SET_NULL,blank=True,null=True)
    prof = models.CharField(max_length=150,blank=True,null=True)
    vec = models.DecimalField(decimal_places=2,max_digits=5,blank=True,null=True)
    patient_p = models.OneToOneField(Patient_P,on_delete=models.SET_NULL,blank=True,null=True)
    sluchay = models.ManyToManyField(Sluchay,blank=True)
    # vb_s = models.ManyToManyField(Vb_s,blank=True)
    # vds = models.ManyToManyField(Vds,blank=True)
    # oper = models.ManyToManyField(Oper,blank=True)
    # le_vr = models.ManyToManyField(Le_Vr,blank=True)
    # le_trv = models.ManyToManyField(Le_trv,blank=True)
    # manpy = models.ManyToManyField(Manpy,blank=True)
    # trs = models.ForeignKey(Trs,on_delete=models.SET_NULL,blank=True,null=True)
    # disability = models.ForeignKey(Disability,on_delete=models.SET_NULL,blank=True,null=True)
    r_name = models.CharField(max_length=30,blank=True,null=True)
    np_name = models.CharField(max_length=30,blank=True,null=True)
    gor_name = models.CharField(max_length=30,blank=True,null=True)
    ul_name = models.CharField(max_length=30,blank=True,null=True)
    cod_adr = models.CharField(max_length=30,blank=True,null=True)
    datnp = models.DateField(blank=True,null=True)
    datkp = models.DateField(blank=True,null=True)
    reg_name = models.CharField(max_length=30,blank=True,null=True)
    
    def __str__(self):
        return str(self.sluchay.values('nib')[0]['nib'])
    
    def rai_display(self):
        return self.get_rai_display()

    

