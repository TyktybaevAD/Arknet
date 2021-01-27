class History {
    constructor() {
        this.vm_init = new Vue({
            el: '#modal_history',
            data: {
                // Справочники
                v_list_w: [],
                v_list_otde: [],
                v_list_rab_ner: [],
                v_list_in_t: [],
                v_list_lpu: [],
                v_list_vrez: [],
                v_list_oksm: [],
                v_list_v012: [],
                v_list_v009: [],
                v_list_v020: [],
                v_list_vra: [],
                v_pr_osob: [],
                v_list_v001: [],
                v_list_t006: [],
                v_list_ab_obsh: [],
                v_list_pope: [],
                v_list_prli: [],
                v_list_trv: [],
                v_list_isfin: [],
                v_list_skom: [],
                v_list_f008: [],
                v_list_f011: [],
                v_list_n018: [],
            },
            mounted: function () {
                if (JSON.parse(sessionStorage.getItem('v_list_w')) == null) {
                    this.rec_list_w()
                }
                else {
                    this.v_list_w = JSON.parse(sessionStorage.getItem('v_list_w'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_otde')) == null) {
                    this.rec_list_otde()
                }
                else {
                    this.v_list_otde = JSON.parse(sessionStorage.getItem('v_list_otde'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_rab_ner')) == null) {
                    this.rec_list_rab_ner()
                }
                else {
                    this.v_list_rab_ner = JSON.parse(sessionStorage.getItem('v_list_rab_ner'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_in_t')) == null) {
                    this.rec_list_in_t()
                }
                else {
                    this.v_list_in_t = JSON.parse(sessionStorage.getItem('v_list_in_t'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_lpu')) == null) {
                    this.rec_list_lpu()
                }
                else {
                    this.v_list_lpu = JSON.parse(sessionStorage.getItem('v_list_lpu'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_vrez')) == null) {
                    this.rec_list_vrez()
                }
                else {
                    this.v_list_vrez = JSON.parse(sessionStorage.getItem('v_list_vrez'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_oksm')) == null) {
                    this.rec_list_oksm()
                }
                else {
                    this.v_list_oksm = JSON.parse(sessionStorage.getItem('v_list_oksm'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_v012')) == null) {
                    this.rec_list_v012()
                }
                else {
                    this.v_list_v012 = JSON.parse(sessionStorage.getItem('v_list_v012'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_v009')) == null) {
                    this.rec_list_v009()
                }
                else {
                    this.v_list_v009 = JSON.parse(sessionStorage.getItem('v_list_v009'))
                }
                if (JSON.parse(sessionStorage.getItem('v_list_v020')) == null) {
                    this.rec_list_v020()
                }
                else {
                    this.v_list_v020 = JSON.parse(sessionStorage.getItem('v_list_v020'))
                }

                if (JSON.parse(sessionStorage.getItem('v_list_vra')) == null) {
                    this.rec_list_vra()
                }
                else {
                    this.v_list_vra = JSON.parse(sessionStorage.getItem('v_list_vra'))
                }

                if (JSON.parse(sessionStorage.getItem('v_pr_osob')) == null) {
                    this.rec_list_pr_osob()
                }
                else {
                    this.v_pr_osob = JSON.parse(sessionStorage.getItem('v_pr_osob'))
                }


                if (JSON.parse(sessionStorage.getItem('v_v001')) == null) {
                    this.rec_list_v001()
                }
                else {
                    this.v_list_v001 = JSON.parse(sessionStorage.getItem('v_v001'))
                }

                if (JSON.parse(sessionStorage.getItem('v_t006')) == null) {
                    this.rec_list_t006()
                }
                else {
                    this.v_list_t006 = JSON.parse(sessionStorage.getItem('v_t006'))
                }

                if (JSON.parse(sessionStorage.getItem('v_ab_obsh')) == null) {
                    this.rec_list_ab_obsh()
                }
                else {
                    this.v_list_ab_obsh = JSON.parse(sessionStorage.getItem('v_ab_obsh'))
                }

                if (JSON.parse(sessionStorage.getItem('v_pope')) == null) {
                    this.rec_list_pope()
                }
                else {
                    this.v_list_pope = JSON.parse(sessionStorage.getItem('v_pope'))
                }

                if (JSON.parse(sessionStorage.getItem('v_prli')) == null) {
                    this.rec_list_prli()
                }
                else {
                    this.v_list_prli = JSON.parse(sessionStorage.getItem('v_prli'))
                }

                if (JSON.parse(sessionStorage.getItem('v_trv')) == null) {
                    this.rec_list_trv()
                }
                else {
                    this.v_list_trv = JSON.parse(sessionStorage.getItem('v_trv'))
                }

                if (JSON.parse(sessionStorage.getItem('v_isfin')) == null) {
                    this.rec_list_isfin()
                }
                else {
                    this.v_list_isfin = JSON.parse(sessionStorage.getItem('v_isfin'))
                }

                if (JSON.parse(sessionStorage.getItem('v_skom')) == null) {
                    this.rec_list_skom()
                }
                else {
                    this.v_list_skom = JSON.parse(sessionStorage.getItem('v_skom'))
                }

                if (JSON.parse(sessionStorage.getItem('v_f008')) == null) {
                    this.rec_list_f008()
                }
                else {
                    this.v_list_f008 = JSON.parse(sessionStorage.getItem('v_f008'))
                }


                if (JSON.parse(sessionStorage.getItem('v_f011')) == null) {
                    this.rec_list_f011()
                }
                else {
                    this.v_list_f011 = JSON.parse(sessionStorage.getItem('v_f011'))
                }

                if (JSON.parse(sessionStorage.getItem('v_n018')) == null) {
                    this.rec_list_n018()
                }
                else {
                    this.v_list_n018 = JSON.parse(sessionStorage.getItem('v_n018'))
                }


            },
            methods: {
                // Заполняем справочники
                rec_list_w: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-w')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_w = response.data.rez
                            sessionStorage.setItem('v_list_w', JSON.stringify(this.v_list_w))
                        })
                        .catch(error => {
                            this.v_list_w = []
                        })
                },
                rec_list_otde: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-otde')

                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_otde = response.data.rez
                            sessionStorage.setItem('v_list_otde', JSON.stringify(this.v_list_otde))
                        })
                        .catch(error => {
                            this.v_list_otde = []
                        })
                },

                rec_list_rab_ner: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-rab_ner')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_rab_ner = response.data.rez
                            sessionStorage.setItem('list_rab_ner', JSON.stringify(this.v_list_rab_ner))
                        })
                        .catch(error => {
                            this.v_list_rab_ner = []
                        })
                },
                rec_list_in_t: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-in_t')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_in_t = response.data.rez
                            sessionStorage.setItem('v_list_in_t', JSON.stringify(this.v_list_in_t))
                        })
                        .catch(error => {
                            this.v_list_in_t = []
                        })
                },
                rec_list_lpu: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-lpu')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_lpu = response.data.rez
                            sessionStorage.setItem('v_list_lpu', JSON.stringify(this.v_list_lpu))
                        })
                        .catch(error => {
                            this.v_list_lpu = []
                        })
                },
                rec_list_vrez: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-vrez')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_vrez = response.data.rez
                            sessionStorage.setItem('v_list_vrez', JSON.stringify(this.v_list_vrez))
                        })
                        .catch(error => {
                            this.v_list_vrez = []
                        })

                },
                rec_list_oksm: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-oksm')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_oksm = response.data.rez
                            sessionStorage.setItem('v_list_oksm', JSON.stringify(this.v_list_oksm))
                        })
                        .catch(error => {
                            this.v_list_oksm = []
                        })
                },
                rec_list_v012: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-list-v012')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_v012 = response.data.rez
                            sessionStorage.setItem('v_list_v012', JSON.stringify(this.v_list_v012))
                        })
                        .catch(error => {
                            this.v_list_v012 = []
                        })
                },
                rec_list_v009: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-list-v009')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_v009 = response.data.rez
                            sessionStorage.setItem('v_list_v009', JSON.stringify(this.v_list_v009))
                        })
                        .catch(error => {
                            this.v_list_v009 = []
                        })
                },
                rec_list_v020: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-list-v020')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_v020 = response.data.rez
                            sessionStorage.setItem('v_list_v020', JSON.stringify(this.v_list_v020))
                        })
                        .catch(error => {
                            this.v_list_v020 = []
                        })
                },
                rec_list_vra: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-list-vra')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_vra = response.data.rez
                            sessionStorage.setItem('v_list_vra', JSON.stringify(this.v_list_vra))
                        })
                        .catch(error => {
                            this.v_list_vra = []
                        })
                },
                rec_list_pr_osob: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-pr_osob')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_pr_osob = response.data.rez
                            sessionStorage.setItem('v_pr_osob', JSON.stringify(this.v_pr_osob))
                        })
                        .catch(error => {
                            this.v_pr_osob = []
                        })
                },
                rec_list_v001: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-v001')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_v001 = response.data.rez
                            sessionStorage.setItem('v_v001', JSON.stringify(this.v_list_v001))
                        })
                        .catch(error => {
                            this.v_list_v001 = []
                        })
                },
                rec_list_t006: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-t006')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_t006 = response.data.rez
                            sessionStorage.setItem('v_t006', JSON.stringify(this.v_list_t006))
                        })
                        .catch(error => {
                            this.v_list_t006 = []
                        })
                },
                rec_list_ab_obsh: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-ab_obsh')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_ab_obsh = response.data.rez
                            sessionStorage.setItem('v_ab_obsh', JSON.stringify(this.v_list_ab_obsh))
                        })
                        .catch(error => {
                            this.v_list_ab_obsh = []
                        })
                },
                rec_list_pope: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-pope')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_pope = response.data.rez
                            sessionStorage.setItem('v_pope', JSON.stringify(this.v_list_pope))
                        })
                        .catch(error => {
                            this.v_list_pope = []
                        })
                },
                rec_list_prli: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-prli')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_prli = response.data.rez
                            sessionStorage.setItem('v_prli', JSON.stringify(this.v_list_prli))
                        })
                        .catch(error => {
                            this.v_list_prli = []
                        })
                },
                rec_list_trv: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-trv')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_trv = response.data.rez
                            sessionStorage.setItem('v_trv', JSON.stringify(this.v_list_trv))
                        })
                        .catch(error => {
                            this.v_list_trv = []
                        })
                },

                rec_list_isfin: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-isfin')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_isfin = response.data.rez
                            sessionStorage.setItem('v_isfin', JSON.stringify(this.v_list_isfin))
                        })
                        .catch(error => {
                            this.v_list_isfin = []
                        })
                },
                rec_list_skom: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-skom')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_skom = response.data.rez
                            sessionStorage.setItem('v_skom', JSON.stringify(this.v_list_skom))
                        })
                        .catch(error => {
                            this.v_list_skom = []
                        })
                },
                rec_list_f008: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-f008')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_f008 = response.data.rez
                            sessionStorage.setItem('v_f008', JSON.stringify(this.v_list_f008))
                        })
                        .catch(error => {
                            this.v_list_f008 = []
                        })
                },
                rec_list_f011: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-f011')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_f011 = response.data.rez
                            sessionStorage.setItem('v_f011', JSON.stringify(this.v_list_f011))
                        })
                        .catch(error => {
                            this.v_list_f011 = []
                        })
                },
                rec_list_n018: function () {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-n018')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_n018 = response.data.rez
                            sessionStorage.setItem('v_n018', JSON.stringify(this.v_list_n018))
                        })
                        .catch(error => {
                            this.v_list_n018 = []
                        })
                }
            }
        })

        this.vm_search_history = new Vue({
            el: '#search_histor',
            data: {
                // Поиск записей истории
                v_check_history: true,
                v_search_history: '',
                v_check_response_history: false,
                v_response_history: [],


            },
            methods: {
                get_history: function () {
                    this.v_check_history = true
                    if (this.v_search_history != '') {
                        var formData = new FormData()
                        formData.append('history', this.v_search_history)
                        formData.append('type', 'search')
                        var r = sendRequest('', 'post', formData)
                            .then(response => {
                                this.v_check_response_history = true
                                this.v_response_history = response.data.rez
                            })
                            .catch(error => {
                                this.v_check_response_history = false
                            })
                    }
                    else {
                        this.v_check_history = false
                    }
                },
            }
        })

        this.modal_history = new Vue({
            el: '#content',
            data: {
                pers_info: false,
                inf_diagnoses: false,
                inf_koyko: false,
                inf_operation: false,
                inf_ks_zabolev: false,
                inf_complication: false,
                inf_work_capacity: false,
                inf_manipulation: false,
                inf_translations: false,
                inf_post_mortem: false,
                inf_injury: false,
                inf_policy_passport_snills: false,
                inf_pregnancy: false,
                inf_disability: false,
                inf_patient_p: false,
                inf_address: false,
                inf_onmk: false,
                inf_onk: false,
                inf_mo: false,

                v_vra_name: [],
                v_ds_naim: '',
                v_spec: [],

                //Справочники
                v_list_w: [],
                v_list_otde: [],
                v_list_rab_ner: [],
                v_list_in_t: [],
                v_list_lpu: [],
                v_list_vrez: [],
                v_list_oksm: [],
                v_list_ds: [],
                v_list_v012: [],
                v_list_v009: [],
                v_list_v020: [],
                v_list_vra: [],
                v_pr_osob: [],
                v_list_v001: [],
                v_list_t006: [],
                v_list_ab_obsh: [],
                v_list_pope: [],
                v_list_prli: [],
                v_list_trv: [],
                v_list_isfin: [],
                v_list_skom: [],
                v_list_f008: [],
                v_list_f011: [],
                v_list_n018: [],
                // Данные из карточки пациента шапка
                v_data_cards: [],
                v_history: '',
                v_fam: '',
                v_im: '',
                v_ot: '',
                v_pol: '',
                v_datp: '',
                v_tm_otd: '',
                v_datv: '',
                v_datr: '',
                //
                // Персональные данные
                v_otd: '',
                v_vec: '',
                // v_m_roj: '',
                // v_adr: '',
                v_rab: '',
                v_prof: '',
                v_r_n: '',
                v_in_t: '',
                v_lpy: '',
                v_goc: '',
                v_prpg: '',
                v_vrez: '',
                v_c_oksm: '',
                //
                //Сведения о диагнозах
                v_dsny_kod: '',
                v_dsny_naim: '',
                v_ds_0_kod: '',
                v_ds_0_naim: '',
                v_dsk_kod: '',
                v_dsk_naim: '',
                v_dskz_kod: '',
                v_dskz_naim: '',
                v_ds_osl_kod: '',
                v_ds_osl_naim: '',
                v_dsc_kod: '',
                v_dsc_naim: '',
                v_dson_kod: '',
                v_dson_naim: '',
                v_icx: '',

                // 3.Койко-дни
                v_le_vr: [],
                v_le_vr_update: [],
                //

                //4.Операции
                v_oper: [],
                //

                //5.Клинико-стат.гр.заболев-я
                ksg_osn: '',
                ksg_sop: '',
                iddoc: '',

                //6.Oсложнение
                v_complication: [],

                //7.Трудоспособность
                v_trs: '',
                //8.Манипуляции
                v_manipulation: [],

                //9./Переводы
                v_kod_y: '',
                v_pr_per: '',
                v_dat_pe: '',
                v_potd: '',
                vb_s_datv: '',

                //А.Патанатомический Ds
                v_tm_let: '',
                v_pri: '',
                v_ds_let: '',
                v_ds_let_naim: '',
                v_wskr: '',
                v_dspat: '',
                v_dspat_naim: '',
                v_rasxp: '',
                v_otd_y: '',
                //B.Сведения о травмах
                v_details: '',
                v_details_name: '',
                v_t_trv: '',
                v_trav_ns: '',
                //C.Полис/Документ/Снилс
                v_vds: '',
                v_sctp: '',
                v_nctp: '',
                v_ctkom: '',
                v_t_pol: '',
                v_udl: '',
                v_s_pasp: '',
                v_n_pasp: '',
                v_docdate: '',
                v_docorg: '',
                v_m_roj: '',
                v_ss: '',

                //D.Прерывание беременности
                v_vb_a_datv: '',
                v_srber: '',
                v_n_ber: '',
                v_pria: '',
                v_m_prer: '',

                //F.Представитель пациента
                v_fam_p: '',
                v_im_p: '',
                v_ot_p: '',
                v_sex_bol: '',
                v_mp_roj: '',
                v_udl_p: '',
                v_sp_pasp: '',
                v_np_pasp: '',
                v_skom_p: '',
                v_stat_p: '',
                v_s_pol: '',
                v_n_pol: '',

                //E.Лист нетрудоспособности
                v_dat_l1: '',
                v_dat_l2: '',
                v_ot_ln: '',
                v_vs_bol: '',
                v_dis_sex_bol: '',

                //G.Адрес проживания
                v_m_roj: '',
                v_adr: '',
                v_kv: '',
                v_kp: '',
                v_stro: '',
                v_cj: '',
                v_rai: '',


                //#J.Карта онкобольного
                v_ds1_t: '',
                v_stad: '',
                v_onk_t: '',
                v_onk_n: '',
                v_onk_m: '',
                v_mtstz: '',
                v_c_zab: '',
                v_diag_date: '',
                v_diag_tip: '',
                v_diag_code: '',
                v_diag_rslt: '',
                v_rec_rslt: '',
                v_pr_cons: '',
                v_dt_cons: '',
                v_usl_tip: '',
                v_hir_tip: '',
                v_prot: '',
                v_d_prot: '',
                v_naprdate: '',
                v_napr_mo: '',
                v_napr_v: '',
                v_napr_issl: '',
                v_napr_usl: '',
                //K.Мо прикрепления
                v_pmg: ''
            },
            methods: {
                get_data_cards: function (history, date_z_1) {
                    console.log(history, date_z_1)
                    var formData = new FormData()
                    formData.append('history', history)
                    formData.append('date_z_1', date_z_1)
                    formData.append('type', 'data_history')
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.pers_info = true
                            this.v_data_cards = response.data.rez
                            console.log(this.v_data_cards)
                            //Шапка
                            this.v_history = this.v_data_cards['history']
                            this.v_fam = this.v_data_cards['fam']
                            this.v_im = this.v_data_cards['im']
                            this.v_ot = this.v_data_cards['ot']
                            this.v_pol = this.v_data_cards['pol']
                            this.v_datp = this.v_data_cards['datp']
                            this.v_tm_otd = this.v_data_cards['tm_otd']
                            this.v_datv = this.v_data_cards['datv']
                            this.v_datr = this.v_data_cards['datr']



                            //Персональные данные
                            this.v_otd = this.v_data_cards['otd']
                            this.v_vec = this.v_data_cards['vec']
                            // this.v_m_roj = this.v_data_cards['m_roj']
                            // this.v_adr = this.v_data_cards['adr']
                            this.v_rab = this.v_data_cards['rab']
                            this.v_prof = this.v_data_cards['prof']
                            this.v_r_n = this.v_data_cards['r_n']
                            this.v_in_t = this.v_data_cards['in_t']
                            this.v_lpy = this.v_data_cards['lpy']
                            this.v_goc = this.v_data_cards['goc']
                            this.v_prpg = this.v_data_cards['prpg']
                            this.v_vrez = this.v_data_cards['vrez']
                            this.v_c_oksm = this.v_data_cards['c_oksm']

                            //Сведения о диагнозах
                            if (this.v_data_cards['dsny'] != null) {
                                this.v_dsny_kod = this.v_data_cards['dsny']['kod']
                                this.v_dsny_naim = this.v_data_cards['dsny']['naim']
                            }

                            if (this.v_data_cards['dsny'] != null) {
                                this.v_ds_0_kod = this.v_data_cards['ds_0']['kod']
                                this.v_ds_0_naim = this.v_data_cards['ds_0']['naim']
                            }

                            if (this.v_data_cards['dsk'] != null) {
                                this.v_dsk_kod = this.v_data_cards['dsk']['kod']
                                this.v_dsk_naim = this.v_data_cards['dsk']['naim']
                            }
                            if (this.v_data_cards['dskz'] != null) {
                                this.v_dskz_kod = this.v_data_cards['dskz']['kod']
                                this.v_dskz_naim = this.v_data_cards['dskz']['naim']
                            }
                            if (this.v_data_cards['ds_osl'] != null) {
                                this.v_ds_osl_kod = this.v_data_cards['ds_osl']['kod']
                                this.v_ds_osl_naim = this.v_data_cards['ds_osl']['naim']
                            }

                            if (this.v_data_cards['dsc'] != null) {
                                this.v_dsc_kod = this.v_data_cards['dsc']['kod']
                                this.v_dsc_naim = this.v_data_cards['dsc']['naim']
                            }

                            if (this.v_data_cards['dson'] != null) {
                                this.v_dson_kod = this.v_data_cards['dson']['kod']
                                this.v_dson_naim = this.v_data_cards['dson']['naim']
                            }
                            this.v_icx = this.v_data_cards['icx']

                            //Койко-дни
                            this.v_le_vr = this.v_data_cards['le_vr']

                            //Операции
                            this.v_oper = this.v_data_cards['oper']
                            // console.log( this.v_data_cards['oper'])

                            //5.Клинико-стат.гр.заболев-я
                            this.ksg_osn = this.v_data_cards['ksg_osn']
                            this.ksg_sop = this.v_data_cards['ksg_sop']
                            this.iddoc = this.v_data_cards['iddoc']

                            //6.Oсложнение
                            this.v_complication = this.v_data_cards['oslo']

                            //7.Трудоспособность
                            this.v_trs = this.v_data_cards['trs']
                            //8.Манипуляции
                            this.v_manipulation = this.v_data_cards['manpys']
                            //9.Переводы
                            this.v_kod_y = this.v_data_cards['kod_y']
                            this.v_pr_per = this.v_data_cards['pr_per']
                            this.v_dat_pe = this.v_data_cards['dat_pe']
                            this.v_potd = this.v_data_cards['potd']
                            this.vb_s_datv = this.v_data_cards['vb_s_datv']
                            //А.Патанатомический Ds
                            this.v_tm_let = this.v_data_cards['tm_let']
                            this.v_pri = this.v_data_cards['pri']
                            this.v_ds_let = this.v_data_cards['ds_let']
                            this.v_ds_let_naim = this.v_data_cards['ds_let_naim']
                            this.v_wskr = this.v_data_cards['wskr']
                            this.v_dspat = this.v_data_cards['dspat']
                            this.v_dspat_naim = this.v_data_cards['dspat_naim']
                            this.v_rasxp = this.v_data_cards['rasxp']
                            this.v_otd_y = this.v_data_cards['otd_y']
                            //B.Сведения о травмах
                            this.v_details = this.v_data_cards['details']
                            this.v_details_name = this.v_data_cards['details_name']
                            this.v_t_trv = this.v_data_cards['t_trv']
                            this.v_trav_ns = this.v_data_cards['trav_ns']
                            //C.Полис/Документ/Снилс
                            this.v_vds = this.v_data_cards['vds']
                            this.v_sctp = this.v_data_cards['sctp']
                            this.v_nctp = this.v_data_cards['nctp']
                            this.v_ctkom = this.v_data_cards['ctkom']
                            this.v_t_pol = this.v_data_cards['t_pol']
                            this.v_udl = this.v_data_cards['udl']
                            this.v_s_pasp = this.v_data_cards['s_pasp']
                            this.v_n_pasp = this.v_data_cards['n_pasp']
                            this.v_docdate = this.v_data_cards['docdate']
                            this.v_docorg = this.v_data_cards['docorg']
                            this.v_m_roj = this.v_data_cards['m_roj']
                            this.v_ss = this.v_data_cards['ss']

                            //D.Прерывание беременности
                            this.v_vb_a_datv = this.v_data_cards['vb_a_datv']
                            this.v_srber = this.v_data_cards['srber']
                            this.v_n_ber = this.v_data_cards['n_ber']
                            this.v_pria = this.v_data_cards['pria']
                            this.v_m_prer = this.v_data_cards['m_prer']
                            //E.Лист нетрудоспособности
                            this.v_dat_l1 = this.v_data_cards['dat_l1']
                            this.v_dat_l2 = this.v_data_cards['dat_l2']
                            this.v_ot_ln = this.v_data_cards['ot_ln']
                            this.v_vs_bol = this.v_data_cards['vs_bol']
                            this.v_dis_sex_bol = this.v_data_cards['dis_sex_bol']
                            //F.Представитель пациента
                            this.v_fam_p = this.v_data_cards['fam_p']
                            this.v_im_p = this.v_data_cards['im_p']
                            this.v_ot_p = this.v_data_cards['ot_p']
                            this.v_sex_bol = this.v_data_cards['sex_bol']
                            this.v_mp_roj = this.v_data_cards['mp_roj']
                            this.v_udl_p = this.v_data_cards['udl_p']
                            this.v_sp_pasp = this.v_data_cards['sp_pasp']
                            this.v_np_pasp = this.v_data_cards['np_pasp']
                            this.v_skom_p = this.v_data_cards['skom_p']
                            this.v_stat_p = this.v_data_cards['stat_p']
                            this.v_s_pol = this.v_data_cards['s_pol']
                            this.v_n_pol = this.v_data_cards['n_pol']

                            //G.Адрес проживания
                            this.v_m_roj = this.v_data_cards['m_roj']
                            this.v_adr = this.v_data_cards['adr']
                            this.v_kv = this.v_data_cards['kv']
                            this.v_kp = this.v_data_cards['kp']
                            this.v_stro = this.v_data_cards['stro']
                            this.v_cj = this.v_data_cards['cj']
                            this.v_rai = this.v_data_cards['rai']

                            //J.Карта онкобольного
                            this.v_ds1_t = this.v_data_cards['ds1_t']
                            this.v_stad = this.v_data_cards['stad']
                            this.v_onk_t = this.v_data_cards['onk_t']
                            this.v_onk_n = this.v_data_cards['onk_n']
                            this.v_onk_m = this.v_data_cards['onk_m']
                            this.v_mtstz = this.v_data_cards['mtstz']
                            this.v_c_zab = this.v_data_cards['c_zab']
                            this.v_diag_date = this.v_data_cards['diag_date']
                            this.v_diag_tip = this.v_data_cards['diag_tip']
                            this.v_diag_code = this.v_data_cards['diag_code']
                            this.v_diag_rslt = this.v_data_cards['diag_rslt']
                            this.v_rec_rslt = this.v_data_cards['rec_rslt']
                            this.v_pr_cons = this.v_data_cards['pr_cons']
                            this.v_dt_cons = this.v_data_cards['dt_cons']
                            this.v_usl_tip = this.v_data_cards['usl_tip']
                            this.v_hir_tip = this.v_data_cards['hir_tip']
                            this.v_prot = this.v_data_cards['prot']
                            this.v_d_prot = this.v_data_cards['d_prot']
                            this.v_naprdate = this.v_data_cards['naprdate']
                            this.v_napr_mo = this.v_data_cards['napr_mo']
                            this.v_napr_v = this.v_data_cards['napr_v']
                            this.v_napr_issl = this.v_data_cards['napr_issl']
                            this.v_napr_usl = this.v_data_cards['napr_usl']
                            //K.Мо прикрепления
                            this.v_pmg = this.v_data_cards['pmg']

                        })
                        .catch(error => {

                        })

                },
                rec_list_ds: function (kod) {
                    var formData = new FormData()
                    formData.append('type', 'auto-complate-list-ds')
                    formData.append('kod', kod)
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_list_ds = response.data.rez
                            // console.log(this.v_list_ds)
                        })
                        .catch(error => {

                        })
                },
                rec_ds_naim: function (kod) {
                    var formData = new FormData()
                    formData.append('type', 'ds_naim')
                    formData.append('kod', kod)
                    var r = sendRequest('', 'post', formData)
                        .then(response => {
                            this.v_ds_naim = response.data.rez
                        })
                        .catch(error => {
                            this.v_ds_naim = ''
                        })
                    return this.v_ds_naim
                },
                default_temp: function () {
                    this.pers_info = false
                    this.inf_diagnoses = false
                    this.inf_koyko = false
                    this.inf_operation = false
                    this.inf_ks_zabolev = false
                    this.inf_complication = false
                    this.inf_work_capacity = false
                    this.inf_manipulation = false
                    this.inf_translations = false
                    this.inf_post_mortem = false
                    this.inf_injury = false
                    this.inf_policy_passport_snills = false
                    this.inf_pregnancy = false
                    this.inf_disability = false
                    this.inf_patient_p = false
                    this.inf_address = false
                    this.inf_onmk = false
                    this.inf_onk = false
                    this.inf_mo = false
                }
                , clear: function () {
                    this.v_data_cards = []
                    this.v_history = ''
                    this.v_fam = ''
                    this.v_im = ''
                    this.v_ot = ''
                    this.v_pol = ''
                    this.v_datp = ''
                    this.v_tm_otd = ''
                    this.v_datv = ''
                    this.v_datr = ''
                    this.v_otd = ''
                    this.v_vec = ''
                    this.v_m_roj = ''
                    this.v_adr = ''
                    this.v_rab = ''
                    this.v_prof = ''
                    this.v_r_n = ''
                    this.v_in_t = ''
                    this.v_lpy = ''
                    this.v_goc = ''
                    this.v_prpg = ''
                    this.v_vrez = ''
                    this.v_c_oksm = ''
                    this.v_dsny_kod = ''
                    this.v_dsny_naim = ''
                    this.v_ds_0_kod = ''
                    this.v_ds_0_naim = ''
                    this.v_dsk_kod = ''
                    this.v_dsk_naim = ''
                    this.v_dskz_kod = ''
                    this.v_dskz_naim = ''
                    this.v_ds_osl_kod = ''
                    this.v_ds_osl_naim = ''
                    this.v_dsc_kod = ''
                    this.v_dsc_naim = ''
                    this.v_dson_kod = ''
                    this.v_dson_naim = ''
                    this.v_icx = ''
                    this.v_le_vr = []
                    this.v_le_vr_update = []
                    this.v_vra_name = []
                    this.v_oper = []
                    this.ksg_osn = ''
                    this.ksg_sop = ''
                    this.iddoc = ''
                    //8.Манипуляции
                    this.v_complication = []
                    //9.Переводы
                    this.v_kod_y = ''
                    this.v_pr_per = ''
                    this.v_dat_pe = ''
                    this.v_potd = ''
                    this.vb_s_datv = ''
                    //А.Патанатомический Ds
                    this.v_tm_let = '',
                        this.v_pri = '',
                        this.v_ds_let = '',
                        this.v_ds_let_naim = '',
                        this.v_wskr = '',
                        this.v_dspat = '',
                        this.v_dspat_naim = '',
                        this.v_rasxp = '',
                        this.v_otd_y = ''
                    //D.Прерывание беременности
                    this.v_vb_a_datv = ''
                    this.v_srber = ''
                    this.v_n_ber = ''
                    this.v_pria = ''
                    this.v_m_prer = ''
                    //F.Представитель пациента
                    this.v_fam_p = ''
                    this.v_im_p = ''
                    this.v_ot_p = ''
                    this.v_sex_bol = ''
                    this.v_mp_roj = ''
                    this.v_udl_p = ''
                    this.v_sp_pasp = ''
                    this.v_np_pasp = ''
                    this.v_skom_p = ''
                    this.v_stat_p = ''
                    this.v_s_pol = ''
                    this.v_n_pol = ''
                    //E.Лист нетрудоспособности
                    this.v_dat_l1 = ''
                    this.v_dat_l2 = ''
                    this.v_ot_ln = ''
                    this.v_vs_bol = ''
                    this.v_dis_sex_bol = ''

                    this.v_kv = ''
                    this.v_kp = ''
                    this.v_stro = ''
                    this.v_cj = ''
                    this.v_rai = ''
                    //J.Карта онкобольного
                    this.v_ds1_t = ''
                    this.v_stad = ''
                    this.v_onk_t = ''
                    this.v_onk_n = ''
                    this.v_onk_m = ''
                    this.v_mtstz = ''
                    this.v_c_zab = ''
                    this.v_diag_date = ''
                    this.v_diag_tip = ''
                    this.v_diag_code = ''
                    this.v_diag_rslt = ''
                    this.v_rec_rslt = ''
                    this.v_pr_cons = ''
                    this.v_dt_cons = ''
                    this.v_usl_tip = ''
                    this.v_hir_tip = ''
                    this.v_prot = ''
                    this.v_d_prot = ''
                    this.v_naprdate = ''
                    this.v_napr_mo = ''
                    this.v_napr_v = ''
                    this.v_napr_issl = ''
                    this.v_napr_usl = ''
                    //K.Мо прикрепления
                    this.v_pmg = ''
                }
            }

        })


    }
    init() {
        this.modal_history.$data.v_list_w = this.vm_init.$data.v_list_w
        this.modal_history.$data.v_list_otde = this.vm_init.$data.v_list_otde
        this.modal_history.$data.v_list_rab_ner = this.vm_init.$data.v_list_rab_ner
        this.modal_history.$data.v_list_in_t = this.vm_init.$data.v_list_in_t
        this.modal_history.$data.v_list_lpu = this.vm_init.$data.v_list_lpu
        this.modal_history.$data.v_list_vrez = this.vm_init.$data.v_list_vrez
        this.modal_history.$data.v_list_oksm = this.vm_init.$data.v_list_oksm
        this.modal_history.$data.v_list_ds = this.vm_init.$data.v_list_ds
        this.modal_history.$data.v_list_v012 = this.vm_init.$data.v_list_v012
        this.modal_history.$data.v_list_v009 = this.vm_init.$data.v_list_v009
        this.modal_history.$data.v_list_v020 = this.vm_init.$data.v_list_v020
        this.modal_history.$data.v_list_vra = this.vm_init.$data.v_list_vra
        this.modal_history.$data.v_pr_osob = this.vm_init.$data.v_pr_osob
        this.modal_history.$data.v_list_v001 = this.vm_init.$data.v_list_v001
        this.modal_history.$data.v_list_t006 = this.vm_init.$data.v_list_t006
        this.modal_history.$data.v_list_ab_obsh = this.vm_init.$data.v_list_ab_obsh
        this.modal_history.$data.v_list_pope = this.vm_init.$data.v_list_pope
        this.modal_history.$data.v_list_prli = this.vm_init.$data.v_list_prli
        this.modal_history.$data.v_list_trv = this.vm_init.$data.v_list_trv
        this.modal_history.$data.v_list_isfin = this.vm_init.$data.v_list_isfin
        this.modal_history.$data.v_list_skom = this.vm_init.$data.v_list_skom
        this.modal_history.$data.v_list_f008 = this.vm_init.$data.v_list_f008
        this.modal_history.$data.v_list_f011 = this.vm_init.$data.v_list_f011
        this.modal_history.$data.v_list_n018 = this.vm_init.$data.v_list_n018




    }



}

