//Манипуляции
function add_manipulation() {
    let tbody = document.getElementById('manipulation_table').querySelector('tbody')
    let count = tbody.childNodes
    if (count.length == 0) {
        var n = 0
    }
    else {
        var n = count.length
    }
    let tr = document.createElement('tr')
    tr.setAttribute("n", n)
    let manipulation = ['datm', 'tnvr', 'tnvr_fam', 'kodmn', 'kodmn_naim', 'kol', 'pl', 'btn']
    for (let i = 0; i < manipulation.length; i++) {
        let td = document.createElement('td')
        td.setAttribute('name', manipulation[i])
        td.setAttribute("tr", n)
        if (manipulation[i] == "pl"){
            let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let pl = ['Неизвестно', 'Да', 'Нет']
                for (let i = 0; i < pl.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = pl[i]
                    select.appendChild(option)
                }
                td.appendChild(select)
        }
        else if ((manipulation[i] == "btn")){
            let btn = document.createElement("input")
            btn.setAttribute('type', 'button')
            btn.classList.add('btn')
            btn.classList.add('btn-danger')
            btn.value = 'Удалить'
            btn.addEventListener("click", function () {
                tr.remove()
                Manipulation_delete(td)
            })
            td.appendChild(btn)
        }
       
        tr.appendChild(td)
    }
    tbody.appendChild(tr)
    obj = {}
    for (let t = 0; t < tr.childNodes.length; t++) {
        let td = tr.childNodes[t]
        if (td.getAttribute("name") != "btn") {
            obj[td.getAttribute("name")] = ''
        }
        
    }
    history_obj.modal_history.$data.v_manipulation.push(obj)
    Manipulation_click_edit()
}

function Manipulation_edit() {
    let tbody = document.getElementById("inf_manipulation").querySelector("tbody")
    tbody.innerHTML = ""
    let v_manipulation = history_obj.modal_history.$data.v_manipulation
    var n = 0
    for (let manipulations in v_manipulation) {
        let tr = document.createElement("tr")
        tr.setAttribute("n", n)
        let manipulation = v_manipulation[manipulations]
        for (let man in manipulation) {
            let td = document.createElement("td")
            td.setAttribute("name", man)
            td.setAttribute("tr", n)
            if (man == "pl") {
                let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let pl = ['Неизвестно', 'Да', 'Нет']
                for (let i = 0; i < pl.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = pl[i]
                    select.appendChild(option)
                }
                select.value = manipulation[man]
                td.appendChild(select)
            }
            else {
                td.innerText = manipulation[man]
            }
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
            Manipulation_delete(td)
        })
        td.appendChild(btn)
        td.setAttribute("tr", n)
        tr.appendChild(td)

        tbody.appendChild(tr)
        n += 1
    }
Manipulation_click_edit()
}

function Manipulation_update(td) {
    let v_manipulation = history_obj.modal_history.$data.v_manipulation
    if (td.getAttribute("name") == "pl"){
        v_manipulation[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value
    }
    else{
        v_manipulation[td.getAttribute("tr")][td.getAttribute("name")] = td.innerText
    }
}

function Manipulation_delete(td) {
    let v_manipulation = history_obj.modal_history.$data.v_manipulation
    let manipulation = []

    for (let m = 0; m < v_manipulation.length; m++) {
        if (m != td.getAttribute("tr")) {
            manipulation.push(v_manipulation[m])
        }
    }
    history_obj.modal_history.$data.v_manipulation = manipulation
    Manipulation_edit()
    Manipulation_click_edit()
}

function Manipulation_click_edit() {
    let kod_vra = history_obj.modal_history.$data.v_list_vra
    let str_vra = ''
    for (let k = 0; k < kod_vra.length; k++) {
        str_vra += '<option value="' + kod_vra[k] + '" />'
    }

    let kodmn = history_obj.modal_history.$data.v_list_ab_obsh
    let str_kodmn = ''
    for (let k = 0; k < kodmn.length; k++) {
        str_kodmn += '<option value="' + kodmn[k] + '" />'
    }


    var table = document.getElementById("manipulation_table")
    var cells = table.getElementsByTagName("td")
    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") == "datm") || (cells[i].getAttribute("name") == "tnvr") || (cells[i].getAttribute("name") == "kodmn")
            || (cells[i].getAttribute("name") == "kol")) {
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

                input.onblur = function () {
                    var td = input.parentElement
                    var orig_text = input.parentElement.getAttribute('data-text')
                    var current_text = this.value

                    if (orig_text != current_text) {
                        td.removeAttribute('data-clicked')
                        td.removeAttribute('data-text')
                        td.innerHTML = current_text
                        Manipulation_update(td)

                    }
                    else {
                        td.removeAttribute('data-clicked')
                        td.removeAttribute('data-text')
                        td.innerHTML = orig_text
                        Manipulation_update(td)
                    }
                }
                input.onkeypress = function (Event) {
                    if (Event.keyCode == 13) {
                        this.blur()
                    }
                }
                this.innerHTML = ""
                this.append(input)
                if (this.getAttribute("name") == "tnvr") {
                    let data = document.createElement("datalist")
                    data.setAttribute('id', this.getAttribute('name'))
                    data.innerHTML = str_vra
                    input.setAttribute('list', this.getAttribute('name'))
                    this.append(data)
                    input.addEventListener('change', function () {
                        var formData = new FormData()
                        formData.append('type', 'vra_name_spec')
                        formData.append('kod', input.value)
                        var r = sendRequest('', 'post', formData)
                            .then(response => {
                                var tr_list = document.getElementById("manipulation_table").querySelector("tbody").querySelectorAll("tr")
                                var tr = tr_list[cells[i].getAttribute("tr")]
                                var naim = tr.childNodes[2]
                                naim.innerText = response.data.rez['naim']
                                Manipulation_update(tr.childNodes[2])
                                
                            })
                            .catch(error => {

                            })
                    })
                }

                else if (this.getAttribute("name") == "kodmn"){
                    let data = document.createElement("datalist")
                    data.setAttribute('id', this.getAttribute('name'))
                    data.innerHTML = str_kodmn
                    input.setAttribute('list', this.getAttribute('name'))
                    this.append(data)

                    input.addEventListener('change', function () {
                        var formData = new FormData()
                        formData.append('type', 'ab_obsh_name')
                        formData.append('kod', input.value)
                        var r = sendRequest('', 'post', formData)
                            .then(response => {
                                var tr_list = document.getElementById("manipulation_table").querySelector("tbody").querySelectorAll("tr")
                                var tr = tr_list[cells[i].getAttribute("tr")]
                                var naim = tr.childNodes[4]
                                naim.innerText = response.data.rez
                                Manipulation_update(tr.childNodes[4])
                            })
                            .catch(error => {

                            })
                    })
                }
            }
        }
        else{
            cells[i].onchange = function () {
                Manipulation_update(cells[i])
            }
        }
    }
}