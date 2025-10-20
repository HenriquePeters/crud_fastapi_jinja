from fastapi import FastAPI, Form, Request, HTTPException, Query
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

itens = []
contador = 1


@app.get("/")
def listar_itens(request: Request, search: Optional[str] = Query(None)):
    if search:
        itens_filtrados = [i for i in itens if search.lower() in i["nome"].lower()]
    else:
        itens_filtrados = itens


    message = request.query_params.get("message")
    message_type = request.query_params.get("type", "info")

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "itens": itens_filtrados,
            "search": search or "",
            "message": message,
            "message_type": message_type,
        },
    )


@app.get("/novo")
def form_criar_item(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


@app.post("/criar")
def criar_item(nome: str = Form(...), descricao: str = Form(...)):
    global contador
    item = {"id": contador, "nome": nome, "descricao": descricao}
    itens.append(item)
    contador += 1
    return RedirectResponse(
        "/?message=Item criado com sucesso!&type=success", status_code=303
    )


@app.get("/editar/{item_id}")
def editar_item(request: Request, item_id: int):
    for item in itens:
        if item["id"] == item_id:
            return templates.TemplateResponse("edit.html", {"request": request, "item": item})
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.post("/atualizar/{item_id}")
def atualizar_item(item_id: int, nome: str = Form(...), descricao: str = Form(...)):
    for item in itens:
        if item["id"] == item_id:
            item["nome"] = nome
            item["descricao"] = descricao
            return RedirectResponse(
                "/?message=Item atualizado com sucesso!&type=success", status_code=303
            )
    return RedirectResponse(
        "/?message=Erro: item não encontrado&type=error", status_code=303
    )


@app.get("/deletar/{item_id}")
def deletar_item(item_id: int):
    for item in itens:
        if item["id"] == item_id:
            itens.remove(item)
            return RedirectResponse(
                "/?message=Item excluído com sucesso!&type=success", status_code=303
            )
    return RedirectResponse(
        "/?message=Erro: item não encontrado&type=error", status_code=303
    )
