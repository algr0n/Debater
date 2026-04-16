class PerformanceTracker:
    def __init__(self):
        self.debates = []

    def record_debate(self, debate_id, participants, winner):
        self.debates.append({
            'debate_id': debate_id,
            'participants': participants,
            'winner': winner
        })

    def calculate_stats(self):
        total_debates = len(self.debates)
        winners_count = {}
        for debate in self.debates:
            winner = debate['winner']
            if winner in winners_count:
                winners_count[winner] += 1
            else:
                winners_count[winner] = 1
        return total_debates, winners_count

    def analyze_trends(self):
        # Analyze trends over time (could be enhanced with timestamps)
        trends = {}  # Placeholder for trend analysis logic
        return trends

    def generate_leaderboard(self):
        total_debates, winners_count = self.calculate_stats()
        leaderboard = sorted(winners_count.items(), key=lambda x: x[1], reverse=True)
        return leaderboard
