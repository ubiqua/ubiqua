#coding:utf-8

def client_list():
    return [
        {
            "LOGO": "/img/clientes_bw/arce.jpg",
            "NAME": "Arrocha",
        }, {
            "LOGO": "/img/clientes_bw/arrocha.jpg",
            "NAME": "CG Haseth",
        },{
            "LOGO": "/img/clientes_bw/feduro.jpg",
            "NAME": "Del Día",
        },{
            "LOGO": "/img/clientes_bw/mota.jpg",
            "NAME": "Feduro",
        },{
            "LOGO": "/img/clientes_bw/global.jpg",
            "NAME": "Felipe Motta",
        },{
            "LOGO": "/img/clientes_bw/dilupa.png",
            "NAME": "Impa",
        },{
            "LOGO": "/img/clientes_bw/impadoel.jpg",
            "NAME": "medimex",
        },{
            "LOGO": "/img/clientes_bw/medimex.jpg",
            "NAME": "Metro",
        },{
            "LOGO": "/img/clientes_bw/escoffery.png",
            "NAME": "Tasty Choice",
        },{
            "LOGO": "/img/clientes_bw/tasty.jpg",
            "NAME": "Tshirt",
        },{
            "LOGO": "/img/clientes_bw/cochez.png",
            "NAME": "Wurth",
        },{
            "LOGO": "/img/clientes_bw/wurth.jpg",
            "NAME": "Wurth",
        },
    ]

def brand_list():
    return [
        {
            "LOGO": "/img/brands_bw/bacardi.jpg",
            "NAME": "Bacardi"
        }, {
            "LOGO": "/img/brands_bw/bayer.jpg",
            "NAME": "Bayer"
        }, {
            "LOGO": "/img/brands_bw/flor.jpg",
            "NAME": "Flor de Caña"
        },{
            "LOGO": "/img/brands_bw/glaxo.jpg",
            "NAME": "Grey Goose"
        },{
            "LOGO": "/img/brands_bw/grey.jpg",
            "NAME": "GSK"
        },{
            "LOGO": "/img/brands_bw/her.jpg",
            "NAME": "Hershey's"
        },{
            "LOGO": "/img/brands_bw/novartis.jpg",
            "NAME": "Novartis"
        },{
            "LOGO": "/img/brands_bw/pepsico.jpg",
            "NAME": "Pepsico"
        },{
            "LOGO": "/img/brands_bw/pfizer.jpg",
            "NAME": "Pfizer"
        },{
            "LOGO": "/img/brands_bw/pg.jpg",
            "NAME": "P&G"
        },{
            "LOGO": "/img/brands_bw/saba.jpg",
            "NAME": "Saba"
        },{
            "LOGO": "/img/brands_bw/saralee.jpg",
            "NAME": "Sara Lee"
        },{
            "LOGO": "/img/brands_bw/shell.jpg",
            "NAME": "Shell"
        },
    ]

def industry_list():
    return [
        {
            "ICON": "fa-cutlery",
            "NAME": "Alimentos y bebidas",
            "NAME_EN": "Food & drinks"
        },{
            "ICON": "fa-heartbeat",
            "NAME": "Farmaceútica",
            "NAME_EN": "Pharmaceutical"
        },{
            "ICON": "fa-diamond",
            "NAME": "Cosméticos",
            "NAME_EN": "Cosmetic"
        },{
            "ICON": "fa-truck",
            "NAME": "Artículos de limpieza",
            "NAME_EN": "Cleaning product"
        },{
            "ICON": "fa-cog",
            "NAME": "Maquinaria y repuestos",
            "NAME_EN": "Machinery & spare parts"
        },{
            "ICON": "fa-shopping-bag",
            "NAME": "Textil",
            "NAME_EN": "Textile industry"
        },
    ]

def preBuildPage(page, context, data):
    context.update({
        "CLIENT_LIST": client_list(),
        "BRAND_LIST": brand_list(),
        "INDUSTRY_LIST": industry_list(),
    })
    return context, data
