from otree.api import *
from collections import defaultdict
import random

       
class C(BaseConstants):
    NAME_IN_URL = 'reshuffle_roles'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    
    pass
    
class Group(BaseGroup):

    pass

class Player(BasePlayer):
    group_role2 = models.StringField(choices=['lider', 'seguidor'], default="")
    follower_type2 = models.StringField(choices=['tipo 1', 'tipo 2', 'tipo 3'], default ="")


# FUNCTIONS


# PAGES
class wellcome(Page):
    pass

class minimal_instructions(Page):
    form_model = 'player'



class asignacion_grupos(WaitPage):
    wait_for_all_groups=True
    

class ReshuffleRolesWaitPage(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        from collections import defaultdict
        import random

        # Group players by existing group_artist (already assigned)
        groups = defaultdict(list)
        for player in subsession.get_players():
            groups[player.participant.group_artist].append(player)

        # Re-assign new roles (group_role2) and follower types (follower_type2)
        for group_players in groups.values():
            leader = random.choice(group_players)
            leader.group_role2 = 'lider'
            leader.follower_type2 = ''
            
            # Get the followers
            followers = [p for p in group_players if p != leader]
            tipos = ['tipo 1', 'tipo 3']
            random.shuffle(tipos)

            for follower, tipo in zip(followers, tipos):
                follower.group_role2 = 'seguidor'
                follower.follower_type2 = tipo

        # Save them into participant vars for persistence
        for player in subsession.get_players():
            player.participant.group_role2 = player.group_role2
            player.participant.follower_type2 = player.follower_type2

            print(f"[RESHUFFLE] {player.participant.code} | {player.participant.group_artist} | {player.group_role2} | {player.follower_type2}")



class Group1_follower(Page):
    
    def is_displayed(player):
        return player.participant.group_artist == "grupo_klee" and player.group_role2 == 'seguidor'

    def vars_for_template(player):

        group_players = player.group.get_players()
        
        leader = next((p for p in group_players if p.group_role2 == "lider"), None)


class Group2_follower(Page):

    def is_displayed(player):
        return player.participant.group_artist == "grupo_kandinski" and player.group_role2 == 'seguidor'
    
    def vars_for_template(player):
   
        group_players = player.group.get_players()
        
        leader = next((p for p in group_players if p.group_role2 == "lider"), None)


class Group1_leader(Page):
    
    def is_displayed(player):
        return player.participant.group_artist == "grupo_klee" and player.group_role2 == 'lider'

    def vars_for_template(player):
             
        return {
            'rol':  player.group_role2
        }


class Group2_leader(Page):

    def is_displayed(player):
        return player.participant.group_artist == "grupo_kandinski" and player.group_role2 == 'lider'

    def vars_for_template(player):
               
        return {
            'rol':  player.group_role2,
        }

class intro_grupos(Page):
    form_model = 'player'



# secuencia real que comentamos para usar una abreviada
# page_sequence = [Consent, end_experiment, minimal, Demographics, SDP, ShuffleWaitPage, GroupAssignment, Group2Assignment] 


page_sequence = [
    intro_grupos,
    ReshuffleRolesWaitPage,
    Group1_follower,
    Group2_follower,
    Group1_leader,
    Group2_leader,
]

