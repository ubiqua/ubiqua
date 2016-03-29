#coding:utf-8


def services_list():
    return [
        {
            "title": "Soporte",
            "text": "Soporte técnico directo a usuarios y gerentes:",
            "icon": "fa-life-ring",
        },{
            "title": "Solución Manejada",
            "text": "Olvídate de comprar servidores nuevos o contratar más personal.",
            "icon": "fa-server",
        },{
            "title": "Seguro",
            "text": "Información bajo las mejores prácticas de seguridad",
            "icon": "fa-lock",
        },{
            "title": "Actualizaciones",
            "text": "Nuestras soluciones cada vez son más eficientes",
            "icon": "fa-arrow-circle-up",
        },{
            "title": "Validación",
            "text": "Todas nuestras mejoras son validadas por usuarios para asegurarnos que sean fáciles de usar",
            "icon": "fa-check-circle",
        },
    ]

def preBuildPage(page, context, data):
    context.update({
        "SERVICES_LIST": services_list(),
    })
    return context, data
