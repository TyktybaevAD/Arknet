from okb2.models import (V005, otde, Rab_Ner, T004, F003, Vrzb, Oksm,Ds,
                         V012,V009,V020,Vra,V021,PR_OSOB,V001,T006,Ab_Obsh,
                         V001,Pope,Ab_Obsh,Prli,Trv,Isfin,Skom,F008,F011,
                         N018,N002,N003,N004,N005)


class Directory:

    def get_v005(self):
        return list(map(lambda w: w[0], V005.objects.values_list('polname')))

    def get_otde(self):
        return list(map(lambda o: o[0], otde.objects.values_list('naim')))

    def get_rab_ner(self):
        return list(map(lambda t: t[0], Rab_Ner.objects.values_list('naim')))

    def get_t004(self):
        return list(map(lambda s: s[0], T004.objects.values_list('name')))

    def get_F003(self):
        return list(map(lambda l: l[0], F003.objects.values_list('naim')))

    def get_vrzb(self):
        return list(map(lambda l: l[0], Vrzb.objects.values_list('naim')))

    def get_oksm(self):
        return list(map(lambda o: o[0], Oksm.objects.values_list('naim')))

    def get_ds(self,kod=None):
         return list(map(lambda v: v[0],Ds.objects.values_list('kod').filter(kod__icontains=kod)[:10]))
    
    def get_ds_naim(self,kod=None):
        try:
            return Ds.objects.values('naim').filter(kod=kod)[0]['naim']
        except IndexError:
            return None


        # return dict(Ds.objects.values_list('kod','naim').filter(kod__icontains=kod)[:10])
        # return dict(map(lambda v: v,Ds.objects.values_list('kod','naim').filter(kod__icontains=kod)[:10]))
        # return dict(map(lambda v: v,Ds.objects.values_list('kod','naim')[:10]))
        # # return Ds.objects.values('kod','naim').filter(kod__istartswith='S')
        # return dict(map(lambda v: v,Ds.objects.values_list('kod','naim').filter(kod__icontains=kod)[:10]))
    
    def get_v012(self):
        return list(map(lambda v: v[0], V012.objects.values_list('iz_name')))
    

    def get_v009(self):
        return list(map(lambda v: v[0], V009.objects.values_list('tip_name')))
    
    def get_v020(self):
        return list(map(lambda v: v[0], V020.objects.values_list('k_prname')))
    #  Недоделано
    def get_vra(self):
        return list(map(lambda v: v[0],Vra.objects.values_list('kod')[:10]))
    
    def get_vra_name_spec(self,kod):
        spec_naim = []
        vra = Vra.objects.values('naim','v021').filter(kod=kod).distinct()
        spec_kod = [v['v021'] for v in vra]
        for s in range(len(spec_kod)):
            try:
                spec_naim.append(V021.objects.values('postname').filter(id_spec=spec_kod[s],dateend=None)[0]['postname'])
            except IndexError:
                 spec_naim.append(None)
        rez = {}
        try:
            rez['naim'] = vra[0]['naim']
        except IndexError:
            rez['naim'] = None
        rez['spec'] = spec_naim
        return rez
    
    def get_pr_osob(self):
        return list(PR_OSOB.objects.values_list('kod','naim').order_by('-kod'))
    
    def get_v001(self):
        return list(V001.objects.values_list('kod').order_by('kod'))
    
    def get_t006(self):
        return list(map(lambda v: v[0], T006.objects.values_list('ksg')))

    def get_ab_obsh(self):
        return list(map(lambda v: v[0],Ab_Obsh.objects.values_list('kod')))
    
    def get_name_v001(self,kod):
        try:
            return V001.objects.values('naim').filter(kod = kod)[0]['naim']
        except IndexError:
            return None
    
    def get_name_pope(self):
        return list(map(lambda v: v[0],Pope.objects.values_list('kod')))
    
    def get_osl_naim(self,kod):
        try:
            return Pope.objects.values('naim').filter(kod = kod)[0]['naim']
        except IndexError:
            return None
    
    def ab_obsh_name(self,kod):
        try:
            return Ab_Obsh.objects.values('ima').filter(kod=kod)[0]['ima']
        except IndexError:
            return None
    
    def get_prli(self):
        return list(map(lambda v: v[0],Prli.objects.values_list('naim')))
    
    def get_trv(self):
        return list(map(lambda v: v[0],Trv.objects.values_list('naim')))
    
    def get_isfin(self):
        return list(map(lambda v: v[0],Isfin.objects.values_list('naim')))
    
    def get_skom(self):
        return list(map(lambda v: v[0],Skom.objects.values_list('naim')))
    
    def get_f008(self):
        return list(map(lambda v: v[0],F008.objects.values_list('tip_name')))
    
    def get_f011(self):
        return list(map(lambda v: v[0],F011.objects.values_list('docname')))
    
    def get_n018(self):
        return list(map(lambda v:v[0],N018.objects.values_list('reas_name')))
    # Поправить С диагнозом если если диагноз Онко то выводим 
    #__icontains
    def get_n002(self,kod):
        return list(max(lambda v:v[0],N002.objects.values_list('kod_st').filter(ds_st=kod)))

    def get_n003(self,kod):
        return list(max(lambda v:v[0],N003.objects.values_list('kod_t').filter(ds_t=kod)))
    def get_n004(self,kod):
        return list(max(lambda v:v[0],N004.objects.values_list('kod_n').filter(ds_n=kod)))
    def get_n005(self,kod):
        return list(max(lambda v:v[0],N005.objects.values_list('kod_m').filter(ds_m=kod)))