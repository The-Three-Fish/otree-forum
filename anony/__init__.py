import logging
import itertools
from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'anony'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def do_my_shuffle(self): 
        print(1111)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def creating_session(self):
        # Log a message at the start of the session creation
        logging.info("Session is being created")

        # Example: Randomly grouping players
        self.group_randomly()

        # Log another message after some operations
        logging.info("Players have been grouped randomly")



# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    body_text = "We are waiting for the other participants. We thank you for your patience!"
    wait_for_all_groups = True

    #after_all_players_arrive = 'after_all_players_arrive'
    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.do_my_shuffle()
        print(666)

class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
