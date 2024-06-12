def sidebar_collapsed(request):

    url_da_pagina = str(request.build_absolute_uri())

    in_trabalho = False
    in_pessoal = False
    pagina_url = ""

    lista_trabalho = ["/areatrabalhador/", "/tarefas/", "/compromissos/"]

    lista_pessoal = ["/areapessoal/", "/dieta/", "/lista_compras/", "/lista_desejos/", "/plano_academia/"]

    for item in lista_trabalho:
        if item in url_da_pagina:
            in_trabalho = True
            pagina_url = item

    if not in_trabalho:
        for item in lista_pessoal:
            if item in url_da_pagina:
                in_pessoal = True
                pagina_url = item

    return {"in_pessoal": in_pessoal, "in_trabalho": in_trabalho, "pagina_url": pagina_url}