#coding:utf-8

def client_list():
    return [
        {
            "LOGO": "/img/client/pepsico.jpg",
            "NAME": "Pepsico",
        }, {
            "LOGO": "/img/client/mota.jpg",
            "NAME": "Motta",
        },{
            "LOGO": "/img/client/pfizer.jpg",
            "NAME": "Pfizer",
        },{
            "LOGO": "/img/client/pg.jpg",
            "NAME": "P&G",
        },{
            "LOGO": "/img/client/shell.jpg",
            "NAME": "Shell",
        },{
            "LOGO": "/img/client/bacardi.jpg",
            "NAME": "Bacardi",
        },{
            "LOGO": "/img/client/bayer.jpg",
            "NAME": "Bayer",
        },{
            "LOGO": "/img/client/flor.jpg",
            "NAME": "Flor",
        },{
            "LOGO": "/img/client/grey.jpg",
            "NAME": "Grey",
        },{
            "LOGO": "/img/client/glaxo.jpg",
            "NAME": "Glaxo",
        },{
            "LOGO": "/img/client/novartis.jpg",
            "NAME": "Novartis",
        },{
            "LOGO": "/img/client/saba.jpg",
            "NAME": "Saba",
        },{
            "LOGO": "/img/client/saralee.jpg",
            "NAME": "Saralee",
        },
    ]


def preBuildPage(page, context, data):
    context.update({
        "CLIENT_LIST": client_list(),
    })
    return context, data
