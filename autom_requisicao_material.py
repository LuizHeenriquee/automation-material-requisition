import pyautogui
import pyperclip
from time import sleep

# Função para saber quantos materiais o servidor deseja retirar
def numeroDeMateriais():
    while True:
        numero_de_materiais_str = pyautogui.prompt("Quantos materiais você vai retirar? (Máximo 10)")

        try:
            numero_de_materiais = int(numero_de_materiais_str)

            if len(numero_de_materiais_str) < 1:
                pyautogui.alert("Você não digitou nada. Por favor informe quantos materiais serão retirados.")
                continue
            elif 1 <= numero_de_materiais <= 10:
                break
            else:
                pyautogui.alert("Quantidade indisponível. O número máximo de itens é 10 e o mínimo 1.")
        except(ValueError, TypeError):
            pyautogui.alert("Entrada inválida. Por favor, digite um número entre 1 e 10.")

    return numero_de_materiais

# Função para saber o nome e a quantidade do material em questão
def nomeMateriaisQuantidade(numero_materiais):
    materiais_e_quantidade = []

    for i in range(numero_materiais):
        nome_material = ""
        while True:
            nome_material = pyautogui.prompt(f"Digite o nome do {i+1}º material")
            if len(nome_material) < 1:
                pyautogui.alert("Você não digitou nada. Por favor, informe o nome do material.")
                continue
            elif nome_material.isdigit():
                pyautogui.alert("Apenas números não são suportados. Por favor, informe o nome correto do material")
                continue
            break

        while True:
            quantidade_str = pyautogui.prompt(f"Digite a quantidade do material: {nome_material.upper()}")
            if len(quantidade_str) < 1:
                pyautogui.alert("Você não digitou nada. Por favor, informe a quantidade do material.")
                continue
            elif not quantidade_str.isdigit():
                pyautogui.alert("Strings são inválidas. Por favor, informe com números a quantidade.")
                continue
            break

        try:
            quantidade = int(quantidade_str)
            materiais_e_quantidade.append((nome_material, quantidade))
        except(ValueError, TypeError):
            pyautogui.alert(f"Quantidade inválida para o material {nome_material}. Por favor, digite um número válido.")
    return materiais_e_quantidade

# Função para definir de onde virá o(s) material(is) selecionado(s)
def tiposDeMateriais():
    tipo_de_material = pyautogui.confirm("Informe o tipo de material:", buttons=["Expediente", "Limpeza", "Copa e Cozinha", "Gêneros de Alimentação", "Outros"])
    
    match tipo_de_material:
        case "Expediente":
            pyautogui.click(678,755, duration=1)
            pyautogui.write(' X')
            pyautogui.press('del')
        case "Limpeza":
            pyautogui.click(677,777, duration=1)
            pyautogui.write(' X')
            pyautogui.press('del')
        case "Copa e Cozinha":
            pyautogui.click(680,797, duration=1)
            pyautogui.write('X ')
            pyautogui.press('del')
        case "Gêneros de Alimentação":
            pyautogui.click(678,819, duration=1)
            pyautogui.write(' X')
            pyautogui.press('del')
        case "Outros":
            pyautogui.click(678,839, duration=1)
            pyautogui.write(' X')
            pyautogui.press('del')
            pyautogui.click(747,836, duration=1)
            while True:
                material_outros = pyautogui.prompt("Digite o tipo do material:")
                
                if len(material_outros) < 1:
                    pyautogui.alert("Você não digitou nada. Por favor, informe o tipo do material.")
                    continue
                elif material_outros.isdigit():
                    pyautogui.alert("Apenas números não são suportados. Por favor, informe o tipo correto do material")
                    continue
                pyautogui.write(material_outros)
                pyautogui.press('del', presses=13)
                break
        case _:
            pyautogui.alert('Algo deu errado.')
    return tipo_de_material

# Função para o mouse iniciar a inserção do processo
def inserirProcesso():
    pyautogui.click(1392,477, duration=1) # Original
    # pyautogui.click(1384,644, duration=1) # posição do botão no homologa (para testes)

# Função para o mouse cadastrar o protocolo
def cadastrarProtocolo():
    pyautogui.click(1384,403)
    pyautogui.click(910,408,duration=1)
    pyautogui.click(890,544,duration=1)
    pyautogui.click(816,448,duration=1)
    pyautogui.press('down', presses=22)
    pyautogui.press('enter')
    pyautogui.click(1006,517,duration=1)

# Função para escrever o nome do requisitante
def nomeRequisitante():
    pyautogui.click(886,887,duration=1)
    while True:
        setor_requisitante = pyautogui.prompt("Qual o nome do setor requisitante?")

        if len(setor_requisitante) < 1:
            pyautogui.alert("Você não digitou nada. Por favor, informe o nome do setor.")
            continue
        elif setor_requisitante.isdigit():
            pyautogui.alert("Apenas números não são suportados. Por favor, informe o nome correto do setor")
            continue

        pyperclip.copy(setor_requisitante)
        pyautogui.hotkey('ctrl', 'v')
        break

# Função para escrever o(s) nome(s) e quantidade(s) do(s) material(is) no protocolo
def escreverMateriais(numero_materiais, nomeMateriais_e_quantidade):
    pyautogui.click(739,1018,duration=1)
    for i, (nome_material, quantidade) in enumerate(nomeMateriais_e_quantidade):
        pyperclip.copy(nome_material)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('down')
        pyperclip.copy(quantidade)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('down', presses=2)

# Função para ir para o fim do documento
def fimDocumento():
    pyautogui.hotkey('ctrl', 'end')

# Função para saber se o requisitante irá realizar a retirada
def retirada():
    retirada = pyautogui.confirm("O próprio solicitante irá fazer a retirada?", buttons=["Sim", "Não"])

    signatario = ""

    match retirada:
        case "Sim":
            pyautogui.click(679,887,duration=1)
            pyautogui.write('X')
        case "Não":
            pyautogui.click(679,908,duration=1)
            pyautogui.write('X')
            cargo = ""
            signatario = pyautogui.prompt("Digite o nome do signatário")
            cargo = pyautogui.prompt("Digite o cargo do signatário informado")
            pyautogui.click(930,1009, duration=1)
            pyautogui.press('home')
            pyautogui.press('del', presses=200)      
            pyperclip.copy(signatario)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('shiftleft', 'shiftright', 'home')
            pyautogui.hotkey('ctrl', 'b')
            sleep(1)
            pyautogui.press('end')
            pyautogui.press('enter')
            pyperclip.copy(cargo)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('shiftleft', 'shiftright', 'home')
            pyautogui.hotkey('ctrl', 'b')
                        
        case _:
            pyautogui.alert("Algo deu errado")

    return retirada, signatario

# Função para confirmar o envio do protocolo
def aprovarProtocolo(salvarProtolo):
    aprovar = pyautogui.confirm("O protocolo pode ser salvo?", buttons=["Sim","Não"])

    match aprovar:
        case "Sim":
            salvarProtocolo()
        case "Não":
            pyautogui.alert("Edite o que for necessário e prossiga com o protocolo de maneira MANUAL.")
            exit()
        case _:
            pyautogui.alert("Algo deu errado.")

# Função para compartilhar com o setor
def compartilharComSetor():
    pyautogui.click(535,553, duration=1)
    pyautogui.hotkey('ctrl', 'end')
    pyautogui.click(760,750, duration=1)
    pyautogui.press('down')
    pyautogui.press('enter')

# Função para salvar o protocolo
def salvarProtocolo():
    pyautogui.click(997,878, duration=1)

numero_materiais = numeroDeMateriais()
nomeMateriais_e_quantidade = nomeMateriaisQuantidade(numero_materiais)
inserirProcesso()
cadastrarProtocolo()
tiposDeMateriais()
nomeRequisitante()
escreverMateriais(numero_materiais, nomeMateriais_e_quantidade)
fimDocumento()
tipo_retirada, signatario = retirada()
compartilharComSetor()
aprovarProtocolo(salvarProtocolo)
salvarProtocolo()

pyautogui.alert('Protocolo salvo com sucesso!')

print('************************************')
print('* Cadastro finalizado com sucesso! *')
print('************************************')