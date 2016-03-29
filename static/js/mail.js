jQuery(function($){

  $("#contactForm").submit(function(event){
    event.preventDefault();

    var name = $("#contactForm #name").val();
    var mail = $("#contactForm #email").val();
    var title = $("#contactForm #subject").val();
    var text = $("#contactForm #message").val();

    var message = "<h1>Nuevo Contacto via Web</h1>" +
      "<p>Nombre: " + name + "</p>" +
      "<p>Correo: " + mail + "</p>" +
      "<p>Mensaje: " + text + "</p>";

    // Public Keys and Values
    var form_data = {
      "to": "ghurtado@ubiqua.me",
      "toname": "Ubiqua",
      "subject": title,
      "html": message,
      "from": mail,
      "fromname": name
    };

    $.ajax({
        type: 'POST',
        url: "https://formspree.io/gregesf@reseller.bluetideconsulting.com",
        data: form_data,
        dataType: "json"
    })
    .always(function(){ alert("Mensaje enviado con exito"); })
    ;
  })
})
