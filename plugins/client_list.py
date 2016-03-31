#coding:utf-8

def client_list():
    placeholder_item = {
        "LOGO": "http://placehold.it/585x585",
        "NAME": "Lorem Ipsum",
        "TITLE": "Digital Media"
    }
    return [placeholder_item for counter in range(8)]


def preBuildPage(page, context, data):
    context.update({
        "CLIENT_LIST": client_list(),
    })
    return context, data
