var history_obj = new History()

function Get_data_cards() {
    history_obj.init()
    // console.log(this.event)
    let history = this.event.target.value
    let date_z_1 = this.event.target.getAttribute("date_z_1")
    history_obj.modal_history.get_data_cards(history,date_z_1)
}

function get_name_ds(event) {
    let kod = event.target.value
    if (event.target.getAttribute('name') == 'v_dsny_naim') {
        history_obj.modal_history.$data.v_dsny_naim = history_obj.modal_history.rec_ds_naim(kod)
    }
    else if (event.target.getAttribute('name') == 'v_ds_0_naim') {
        history_obj.modal_history.$data.v_ds_0_naim = history_obj.modal_history.rec_ds_naim(kod)
    }
    else if (event.target.getAttribute('name') == 'v_dsk_naim') {
        history_obj.modal_history.$data.v_dsk_naim = history_obj.modal_history.rec_ds_naim(kod)
    }
    else if (event.target.getAttribute('name') == 'v_dskz_naim') {
        history_obj.modal_history.$data.v_dskz_naim = history_obj.modal_history.rec_ds_naim(kod)
    }
    else if (event.target.getAttribute('name') == 'v_ds_osl_naim') {
        history_obj.modal_history.$data.v_ds_osl_naim = history_obj.modal_history.rec_ds_naim(kod)
    }
    else if (event.target.getAttribute('name') == 'v_dsc_naim') {
        history_obj.modal_history.$data.v_dsc_naim = history_obj.modal_history.rec_ds_naim(kod)
    }

    else if (event.target.getAttribute('name') == 'v_dson_naim') {
        history_obj.modal_history.$data.v_dson_naim = history_obj.modal_history.rec_ds_naim(kod)
    }

    else if (event.target.getAttribute('name') == 'v_ds_let') {
        history_obj.modal_history.$data.v_ds_let_naim = history_obj.modal_history.rec_ds_naim(kod)
    }
    else if (event.target.getAttribute('name') == 'v_dspat') {
        history_obj.modal_history.$data.v_dspat_naim = history_obj.modal_history.rec_ds_naim(kod)
    }
    else if (event.target.getAttribute('name') == 'v_details') {
        history_obj.modal_history.$data.v_details_name = history_obj.modal_history.rec_ds_naim(kod)
    }
    

    


}
function Select_trs(){
    let trs_radio = document.getElementById("Trs").getElementsByClassName("form-group form-check")
    let v_trs = history_obj.modal_history.$data.v_trs.toLowerCase()
    for(let trs in trs_radio){
        try {
            let label = trs_radio[trs].getElementsByTagName("label")
            label[0].onclick = function(){
                history_obj.modal_history.$data.v_trs = trs_radio[trs].textContent.replace(/\s+/g, ' ').trim()
            }
            v_trs = v_trs[0].toUpperCase() + v_trs.slice(1)
            if ( trs_radio[trs].textContent.replace(/\s+/g, ' ').trim() == v_trs){
                trs_radio[trs].childNodes[0].checked=true
            }
        }
        catch(err){
        }
    }
}
function Clear() {
    console.log('clear')
    history_obj.modal_history.$data.v_le_vr = []
    history_obj.modal_history.$data.inf_koyko = false
    
    history_obj.modal_history.$data.v_oper = []
    history_obj.modal_history.$data.inf_operation = false

    history_obj.modal_history.$data.v_complication = []
    history_obj.modal_history.$data.inf_complication = false

    history_obj.modal_history.$data.v_manipulation = []
    history_obj.modal_history.$data.inf_manipulation = false

    history_obj.modal_history.clear()
    history_obj.modal_history.default_temp()

    let operation_tbody = document.getElementById("operation_table").querySelector("tbody")
    operation_tbody.innerHTML = ""




    var med_card_menu = document.getElementById("med_card_menu")
    for (let menu of med_card_menu.querySelectorAll('a')) {
        menu.classList.remove("active")
    }
    med_card_menu.querySelector('a').classList.add("active")


}


function address_api(){
    (function () {
        var $container = $(document.getElementById('form_with_map'));
    
        var $region = $container.find('[name="region"]'),
            $district = $container.find('[name="district"]'),
            $city = $container.find('[name="city"]'),
            $street = $container.find('[name="street"]'),
            $building = $container.find('[name="building"]'),
            $address = $container.find('#address'),
            $zip = $container.find('#map_zip'),
            $kladrId = $container.find('#kladrId'),
            $okatoId = $container.find('#okatoId'),
            $typeId = $container.find('#typeId'),
            $typeShortId = $container.find('#typeShortId'),
            $contentTypeId = $container.find('#contentTypeId');
    
        var map = null,
            map_created = false;
    
        $()
            .add($region)
            .add($district)
            .add($city)
            .add($street)
            .add($building)
            .fias({
                parentInput: $container.find('.js-form-address-map'),
                verify: true,
                change: function (obj) {
                    if (obj) {
                        setLabel($(this), obj.type);
                        $kladrId.text(obj.id ? obj.id : '');
                        $okatoId.text(obj.okato ? obj.okato : '');
                        $typeId.text(obj.type ? obj.type : '');
                        $typeShortId.text(obj.typeShort ? obj.typeShort : '');
                        $contentTypeId.text(obj.contentType ? obj.contentType : '');
    
                        if (obj.parents) {
                            $.fias.setValues(obj.parents, '.js-form-address-map');
                        }
                    }
    
                    var $zipWrap = $zip.parent();
                    if (obj && obj.zip) {
                        $zip.text(obj.zip);
                        $zipWrap.show();
                    }//Обновляем поле zip
                    else {
                        $zipWrap.hide();
                    }
    
    
                    addressUpdate();
                    mapUpdate();
                },
                checkBefore: function () {
                    var $input = $(this);
    
                    if (!$.trim($input.val())) {
                        addressUpdate();
                        mapUpdate();
                        return false;
                    }
                }
            });
    
        $region.fias('type', $.fias.type.region);
        $district.fias('type', $.fias.type.district);
        $city.fias('type', $.fias.type.city);
        $street.fias('type', $.fias.type.street);
        $building.fias('type', $.fias.type.building);
    
        // Включаем получение родительских объектов для населённых пунктов
        $district.fias('withParents', true);
        $city.fias('withParents', true);
        $street.fias('withParents', true);
    
    
        // Отключаем проверку введённых данных для строений
        $building.fias('verify', false);
    
        ymaps.ready(function () {
            if (map_created) return;
            map_created = true;
    
            map = new ymaps.Map('map', {
                center: [55.76, 37.64],
                zoom: 12,
                controls: []
            });
    
            map.controls.add('zoomControl', {
                position: {
                    right: 10,
                    top: 10
                }
            });
        });
    
        function setLabel($input, text) {
            text = text.charAt(0).toUpperCase() + text.substr(1).toLowerCase();
            $input.parent().find('label').text(text);
        }
    
        function mapUpdate() {
            var zoom = 4;
    
            var address = $.fias.getAddress('.js-form-address-map', function (objs) {
                var result = '';
    
                $.each(objs, function (i, obj) {
                    var name = '',
                        type = '';
    
                    if ($.type(obj) === 'object') {
                        name = obj.name;
                        type = ' ' + obj.type;
    
                        switch (obj.contentType) {
                            case $.fias.type.region:
                                zoom = 4;
                                break;
    
                            case $.fias.type.district:
                                zoom = 7;
                                break;
    
                            case $.fias.type.city:
                                zoom = 10;
                                break;
    
                            case $.fias.type.street:
                                zoom = 13;
                                break;
    
                            case $.fias.type.building:
                                zoom = 16;
                                break;
                        }
                    }
                    else {
                        name = obj;
                    }
    
                    if (result) result += ', ';
                    result += type + name;
                });
    
                return result;
            });
    
            if (address && map_created) {
                var geocode = ymaps.geocode(address);
                geocode.then(function (res) {
                    map.geoObjects.each(function (geoObject) {
                        map.geoObjects.remove(geoObject);
                    });
    
                    var position = res.geoObjects.get(0).geometry.getCoordinates(),
                        placemark = new ymaps.Placemark(position, {}, {});
    
                    map.geoObjects.add(placemark);
                    map.setCenter(position, zoom);
                });
            }
        }
    
        function addressUpdate() {
            var address = $.fias.getAddress($container.find('.js-form-address-map'));
    
            $address.text(address);
        }
    
    })();

}

function mod_adr(){
    let adr = document.getElementById("adr").querySelector("input")
    let adr_kv_kp_st = document.getElementById("adr_kv_kp_st").querySelectorAll("input")
    history_obj.modal_history.$data.v_m_roj = adr.value
    if (adr.value.length == 0){
        history_obj.modal_history.$data.v_kv = ''
        history_obj.modal_history.$data.v_kp = ''
        history_obj.modal_history.$data.v_stro = ''
        history_obj.modal_history.$data.v_cj = ''
        history_obj.modal_history.$data.v_rai = ''
    }
    
}