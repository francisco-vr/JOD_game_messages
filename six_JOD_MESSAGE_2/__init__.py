from otree.api import *
from collections import defaultdict
import random
import json
from statistics import mode, StatisticsError

def make_field(label):
    return models.StringField(
        choices=[[1, 'Muy inapropiado socialmente'], [2, 'Algo inapropiado socialmente'], [3,'Algo apropiado socialmente'], [4,'Muy apropiado socialmente']],
        label=label,
        widget=widgets.RadioSelect
    )


class C(BaseConstants):
    NAME_IN_URL = 'six_JOD_MESSAGE_2'
    PLAYERS_PER_GROUP = 3 
    NUM_ROUNDS = 9
    PASSWORD = 'LEMCICS'


class Subsession(BaseSubsession):
    promedio_grupoklee = models.FloatField()
    promedio_grupokandinski = models.FloatField()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    evaluacion = models.StringField(choices=[[1,'Muy desagradable'],[2 , 'Desagradable'], [3, 'ni agradable ni desagradable'], [4, 'Agradable'], [5, 'Muy Agradable']],
    label= '¿Cómo calificas esta imagen?', widget=widgets.RadioSelect)
    punished_player_id = models.IntegerField(initial=None, blank=True, null=True)
    endownment = models.IntegerField(initial=6000, max = 6000)
    agression = models.IntegerField(min=0, max=6000, initial=0)
    agression_lider = models.IntegerField()
    endownment_final = models.IntegerField()
    agresion_guardada = models.IntegerField()
    leader_message = models.StringField( 
        choices=[['No le destruyas dinero', 'No le destruyas dinero'],
        ['Deberías destruirle la mitad del dinero', 'Deberías destruirle la mitad del dinero'],
        ['Deberías destruirle todo el dinero', 'Deberías destruirle todo el dinero'],
        ['Puedes hacer lo que prefieras','Puedes hacer lo que prefieras'],
        ['Sugiero destruirle la mitad del dinero', 'Sugiero destruirle la mitad del dinero'],
        ['Sugiero destruirle todo el dinero', 'Sugiero destruirle todo el dinero'],
        ['Sugiero destruirle $1.000', 'Sugiero destruirle $1.000'],
        ['Deberías destruirle $1.000','Deberías destruirle $1.000']],label='¿Cuál mensaje les enviarás a tus seguidores?',
        widget=widgets.RadioSelect, blank=True)
    norms_elicitation4_1 = make_field('Destruir $0')
    norms_elicitation4_2 = make_field('Destruir entre 100 y 1000')
    norms_elicitation4_3 = make_field('Destruir entre 1100 y 2000')
    norms_elicitation4_4 = make_field('Destruir entre 2100 y 3000')
    norms_elicitation4_5 = make_field('Destruir entre 3100 y 4000')
    norms_elicitation4_6 = make_field('Destruir entre 4100 y 5000')
    norms_elicitation4_7 = make_field('Destruir entre 5100 y 6000')
    norms_elicitation5_1 = make_field('Destruir $0')
    norms_elicitation5_2 = make_field('Destruir entre 100 y 1000')
    norms_elicitation5_3 = make_field('Destruir entre 1100 y 2000')
    norms_elicitation5_4 = make_field('Destruir entre 2100 y 3000')
    norms_elicitation5_5 = make_field('Destruir entre 3100 y 4000')
    norms_elicitation5_6 = make_field('Destruir entre 4100 y 5000')
    norms_elicitation5_7 = make_field('Destruir entre 5100 y 6000')
    norms_elicitation6_1 = make_field('Destruir $0')
    norms_elicitation6_2 = make_field('Destruir entre 100 y 1000')
    norms_elicitation6_3 = make_field('Destruir entre 1100 y 2000')
    norms_elicitation6_4 = make_field('Destruir entre 2100 y 3000')
    norms_elicitation6_5 = make_field('Destruir entre 3100 y 4000')
    norms_elicitation6_6 = make_field('Destruir entre 4100 y 5000')
    norms_elicitation6_7 = make_field('Destruir entre 5100 y 6000')
    beliefs_other_followers3 = models.IntegerField(label='Sobre los seguidores del otro equipo: Cuánto crees que destruirán?', min = 0,  max = 6000)
    beliefs_other_leader3 = models.IntegerField(label='¿Sobre el lider del otro equipo: Cuánto crees que destruirá?', min = 0, max = 6000)
    beliefs_your_leader3 = models.IntegerField(label='¿Cuánto crees que el lider de tu equipo destruirá?', min = 0, max = 6000)
    beliefs_your_group3 = models.IntegerField(label='¿Cuánto crees que los miembros de tu equipo destruirán?', min = 0, max = 6000)
    beliefs_other_followers4 = models.IntegerField(label='Sobre los seguidores del otro equipo: Cuánto crees que han destruído en promedio?', min = 0,  max = 6000)
    beliefs_other_leader4 = models.IntegerField(label='Sobre el lider del otro equipo: cuánto crees que ha destruído?', min = 0,  max = 6000)
    beliefs_your_leader4 = models.IntegerField(label='¿Cuánto crees que el lider de tu equipo ha destruído?', min = 0,  max = 6000)
    beliefs_your_group4 = models.IntegerField(label='¿Cuánto crees que los miembros de tu equipo han destruído?', min = 0,  max = 6000)
    promedio_grupokandinski = models.IntegerField()
    promedio_grupoklee = models.IntegerField()
    comprension1 = models.StringField(choices=[[0,'$7.000: $3.000 por el juego de la destrucción y 4.000 por la tarea de predicción'], 
    [1, '$7.000:  $6.000 por el juego de la destrucción y $1.000 por la tarea de predicción'], [0, '$5.000: Sólo se paga la tarea de predicción'],
    [0, '$12.000 fijo, sin importar las actividades'], [0,'$1.000: sólo por la tarea de predicción']], widget=widgets.RadioSelect, blank=True, label=' ')
    comprension2 = models.StringField(choices=[[0,'I y II'],[0, 'II y III'], [0, 'I y III'],
    [0, 'Sólo III'], [1, 'Sólo IV']],
    label=' ', widget=widgets.RadioSelect)
    intentos_fallidos1 = models.IntegerField(initial=0)
    password_input1 = models.StringField(blank=True, initial="", label="Contraseña")
    intentos_fallidos2 = models.IntegerField(initial=0)
    password_input2 = models.StringField(blank=True, initial="", label="Contraseña")
    promedio_grupal = models.IntegerField()
    intentos_fallidos = models.IntegerField(initial=0)
    password_input = models.StringField(blank=True)
    comprension3 = models.StringField(choices=[[0,'$0'], [0, '$60.000'], [0, '$12.000'], [1, '$5.000'], [0,'Ninguna de las anteriores']], widget=widgets.RadioSelect, blank=True, label=' ')
    comprension4 = models.StringField(choices=[[0,'$0'], [0, '$3.500'], [0, '$5.000'], [0, '$7.000'], [1,'$10.000']], widget=widgets.RadioSelect, blank=True, label=' ')
    intentos_fallidos3 = models.IntegerField(initial=0)
    password_input3 = models.StringField(blank=True, initial="", label="Contraseña")
    intentos_fallidos4 = models.IntegerField(initial=0)
    password_input4 = models.StringField(blank=True, initial="", label="Contraseña")
    moda_norms = models.IntegerField()
    acierto_norma4_1 = models.IntegerField()
    acierto_norma4_2 = models.IntegerField()
    acierto_norma4_3 = models.IntegerField()
    acierto_norma4_4 = models.IntegerField()
    acierto_norma4_5 = models.IntegerField()
    acierto_norma4_6 = models.IntegerField()
    acierto_norma4_7 = models.IntegerField()
    acierto_norma5_1 = models.IntegerField()
    acierto_norma5_2 = models.IntegerField()
    acierto_norma5_3 = models.IntegerField()
    acierto_norma5_4 = models.IntegerField()
    acierto_norma5_5 = models.IntegerField()
    acierto_norma5_6 = models.IntegerField()
    acierto_norma5_7 = models.IntegerField()
    acierto_norma6_1 = models.IntegerField()
    acierto_norma6_2 = models.IntegerField()
    acierto_norma6_3 = models.IntegerField()
    acierto_norma6_4 = models.IntegerField()
    acierto_norma6_5 = models.IntegerField()
    acierto_norma6_6 = models.IntegerField()
    acierto_norma6_7 = models.IntegerField()
    endownment_final10 = models.IntegerField(blank=True, null=True)
    endownment_final11 = models.IntegerField(blank=True, null=True)
    endownment_final12 = models.IntegerField(blank=True, null=True)
    endownment_final13 = models.IntegerField(blank=True, null=True)
    endownment_final14 = models.IntegerField(blank=True, null=True)
    endownment_final15 = models.IntegerField(blank=True, null=True)
    endownment_final16 = models.IntegerField(blank=True, null=True)
    endownment_final17 = models.IntegerField(blank=True, null=True)
    endownment_final18 = models.IntegerField(blank=True, null=True)
    slider_touched = models.StringField()

    

# FUNCTIONS

def calculate_group_mode_and_accuracy_all(player: Player, round_number: int):
    """
    Calcula la moda y los aciertos para un conjunto de normas elicitadas y los guarda en player.participant.
    - round_number: de 1 a 6, donde 1–3 corresponden a la primera app, y 4–6 a la segunda.
    """
    session_players = player.subsession.get_players()

    # Separar por grupo
    klee_players = [p for p in session_players if p.participant.group_artist == 'grupo_klee']
    kandinski_players = [p for p in session_players if p.participant.group_artist == 'grupo_kandinski']

    field_prefix = f'norms_elicitation{round_number}_'

    for i in range(1, 8):
        klee_values = []
        kandinski_values = []

        for p in klee_players:
            response = getattr(p, f'{field_prefix}{i}', None)
            if response is not None:
                klee_values.append(int(response))

        for p in kandinski_players:
            response = getattr(p, f'{field_prefix}{i}', None)
            if response is not None:
                kandinski_values.append(int(response))

        # Calcular moda
        try:
            moda_klee = mode(klee_values) if klee_values else None
        except StatisticsError:
            moda_klee = None

        try:
            moda_kandinski = mode(kandinski_values) if kandinski_values else None
        except StatisticsError:
            moda_kandinski = None

        # Comparar con respuestas individuales
        for p in session_players:
            player_response = getattr(p, f'{field_prefix}{i}', None)
            if player_response is None:
                continue

            player_response = int(player_response)
            group = p.participant.group_artist

            acierto = 0
            if group == 'grupo_klee' and moda_klee is not None and player_response == moda_klee:
                acierto = 1
            elif group == 'grupo_kandinski' and moda_kandinski is not None and player_response == moda_kandinski:
                acierto = 1

            # Guardar en Player y participant
            setattr(p, f'acierto_norma{round_number}_{i}', acierto)
            setattr(p.participant, f'acierto_norma{round_number}_{i}', acierto)



# PAGES
class pagina_cero(Page):
    pass


class ShuffleWaitPage2(WaitPage):
    
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):

        range_lista = [[] for _ in range(subsession.session.num_participants)]
    

        estructura = subsession.get_group_matrix(range_lista)

        # Identificación de los líderes de cada grupo
        leaders_pair = [None, None]

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_klee" and player.participant.group_role2 == "lider":
                    leaders_pair[0] = player.participant.id_in_session
                    break

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_kandinski" and player.participant.group_role2 == "lider":
                    leaders_pair[1] = player.participant.id_in_session
                    break


        # Crear listas vacías para los seguidores de cada grupo
        group1_seguidores = []  # Seguidores de grupo_klee
        group2_seguidores = []  # Seguidores de grupo_kandinski

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_klee" and player.participant.group_role2 == "seguidor":
                    group1_seguidores.append(player.participant.id_in_session)

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_kandinski" and player.participant.group_role2 == "seguidor":
                    group2_seguidores.append(player.participant.id_in_session)



        # Seleccionar aleatoriamente seguidores de cada grupo
        follower1 = random.choice(group1_seguidores)
        follower2 = random.choice(group2_seguidores)

        follower3 = random.choice([f for f in group1_seguidores if f != follower1])
        follower4 = random.choice([f for f in group2_seguidores if f != follower2])

        # Emparejar los seguidores
        pairs_followers1 = [follower1, follower2]  # Primera pareja
        pairs_followers2 = [follower3, follower4]  # Segunda pareja

        

        # Nueva matriz de grupos
        new_group_matrix = [leaders_pair, pairs_followers1, pairs_followers2]

        # Asignar la nueva matriz de grupos
        subsession.set_group_matrix(new_group_matrix)



class norms_elicitation1(Page):
    form_model = 'player'
    form_fields = ['norms_elicitation4_1', 'norms_elicitation4_2', 'norms_elicitation4_3',
                   'norms_elicitation4_4', 'norms_elicitation4_5', 'norms_elicitation4_6', 
                   'norms_elicitation4_7']

    def is_displayed(player: Player):
        return player.round_number == 1


class calculo_moda(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        round_number = subsession.round_number  # Obtenemos la ronda actual de la subsession

        for group in subsession.get_groups():
            for player in group.get_players():
                # Usar 1 para la ronda 1, 2 para la ronda 7 y 3 para la ronda 9
                if player.round_number == 1:
                    calculate_group_mode_and_accuracy_all(player, 1)
                elif player.round_number == 3:
                    calculate_group_mode_and_accuracy_all(player, 2)
                elif player.round_number == 9:
                    calculate_group_mode_and_accuracy_all(player, 3)
                else:
                    print(f"Ronda desconocida: {player.round_number}")


class norms_elicitation2(Page):
    form_model = 'player'
    form_fields = ['norms_elicitation5_1', 'norms_elicitation5_2', 'norms_elicitation5_3',
                   'norms_elicitation5_4', 'norms_elicitation5_5', 'norms_elicitation5_6', 
                   'norms_elicitation5_7']

    def is_displayed(player: Player):
        return player.round_number == 3

   
class norms_elicitation3(Page):
    form_model = 'player'
    form_fields = ['norms_elicitation6_1', 'norms_elicitation6_2', 'norms_elicitation6_3',
                   'norms_elicitation6_4', 'norms_elicitation6_5', 'norms_elicitation6_6', 
                   'norms_elicitation6_7']

    def is_displayed(player: Player):
        return player.round_number == 9



class beliefs_your_group3(Page):
    form_model = 'player'
    form_fields=['beliefs_your_group3', 'beliefs_your_leader3']


    @staticmethod
    def get_form_fields(player: Player):
        if player.participant.group_role2 == "seguidor":
            return ['beliefs_your_leader3', 'beliefs_your_group3']
        else:
            return ['beliefs_your_group3']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class beliefs_other_group3(Page):
    form_model = 'player'
    form_fields=['beliefs_other_leader3', 'beliefs_other_followers3']

    def is_displayed(player:Player):
        return player.round_number == 1


class espera(WaitPage):
    wait_for_all_groups = True
    

class JOD_leader(Page):
    form_model = 'player'
    form_fields = ['agression', 'leader_message', 'slider_touched']

    @staticmethod
    def is_displayed(player:Player):
        return player.participant.group_role2 == 'lider'
    
    def before_next_page(player:Player, timeout_happened):
        seguidores = player.get_others_in_subsession()
        print("seguidores es: ", seguidores)
        print(player.leader_message)
        for p in seguidores:
            if p.participant.group_artist == player.participant.group_artist:
                p.leader_message = player.leader_message
                p.agression_lider = player.agression

    @staticmethod
    def error_message(player, values):
        errors = []
        if values.get('slider_touched') != '1':
            errors.append("Debes mover la barra de agresión.")
        if not values.get('leader_message'):
            errors.append("Debes seleccionar un mensaje.")
        if errors:
            print("🔍 Values received:", values)
            return " ".join(errors)


    @staticmethod
    def vars_for_template(player: Player):
        # Obtén el promedio grupal según el grupo y la ronda
        if player.round_number >= 2:
            if player.participant.group_artist == "grupo_klee":
                promedio_grupal = player.subsession.in_round(player.round_number - 1).promedio_grupoklee            
            elif player.participant.group_artist == "grupo_kandinski":
                promedio_grupal = player.subsession.in_round(player.round_number - 1).promedio_grupokandinski
        else:
            promedio_grupal = None

        return dict(
            promedio_grupal=promedio_grupal,
            agression_p1=None,  # Inicializa las variables de agresión, que puedes actualizar después
            agression_p2=None,
            display_round=player.round_number + 9
            
        )


class endownment_final_lideres(WaitPage):
    def is_displayed(player: Player):
        return player.participant.group_role2 == 'lider'

    @staticmethod
    def after_all_players_arrive(group: Group):
        # Obtenemos la subsession a partir del grupo
        subsession = group.subsession
        
        # Obtener los jugadores por ID
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)


        # Calcular la agresión y el endowment final
        agression_p2 = p2.agression
        agression_p1 = p1.agression
        p1.endownment_final = p1.endownment - p2.agression
        p2.endownment_final = p2.endownment - p1.agression
        p1.agresion_guardada = p1.endownment - p1.endownment_final
        p2.agresion_guardada = p2.endownment - p2.endownment_final


        # Guardar el valor de endownment_final en la variable correspondiente según la ronda
        real_round = p1.round_number + 9  # Shift rounds 1–9 to 10–18
        setattr(p1.participant, f'endownment_final{real_round}', p1.endownment_final)
        setattr(p2.participant, f'endownment_final{real_round}', p2.endownment_final)


    @staticmethod
    def vars_for_template(player: Player):
        # Retornar el valor de las agresiones para el template
        return dict(agression_p1=player.agression, agression_p2=player.agression)

class leader_results(Page):

    def is_displayed(player:Player):
        return player.participant.group_role2 == 'lider'
            
            

class followers_JOD(Page):
    form_model = 'player'
    form_fields = ['agression', 'slider_touched']

    def is_displayed(player:Player):
        return player.participant.group_role2 == 'seguidor'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(leader_message=player.leader_message,
        display_round=player.round_number + 9)


    def error_message(player, values):
        if values.get('slider_touched') != '1':
            return 'Debes mover la barra para tomar una decisión.'

      

class endownment_final_seguidores(WaitPage):
    def is_displayed(player: Player):
        return player.participant.group_role2 == 'seguidor'

    @staticmethod
    def after_all_players_arrive(group: Group):
        followers = [p for p in group.get_players() if p.participant.group_role2 == 'seguidor']

        print("🎯 Found followers:", [f.participant.code for f in followers])

        if len(followers) != 2:
            print(f"⚠️ Error: Expected 2 followers, got {len(followers)}")
            return  # Exit early

        p1, p2 = followers

        print(f"💰 Agression values: {p1.participant.code} -> {p1.agression}, {p2.participant.code} -> {p2.agression}")

        p1.endownment_final = p1.endownment - p2.agression
        p2.endownment_final = p2.endownment - p1.agression
        p1.agresion_guardada = p1.endownment - p1.endownment_final
        p2.agresion_guardada = p2.endownment - p2.endownment_final

        real_round = p1.round_number + 9
        setattr(p1.participant, f'endownment_final{real_round}', p1.endownment_final)
        setattr(p2.participant, f'endownment_final{real_round}', p2.endownment_final)

        print(f"✅ Round {real_round}: Saved final endowments {p1.endownment_final} and {p2.endownment_final}")




class followers_JOD_results(Page):
    def is_displayed(player:Player):
            return (
                player.participant.group_role2 == 'seguidor' and 
                player.round_number >= 3  and player.participant.follower_type2 == 'tipo 1')

    @staticmethod
    def after_all_players_arrive(group:Group):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        agression_p2 = p2.aggression
        agression_p1 = p1.agression

        def vars_for_template(player:Player):
            return dict(
                agression_p1=agression_p1, agression_p2=agression_p2,
                    )


class CalcularPromedios(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        destruccion_seguidores_klee = []
        destruccion_seguidores_kandinski = []

        # Recorremos todos los jugadores para recolectar la agresión
        for p in subsession.get_players():
            if p.participant.group_artist == 'grupo_klee' and p.participant.group_role2 == 'seguidor':
                destruccion_seguidores_klee.append(p.agression)
            elif p.participant.group_artist == 'grupo_kandinski' and p.participant.group_role2 == 'seguidor':
                destruccion_seguidores_kandinski.append(p.agression)

        # Calculamos los promedios por grupo
        promedio_grupoklee = int(round(sum(destruccion_seguidores_klee) / len(destruccion_seguidores_klee))) if destruccion_seguidores_klee else 0
        promedio_grupokandinski = int(round(sum(destruccion_seguidores_kandinski) / len(destruccion_seguidores_kandinski))) if destruccion_seguidores_kandinski else 0

        # Guardamos los valores en la subsession para cada ronda
        subsession.promedio_grupoklee = promedio_grupoklee
        subsession.promedio_grupokandinski = promedio_grupokandinski

class ejemplo_lider(Page):
    
    def is_displayed(player:Player):
        return player.round_number == 1

class ejemplo_miembrogrupo(Page):
    def is_displayed(player:Player):
        return player.round_number == 1

class ejemplo_grupos(Page):
    def is_displayed(player:Player):
        return player.round_number == 1

class descripcion_pago(Page):
    def is_displayed(player:Player):
        return player.round_number == 1

class sistema_pagos(Page):
    def is_displayed(player:Player):
        return player.round_number == 1

class beliefs_your_group4(Page):
    form_model = 'player'
    form_fields = ['beliefs_your_leader4', 'beliefs_your_group4']
    
    
    @staticmethod
    def get_form_fields(player: Player):
        if player.participant.group_role2 == 'seguidor':
            return ['beliefs_your_leader4', 'beliefs_your_group4']
        else:
            return ['beliefs_your_group4']

    def is_displayed(player:Player):
        return player.round_number == 3

class beliefs_other_group4(Page):
    form_model = 'player'
    form_fields=['beliefs_other_leader4', 'beliefs_other_followers4']

    def is_displayed(player:Player):
        return player.round_number == 3

class instruccion_promedio(Page):
    form_model = 'player'
    
    def is_displayed(player:Player):
        return player.round_number == 3




page_sequence = [ShuffleWaitPage2, norms_elicitation1, 
 norms_elicitation2, espera, beliefs_your_group3, beliefs_other_group3, instruccion_promedio, beliefs_your_group4, beliefs_other_group4, espera, JOD_leader, espera,
endownment_final_lideres, leader_results, followers_JOD, CalcularPromedios, endownment_final_seguidores, 
followers_JOD_results, norms_elicitation3, calculo_moda] 


