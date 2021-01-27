from hospital.models import (Sluchay, Patient, otde, V020, Le_Vr, Oper,
                             V001, Vra, Oslo,Manpy,Vb_s,Le_trv,Vds,Vb_a)
import datetime


class History:
    def __init__(self, history, date_z_1):
        self.history = history
        self.date_z_1 = date_z_1

    def get_History_data(self):
        data = dict()
        sluchay = Sluchay.objects.get(
            nib__icontains=self.history, datp__icontains=self.date_z_1)
        patient = Patient.objects.get(id_pac=sluchay.id_pac)
        # Шапка
        data['history'] = self.history
        data['fam'] = patient.fam if patient.fam != None else None
        data['im'] = patient.im if patient.im != None else None
        data['ot'] = patient.ot if patient.ot != None else None
        data['pol'] = patient.pol.polname if patient.pol != None else None
        data['datp'] = self.format_date(
            str(sluchay.datp)) if sluchay.datp != None else None
        data['tm_otd'] = sluchay.tm_otd if sluchay.tm_otd != None else None
        data['datv'] = self.format_date(
            str(sluchay.datv)) if sluchay.datv != None else None
        data['datr'] = self.format_date(
            str(patient.datr)) if patient.datr != None else None
        ###

        # Персональные данные
        data['otd'] = sluchay.otd.naim if sluchay.otd != None else None
        data['vec'] = patient.vec if patient.vec != None else None
        # data['m_roj'] = patient.m_roj if patient.m_roj != None else None
        # data['adr'] = patient.adr if patient.adr != None else None
        data['rab'] = patient.rab if patient.rab != None else None
        data['prof'] = patient.prof if patient.prof != None else None
        data['r_n'] = patient.r_n.naim if patient.r_n != None else None
        data['in_t'] = patient.in_t.name if patient.in_t != None else None
        data['lpy'] = sluchay.lpy.naim if sluchay.lpy != None else None
        data['goc'] = sluchay.goc.tip_name if sluchay.goc != None else None
        data['prpg'] = sluchay.prpg.naim if sluchay.prpg != None else None
        data['vrez'] = sluchay.vrez.naim if sluchay.vrez != None else None
        ##

        # Адрес
        data['c_oksm'] = patient.c_oksm.naim if patient.c_oksm != None else None

        # 2.Сведения о диагнозах
        data['dsny'] = {'kod': sluchay.dsny.kod,
                        'naim': sluchay.dsny.naim} if sluchay.dsny != None else None
        data['ds_0'] = {'kod':sluchay.ds_0.kod if sluchay.ds_0 != None else None ,
                        'naim':sluchay.ds_0.naim if sluchay.ds_0 != None else None } 
        data['dsk'] = {'kod': sluchay.dsk.kod,
                       'naim': sluchay.dsk.naim} if sluchay.dsk != None else None
        data['dskz'] = {'kod': sluchay.dskz.kod,
                        'naim': sluchay.dskz.naim} if sluchay.dskz != None else None
        data['ds_osl'] = {'kod': sluchay.ds_osl.kod,
                          'naim': sluchay.ds_osl.naim} if sluchay.ds_osl != None else None
        data['dsc'] = {'kod': sluchay.dsc.kod,
                       'naim': sluchay.dsc.naim} if sluchay.dsc != None else None
        data['dson'] = {'kod': sluchay.dson.kod,
                        'naim': sluchay.dson.naim} if sluchay.dson != None else None
        data['icx'] = sluchay.icx.iz_name if sluchay.icx != None else None
        ##

        # 3.Койко-дни
        if sluchay.le_vr != None:
            le_vr_obj = Le_Vr.objects.get(
                id=sluchay.le_vr.values('id')[0]['id'])
            le_vr = {}
            le_vr['N'] = str(sluchay.datv - sluchay.datp).split(' ')[0] if (
                sluchay.datv != None) and (sluchay.datp != None) else None
            le_vr['aro'] = None
            le_vr['otd'] = sluchay.otd.naim if sluchay.otd != None else None
            le_vr['prof_k'] = le_vr_obj.prof_k.k_prname if le_vr_obj.prof_k != None else None
            le_vr['kod'] = le_vr_obj.kod.kod if le_vr_obj.kod != None else None
            le_vr['naim'] = le_vr_obj.kod.naim if le_vr_obj.kod != None else None
            le_vr['spec'] = le_vr_obj.kod.n_spec if le_vr_obj.kod != None else None
            data['le_vr'] = le_vr
        else:
            data['le_vr'] = None

        # 4.Операции
        oper_list = []
        if sluchay.oper != None:
            oper = list(map(lambda o: o, sluchay.oper.values('id')))
            for o in range(len(oper)):
                oper_d = {}
                obj = Oper.objects.get(id=oper[o]['id'])
                oper_d['dato'] = self.format_date(str(obj.dato)) if obj.dato != None else None
                oper_d['tm_o'] = obj.tm_o if obj.tm_o != None else None
                oper_d['py'] = obj.py.kod if obj.py != None else None
                oper_d['kod_op'] = obj.kod_op.kod if obj.kod_op != None else None
                if obj.kod_op != None:
                    try:
                        oper_d['kod_op_name'] = V001.objects.values(
                            'naim').filter(kod=obj.kod_op.kod)[0]['naim']
                    except IndexError:
                        oper_d['kod_op_name'] = None
                else:
                    oper_d['kod_op_name'] = None
                oper_d['goc'] = obj.goc.id_tip if obj.goc != None else None
                oper_d['kodx'] = obj.kodx.kod if obj.kodx != None else None
                if obj.kodx != None:
                    try:
                        oper_d['kodx_naim'] = Vra.objects.values(
                            'naim').filter(kod=obj.kodx.kod)[0]['naim']
                    except IndexError:
                        oper_d['kodx_naim'] = None
                else:
                    oper_d['kodx_naim'] = None

                oper_list.append(oper_d)
                # oper_d['pop'] = obj.pop. if obj.pop != None else None

                if obj.pop != None:
                    if obj.pop:
                        oper_d['pop'] = 'Да'
                    else:
                        oper_d['pop'] = 'Нет'
                else:
                    oper_d['pop'] = 'Неизвестно'

                # oper_d['pr_osob'] = obj.pr_osob.all() if obj.pr_osob != None else None
                try:
                    oper_d['pr_osob'] = list(
                        map(lambda p: p[0], obj.pr_osob.values_list('kod')))
                    if len(oper_d['pr_osob']) == 0:
                        oper_d['pr_osob'] = []
                except (AttributeError, IndexError):
                    oper_d['pr_osob'] = []

                oper_d['k_mm'] = obj.k_mm if obj.k_mm != None else None
                oper_d['kodxa'] = obj.kodxa.kod if obj.kodxa != None else None
                oper_d['kodxa1'] = obj.kodxa1.kod if obj.kodxa1 != None else None
                oper_d['obz'] = obj.obz.kod if obj.obz != None else None
                oper_d['kodan'] = obj.kodan.kod if obj.kodan != None else None

            data['oper'] = oper_list
        else:
            data['oper'] = None

        # 5.Клинико-стат.гр.заболев-я
        data['ksg_osn'] = sluchay.ksg_osn.ksg if sluchay.ksg_osn != None else None
        data['ksg_sop'] = sluchay.ksg_sop.ksg if sluchay.ksg_sop != None else None
        data['iddoc'] = sluchay.iddokt.kod if sluchay.iddokt != None else None

        # 6.Oсложнение
        oslo_list = []
        # print(oper)
        for o in range(len(oper)):
            op = Oper.objects.get(id=oper[o]['id'])
            oslo_values = op.oslo.values('id')
            if len(oslo_values) != 0:
                for os in range(len(oslo_values)):
                    oslo_d = {}
                    obj_oslo = Oslo.objects.get(id=oslo_values[os]['id'])
                    # print(op.dato,obj_oslo.osl.naim)
                    oslo_d['inf_oper'] = (self.format_date(str(op.dato)) if op.dato != None else None) + ' '+ (str(op.kod_op.kod) if op.kod_op != None else None)
                    # oslo_d['dato_oper'] = op.dato if op.dato != None else None
                    # oslo_d['kod_op_oper'] = op.kod_op.kod if op.kod_op != None else None
                    oslo_d['tnvr'] = obj_oslo.tnvr.kod if obj_oslo.tnvr != None else None
                    oslo_d['tnvr_fio'] = obj_oslo.tnvr.naim if obj_oslo.tnvr != None else None
                    oslo_d['dato'] = self.format_date(str(obj_oslo.dato)) if obj_oslo.dato != None else None
                    oslo_d['osl'] = obj_oslo.osl.kod if obj_oslo.osl != None else None
                    oslo_d['osl_naim'] = obj_oslo.osl.naim if obj_oslo.osl != None else None
                    oslo_d['xosl'] = obj_oslo.xosl.naim if obj_oslo.xosl != None else None
                    oslo_d['posl'] = obj_oslo.posl.naim if obj_oslo.posl != None else None
                    oslo_d['aosl'] = obj_oslo.aosl.naim if obj_oslo.aosl != None else None
                    oslo_list.append(oslo_d)
            else:
                continue
            
        if len(oslo_list) != 0:
           data['oslo'] = oslo_list
        else:
            data['oslo'] = None
        
        #7.Трудоспособность
        data['trs'] = sluchay.trs.naim if sluchay.trs != None else None

        #8.Манипуляции
        manpys_list = []
        manpys = sluchay.manpy.values('id') if sluchay.manpy != None else None
        for m in range(len(manpys)):
            obj = Manpy.objects.get(id=manpys[m]['id'])
            manpys_d = {}
            manpys_d['datm'] = self.format_date(str(obj.datm)) if obj.kodmn != None else None
            manpys_d['tnvr'] = obj.tnvr.kod if obj.tnvr != None else None
            manpys_d['tnvr_fam'] = obj.tnvr.naim if obj.tnvr != None else None
            manpys_d['kodmn'] = obj.kodmn.kod if obj.kodmn != None else None
            manpys_d['kodmn_naim'] = obj.kodmn.ima if obj.kodmn != None else None
            manpys_d['kol'] = obj.kol if obj.kol != None else None
            manpys_d['pl'] = obj.pl_display() if obj.pl_display() != None else None
            
            manpys_list.append(manpys_d)
        if len(manpys_list) >0:
            data['manpys'] = manpys_list
        else:
             data['manpys'] = None
        
        #9.Переводы
        if sluchay.vb_s != None:
            try:
                vb_s = Vb_s.objects.get(id=sluchay.vb_s.values('id')[0]['id'])
                data['kod_y'] = vb_s.kod_y.naim if vb_s.kod_y != None else None
                data['pr_per'] = vb_s.pr_per.naim if vb_s.pr_per != None else None
                data['dat_pe'] = self.format_date(str(vb_s.dat_pe)) if vb_s.dat_pe != None else None
                data['potd'] = vb_s.potd.naim if vb_s.potd != None else None
                data['vb_s_datv'] = self.format_date(str(vb_s.datv)) if vb_s.datv != None else None
            except IndexError:
                data['kod_y'] = None
                data['pr_per'] = None
                data['dat_pe'] = None
                data['potd'] = None
                data['vb_s_datv'] = None
        else:
            data['kod_y'] = None
            data['pr_per'] = None
            data['dat_pe'] = None
            data['potd'] = None
            data['vb_s_datv'] = None
        
        # if vb_s != None:
        #     data['kod_y'] = vb_s.kod_y.naim if vb_s.kod_y != None else None
        #     data['pr_per'] = vb_s.pr_per.naim if vb_s.pr_per != None else None
        #     data['dat_pe'] = self.format_date(str(vb_s.dat_pe)) if vb_s.dat_pe != None else None
        #     data['potd'] = vb_s.potd.naim if vb_s.potd != None else None
        #     data['vb_s_datv'] = self.format_date(str(vb_s.datv)) if vb_s.datv != None else None
        # else:
        #     data['kod_y'] = None
        #     data['pr_per'] = None
        #     data['dat_pe'] = None
        #     data['potd'] = None
        #     data['vb_s_datv'] = None
        
        #A.Патанатомический Ds
        data['tm_let'] = sluchay.tm_let if sluchay.tm_let != None else None
        data['pri'] = sluchay.pri.naim if sluchay.pri != None else None
        data['ds_let'] = sluchay.ds_let.kod if sluchay.ds_let != None else None
        data['ds_let_naim'] = sluchay.ds_let.naim if sluchay.ds_let != None else None
        data['wskr']  = sluchay.wskr_display() if sluchay.wskr_display() != None else None
        data['dspat'] = sluchay.dspat.kod if sluchay.dspat != None else None
        data['dspat_naim'] = sluchay.dspat.naim if sluchay.dspat != None else None
        data['rasxp'] = sluchay.rasxp_display() if sluchay.rasxp_display() != None else None
        data['otd_y'] = sluchay.otd_y.naim if sluchay.otd_y != None else None

        #B.Сведения о травмах
        if sluchay.le_trv != None:
            
            le_trv = Le_trv.objects.get(id=sluchay.le_trv.values('id')[0]['id'])
            data['details'] = le_trv.details.kod if le_trv.details != None else None
            data['details_name'] = le_trv.details.naim if le_trv.details != None else None
            data['t_trv'] = le_trv.t_trv.naim if le_trv.t_trv != None else None
            if le_trv.trav_ns:
                data['trav_ns'] = 'Да'
            elif  le_trv.trav_ns == False:
                data['trav_ns'] = 'Нет'
            else:
                data['trav_ns'] = None
        else:
            data['details'] = None
            data['details_name'] = None
            data['t_trv'] = None
            data['trav_ns'] = None
        

        #C.Полис/Документ/Снилс
        if sluchay.vds != None:
            try:
                #Полис
                vds = Vds.objects.get(id=sluchay.vds.values('id')[0]['id'])
                data['vds'] = vds.vds.naim if vds.vds != None else None
                data['sctp'] = vds.sctp
                data['nctp'] = vds.nctp
                data['ctkom'] = vds.ctkom.naim if vds.ctkom != None else None
                data['t_pol'] = vds.t_pol.tip_name if vds.t_pol != None else None
                #Документ
                data['udl'] = patient.udl.docname if patient.udl != None else None
                data['s_pasp'] = patient.s_pasp
                data['n_pasp'] = patient.n_pasp
                data['docdate'] = patient.docdate
                data['docorg'] = patient.docorg
                data['m_roj'] = patient.m_roj
                # if patient.m_roj != None:
                #     if (patient.m_roj.find(',') != -1) and (patient.m_roj.rfind(',') != -1):
                #         data['m_roj_list'] = patient.m_roj.split(',')
                #     else:
                #         data['m_roj_list'] = patient.m_roj.split('.')
                # else:
                #     pass
                # print(data['m_roj_list'])
                #Снилс
                data['ss'] = patient.ss
            except IndexError:
                data['vds'] = None
                data['sctp'] = None
                data['nctp'] = None
                data['ctkom'] = None
                data['t_pol'] = None

                data['udl'] = None
                data['s_pasp'] = None
                data['n_pasp'] = None
                data['docdate'] = None
                data['docorg'] = None
                data['m_roj'] = None

                data['ss'] = None
        else:
            data['vds'] = None
            data['sctp'] = None
            data['nctp'] = None
            data['ctkom'] = None
            data['t_pol'] = None
            data['udl'] = None
            data['s_pasp'] = None
            data['n_pasp'] = None
            data['docdate'] = None
            data['docorg'] = None
            data['m_roj'] = None
            data['ss'] = None
        

        #D.Прерывание беременности

        if sluchay.vb_a != None:
            data['vb_a_datv'] = self.format_date(str(sluchay.vb_a.datv)) if sluchay.vb_a.datv != None else None
            data['srber'] = sluchay.vb_a.srber
            data['n_ber'] = sluchay.vb_a.n_ber
            data['pria'] = sluchay.vb_a.pria.naim if sluchay.vb_a.pria != None else None
            data['m_prer'] = sluchay.vb_a.m_prer.naim if sluchay.vb_a.m_prer != None else None
        else:
            data['vb_a_datv'] = None
            data['srber'] = None
            data['n_ber'] = None
            data['pria'] = None
            data['m_prer'] = None

        #F.Представитель пациента
        
        if patient.patient_p != None:
            data['fam_p'] = patient.patient_p.fam_p
            data['im_p'] = patient.patient_p.im_p
            data['ot_p'] = patient.patient_p.ot_p
            data['sex_bol'] = patient.patient_p.pol.polname if patient.patient_p.pol != None else None
            data['mp_roj'] = patient.patient_p.m_roj
            data['udl_p'] = patient.patient_p.udl_p.docname if patient.patient_p.udl_p != None else None
            data['sp_pasp'] = patient.patient_p.sp_pasp
            data['np_pasp'] = patient.patient_p.np_pasp
            data['skom_p'] = patient.patient_p.skom_p.naim if patient.patient_p.skom_p != None else None
            data['stat_p'] = patient.patient_p.stat_p.tip_name if patient.patient_p.stat_p != None else None
            data['s_pol'] = patient.patient_p.s_pol
            data['n_pol'] = patient.patient_p.n_pol
        else:
            data['fam_p'] = None
            data['im_p'] = None
            data['ot_p'] = None
            data['sex_bol'] = None
            data['mp_roj'] = None
            data['udl_p'] = None
            data['sp_pasp'] = None
            data['np_pasp'] = None
            data['skom_p'] = None
            data['stat_p'] = None
            data['s_pol'] = None
            data['n_pol'] = None
        
        #E.Лист нетрудоспособности
        if sluchay.disability != None:
            data['dat_l1'] = self.format_date(str(sluchay.disability.dat_l1)) if sluchay.disability.dat_l1 != None else None
            data['dat_l2'] = self.format_date(str(sluchay.disability.dat_l2)) if sluchay.disability.dat_l2 != None else None
            data['ot_ln'] = sluchay.disability.ot_ln
            data['vs_bol'] = sluchay.disability.vs_bol
            data['dis_sex_bol'] = sluchay.disability.sex_bol.polname if sluchay.disability.sex_bol != None else None
        else:
            data['dat_l1'] = None
            data['dat_l2'] = None
            data['ot_ln'] = None
            data['vs_bol'] = None
            data['dis_sex_bol'] = None
        
        #G.Адрес проживания
        data['m_roj'] = patient.m_roj 
        data['adr'] = patient.adr 
        data['kv'] = patient.kv
        data['kp'] = patient.kp
        data['stro'] = patient.stro
        data['cj'] = patient.cj.naim if patient.cj != None else None
        data['rai'] = patient.rai_display() if patient.rai != None else None


        #J.Карта онкобольного
        if sluchay.onk_sl != None:
            data['ds1_t'] = sluchay.onk_sl.ds1_t.reas_name if sluchay.onk_sl.ds1_t != None else None
            data['stad'] = sluchay.onk_sl.stad.kod_st if sluchay.onk_sl.stad != None else None
            data['onk_t'] = sluchay.onk_sl.onk_t.kod_t if sluchay.onk_sl.onk_t != None else None
            data['onk_n'] = sluchay.onk_sl.onk_n.kod_n if sluchay.onk_sl.onk_n != None else None
            data['onk_m'] = sluchay.onk_sl.onk_m.kod_m if sluchay.onk_sl.onk_m != None else None
            data['mtstz'] = sluchay.onk_sl.mtstz.n_cz if sluchay.onk_sl.mtstz != None else None
        else:
            data['ds1_t'] = None
            data['stad'] = None
            data['onk_t'] = None
            data['onk_n'] = None
            data['onk_m'] = None
            data['mtstz'] = None
        data['c_zab'] = sluchay.c_zab.n_cz if sluchay.c_zab != None else None

        if sluchay.b_diag != None:
            data['diag_date'] = self.format_date(str(sluchay.b_diag.diag_date)) if sluchay.b_diag.diag_date != None else None
            data['diag_tip'] = sluchay.b_diag.diag_tip_display() if sluchay.b_diag.diag_tip != None else None
            data['diag_code'] = sluchay.b_diag.diag_code
            data['diag_rslt'] = sluchay.b_diag.diag_rslt
            data['rec_rslt'] = sluchay.b_diag.rec_rslt
        else:
            data['diag_date'] = None
            data['diag_tip'] = None
            data['diag_code'] = None
            data['diag_rslt'] = None
            data['rec_rslt'] = None
        
        if sluchay.cons != None:
            data['pr_cons'] = sluchay.cons.pr_cons.cons_name if sluchay.cons.pr_cons != None else None
            data['dt_cons'] = self.format_date(str(sluchay.cons.dt_cons)) if sluchay.cons.dt_cons != None else None
        else:
            data['pr_cons'] = None
            data['dt_cons'] = None
        
        if sluchay.onk_usl != None:
            data['usl_tip'] = sluchay.onk_usl.usl_tip.tlech_name if sluchay.onk_usl.usl_tip != None else None
            data['hir_tip'] = sluchay.onk_usl.hir_tip.thir_name if sluchay.onk_usl.hir_tip != None else None
        else:
            data['usl_tip'] = None
            data['hir_tip'] = None

        if sluchay.b_prot != None:
            data['prot'] = sluchay.b_prot.prot.prot_name if sluchay.b_prot.prot != None else None
            data['d_prot'] = self.format_date(str(sluchay.b_prot.d_prot)) if sluchay.b_prot.d_prot != None else None
        else:
            data['prot'] = None
            data['d_prot'] = None
        
        if sluchay.napr != None:
            data['naprdate'] = self.format_date(str(sluchay.napr.naprdate)) if sluchay.napr.naprdate != None else None
            data['napr_mo'] = sluchay.napr.napr_mo.naim if sluchay.napr.napr_mo != None else None
            data['napr_v'] = sluchay.napr.napr_v.n_vn if sluchay.napr.napr_v != None else None
            data['napr_issl'] = sluchay.napr.napr_issl.n_met if sluchay.napr.napr_issl != None else None
            data['napr_usl'] = sluchay.napr.napr_usl.kod if sluchay.napr.napr_usl != None else None
        else:
            data['naprdate'] = None
            data['napr_mo'] = None
            data['napr_v'] = None
            data['napr_issl'] = None
            data['napr_usl'] = None
        
        #K.Мо прикрепления
        data['pmg'] = sluchay.pmg.naim if sluchay.pmg != None else None 

        return data

    def format_date(self, date):
        if date != 'None':
            y, m, d = date.split('-')
            date = '{}-{}-{}'.format(d, m, y)
            return date
        return None
