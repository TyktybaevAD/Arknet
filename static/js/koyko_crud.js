function Koyko_add() {
    let tbody = document.getElementById('koyko_table').querySelector('tbody')
    let tr = document.createElement('tr')
    let add_btn = document.getElementById('add_tr_koyko')
    add_btn.setAttribute('disabled', 'disabled')
    let koyko_td = ['n', 'aro', 'otd', 'prof_k', 'kod', 'naim', 'spec', 'btn']
    for (let i = 0; i < koyko_td.length; i++) {
        let td = document.createElement('td')
        td.setAttribute("name", koyko_td[i])
        if (koyko_td[i] == "btn") {
            let btn = document.createElement("input")
            btn.setAttribute('type', 'button')
            btn.classList.add('btn')
            btn.classList.add('btn-danger')
            btn.setAttribute("name", "btn")
            btn.value = 'Удалить'
            btn.addEventListener("click", function () {
                tr.remove()
                add_btn.removeAttribute('disabled')
                history_obj.modal_history.$data.v_le_vr = []
            })
            td.appendChild(btn)
            tr.appendChild(td)
        }
        else {
            tr.appendChild(td)
        }

    }
    tbody.appendChild(tr)

    Koyko_click_edit()

}
function Koyko_edit() {
    let tbody = document.getElementById('koyko_table').querySelector('tbody')
    let add_btn = document.getElementById('add_tr_koyko')
    tbody.innerHTML = ""
    let le_vr = history_obj.modal_history.$data.v_le_vr
    if (le_vr.length != 0) {
        let tr = document.createElement("tr")

        for (let l in le_vr) {
            let td = document.createElement("td")
            td.innerText = le_vr[l]
            td.setAttribute("name", l)
            tr.appendChild(td)
        }
        let td = document.createElement("td")
        td.setAttribute("name", "btn")
        let btn = document.createElement("input")
        btn.setAttribute('type', 'button')
        btn.classList.add('btn')
        btn.classList.add('btn-danger')
        btn.value = 'Удалить'

        btn.addEventListener("click", function () {
            tr.remove()
            add_btn.removeAttribute('disabled')
            history_obj.modal_history.$data.v_le_vr = []
        })
        td.appendChild(btn)
        tr.appendChild(td)

        tbody.appendChild(tr)

        Koyko_click_edit()
    }
}
function Koyko_update() {
    let obj = new Object()
    var td_cells = document.getElementById("koyko_table").querySelector("tbody").querySelector("tr").cells;
    // for (var i=0; i < td_cells.length; i++){
    //     if(td_cells[i].getAttribute("name") != "btn"){
    //         // console.log(td_cells[i].innerHTML);
    //         obj.
    //     }
    // }
    obj.N = td_cells[0].innerText
    obj.aro = td_cells[1].innerText
    obj.otd = td_cells[2].innerText
    obj.prof_k = td_cells[3].innerText
    obj.kod = td_cells[4].innerText
    obj.naim = td_cells[5].innerText
    obj.spec = td_cells[6].innerText

    history_obj.modal_history.$data.v_le_vr = obj
}
function Koyko_click_edit() {
    var table = document.getElementById("koyko_table")
    var cells = table.getElementsByTagName("td")

    var otde = history_obj.modal_history.$data.v_list_otde
    var str_otde = ''
    for (var i = 0; i < otde.length; ++i) {
        str_otde += '<option value="' + otde[i] + '" />'
    }
    var prof_k = history_obj.modal_history.$data.v_list_v020
    var str_prof_k = ''
    for (var i = 0; i < prof_k.length; ++i) {
        str_prof_k += '<option value="' + prof_k[i] + '" />'
    }

    var vra_kod = history_obj.modal_history.$data.v_list_vra
    var str_vra_kod = ''
    for (var i = 0; i < vra_kod.length; ++i) {
        str_vra_kod += '<option value="' + vra_kod[i] + '" />'
    }





    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") != "naim") && (cells[i].getAttribute("name") != "spec") && (cells[i].getAttribute("name") != "btn")) {
            cells[i].onclick = function () {
                if (this.hasAttribute('data-clicked')) {
                    return
                }
                this.setAttribute('data-clicked', 'yes')
                this.setAttribute('data-text', this.innerHTML)
                let input = document.createElement("input")
                input.setAttribute("type", "text")
                input.setAttribute("name", "btn")
                input.value = this.innerHTML

                input.ondblclick = function () {
                    input.value = ""
                }
                input.onblur = function () {
                    var td = input.parentElement
                    var orig_text = input.parentElement.getAttribute('data-text')
                    var current_text = this.value

                    if (orig_text != current_text) {
                        td.removeAttribute('data-clicked')
                        td.removeAttribute('data-text')
                        td.innerHTML = current_text
                        Koyko_update()
                        // 
                    }
                    else {
                        td.removeAttribute('data-clicked')
                        td.removeAttribute('data-text')
                        td.innerHTML = orig_text
                        // console.log(td.innerText)
                        Koyko_update()

                    }
                }

                input.onkeypress = function (event) {
                    if (event.keyCode == 13) {
                        this.blur()
                    }
                }
                this.innerHTML = ""
                this.append(input)
                if (cells[i].getAttribute("name") == "otd") {
                    let data = document.createElement("datalist")
                    data.setAttribute('id', 'otde')
                    data.innerHTML = str_otde
                    input.setAttribute('list', 'otde')
                    this.append(data)
                }
                else if (this.getAttribute('name') == 'prof_k') {
                    let data = document.createElement("datalist")
                    data.setAttribute('id', 'prof_k')
                    data.innerHTML = str_prof_k
                    input.setAttribute('list', 'prof_k')
                    this.append(data)
                }
                else if (this.getAttribute('name') == 'kod') {
                    let data = document.createElement("datalist")
                    data.setAttribute('id', 'kod_le')
                    data.innerHTML = str_vra_kod
                    input.setAttribute('list', 'kod_le')
                    this.append(data)

                    input.addEventListener('change', function () {
                        var formData = new FormData()
                        formData.append('type', 'vra_name_spec')
                        formData.append('kod', input.value)
                        var r = sendRequest('', 'post', formData)
                            .then(response => {
                                for (let i = 0; i < cells.length; i++) {
                                    if (cells[i].getAttribute("name") == "naim") {
                                        cells[i].innerText = response.data.rez['naim']
                                    }
                                    else if (cells[i].getAttribute("name") == "spec") {
                                        cells[i].innerText = response.data.rez['spec']
                                    }
                                }

                                Koyko_update()

                            })
                            .catch(error => {

                            })
                    })
                }

                this.firstElementChild.select()

            }
        }
    }
}