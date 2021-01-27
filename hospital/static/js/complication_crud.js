function add_complication() {
    let tbody = document.getElementById("complication_table").querySelector("tbody")

    let count = tbody.childNodes
    if (count.length == 0) {
        var n = 0
    }
    else {
        var n = count.length
    }
    let v_oper = history_obj.modal_history.$data.v_oper
    var select = document.createElement("select")
    select.classList.add('custom-select')
    select.classList.add('text-center')
    for (let opers in v_oper) {
        let option = document.createElement("option")
        if ((v_oper[opers]['dato'] != NaN) && (v_oper[opers]['kod_op'] != NaN)) {
            option.innerText = v_oper[opers]['dato'] + ' ' + v_oper[opers]['kod_op']
            select.appendChild(option)
        }
    }

    let tr = document.createElement("tr")
    tr.setAttribute("n", n)
    let complication = ['inf_oper', 'tnvr', 'tnvr_fio', 'dato', 'osl', 'osl_naim', 'xosl', 'posl', 'aosl', 'btn']
    for (let i = 0; i < complication.length; i++) {
        let td = document.createElement("td")
        td.setAttribute('name', complication[i])
        if (complication[i] == 'inf_oper') {
            select.value = ''
            td.appendChild(select)
            td.setAttribute("name", complication[i])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'xosl') {
            let select = document.createElement("select")
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let xosl = ['при лечении', 'интрооперационное', 'послеоперационное', 'другое']
            for (let i = 0; i < xosl.length; i++) {
                let option = document.createElement("option")
                option.innerText = xosl[i]
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)

            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'posl') {
            let select = document.createElement("select")
            select.classList.add('custom-select')
            select.classList.add('text-center')
            let posl = ['из-за болезни', 'ятрогенная', 'тех.оснащение', 'другая']
            for (let i = 0; i < posl.length; i++) {
                let option = document.createElement("option")
                option.innerText = posl[i]
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)
            td.setAttribute("name", complication[i])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'aosl') {
            let select = document.createElement("select")
            select.classList.add('custom-select')
            select.classList.add('text-center')

            let aosl = ['приведшеее к летальному исходу', 'опасное для жизни', 'удлиняющее пребывание', 'другое']
            for (let i = 0; i < aosl.length; i++) {
                let option = document.createElement("option")
                option.innerText = aosl[i]
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)
            td.setAttribute("name", complication[i])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'btn') {
            let btn = document.createElement("input")
            btn.setAttribute('type', 'button')
            btn.classList.add('btn')
            btn.classList.add('btn-danger')
            btn.value = 'Удалить'
            btn.addEventListener("click", function () {
                tr.remove()
            })
            td.appendChild(btn)

        }


        else {
            td.setAttribute("tr", n)
            // td.addEventListener("click", function func() {
            //     let input = document.createElement("input")
            //     input.value = this.innerText
            //     input.setAttribute('type', 'text')
            //     input.setAttribute('class', 'control_input text-center')
            //     this.innerHTML = ''
            //     var td = this

            //     if (complication[i] == 'n') {
            //         td.setAttribute("tr", n)
            //         let kod = history_obj.modal_history.$data.v_list_vra
            //         let str_vra = ''
            //         for (let k = 0; k < kod.length; k++) {
            //             str_vra += '<option value="' + kod[k] + '" />'
            //         }
            //         let data = document.createElement("datalist")
            //         data.setAttribute('id', 'kod_vra')
            //         data.innerHTML = str_vra
            //         input.setAttribute('list', 'kod_vra')
            //         this.appendChild(input)
            //         this.appendChild(data)
            //     }
            //     else {
            //         this.appendChild(input)
            //     }

            //     input.addEventListener("blur", function () {
            //         td.innerHTML = this.value
            //         td.addEventListener("click", func)
            //     })
            //     this.removeEventListener("click", func)

            // })
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
    history_obj.modal_history.$data.v_complication.push(obj)
    Complication_click_edit()
}

function Complication_edit() {
    let tbody = document.getElementById("complication_table").querySelector("tbody")
    tbody.innerHTML = ""
    let v_complication = history_obj.modal_history.$data.v_complication
    let v_oper = history_obj.modal_history.$data.v_oper
    var n = 0
    for (let complications in v_complication) {
        let tr = document.createElement("tr")
        tr.setAttribute("n", n)
        let complication = v_complication[complications]
        var select = document.createElement("select")
        select.classList.add('custom-select')
        select.classList.add('text-center')
        for (let opers in v_oper) {
            let option = document.createElement("option")
            if ((v_oper[opers]['dato'] != NaN) && (v_oper[opers]['kod_op'] != NaN)) {
                option.innerText = v_oper[opers]['dato'] + ' ' + v_oper[opers]['kod_op']
                select.appendChild(option)
            }
        }
        for (let com in complication) {

            let td = document.createElement("td")
            if (com == "inf_oper") {
                // console.log(complication[com])
                select.value = complication[com]
                td.appendChild(select)
                td.setAttribute("name", com)
                td.setAttribute("tr", n)
                tr.appendChild(td)

            }
            else if (com == 'xosl') {
                // console.log(complication[com])
                let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let xosl = ['при лечении', 'интрооперационное', 'послеоперационное', 'другое']
                for (let i = 0; i < xosl.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = xosl[i]
                    select.appendChild(option)
                }
                select.value = complication[com]
                td.appendChild(select)
                td.setAttribute("name", com)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }
            else if (com == "posl") {
                let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let posl = ['из-за болезни', 'ятрогенная', 'тех.оснащение', 'другая']
                for (let i = 0; i < posl.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = posl[i]
                    select.appendChild(option)
                }
                select.value = complication[com]
                td.appendChild(select)
                td.setAttribute("name", com)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }
            else if (com == "aosl") {
                let select = document.createElement("select")
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let aosl = ['приведшеее к летальному исходу', 'опасное для жизни', 'удлиняющее пребывание', 'другое']
                for (let i = 0; i < aosl.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = aosl[i]
                    select.appendChild(option)
                }
                select.value = complication[com]
                td.appendChild(select)
                td.setAttribute("name", com)
                td.setAttribute("tr", n)
                tr.appendChild(td)
            }
            else {
                td.innerText = complication[com]
                td.setAttribute("name", com)
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
            Complication_delete(td)
        })
        td.appendChild(btn)
        td.setAttribute("tr", n)
        tr.appendChild(td)

        tbody.appendChild(tr)
        n += 1
    }

    Complication_click_edit()
}

function Complication_update(td) {
    console.log(td)
    let v_complication = history_obj.modal_history.$data.v_complication
    if ((td.getAttribute("name") == "tnvr") || (td.getAttribute("name") == "tnvr_fio") || (td.getAttribute("name") == "tnvr_fio")
        || (td.getAttribute("name") == "dato") || (td.getAttribute("name") == "osl") || (td.getAttribute("name") == "osl_naim")) {
        let tr_list = document.getElementById("complication_table").querySelector("tbody").querySelectorAll("tr")
        v_complication[td.getAttribute("tr")][td.getAttribute("name")] = td.innerText
    }
    else if ((td.getAttribute("name") == "inf_oper") || (td.getAttribute("name") == "xosl") || (td.getAttribute("name") == "posl")
        || (td.getAttribute("name") == "aosl")) {
        v_complication[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value

    }
}

function Complication_delete(td) {
    let v_complication = history_obj.modal_history.$data.v_complication
    let complication = []

    for (let c = 0; c < v_complication.length; c++) {
        if (c != td.getAttribute("tr")) {
            complication.push(v_complication[c])
        }
    }
    history_obj.modal_history.$data.v_complication = complication
    Complication_edit()
    Complication_click_edit()
}

function Complication_click_edit() {
    let kod_vra = history_obj.modal_history.$data.v_list_vra
    let str_vra = ''
    for (let k = 0; k < kod_vra.length; k++) {
        str_vra += '<option value="' + kod_vra[k] + '" />'
    }

    let kod_osl = history_obj.modal_history.$data.v_list_pope
    let str_osl = ''
    for (let o = 0; o < kod_osl.length; o++) {
        str_osl += '<option value="' + kod_osl[o] + '" />'
    }

    var table = document.getElementById("complication_table")
    var cells = table.getElementsByTagName("td")

    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") == "tnvr") || (cells[i].getAttribute("name") == "dato") || (cells[i].getAttribute("name") == "osl")) {
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
                        Complication_update(td)

                    }
                    else {
                        td.removeAttribute('data-clicked')
                        td.removeAttribute('data-text')
                        td.innerHTML = orig_text
                        Complication_update(td)
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
                                var tr_list = document.getElementById("complication_table").querySelector("tbody").querySelectorAll("tr")
                                var tr = tr_list[cells[i].getAttribute("tr")]
                                var naim = tr.childNodes[2]
                                naim.innerText = response.data.rez['naim']
                                Complication_update(tr.childNodes[2])
                            })
                            .catch(error => {

                            })
                    })

                }
                else if (this.getAttribute("name") == "osl") {
                    let data = document.createElement("datalist")
                    data.setAttribute('id', this.getAttribute('name'))
                    data.innerHTML = str_osl
                    input.setAttribute('list', this.getAttribute('name'))
                    this.append(data)

                    input.addEventListener('change', function () {
                        var formData = new FormData()
                        formData.append('type', 'osl_naim')
                        formData.append('kod', input.value)
                        var r = sendRequest('', 'post', formData)
                            .then(response => {
                                var tr_list = document.getElementById("complication_table").querySelector("tbody").querySelectorAll("tr")
                                var tr = tr_list[cells[i].getAttribute("tr")]
                                var naim = tr.childNodes[5]
                                naim.innerText = response.data.rez
                                Complication_update(tr.childNodes[5])
                            })
                            .catch(error => {

                            })
                    })
                }
            }

        }
        // else {
        //     cells[i].onchange = function () {
        //         Complication_update(cells[i])
        //     }
        // }
    }
}