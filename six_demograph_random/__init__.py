from otree.api import *
from collections import defaultdict
import random



def make_field(label):
    return models.StringField(
        choices=[[1, 'Muy inapropiado socialmente'], [2, 'Algo inapropiado socialmente'], [3,'Algo apropiado socialmente'], [4,'Muy apropiado socialmente']],
        label=label,
        widget=widgets.RadioSelect
    )


def SDO_make_field(label):
    return models.StringField(
        choices=[[1, '1. Fuertemente en contra'], [2, '2. Algo en contra'], [3,'3.Ligeramente en contra'], [4,'4. neutral'],
        [5,'5. Ligeramente a favor'], [6,'6. Algo a favor'], [7,'7. Fuertemente a favor']],
        label=label,
        widget=widgets.RadioSelect
    )

def SDO_make_inverted_field(label):
    return models.StringField(
        choices=[[7, '1. Fuertemente en contra'], [6, '2. Algo en contra'], [5,'3.Ligeramente en contra'], [4,'4. neutral'],
        [3,'5. Ligeramente a favor'], [2,'6. Algo a favor'], [1,'7.Fuertemente a favor']],
        label=label,
        widget=widgets.RadioSelect
    )

def SDP_make_field(label):
    return models.StringField(
        choices=[[1, '1. No me describe nada'], [2, '2'], [3,'3'], [4,'4. Algunas veces'], [5,'5'], [6,'6'], [7,'7 Me describe completamente']],
        label=label,
        widget=widgets.RadioSelect
    )

def SDP_make_inverted_field(label):
    return models.StringField(
        choices=[[7, '1. No me describe nada'], [6, '2'], [5,'3'], [4,'4. Algunas veces'], [3,'5'], [2,'6'], [1,'7 Me describe completamente']],
        label=label,
        widget=widgets.RadioSelect
    )



class C(BaseConstants):
    NAME_IN_URL = 'six_demograph_random'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    PAGO_BASE = 5000


class Subsession(BaseSubsession):
    
    pass
    
class Group(BaseGroup):

    pass

class Player(BasePlayer):
    age = models.IntegerField(label='¿Cuál es su edad?', min=18, max=125)
    gender = models.StringField( 
        choices=[['Masculino', 'Masculino'], ['Femenino', 'Femenino'],['Otro','Otro']],
        label='¿Cuál es su género?',
        widget=widgets.RadioSelect)
    income = models.StringField(choices =[[1, "$0 a $150.0000"], [2, "$151.000 a $270.000"], [3, "$271.000 a $460.000"], [4, "$461.000 a $810.000"],
    [5, "$811.000 a 1.4 Millones"],[6, "1.5 Millones a 2.4 Millones"],[7, "2.5 Millones o más"]],
    label="¿Cuál es el ingreso familiar de su hogar?", widget=widgets.RadioSelect)
    educacion = models.StringField(choices=[[0, 'Sin estudios formales'], [1, 'Básica completa'], [2, 'Media Completa'],
    [3, 'Educación superior técnica o universidaria completa'],[4, 'Postgrado completo']],
    label = 'Con respecto al jefe de su hogar: ¿Cuál es el mayor nivel educacional completado?', widget= widgets.RadioSelect)
    SDO7_1=SDO_make_field('Algunos grupos de personas deben ser forzados a quedarse en su lugar')
    SDO7_2=SDO_make_field('Está bien que ciertos grupos estén arriba y otros grupos estén abajo')
    SDO7_3=SDO_make_field('En una sociedad ideal algunos grupos deben estar arriba y otros gruposdeben estar abajo')
    SDO7_4=SDO_make_field('Algunos grupos de personas son simplemente inferiores a otros grupos')
    SDO7_5=SDO_make_inverted_field('Los grupos que están abajo en la sociedad merecen tener lo mismo que los grupos que están arriba')
    SDO7_6=SDO_make_inverted_field('Ningún grupo debiera dominar en la sociedad')
    SDO7_7=SDO_make_inverted_field('Los grupos que están abajo no debieran ser forzados a mantenerse en su posición')
    SDO7_8=SDO_make_inverted_field('Que algunos grupos dominen por sobre otros es poco ético')
    SDO7_9=SDO_make_field('No debiéramos defender la igualdad entre distintos grupos')
    SDO7_10=SDO_make_field('No debiéramos tratar de garantizar que todos los grupos tengan la misma calidad de vida')
    SDO7_11=SDO_make_field('Es injusto intentar que haya igualdad entre todos los grupos')
    SDO7_12=SDO_make_field('La igualdad entre grupos no debiera ser nuestro objetivo principal')
    SDO7_13=SDO_make_inverted_field('Debiéramos trabajar para que todos los grupos tengan la misma oportunidad de éxito en la sociedad')
    SDO7_14=SDO_make_inverted_field('Debiéramos hacer todo lo posible por igualar las condiciones de diferentes grupos')
    SDO7_15=SDO_make_inverted_field('Sin importar qué tan difícil sea, debiéramos esforzarnos por asegurar que todos los grupos tengan la misma oportunidad en la vida')
    SDO7_16=SDO_make_inverted_field('La igualdad entre los grupos debiera ser nuestro ideal')
    interes = models.StringField(choices=[[5, 'Muy interesado'], [4, 'Bastante interesado'], [3, 'Algo interesado'], [2, 'No muy interesado'], [1, 'Nada interesado']],
    widget=widgets.RadioSelect, label= "")
    ideologia=models.StringField(label="Habitualmente la gente se identifica como 'izquierda', 'derecha' o 'centro' para explicar su ideología política. indique cuál es su ideología siendo 1 'Muy de izquierda' y 10 'muy de derecha'",
    choices=[[1, '1.Muy de izquierda'],[2, '2'],[3,'3'],[4,'4'],[5,'Centro'],[6,'6'],[7,'7'],[8,'8'],[9,'9'],[10,'10 Muy de derecha'],[0, 'Sin ideología']],
    widget=widgets.RadioSelect)
    comentario_lider = models.LongStringField(label= "Señale qué sentimientos y/o pensamientos le inspira su líder durante el juego", blank=True)
    comentario_otro = models.LongStringField(label="Señale qué sentimientos y/o pensamientos le inspira la pareja con la que Ud. jugó", blank=True)
    comentarios = models.LongStringField(label="Si tiene algún comentario o pensamiento sobre este experimento, puede escribirlo aquí", blank=True)
    beliefs_your_group_final = models.IntegerField(label='¿Cuánto crees que los miembros de tu equipo destruyeron?', min=0, max=6000)
    beliefs_your_leader_final = models.IntegerField(label='¿Cuánto crees que el lider de tu equipo destruyó?', min=0, max=6000)
    beliefs_other_followers_final = models.IntegerField(label='Sobre los seguidores del otro equipo: Cuánto crees que han destruído?', min=0, max=6000)
    beliefs_other_leader_final = models.IntegerField(label='Sobre el lider del otro equipo: cuánto crees que destruyó?', min=0, max=6000)
    reelection = models.StringField(choices=[[1, 'Sí'], [0, 'No']])
    SDO7_TRUE = models.BooleanField()
    norms_elicitation3_1 = make_field('Destruir $0')
    norms_elicitation3_2 = make_field('Destruir entre $100 y menos de $1000')
    norms_elicitation3_3 = make_field('Destruir $1000')
    norms_elicitation3_4 = make_field('Destruir entre $1100 y $2900')
    norms_elicitation3_5 = make_field('Destruir la mitad')
    norms_elicitation3_6 = make_field('Destruir entre $3100 y $5900')
    norms_elicitation3_7 = make_field('Destruir todo')
    acierto_norma3_1 = models.IntegerField()
    acierto_norma3_2 = models.IntegerField()
    acierto_norma3_3 = models.IntegerField()
    acierto_norma3_4 = models.IntegerField()
    acierto_norma3_5 = models.IntegerField()
    acierto_norma3_6 = models.IntegerField()
    acierto_norma3_7 = models.IntegerField()
    acierto_norma3_8 = models.IntegerField()
    random_JODPago = models.IntegerField(blank=True, null=True)
    random_norms = models.IntegerField(blank=True, null=True)
    area_estudio = models.StringField(choices=[['Arquitectura y Arte','Arquitectura y Arte'],['Comunicaciones', 'Comunicaciones'],
    ['Ciencias de la salud', 'Ciencias de la salud'],['Derecho','Derecho'],['Diseño','Diseño'],
    ['Economía y Negocios','Economía y Negocios'], ['Educación','Educación'],['Gobierno','Gobierno'],['Ingeniería','Ingeniería'],
    ['Psicología','Psicología']])
    SDP1 = SDP_make_field('Disfruto tener el control sobre otros')
    SDP2 = SDP_make_field('A menudo intento salirme con la mía, sin importar lo que quieran los demás')
    SDP3 = SDP_make_field('Estoy dispuesto a utilizar tácticas agresivas para salirme con la mía')
    SDP4 = SDP_make_field('Intento controlar a los demás en lugar de permitir que me controlen a mí')
    SDP5 = SDP_make_inverted_field('NO tengo una personalidad enérgica ni dominante')
    SDP6 = SDP_make_inverted_field('Otros saben que es mejor dejarme salirme con la mía')
    SDP7 = SDP_make_inverted_field('NO me gusta tener autoridad sobre otras personas')
    SDP8 = SDP_make_field('Algunas personas me tienen miedo')
    risk_aversion = models.IntegerField(
        choices=[[1, '100% de probabilidad de ganar $720'],
                 [2, '50% de probabilidad de ganar $1080 y 50% de ganar $540'],
                 [3, '50% de probabilidad de ganar $1440 y 50% de ganar $360'],
                 [4, '50% de probabilidad de ganar $1800 y 50% de ganar $180'],
                 [5, '50% de probabilidad de ganar $2160 y 50% de ganar $0']],
        label='',
        widget=widgets.RadioSelect
    ) 


# FUNCTIONS


# PAGES

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class Demographics2(Page):
    form_model = 'player'
    form_fields = ['income', 'educacion']

class BFI2_XS(Page):
    form_model = 'player'
    form_fields= [f'BFI2_XS_{i}' for i in range (1, 16)]  

class SDO7_1(Page):
    form_model = 'player'
    form_fields = [f'SDO7_{i}' for i in range (1,9)]

class SDO7_2(Page):
    form_model = 'player'
    form_fields = [f'SDO7_{i}' for i in range (9,17)]


class interest(Page):
    form_model = 'player'
    form_fields = ['interes']


class politics(Page):
    form_model = 'player'
    form_fields = ['ideologia']

class comentario(Page):
    form_model = 'player'
    form_fields = ['comentario_lider', 'comentario_otro','comentarios']

class relection(Page):
    form_model = 'player'
    form_fields = ['reelection']


class norms_elicitation_final(Page):
    form_model = 'player'
    form_fields= ['norms_elicitation3_1', 'norms_elicitation3_2', 'norms_elicitation3_3','norms_elicitation3_3','norms_elicitation3_4',
    'norms_elicitation3_4', 'norms_elicitation3_5', 'norms_elicitation3_6','norms_elicitation3_7']


class beliefs_your_group_final(Page):
    form_model = 'player'
    
    @staticmethod
    def get_form_fields(player: Player):
        if player.participant.group_role == 'seguidor':
            return ['beliefs_your_leader_final', 'beliefs_your_group_final']
        else:
            return ['beliefs_your_group_final']
    

class beliefs_other_group_final(Page):
    form_model = 'player'
    form_fields = ['beliefs_other_leader_final', 'beliefs_other_followers_final']
       
class final(Page):
    pass

class reelection(Page):
    form_model = 'player'
    form_fields = ['reelection']

class risk_aversion(Page):
    form_model = 'player'
    form_fields = ['risk_aversion']

    

class CalcularPagos(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        for player in subsession.get_players():
            acierto_norms = []
            aciertos_index = []
            JOD_PagoFinal = []

            # 1. Aciertos en normas
            for round_num in range(1, 4):
                for i in range(1, 8):
                    val = getattr(player.participant, f'acierto_norma{round_num}_{i}', None)
                    if val is not None:
                        acierto_norms.append(val)
                        aciertos_index.append((round_num, i))

            # 2. Endownment final por ronda
            for round_num in range(1, 19):
                val = getattr(player.participant, f'endownment_final{round_num}', None)
                if val is not None:
                    JOD_PagoFinal.append((round_num, val))

            # 3. Escoger valores aleatorios
            if acierto_norms:
                idx = random.randrange(len(acierto_norms))
                norm_val = acierto_norms[idx]
                norm_round, norm_q = aciertos_index[idx]
            else:
                norm_val = 0
                norm_round = 0
                norm_q = 0

            if JOD_PagoFinal:
                jod_round, jod_val = random.choice(JOD_PagoFinal)
            else:
                jod_round, jod_val = 0, 0

            # 4. Guardar info persistente
            player.participant.selected_jod_round = jod_round
            player.participant.selected_jod_value = jod_val
            player.participant.selected_norm_round = norm_round
            player.participant.selected_norm_question = norm_q
            player.participant.selected_norm_value = norm_val

            # 5. Calcular pago
            if norm_val == 1:
                player.payoff = C.PAGO_BASE + jod_val + 1000
            else:
                player.payoff = C.PAGO_BASE + jod_val

            # 6. Debug
            print(f"[{player.participant.code}] Norm round={norm_round}, question={norm_q}, value={norm_val}")
            print(f"[{player.participant.code}] JOD round={jod_round}, value={jod_val}")
            print(f"[{player.participant.code}] Final payoff={player.payoff}")

 
 
class Pregunta_Facultad(Page):
    form_model = 'player'
    form_fields = ['area_estudio']


class SDP(Page):
    form_model = 'player'
    form_fields = [f'SDP{i}' for i in range (1, 9)]


page_sequence = [beliefs_your_group_final, beliefs_other_group_final, CalcularPagos, Demographics, Demographics2, risk_aversion ,
SDP, Pregunta_Facultad, SDO7_1, SDO7_2, interest, politics, reelection, comentario, final] 
