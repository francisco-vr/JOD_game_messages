from os import environ


SESSION_CONFIGS = [
    dict(
        name='6_JOD_RANDOM_MESSAGE',
        display_name='6_RANDOM MESSAGE',
        app_sequence=['six_survey_random','six_JOD_MESSAGE','reshuffle_roles','six_JOD_MESSAGE_2','six_demograph_random'],
        num_demo_participants=6
    )
    ]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['group_artist', 'group_role', 'follower_type', 'interface', 'group_role2', 'follower_type2','acierto_norma1_1', 'acierto_norma1_2', 'acierto_norma1_3',
                   'acierto_norma1_4', 'acierto_norma1_5', 'acierto_norma1_6', 
                   'acierto_norma1_7','acierto_norma2_1', 'acierto_norma2_2', 'acierto_norma2_3',
                   'acierto_norma2_4', 'acierto_norma2_5', 'acierto_norma2_6', 
                   'acierto_norma2_7', 'acierto_norma3_1','acierto_norma3_2','acierto_norma3_3','acierto_norma3_4',
                   'acierto_norma3_5','acierto_norma3_6','acierto_norma3_7', 'endownment_final1','endownment_final2',
                   'endownment_final3','endownment_final4','endownment_final5','endownment_final6','endownment_final7','endownment_final8',
                   'endownment_final9','endownment_final10','endownment_final11','endownment_final12', 'endownment_final13', 'endownment_final14',
                   'endownment_final15', 'endownment_final16', 'endownment_final17', 'endownment_final18',     'selected_jod_round',
                    'selected_jod_value', 'selected_norm_round', 'selected_norm_question', 'selected_norm_value'] 
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CLP'
USE_POINTS = False

ROOMS = [
    dict(
        name='piloto',
        display_name='Piloto',
        participant_label_file='_rooms/piloto.txt',
    ),
    dict(
        name='lem_s1',
        display_name='LEM_S1',
        participant_label_file='_rooms/demografico.txt',
    ),
    dict(name='LEM2',
    display_name='Experimento líderes',
    participant_label_file='_rooms/piloto.txt',
    )
]


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""
DEBUG = False

SECRET_KEY = '1250236917610'

INSTALLED_APPS = ['otree']
