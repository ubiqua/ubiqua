#coding:utf-8
def quotes():
    return [
            {
                "quote": "Voy más bien, metiendo el pedido disque pin pin pin, me siento como James Bond",
                "speaker": "Fidel Barrios",
                "company": "Impa-Doel",
            },{
                "quote": "Mucho mejor porque esperando que contesten el teléfono en facturacion me atrasa muchísimo",
                "speaker": "Fernando",
                "company": "Impa-Doel",
            },{
                "quote": "Yo tomaba 3, 4, o 5 pedidos, después codificaba, y después llamaba a facturación. Ahora todo va saliendo de ya para ya. Voy más rápido y no pierdo tiempo.",
                "speaker": "Lionel",
                "company": "Impa-Doel",
            },{
                "quote": "Quiero darles las gracias a ustedes por lo que han hecho. Desde que uso las tablets he pegado todas mis cuotas. La herramienta Ubiqua ha sido parte de mi éxito laboral. Me ha ayudado a mejorar la calidad de vida para mi familia.",
                "speaker": "Gabriel Samudio",
                "company": "",
            },{
                "quote": "Buenisimo. Ya no me tengo que quedar hasta las 9:00 pm pasando los pedidos.",
                "speaker": "Norma Corro",
                "company": "Supervisora de ventas",
            },{
                "quote": "La aplicación está perfecta. Ya no tengo que llamar al call center para pasar mi pedido.  Tampoco tengo que ir en persona hasta el call center. Me ahorro todo ese tiempo.",
                "speaker": "Patricio Calderón",
                "company": "Arce Avícola",
            }
        ]

def preBuildPage(page, context, data):
    context.update({
        "QUOTE_LIST": quotes(),
    })
    return context, data
