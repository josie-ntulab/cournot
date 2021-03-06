from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
In Cournot competition, firms simultaneously decide the units of products to
manufacture. The unit selling price depends on the total units produced. In
this implementation, there are 2 firms competing for 1 period.
"""


class Constants(BaseConstants):
    name_in_url = 'cournot'
    players_per_group = 2
    num_rounds = 10 # +5
    # demand_coef = self.session.config['demand_coef']

    instructions_template = 'cournot/instructions.html'

    # Total production capacity of all players
    total_capacity = 100
    max_units_per_player = int(total_capacity / players_per_group)


with open( './_rooms/MicroEcon.txt' ) as f:
    students = f.readlines()
    f.close()


class Subsession(BaseSubsession):

    # if participant label isn't pre-assign, it can not be access here
    def creating_session(self):
        from pathlib import Path
        labels = students
        for p, label in zip(self.get_players(), labels):
            p.participant.label = label.strip()
            if p.id_in_group == 1:
                p.cost = 1
            if p.id_in_group == 2:
                p.cost = 7.5
            p.participant.vars['history'] = []
            p.participant.vars['opponent'] = p.other_player().participant.label


class Group(BaseGroup):

    unit_price = models.CurrencyField()

    total_units = models.IntegerField(doc="""Total units produced by all players""")

    #asymmetric

#    def get_history(self):
#        players = self.get_players()
#        for p in players:
#            # get the history
#            path = p.previous_outcome()
#            history = []
#            for _, past in enumerate( path ):
#                history.append( ' '.join( [ 'round ' + str( _ + 1 ) + ':', '( ' + str( past.units ) + ' units,', str( past.payoff ) + ' ) | ' ] ) )
#            history = '\n'.join( history )
#            p.history = history
        


    def set_payoffs(self):
        players = self.get_players()
        self.total_units = sum([p.units for p in players])
        self.unit_price = max( [Constants.total_capacity - self.session.config['demand_coef'] * self.total_units, 0] )
        for p in players:
            p.payoff = self.unit_price * p.units - p.units * p.cost
        for p in players:
            p.participant.vars['history'].append( (p.units, p.payoff, p.other_player().units, p.other_player().payoff, p.round_number, self.unit_price) )
            # p.participant.vars['opponent'] = p.other_player().participant.label
            # get the history
            # path = p.previous_outcome()
            # history = []
            # for _, past in enumerate( path ):
            #     history.append( ' '.join( [ 'round ' + str( _ + 1 ) + ':', '( ' + str( past.units ) + ' units,', str( past.payoff ) + ' ) | ' ] ) )
            # history = '\n'.join( history )
            # p.history = history
                


class Player(BasePlayer):

    units = models.IntegerField(
        min=0,
        # max=Constants.max_units_per_player,
        doc="""Quantity of units to produce""",
    )
    
    # this is duplicate, maybe fixed?
    cost = models.FloatField()


    def other_player(self):
        return self.get_others_in_group()[0]

    def previous_outcome(self):
        return self.in_previous_rounds()


    # def get_history(self):
    #     path = self.previous_outcome()
    #     history = []
    #     for _, past in enumerate( path ):
    #         history.append( ' '.join( [ 'round ' + str( _ + 1 ) + ':', '( ' + str( past.units ) + ' units,', str( past.payoff ) + ' ) | ' ] ) )
    #     history = '\n'.join( history )
    #     self.history = history
