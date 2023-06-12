regioes = {
    1: "Norte",
    2: "Nordeste",
    3: "Sudeste",
    4: "Sul",
    5: "Centro-Oeste"
}

for codigo, regiao in regioes.items():
    print(f"[{codigo}] {regiao}")

regiao_escolhida = int(input("De qual região do Brasil você é? "))

estados = {
        1: ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"],
        2: ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"],
        3: ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"],
        4: ["Paraná", "Rio Grande do Sul", "Santa Catarina"],
        5: ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]
    }

for estado_numero, estado in enumerate(estados[regiao], start=1):
    print(f"[{estado_numero}] {estado}")


estado_escolhido_numero = int(input("Qual o número do seu estado? "))


estados = {
    1: ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"],
    2: ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"],
    3: ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"],
    4: ["Paraná", "Rio Grande do Sul", "Santa Catarina"],
    5: ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]
}

estado_escolhido = estados[regiao_escolhida][estado_escolhido_numero - 1]

regioes = {
    1: "Norte",
    2: "Nordeste",
    3: "Sudeste",
    4: "Sul",
    5: "Centro-Oeste"
}

print("Você é da região", regioes[regiao_escolhida], "e do estado", estado_escolhido)
