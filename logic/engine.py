import random

class ClarityEngine:
    def __init__(self):
        # In a real enterprise app, this is where we'd initialize Kafka/Spark connections
        self.kafka_enabled = False
        self.spark_enabled = False

    def get_next_action(self, goals, available_time):
        """
        Analyzes goals and time to provide a specific, actionable next step.
        """
        if not goals:
            return {
                "action": "Plan your day",
                "reason": "The mind is for having ideas, not holding them. Add a few tasks to get started.",
                "duration": 5
            }

        total_tasks = len(goals)
        
        # Filter goals that can fit in the available time
        valid_options = []
        for goal in goals:
            est_time = goal.get('estimated_time', 30)
            if est_time <= available_time:
                valid_options.append(goal)

        if not valid_options:
            # Pick a random goal for micro-slicing to avoid "first-task bias"
            target_goal = random.choice(goals)
            return {
                "action": f"5-Minute Focus: {target_goal.get('name')}",
                "reason": f"With {total_tasks} tasks and limited time, momentum matters most. Breaking the friction on '{target_goal.get('name')}' is your best move.",
                "duration": 5
            }

        # Select a task
        # In a real app, this would use priority/energy levels.
        # Here we'll simulate "smart" selection by favoring higher energy tasks if time is high
        if available_time >= 60:
            # Look for "Big Wins" (long tasks) or just the most significant one
            chosen_goal = random.choice(valid_options)
            reason_prefix = f"Significant window detected ({available_time}m)."
        else:
            chosen_goal = random.choice(valid_options)
            reason_prefix = "Quick-win mode."

        # Analysis-based reasons
        reasons = [
            f"Of your {total_tasks} tasks, this one provides the best ROI for your current {available_time}m window.",
            f"Context Analysis: Starting with '{chosen_goal.get('name')}' reduces the cognitive load of your remaining schedule.",
            f"Focused Action: Your {available_time}m window is best utilized by tackling this specific task to clear mental space."
        ]

        return {
            "action": chosen_goal.get('name'),
            "reason": f"{reason_prefix} {random.choice(reasons)}",
            "duration": chosen_goal.get('estimated_time', 30)
        }
