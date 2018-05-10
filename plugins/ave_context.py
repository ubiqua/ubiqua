#coding:utf-8

def ave_quotes():
    return [
        {
            "QUOTE": "Soporte trabaja muy bien. Es un equipo eficiente; atiende rápido las solicitudes. Los felicito",
            "NAME": "Victor Medina",
            "SOURCE": "Farmacias Arrocha",
        },{
            "QUOTE": "Su servicio al cliente es increíble. Nunca había visto una compañía de tecnología que brinde tanto apoyo.",
            "NAME": "Ricardo Mouynes",
            "SOURCE": "Airco",
        },{
            "QUOTE": "Quiero darles las gracias a ustedes por lo que han hecho. Desde que uso las tablets he pegado todas mis cuotas. La herramienta Ubiqua ha sido parte de mi éxito laboral. Me ha ayudado a mejorar la calidad de vida para mi familia.",
            "NAME": "Gabriel Samudio",
            "SOURCE": "Agencias Feduro",
        },
    ]

def preBuildPage(page, context, data):
    context.update({
        "AVE_QUOTES": ave_quotes(),
    })
    return context, data
