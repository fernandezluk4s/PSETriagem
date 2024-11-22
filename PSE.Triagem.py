import datetime

data_atual =datetime.date.today()
data = data_atual
prioridade_idade = None
prioridade = prioridade_idade

class Paciente:
    def __init__(self, nome, idade,data,prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade_idade = prioridade
        if idade>=65:
            self.prioridade = "Com prioridade"
        else:
            self.prioridade = "Sem prioridade"
        self.data = data
        self.codigo = "Baixo risco"
        self.diabetes = diabetes
        self.hipoglicemia = hipoglicemia
        self.coração = coração
        self.resp_alergia = resp_alergia
    
         

    def classificar(self, sintomas):

        # Sintomas 
        #Dores
        if sintomas['dores']['intensidade'] == 'alta':
            self.codigo = 'Amarelo'
            if sintomas['dores']['região'] in ['cabeça','peito']: 
                self.codigo = 'Vermelho'
        if sintomas['dores']['intensidade'] == 'alta'and idade>=65:
            self.codigo = 'Vermelho'
            if sintomas['dores']['região'] in ['cabeça', 'peito'] and idade>=65:
                self.codigo = 'Vermelho'
                self.prioridade = "Prioridade Máxima" 

        #Respiração
        if sintomas['respiração']['falta_de_ar']:
            self.codigo = 'Amarelo'
        if sintomas['respiração']['asma']:
                self.codigo = 'Amarelo'
                if sintomas ['respiração']['asma'] and sintomas['respiração']['falta_de_ar']:
                    self.codigo = 'Vermelho'
        if sintomas['respiração']['falta_de_ar'] and idade >=65:
            self.codigo = 'Vermelho'
            self.prioridade = "Prioridade Máxima"
            if sintomas['respiração']['asma'] and idade >=65:
                self.codigo = 'Vermelho'
                self.prioridade = "Prioridade Máxima"

        #Consciencia - Trauma        
        if sintomas ['perda_consciencia']['trauma']:
            self.codigo = 'Amarelo'
        if sintomas ['perda_consciencia']['perda_de_consciencia'] and sintomas['perda_consciencia']['trauma']:
            self.codigo = 'Vermelho'
            if idade >= 65:
                self.prioridade = 'Prioridade Máxima'
        
        #Digestivo 
        if sintomas ['digestivo']['nausea'] and sintomas ['digestivo']["vomito"]:
            self.codigo = "Amarelo"
            if sintomas['digestivo']['nausea'] and sintomas['digestivo']['vomito'] and sintomas['digestivo']['diarreia']:
                self.codigo = 'Amarelo'
                if sintomas ['digestivo']['nausea'] and sintomas ['digestivo']["vomito"]:
                    self.codigo = "Amarelo"

        #Sangue
        if sintomas['sangue']['diabetes'] or sintomas['sangue']['hipoglicemia']:
            self.codigo = 'Baixo risco'
            if idade >=65:
                self.codigo = 'Amarelo'
        if sintomas ['sangue']['hipoglicemia'] and sintomas['perda_consciencia']['perda_de_consciencia']:
            self.codigo = 'Amarelo'
            if idade >=65:
                self.codigo = 'Vermelho'
                self.prioridade = 'Prioridade Máxima'
       
        #Coração
        if sintomas ['coração']['coração']:
            self.codigo = 'Amarelo'
            if idade >=65:
                self.codigo = 'Vermelho'
        if sintomas ['coração']['coração'] and sintomas['dores']['região'] in ['peito, torax']:
            self.codigo = 'Vermelho'
            self.prioridade = 'Prioridade Máxima'
            print("Indício de ataque cardiaco!")
 
      
    def exibir_informacoes(self):
        print("-----------------------\n")
        print(f"Paciente: {self.nome}\nIdade: {self.idade}\nPrioridade: {self.prioridade}\nCódigo de Risco: {self.codigo}\nData da consulta: {self.data}")
        print("-----------------------")
        print("HISTÓRICO PRÉ-EXISTENTE")
        print(f"Diabetes: {self.diabetes}\nHipoglicemia: {self.hipoglicemia}\nDoença de coração: {self.coração}\nAlergia: {self.resp_alergia}")
       

def verificar_resposta(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in ['sim','não']:
            return resposta
        else:
            print("Resposta inválida, insira sim ou não.")


# Funções para verificar sintomas 
def verificar_dores(intensidade, região):
    return { 'intensidade':intensidade,  'região':região}

def verificar_respiracao(falta_de_ar, asma):
    return {'falta_de_ar': falta_de_ar, 'asma': asma}

def verificar_consciencia(perda_de_consciencia,trauma):
    return{'perda_de_consciencia':perda_de_consciencia, 'trauma':trauma}

def verificar_digestivo(nausea,vomito,diarreia):
    return{'nausea':nausea,'vomito':vomito, 'diarreia':diarreia}

def verificar_sangue(diabetes,hipoglicemia):
    return{'diabetes':diabetes,'hipoglicemia':hipoglicemia}

def verificar_coração(coração):
    return{'coração':coração}

def verificar_alergia(alergia,resp_alergia):
    return{'alergia':alergia,"resp_alergia":resp_alergia}

# Cadastrando cliente e seus sintomas 
nome = input("Qual o nome do paciente? ")
idade = int(input("Qual a idade do paciente? "))
diabetes = verificar_resposta("Diabetes?[sim, não]")
hipoglicemia = verificar_resposta("Hipoglicêmica?[sim, não]")
coração = verificar_resposta ("Doença do coração?[sim,não]")
alergia = verificar_resposta("O paciente tem alguma alergia?[sim, não]")
if alergia == 'sim':
    resp_alergia = input('Qual a alergia?')
else:
    resp_alergia = 'não'
intensidade_dor = input("Qual a intensidade da dor? [baixa, média, alta] ")
regiao_dor = input("Qual a região da dor? ")
falta_de_ar = verificar_resposta("Tem falta de ar? [sim, não]")
asma = verificar_resposta("Tem asma? [sim, não] ")
perda_de_consciencia = verificar_resposta("Houve perda de consciência?[sim, não]")
trauma = verificar_resposta("Houve algum trauma?[sim, não]")
nausea = verificar_resposta("O paciente tem náusea?[sim, não]")
vomito = verificar_resposta("Vômito?[sim, não]")
diarreia = verificar_resposta("Diarreia?[sim, não]")

#Dicionário 
sintomas = {
    'dores': verificar_dores(intensidade_dor, regiao_dor),
    'respiração': verificar_respiracao(falta_de_ar == 'sim', asma == 'sim'),
    'perda_consciencia': verificar_consciencia(perda_de_consciencia =='sim', trauma =='sim'),
    'digestivo': verificar_digestivo(nausea=='sim',vomito =='sim', diarreia =='sim'),
    'sangue': verificar_sangue(diabetes=='sim', hipoglicemia == 'sim'),
    'coração':verificar_coração(coração == 'sim'),
    'alergia': verificar_alergia(alergia == 'sim',resp_alergia)
}
#Instanciando o objeto da classe 
paciente = Paciente(nome, idade, data, prioridade)
paciente.classificar(sintomas)
paciente.exibir_informacoes()