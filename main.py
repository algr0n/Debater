# main.py

# Entry point script for the Debater project

class DebateAgent:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def debate(self, topic):
        # Simulate the debate on the given topic
        import random
        self.score += random.randint(1, 10)  # Randomly assign score

    def __str__(self):
        return f'{self.name}: {self.score}'


class Debater:
    def __init__(self, agents, topics):
        self.agents = agents
        self.topics = topics
        self.leaderboard = {agent.name: 0 for agent in agents}

    def run_debates(self):
        for topic in self.topics:
            print(f'\nDebating on topic: {topic}\n')
            for agent in self.agents:
                agent.debate(topic)
                self.leaderboard[agent.name] = agent.score

    def display_results(self):
        print('\nFinal Results:')
        for agent in self.agents:
            print(agent)
        self.display_leaderboard()

    def display_leaderboard(self):
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda item: item[1], reverse=True)
        print('\nLeaderboard:')
        for name, score in sorted_leaderboard:
            print(f'{name}: {score}')


if __name__ == '__main__':
    topics = ['AI Ethics', 'Climate Change', 'Space Exploration', 'Economic Policies']
    agents = [DebateAgent('Agent A'), DebateAgent('Agent B'), DebateAgent('Agent C')]
    debater = Debater(agents, topics)
    debater.run_debates()
    debater.display_results()  
