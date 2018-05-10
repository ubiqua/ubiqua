#coding:utf-8

"""
Cactus forces me to make an entire file to call a one-liner from a template.
"""
def preBuildPage(page, context, data):
    context.update({
        "ERP_IMAGE_LIST": [
                '/img/productos/imp/erp' + str(number+1) + '.png'
                for number in range(6)
            ],
    })
    return context, data
