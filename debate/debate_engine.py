class DebateEngine:
    def __init__(self):
        self.debates = []
        
    def start_debate(self, topic):
        debate = {
            'topic': topic,
            'opening_rounds': [],
            'counter_arguments': [],
            'rebuttals': []
        }
        self.debates.append(debate)
        return debate
    
    def add_opening_round(self, debate, argument):
        debate['opening_rounds'].append(argument)

    def add_counter_argument(self, debate, argument):
        debate['counter_arguments'].append(argument)

    def add_rebuttal(self, debate, argument):
        debate['rebuttals'].append(argument)

    def get_debate_summary(self, debate):
        return {
            'topic': debate['topic'],
            'opening_rounds': debate['opening_rounds'],
            'counter_arguments': debate['counter_arguments'],
            'rebuttals': debate['rebuttals']
        }