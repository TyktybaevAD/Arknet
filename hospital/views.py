from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
from .models import Load_1c
from .forms import Load_1c_forms
from services.hospital.insert_to_hospital_in_1c import InsertHospital
from services.hospital.search_history import Search_history
from services.hospital.history import History
from services.hospital.directory import Directory
from okb2.models import Ds


class index(View):
    def get(self, request):
        return render(request, 'hospital_index.html')

    def post(self, request):
        if request.POST.get('type') == 'get_user':
            return JsonResponse({'user': request.user.id})
        elif request.POST.get('type') == 'load_fales':
            Load_1c.objects.filter(user=request.user.id).delete()
            form = Load_1c_forms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'goods'}, status=200)
            else:
                return JsonResponse({'message': 'errors'}, status=200)
        elif request.POST.get('type') == 'processing_file':
            IH = InsertHospital(request)
            rez = IH.get_rez()
            return JsonResponse({'rez': rez})


class search(View):
    def get(self, request):
        return render(request, 'search_history.html')

    def post(self, request):
        init_dir = Directory()
        if request.POST.get('type') == 'search':
            history_list = Search_history(request.POST.get('history'))
            rez = history_list.get_history()
            return JsonResponse({'rez': rez})

        elif request.POST.get('type') == 'data_history':
            print('get_history')
            history = request.POST.get('history')
            date_z_1 = request.POST.get('date_z_1')
            h = History(history,date_z_1)
            rez = h.get_History_data()
            return JsonResponse({'rez': rez})

        elif request.POST.get('type') == 'auto-complate-w':
            return JsonResponse({'rez': init_dir.get_v005()})

        elif request.POST.get('type') == 'auto-complate-otde':
            return JsonResponse({'rez': init_dir.get_otde()})

        elif request.POST.get('type') == 'auto-complate-rab_ner':
            return JsonResponse({'rez': init_dir.get_rab_ner()})

        elif request.POST.get('type') == 'auto-complate-in_t':
            return JsonResponse({'rez': init_dir.get_t004()})

        elif request.POST.get('type') == 'auto-complate-lpu':
            return JsonResponse({'rez': init_dir.get_F003()})

        elif request.POST.get('type') == 'auto-complate-vrez':
            return JsonResponse({'rez': init_dir.get_vrzb()})

        elif request.POST.get('type') == 'auto-complate-oksm':
            return JsonResponse({'rez': init_dir.get_oksm()})

        elif request.POST.get('type') == 'auto-complate-list-ds':
            return JsonResponse({'rez': init_dir.get_ds(kod=request.POST.get('kod'))})

        elif request.POST.get('type') == 'ds_naim':
            return JsonResponse({'rez': init_dir.get_ds_naim(kod=request.POST.get('kod'))})

        elif request.POST.get('type') == 'auto-complate-list-v012':
            return JsonResponse({'rez': init_dir.get_v012()})

        elif request.POST.get('type') == 'auto-complate-list-v009':
            return JsonResponse({'rez': init_dir.get_v009()})

        elif request.POST.get('type') == 'auto-complate-list-v020':
            return JsonResponse({'rez': init_dir.get_v020()})

        elif request.POST.get('type') == 'auto-complate-list-vra':
            return JsonResponse({'rez': init_dir.get_vra()})

        elif request.POST.get('type') == 'vra_name_spec':
            return JsonResponse({'rez': init_dir.get_vra_name_spec(kod=request.POST.get('kod'))})

        elif request.POST.get('type') == 'auto-complate-pr_osob':
            return JsonResponse({'rez': init_dir.get_pr_osob()})

        elif request.POST.get('type') == 'auto-complate-v001':
            return JsonResponse({'rez': init_dir.get_v001()})

        elif request.POST.get('type') == 'auto-complate-t006':
            return JsonResponse({'rez': init_dir.get_t006()})

        elif request.POST.get('type') == 'auto-complate-ab_obsh':
            return JsonResponse({'rez': init_dir.get_ab_obsh()})
        elif request.POST.get('type') == 'v001_name':
            return JsonResponse({'rez':init_dir.get_name_v001(kod = request.POST.get('kod'))})
        elif request.POST.get('type') == 'auto-complate-pope':
            return JsonResponse({'rez': init_dir.get_name_pope()})
        elif request.POST.get('type') == 'osl_naim':
            return JsonResponse({'rez':init_dir.get_osl_naim(kod = request.POST.get('kod'))})
        elif request.POST.get('type') == 'ab_obsh_name':
            return JsonResponse({'rez':init_dir.ab_obsh_name(kod = request.POST.get('kod'))})
        elif request.POST.get('type') == 'auto-complate-prli':
            return JsonResponse({'rez':init_dir.get_prli()})
        elif request.POST.get('type') == 'auto-complate-trv':
            return JsonResponse({'rez':init_dir.get_trv()})
        elif request.POST.get('type') == 'auto-complate-isfin':
            return JsonResponse({'rez':init_dir.get_isfin()})
        elif request.POST.get('type') == 'auto-complate-skom':
            return JsonResponse({'rez':init_dir.get_skom()})
        elif request.POST.get('type') == 'auto-complate-f008':
            return JsonResponse({'rez':init_dir.get_f008()})
        elif request.POST.get('type') == 'auto-complate-f011':
            return JsonResponse({'rez':init_dir.get_f011()})
        elif request.POST.get('type') == 'auto-complate-n018':
            return JsonResponse({'rez':init_dir.get_n018()})
        

        
        

