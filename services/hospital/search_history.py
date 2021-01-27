from hospital.models import Sluchay,Patient 

class Search_history:
    def __init__(self,history):
        self.history = history
        
    def get_history(self):
        data = dict()
        history = list()
        sl = Sluchay.objects.values('id_pac').filter(nib__icontains=self.history)
        for s in range(len(sl)):
            data.clear()
            patient = Patient.objects.get(id_pac=sl[s]['id_pac'])
            data['nhistory']=patient.sluchay.values('nib')[0]['nib']
            data['fam']=patient.fam
            data['im']=patient.im
            data['ot']=patient.ot
            data['dr']=patient.datr
            data['date_z_1']=patient.sluchay.values('datp')[0]['datp']
            history.append(data.copy())         
        return history

           





