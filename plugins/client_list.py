#coding:utf-8

def client_list():
    return [
        {
            "LOGO": "/img/clientes/arrocha.png",
            "NAME": "Arrocha",
        }, {
            "LOGO": "/img/clientes/cg_haseth.png",
            "NAME": "CG Haseth",
        },{
            "LOGO": "/img/clientes/del_dia.png",
            "NAME": "Del Día",
        },{
            "LOGO": "/img/clientes/feduro.png",
            "NAME": "Feduro",
        },{
            "LOGO": "/img/clientes/felipe_motta.png",
            "NAME": "Felipe Motta",
        },{
            "LOGO": "/img/clientes/impa.png",
            "NAME": "Impa",
        },{
            "LOGO": "/img/clientes/medimex.png",
            "NAME": "medimex",
        },{
            "LOGO": "/img/clientes/metro.png",
            "NAME": "Metro",
        },{
            "LOGO": "/img/clientes/tasty.png",
            "NAME": "Tasty Choice",
        },{
            "LOGO": "/img/clientes/tshirt.png",
            "NAME": "Tshirt",
        },{
            "LOGO": "/img/clientes/wurth.png",
            "NAME": "Wurth",
        },
    ]

def brand_list():
    return [
        {
            "LOGO": "/img/brands/bacardi.png",
            "NAME": "Bacardi"
        }, {
            "LOGO": "/img/brands/bayer.png",
            "NAME": "Bayer"
        }, {
            "LOGO": "/img/brands/flor.png",
            "NAME": "Flor de Caña"
        },{
            "LOGO": "/img/brands/greygoose.png",
            "NAME": "Grey Goose"
        },{
            "LOGO": "/img/brands/gsk.png",
            "NAME": "GSK"
        },{
            "LOGO": "/img/brands/hersheys.png",
            "NAME": "Hershey's"
        },{
            "LOGO": "/img/brands/novartis.png",
            "NAME": "Novartis"
        },{
            "LOGO": "/img/brands/pepsico.png",
            "NAME": "Pepsico"
        },{
            "LOGO": "/img/brands/pfizer.png",
            "NAME": "Pfizer"
        },{
            "LOGO": "/img/brands/pg.png",
            "NAME": "P&G"
        },{
            "LOGO": "/img/brands/saba.png",
            "NAME": "Saba"
        },{
            "LOGO": "/img/brands/saralee.png",
            "NAME": "Sara Lee"
        },{
            "LOGO": "/img/brands/shell.png",
            "NAME": "Shell"
        },
    ]

def industry_list():
    return [
        {
            "ICON": "fa-cutlery",
            "NAME": "Alimentos y bebidas"
        },{
            "ICON": "fa-heartbeat",
            "NAME": "Farmaceútica"
        },{
            "ICON": "fa-diamond",
            "NAME": "Cosméticos"
        },{
            "ICON": "fa-truck",
            "NAME": "Artículos de limpieza"
        },{
            "ICON": "fa-cog",
            "NAME": "Maquinaria y repuestos"
        },{
            "ICON": "fa-shopping-bag",
            "NAME": "Textil"
        },
    ]

def preBuildPage(page, context, data):
    context.update({
        "CLIENT_LIST": client_list(),
        "BRAND_LIST": brand_list(),
        "INDUSTRY_LIST": industry_list(),
    })
    return context, data
