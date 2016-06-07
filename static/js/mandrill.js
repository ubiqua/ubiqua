/*Formulario de página de contacto*/
function sendMail(email, name, html_final){
    var dest = "ghurtado@ubiqua.me"; /*Email destino para todos los formularios*/

    $.ajax({
      type: "POST",
      url: "https://mandrillapp.com/api/1.0/messages/send.json",
      data: {
            'key': 'MBHp81VsRJz4qh6tJRwMIQ', //API Key asiganada
            'message': {
              'from_email': email,
              "from_name": name,
              'to': [
                {
                  'email': dest, //Destinatario del correo
                  'name': 'Contacto Ubiqua', //Nombre del Remitente
                  'type': 'to'
                }
              ],
              'subject': 'Nuevo contacto vía website', //Titulo del correo
              'html': html_final
            }
        }
    }) 
}
function sendContact(){
    var name = $("#contactForm #name").val();
    var email = $("#contactForm #email").val();
    var title = $("#contactForm #subject").val();
    var msg = $("#contactForm #message").val();
    var url = $("#contactForm #url").val();
    var form = $("#contactForm #form").val();
    var html_datos;
    var html_final;

    if (validationContact(name, email)){
        html_datos = '<h2>Nueva Contacto vía Website<h3><h4>Datos Personales</h2><p>Nombre Cliente: ' +  name + '</p><p>Email: ' + email + '</p><p>Título de mensaje: ' + title + '<p><p>Mensaje: ' + msg + '<p><hr><p>Nombre formulario:' + form + '</p><p>URL:' + url+ '</p>';
        html_final = html_datos + '<br><p><h5>Sistema contacto de ubiqua.me</h5></5>';

        sendMail(email, name, html_final);
    }

}
/*Formulario de modal contact*/
function sendForm1(){
    var name = $("#name_form1").val();
    var email = $("#email_form1").val();
    var tlf = $("#tlf_form1").val();
    var url = $("#url_form1").val();
    var form = $("#form_form1").val();
    var html_datos;
    var html_final;

    if (validationForm1(email)){
        html_datos = '<h2>Nueva Contacto vía Website<h3><h4>Datos Personales</h2><p>Nombre Cliente: ' +  name + '</p><p>Email: ' + email + '</p><p>Teléfono: ' + tlf  + '</p><hr><p>Nombre formulario:' + form + '</p><p>URL:' + url+ '</p>';
        html_final = html_datos + '<br><p><h5>Sistema contacto de ubiqua.me</h5></5>';
        
        sendMail(email, name, html_final);
    }

}

/*Formulario de Solicitus de Demo*/
function sendForm2(){
    var name = $("#name_form2").val();
    var email = $("#email_form2").val();
    var tlf = $("#tlf_form2").val();
    var text = $("#text_form2").val();
    var url = $("#url_form2").val();
    var form = $("#form_form2").val();
    var html_datos;
    var html_final;

    if (validationForm2(name, email)){
        html_datos = '<h2>Nueva solicitud de demostración<h3><h4>Datos Personales</h2><p>Nombre Cliente: ' +  name + '</p><p>Email: ' + email + '</p><p>Teléfono: ' + tlf  + '</p><p>Mensaje: ' + text + '</p><hr><p>Nombre formulario:' + form + '</p><p>URL:' + url+ '</p>';
        html_final = html_datos + '<br><p><h5>Sistema contacto de ubiqua.me</h5></5>';

       sendMail(email, name, html_final);
    }

}

function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);

}
function validationContact(name, email){
    var result
    if (name == '' || !validateEmail(email)){
        $("#contactError").css("display", "block");
        $("#name").addClass('required_field');
        $("#email").addClass('required_field');
        result = false;
    }else{
        $("#contactSuccess").css("display", "block");
        $("#contactError").css("display", "none");
        $("#name").removeClass('required_field');
        $("#email").removeClass('required_field');
        $("#submit").css("display", "none");
        $("#contactForm :input").prop("disabled", true);
        result = true;

    }
    return result;
}
function validationForm1(email){
    var result
    if (!validateEmail(email)){
        $("#contactError_form1").css("display", "block");
        $("#email_form1").addClass('required_field');
        result = false;
    }else{
        $("#contactError_form1").css("display", "none");
        $("#contactSuccess_form1").css("display", "block");
        $("#email_form1").removeClass('required_field');
        $("#submit_form1").css("display", "none");
        $("#demo-form :input").prop("disabled", true);
        result = true;

    }
    return result;
}
function validationForm2(name, email){
    var result
    if (name == '' || !validateEmail(email)){
        $("#contactError_form2").css("display", "block");
        $("#name_form2").addClass('required_field');
        $("#email_form2").addClass('required_field');
        result = false;
    }else{
        $("#contactSuccess_form2").css("display", "block");
        $("#contactError_form2").css("display", "none");
        $("#name_form2").removeClass('required_field');
        $("#email_form2").removeClass('required_field');
        $("#submit_form2").css("display", "none");
        $("#demo-form2 :input").prop("disabled", true);
        result = true;

    }
    return result;
}