#!/usr/bin/env python3
"""
Automated LeetCode Progress Tracker
"""

import json
import os
from datetime import datetime, timedelta

class LeetCodeTracker:
    def __init__(self):
        self.progress_file = '.progress.json'
        self.readme_file = 'README.md'
        self.load_data()
    
    def load_data(self):
        """Load progress from JSON"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            self.data = {
                'total': 0,
                'streak': 0,
                'last_date': None,
                'problems': []
            }
    
    def save_data(self):
        """Save progress to JSON"""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)
    
    def add_problem(self, name, difficulty, topic):
        """Add a new problem"""
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Add to problems list
        problem_num = len(self.data['problems']) + 1
        self.data['problems'].append({
            'num': problem_num,
            'date': today,
            'name': name,
            'difficulty': difficulty,
            'topic': topic
        })
        
        # Update total
        self.data['total'] += 1
        
        # Update streak
        if self.data['last_date']:
            last_date = datetime.strptime(self.data['last_date'], '%Y-%m-%d')
            today_date = datetime.now()
            diff = (today_date.date() - last_date.date()).days
            
            if diff == 0:
                pass  # Same day, no change
            elif diff == 1:
                self.data['streak'] += 1  # Consecutive!
            else:
                self.data['streak'] = 1  # Streak broken, restart
        else:
            self.data['streak'] = 1  # First problem
        
        self.data['last_date'] = today
        
        self.save_data()
        self.update_readme()
        
        # Print success
        print("\n" + "="*50)
        print("✅ PROBLEM ADDED!")
        print("="*50)
        print(f"Problem: {name}")
        print(f"Difficulty: {difficulty}")
        print(f"Topic: {topic}")
        print(f"\n📊 Total Solved: {self.data['total']}")
        print(f"🔥 Current Streak: {self.data['streak']} days")
        print("="*50 + "\n")
    
    def update_readme(self):
        """Automatically update README.md with current progress"""
        
        # Build the problems table
        table_rows = []
        for p in self.data['problems']:
            table_rows.append(
                f"| {p['num']} | {p['date']} | {p['name']} | {p['difficulty']} | {p['topic']} |"
            )
        
        table_content = "\n".join(table_rows) if table_rows else "| - | - | No problems solved yet | - | - |"
        
        # README template
        readme_content = f"""# 🚀 LeetCode Journey 2026

**Goal:** Consistent Practice Preps
**Start Date:** January 1, 2026  

## 📊 Progress

- **Total Solved:** {self.data['total']} problems
- **Current Streak:** {self.data['streak']} days 🔥
- **Last Solved:** {self.data['last_date'] or 'N/A'}

## 📝 Problems Solved

| # | Date | Problem | Difficulty | Topic |
|---|------|---------|------------|-------|
{table_content}

---

## 🎯 Current Focus

**Week 1-2:** Arrays & Hashing  
**Next Goal:** Neetcode Blind 75

## 💡 Quick Stats

- Easy: {sum(1 for p in self.data['problems'] if p['difficulty'] == 'Easy')}
- Medium: {sum(1 for p in self.data['problems'] if p['difficulty'] == 'Medium')}
- Hard: {sum(1 for p in self.data['problems'] if p['difficulty'] == 'Hard')}

---

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
        
        with open(self.readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print("📝 README.md automatically updated!")


def main():
    tracker = LeetCodeTracker()
    
    print("\n🎯 LEETCODE TRACKER")
    print("="*50)
    
    # Get problem number and name
    problem_input = input("Problem (e.g., '1' or '1. Two Sum'): ").strip()
    
    # Extract number and name if both provided, otherwise just use as name
    if '.' in problem_input:
        parts = problem_input.split('.', 1)
        problem_num = parts[0].strip()
        name = parts[1].strip() if len(parts) > 1 else f"Problem {problem_num}"
    else:
        # Just a number or just a name
        if problem_input.isdigit():
            name = f"Problem {problem_input}"
        else:
            name = problem_input
    
    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty_choice = input("Choose (1-3): ").strip()
    
    difficulty_map = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}
    difficulty = difficulty_map.get(difficulty_choice, 'Easy')
    
    print("\nTopic (in BEST learning order):")
    print("1. Arrays & Hashing")
    print("2. Two Pointers")
    print("3. Sliding Window")
    print("4. Stack & Queue")
    print("5. Binary Search")
    print("6. Linked Lists")
    print("7. Trees")
    print("8. Recursion & Backtracking")
    print("9. Dynamic Programming")
    print("10. Graphs")
    print("11. Heaps")
    print("12. Other")
    topic_choice = input("Choose (1-12): ").strip()
    
    topic_map = {
        '1': 'Arrays & Hashing',
        '2': 'Two Pointers', 
        '3': 'Sliding Window',
        '4': 'Stack & Queue',
        '5': 'Binary Search',
        '6': 'Linked Lists',
        '7': 'Trees',
        '8': 'Recursion & Backtracking',
        '9': 'Dynamic Programming',
        '10': 'Graphs',
        '11': 'Heaps',
        '12': 'Other'
    }
    topic = topic_map.get(topic_choice, 'Other')
    
    # Add the problem
    tracker.add_problem(name, difficulty, topic)
    
    print("✨ Don't forget to:")
    print("   1. Save your solution in solutions/ folder")
    print("   2. git add . && git commit -m 'Day X: [problem]' && git push")


if __name__ == "__main__":
    main()