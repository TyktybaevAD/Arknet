//Операции start
function Oper_add() {
    let tbody = document.getElementById("operation_table").querySelector("tbody")
    let count = tbody.childNodes
    // console.log(count.length)
    if (count.length == 0){
        var n = 0
    }
    else{
        var n = count.length 
    }
    let pr = history_obj.modal_history.$data.v_pr_osob
    let op_l = ['dato', 'tm_o', 'py', 'kod_op', 'kod_op_name', 'goc', 'kodx', 'kodx_naim', 'pop', 'pr_osob', 'k_mm', 'kodxa', 'kodxa1', 'obz', 'kodan', 'btn']
    let tr = document.createElement("tr")
    tr.setAttribute("n", n)
    for (o in op_l) {
        let td = document.createElement("td")
        td.setAttribute("name", op_l[o])
        if (op_l[o] == "py") {
            let select = document.createElement("select")
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let py = [1, 2]
            for (let i = 0; i < py.length; i++) {
                let option = document.createElement("option")
                option.innerText = py[i]
                select.appendChild(option)
            }
            td.appendChild(select)
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }

        else if (op_l[o] == "goc") {
            let select = document.createElement("select")
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let goc = ['1', '3']
            for (let i = 0; i < goc.length; i++) {
                let option = document.createElement("option")
                option.innerText = goc[i]
                select.appendChild(option)
            }
            td.appendChild(select)
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (op_l[o] == "pop") {
            let select = document.createElement("select")
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let pop = ['Да', 'Нет', 'Неизвестно']
            for (let p of pop) {
                let option = document.createElement("option")
                option.innerText = p
                select.appendChild(option)
            }
            td.appendChild(select)
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (op_l[o] == "pr_osob") {
            let select = document.createElement("select")
            select.classList.add('form-control')
            select.classList.add('text-center')
            select.setAttribute('multiple', '')
            select.setAttribute('style', 'width: 379px')
            for (let p = 0; p < pr.length; p++) {
                let option = document.createElement("option")
                option.value = pr[p][0]
                option.innerText = pr[p][1]
                select.appendChild(option)
            }
           
            td.appendChild(select)

         
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (op_l[o] == "btn"){
            td.setAttribute("name", "btn")
            let btn = document.createElement("input")
            btn.setAttribute('type', 'button')
            btn.classList.add('btn')
            btn.classList.add('btn-danger')
            btn.value = 'Удалить'
            btn.addEventListener("click", function () {
                tr.remove()
                Oper_delete(td)
            })
            td.appendChild(btn)
            tr.appendChild(td)
        }
        else {
           
            td.setAttribute("name", op_l[o])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }

    }
    tbody.appendChild(tr)
   obj = {}
    for (let t = 0;t < tr.childNodes.length;t++){
        let td = tr.childNodes[t]
        if (td.getAttribute("name")!= "btn"){
            if (td.getAttribute("name")!= "pr_osob"){
                obj[td.getAttribute("name")] = ''
            }
            else{
                obj[td.getAttribute("name")] = []
            }
        }
    }
    history_obj.modal_history.$data.v_oper.push(obj)
    Oper_click_edit()
}

function Oper_edit() {
    let tbody = document.getElementById("operation_table").querySelector("tbody")
    tbody.innerHTML = ""
    let v_oper = history_obj.modal_history.$data.v_oper
    let pr = history_obj.modal_history.$data.v_pr_osob
    var n = 0
    for (let opers in v_oper) {
        let oper = v_oper[opers]
        let tr = document.createElement("tr")
        tr.setAttribute("n", n)
        for (o in oper) {
            let td = document.createElement("td")
            if (o == "py") {
                let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let py = [1, 2]
                for (let i = 0; i < py.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = py[i]
                    select.appendChild(option)
                }
                select.value = oper[o]
                td.appendChild(select)
                td.setAttribute("name", o)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }
            else if (o == "goc") {
                let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let goc = ['1', '3']
                for (let i = 0; i < goc.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = goc[i]
                    select.appendChild(option)
                }
                select.value = oper[o]
                td.appendChild(select)
                td.setAttribute("name", o)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }
            else if (o == "pop") {
                let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let pop = ['Да', 'Нет', 'Неизвестно']
                for (let p of pop) {
                    let option = document.createElement("option")
                    option.innerText = p
                    select.appendChild(option)
                }
                select.value = oper[o]
                td.appendChild(select)
                td.setAttribute("name", o)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }
            else if (o == "pr_osob") {
                let select = document.createElement("select")
                select.classList.add('form-control')
                select.classList.add('text-center')
                select.setAttribute('multiple', '')
                select.setAttribute('style', 'width: 379px')
                for (let p = 0; p < pr.length; p++) {
                    let option = document.createElement("option")
                    option.value = pr[p][0]
                    option.innerText = pr[p][1]
                    select.appendChild(option)
                }
                options = Array.from(select.childNodes)
                td.appendChild(select)

                oper[o].forEach(function (v) {
                    options.find(c => c.value == v).selected = true;
                    // console.log(select.selectedIndex)
                });
                td.setAttribute("name", o)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }
            else {
                td.innerText = oper[o]
                td.setAttribute("name", o)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }

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
            Oper_delete(td)
        })
        td.appendChild(btn)
        td.setAttribute("tr", n)
        tr.appendChild(td)

        tbody.appendChild(tr)
        n += 1
    }
    Oper_click_edit()
}
function Oper_delete(td) {
    let v_oper = history_obj.modal_history.$data.v_oper
    let oper = []

    for (let c = 0;c < v_oper.length;c++){
        if (c != td.getAttribute("tr")){
            oper.push(v_oper[c])
        }
    }
    history_obj.modal_history.$data.v_oper = oper
    Oper_edit()
    Oper_click_edit()
}
function Oper_update(td) {
    // console.log(td)
    var v_oper = history_obj.modal_history.$data.v_oper
    if ((td.getAttribute("name") == "dato") || (td.getAttribute("name") == "tm_o") || (td.getAttribute("name") == "kod_op")
        || (td.getAttribute("name") == "kodx") || (td.getAttribute("name") == "k_mm") || (td.getAttribute("name") == "kodxa")
        || (td.getAttribute("name") == "kodxa1") || (td.getAttribute("name") == "obz") || (td.getAttribute("name") == "kodan")) {
        if (td.getAttribute("name") == "kod_op") {
            let tr_list = document.getElementById("operation_table").querySelector("tbody").querySelectorAll("tr")
            let tr = tr_list[td.getAttribute("tr")]
            v_oper[td.getAttribute("tr")][td.getAttribute("name")] = td.innerText
            v_oper[td.getAttribute("tr")][tr.childNodes[4].getAttribute("name")] = tr.childNodes[4].innerText
        }
        else if (td.getAttribute("name") == "kodx") {
            let tr_list = document.getElementById("operation_table").querySelector("tbody").querySelectorAll("tr")
            let tr = tr_list[td.getAttribute("tr")]
            // console.log(td.innerText)
            // console.log(tr.childNodes[7].innerText)
            v_oper[td.getAttribute("tr")][td.getAttribute("name")] = td.innerText
            v_oper[td.getAttribute("tr")][tr.childNodes[7].getAttribute("name")] = tr.childNodes[7].innerText
        }
        else {
            v_oper[td.getAttribute("tr")][td.getAttribute("name")] = td.innerText
        }
    }
    else if ((td.getAttribute("name") == "py") || (td.getAttribute("name") == "goc") || (td.getAttribute("name") == "pop")) {
        v_oper[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value

    }
    else if (td.getAttribute("name") == "pr_osob") {
        let select_active = td.childNodes[0].selectedOptions
        let active = []
        for (let a of select_active) {
            active.push(a.value)
        }
        v_oper[td.getAttribute("tr")][td.getAttribute("name")] = active

    }
    // console.log(v_oper[0][td.getAttribute("name")])
}

function Oper_click_edit() {
    let kod = history_obj.modal_history.$data.v_list_v001
    let str_kod = ''
    for (let k = 0; k < kod.length; k++) {
        str_kod += '<option value="' + kod[k] + '" />'
    }

    let kod_vra = history_obj.modal_history.$data.v_list_vra
    let str_vra = ''
    for (let k = 0; k < kod_vra.length; k++) {
        str_vra += '<option value="' + kod_vra[k] + '" />'
    }

    var table = document.getElementById("operation_table")
    var cells = table.getElementsByTagName("td")

    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") == "dato") || (cells[i].getAttribute("name") == "tm_o") || (cells[i].getAttribute("name") == "kod_op")
            || (cells[i].getAttribute("name") == "kodx") || (cells[i].getAttribute("name") == "k_mm") || (cells[i].getAttribute("name") == "kodxa")
            || (cells[i].getAttribute("name") == "kodxa1") || (cells[i].getAttribute("name") == "obz") || (cells[i].getAttribute("name") == "kodan")) {
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

           

                // if (cells[i].getAttribute("name") != "kodx"){
                //     input.onchange = function () {
                //         Oper_update(cells[i])
                //     }
                // }

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
                        if (cells[i].getAttribute("name") != "kodx") {
                            Oper_update(td)
                        }

                    }
                    else {
                        td.removeAttribute('data-clicked')
                        td.removeAttribute('data-text')
                        td.innerHTML = orig_text

                        if ((cells[i].getAttribute("name") != "kodx") || (cells[i].getAttribute("name") != "kod_op")) {
                            Oper_update(td)
                        }
                    }
                }
                input.onkeypress = function (Event) {
                    if (Event.keyCode == 13) {
                        this.blur()
                    }
                }
                this.innerHTML = ""
                this.append(input)
                if ((cells[i].getAttribute("name") == "kod_op") || (cells[i].getAttribute('name') == "obz")) {
                    let data = document.createElement("datalist")
                    data.setAttribute('id', cells[i].getAttribute("name"))
                    data.innerHTML = str_kod
                    input.setAttribute('list', cells[i].getAttribute("name"))
                    if (cells[i].getAttribute("name") == "kod_op") {
                        input.addEventListener('change', function () {
                            var formData = new FormData()
                            formData.append('type', 'v001_name')
                            formData.append('kod', input.value)
                            var r = sendRequest('', 'post', formData)
                                .then(response => {
                                    
                                    var tr_list = document.getElementById("operation_table").querySelector("tbody").querySelectorAll("tr")
                                    var tr = tr_list[cells[i].getAttribute("tr")]
                                    console.log(tr.childNodes[4])
                                    var naim = tr.childNodes[4]
                                    naim.innerText = response.data.rez
                                    Oper_update(tr.childNodes[4])

                                })
                                .catch(error => {

                                })
                        })
                    }
                    this.append(data)
                }
                else if ((this.getAttribute('name') == "kodx") || (this.getAttribute('name') == "kodxa")
                    || (this.getAttribute('name') == "kodxa1") || (this.getAttribute('name') == "kodan")) {

                    let data = document.createElement("datalist")
                    data.setAttribute('id', this.getAttribute('name'))
                    data.innerHTML = str_vra
                    input.setAttribute('list', this.getAttribute('name'))
                    this.append(data)

                    if (this.getAttribute('name') == "kodx") {
                        input.addEventListener('change', function () {
                            var formData = new FormData()
                            formData.append('type', 'vra_name_spec')
                            formData.append('kod', input.value)
                            var r = sendRequest('', 'post', formData)
                                .then(response => {
                                    // console.log(cells[i])
                                    var tr_list = document.getElementById("operation_table").querySelector("tbody").querySelectorAll("tr")
                                    var tr = tr_list[cells[i].getAttribute("tr")]
                                    var naim = tr.childNodes[7]
                                    naim.innerText = response.data.rez['naim']
                                    Oper_update(tr.childNodes[7])

                                })
                                .catch(error => {

                                })
                        })
                    }
                }
                this.firstElementChild.select()

            }
        }
        // else {
        //     cells[i].onchange = function () {
        //         Oper_update(cells[i])
        //     }
        // }
    }
    // ('.mask-date').mask('99-99-9999');
}