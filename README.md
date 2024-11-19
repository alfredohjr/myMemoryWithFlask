# MyMemoryWithFlask

Um estudo sobre o uso de filas em memória usando Flask.

### Uma história para contextualizar

Estava estudando sobre filas no Redis e resolvi implementar isso em Rust, entretanto não sei o necessário para fazer isso em Rust, então resolvi dar uma estudada no assunto usando Python mesmo e consegui, o próximo passo é implementar ainda em python mas usando sockets para comunicação entre os clientes e o servidor, e por fim implementar em Rust.

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python server.py
```

### Rotas.

- `GET /<database>` - Retorna todos os itens da fila.
- `GET /<database>/fifo` - Retorna e remove o primeiro item da fila.
- `POST /<database>` - Adiciona um item na fila.
- `PUT /<database>/<id>` - Atualiza o item da fila.
- `DELETE /<database>/<id>` - Remove o item da fila.

## Observações.

- O banco de dados é um dicionário em memória, então ao reiniciar o servidor os dados são perdidos.

## Ainda falta implementar.

- [ ] Testes.
- [ ] Persistência dos dados.

## Outras ideias.

- [ ] Implementar uma fila usando o queue do Python.
- [ ] Implementar a expiração dos itens da fila, por tempo(deve ser configurável) ou por quantidade de itens(este foi uma ideia do Copilot).
