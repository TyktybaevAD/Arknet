function sendRequest(url,method,data){
  var r = axios({
    method:method,
    url:url,
    data:data,
    xsrfCookieName:'csrftoken',
    xsrfHeaderName:'X-CSRFToken',
    headers:{
      'X-Requested-With':'XMLHttpRequest'
    }
  })
  return r
}

var app = new Vue({
    el: '#app',
    data: {
      message: 'Загрузка из 1с',
      oper:'',
      sluch:'',
      user:'',
      mes_div:null,
      loader_mse:null,
      loader_sp:null,
      loader_sp_end:null,
      err_oper:null,
      err_sluch:null
    },
    created:function(){
      var formData = new FormData()
      formData.append('type','get_user')
      var r = sendRequest('','post',formData)
      .then(response => {
        this.user = response.data.user
      })
    },
    methods:{

      exit_end(){
        console.log('asdasd')
      },
      processing_file(){
        this.message = 'Файлы обрабатываются'
        this.mes_div = null
        this.loader_sp_end = null
        this.loader_mse = true
        this.loader_sp = true
        var btn_e = document.getElementById('btn-e')
        var btn_s = document.getElementById('btn-s')
        btn_e.setAttribute('disabled',true)
        btn_s.setAttribute('disabled',true)
        var formData = new FormData()
        formData.append('type','processing_file')
        var r = sendRequest('','post',formData)
        .then(response => {
          console.log(response.data.rez)
          if ((!response.data.rez[0] && !response.data.rez[1])){
              this.message = 'Вы загрузили не файл oper и sluch'
              this.loader_mse = false
              this.loader_sp = false
              this.err_oper = true
              this.err_sluch = true
              btn_e.removeAttribute('disabled')
              btn_s.removeAttribute('disabled')
            }
          else if (!response.data.rez[0]) {
            this.message = 'Вы загрузили не файл oper'
            this.loader_mse = false
            this.loader_sp = false
            this.err_oper = true
            btn_e.removeAttribute('disabled')
            btn_s.removeAttribute('disabled')
        }
          else if (!response.data.rez[1]){
            this.message = 'Вы загрузили не файл sluch'
            this.loader_mse = false
            this.loader_sp = false
            this.err_sluch = true
            btn_e.removeAttribute('disabled')
            btn_s.removeAttribute('disabled')
          }
          else{
              this.message = 'Записи записаны успешно'
              this.loader_mse = false
              this.loader_sp = false
              this.loader_sp_end = true
              btn_e.removeAttribute('disabled')
              btn_s.removeAttribute('disabled')
          }
        })
      }
      ,
        uploadFiles(){
          this.mes_div = null
          this.loader_mse = false
          this.loader_sp = null
          this.err_oper = null
          this.err_sluch = null
          var formData = new FormData()
          const oper_ = document.getElementById('file_oper')
          const sluch_ = document.getElementById('file_sluch')
          if (oper_.files[0] === undefined || sluch_.files[0] === undefined) {
              this.message = 'Файлы не загружены'
              this.mes_div = false
          }
          else {
              formData.append('oper',oper_.files[0])
              formData.append('sluch',sluch_.files[0])
              formData.append('user',this.user)
              formData.append('type','load_fales')
              var r = sendRequest('','post',formData)
                .then(response => {
                this.message = 'Файлы загружены'
                this.mes_div = true
                this.processing_file()
                })        
                .catch(error => {
                this.message = 'Файлы не загружены'
                this.mes_div = false
            })
          }
        }
      }
  })
