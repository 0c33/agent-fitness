import json
import os
from pathlib import Path
import yaml  # You’ll need PyYAML to load config.yaml — install it if needed: pip install pyyaml
from Ai import Ai_Agent, Ai_Test

class ExerciseAgent:
    def __init__(self):
        self.config = self.load_config()
        self.workout_plans = self.load_workout_plans()
        self.summaries = self.load_summaries()
        self.logs = self.load_logs()
        self.notes = self.load_notes()

        self.data = []

        self.name = ''

        # self.analyze = 

    def load_notes(self):
        notes_path = Path(__file__).parent / "data" / "notes.md"
        with open(notes_path, "r", encoding='utf-8') as f:
            return f.read()

    def load_config(self):
        config_path = Path(__file__).parent / "config.yaml"
        with open(config_path, "r") as f:
            return yaml.safe_load(f)

    def load_workout_plans(self):
        plan_path = Path(__file__).parent / "data" / "workout_plans.json"
        with open(plan_path, "r") as f:
            return json.load(f)

    def load_summaries(self):
        summary_path = Path(__file__).parent / "processed" / "summaries.json"
        with open(summary_path, "r") as f:
            return json.load(f)

    def load_logs(self):
        log_path = Path(__file__).parent / "logs" / "exercise_log.txt"
        with open(log_path, "r") as f:
            return f.read()
        

    def get_data(self):
        
        return [self.notes, self.config, self.workout_plans, self.summaries]


    def modify_notes(self, data):
        notes_path = Path(__file__).parent / "data" / "notes.md"
        with open(notes_path, "w") as f:
            f.write(data)

    def modify_config(self, data):
        config_path = Path(__file__).parent / "config.yaml"
        with open(config_path, "w") as f:
            yaml.dump(data, f)

    def modify_workout_plans(self, data):
        plan_path = Path(__file__).parent / "data" / "workout_plans.json"
        with open(plan_path, "w") as f:
            json.dump(data, f)

    def modify_summaries(self, data):
        summary_path = Path(__file__).parent / "processed" / "summaries.json"
        with open(summary_path, "w") as f:
            json.dump(data, f)

    def add_logs(self, data):
        log_path = Path(__file__).parent / "logs" / "exercise_log.txt"
        with open(log_path, "a") as f:
            f.write(f'{data}\n\n')

    # Phase 1
    # Each file
    # Analyze -> Thinking -> Summarise

    def Analyze(self, data):

        prompt = f"""
        you are Exercise Analyzer Agent
        you will analyze each user data

        Analyze this file's content — what does it say about {self.name} training?
        {data}"""

        return Ai_Test(prompt)

    def Thinking(self, data):

        prompt = f"""
        you are Exercise Thinking Agent
        what are your thought about the data provided to you from Exercise Agent:
        {data}"""

        return Ai_Test(prompt)
    

    def Summarise(self, data):

        prompt = f"""
        you are Exercise summarise Agent
        you will summerize what Exercise Thinking Agent said:
        {data}
        """

        result = Ai_Test(prompt)

        self.data.append(result)
        return result
    


    # Phase 2

    # Analyze -> Thinking -> Summarise
    # All Data from phase 1

    def Analyze_All(self):
        prompt = f"""
        You are Exercise System Analyzer Agent
        you will analyze user exercise system at each point
        {self.data}"""

        return Ai_Test(prompt)

    def Thinking_All(self, data):
        prompt = f"""
        you are Exercise System Thinking Agent
        what are your thought about the Exercise System provided to you from Exercise Agent
        {data}"""

        return Ai_Test(prompt)

    
    def Summarise_All(self, data):
        prompt = f"""
        you are Exercise System Summariser Agent
        Synthesize all summaries into one coherent report for {self.name} training system.
        Include patterns, contradictions, and key insights across all files.
        Keep it concise, actionable, and motivational.
        {data}"""

        return Ai_Test(prompt)
    
    # Phase 3
    # here we will makes changes and decide what change will do

    def System_Analyze(self, data):
        prompt = f"""
        you are Exercise System analyzer agent.
        What changes can we make to the system to make it better?
        {data}"""

        return Ai_Test(prompt)

    def System_Thinker(self, data, summarise_all):
        prompt = f"""
        you are Exercise System Thinking Agent.
        what your thought about these new changes ?

        Changes: {data}
        
        Exercise System: {summarise_all}"""

        return Ai_Test(prompt)
    
    def System_Summariser(self, data):
        prompt = f"""
        you are Exercise System Summariser Agent.
        you will summarise the new Exercise System and the changes and the agent thought
        {data}"""

        return Ai_Test(prompt)


    # Phase 4
    # compares RAW data with changes from Phase 2 and takes Decision if its good or not
    # compare 

    def Compare_All(self, New_System, Old_System):
        prompt = f"""
        you are Exercise Systems comparior Agent
        you will compare the OLD exercise system with the new exercise system.

        New System: {New_System}
        
        Old System {Old_System}"""

        return Ai_Test(prompt)

    def Discover_Vulnerability(self, New_System, Old_System):
        prompt = f"""
        you are Exercise System Diagnostician Agent
        you will discover vulnerability for The new Exercise System and the old Exercise System

        New System: {New_System}
        
        Old System {Old_System}"""

        return Ai_Test(prompt)

    def Decision_All(self, Vulns, New_System, Old_System, Comparior):

        prompt = f"""
        you are Exercise System Decision making Agent.
        
        New System: {New_System}

        Old System: {Old_System}

        vulnerability: {Vulns}

        and this data is from 'Exercise Systems comparior Agent' about the OLD System and The New System: {Comparior}
        
        what you will make after this ?
        if this is good and no need to take any changed -> return 'Good' only!
        if this needs changes -> return what that needs changes and why ?
        """

        return Ai_Test(prompt)
    
    
    # Phase 5
    def Validate_Decision(self, Decision, New_System, Old_System):
        prompt = f"""
        you are Exercise System Validator Agent.
        you will makes the changes to the System based on the Decision from 'Exercise System Decision making Agent'.
        
        New System: {New_System}

        Old System: {Old_System}

        Decision: {Decision}
        """

        return Ai_Test(prompt)

    def Human_Readable(self, data):
        prompt = """
        You are Final Reporter Agent.

        Validation: {final_validation}

        Generate a human-readable training report for self.name — including:
        - Key insights from each file
        - What needs to change (if anything)
        - Coach verdict

        Keep it concise, actionable, and motivational."""
        
    

    def generate_plan(self, user_input):
        
        status = self.get_status_for_plan(user_input)
        return Ai_Agent(self.get_data(), f"User input: {user_input}\n\nStatus: {status}")


    def get_status_for_plan(self, plan_name):
        # Look for status in summaries.json
        for summary in self.summaries:
            if summary["content"].find(plan_name) != -1:
                return summary["status"]
        return "progressing"  # Default — you can change this later

    def _generate_response(self, user_input, plan):
        pass


# Example usage
if __name__ == "__main__":
    agent = ExerciseAgent()

    # Phase 1
    for i in agent.get_data():
        analyze = agent.Analyze(i)
        Thinking = agent.Thinking(analyze)
        Summarise = agent.Summarise(Thinking)

    
    # Phase 2
    analyze_all = agent.Analyze_All()
    Thinking_all = agent.Thinking_All(analyze_all)
    Summarise_All = agent.Summarise_All(Thinking_all) # the whole system summarized | OLD system

    
    # Phase 3
    System_Analyze = agent.System_Analyze(Summarise_All)
    System_Thinker = agent.System_Thinker(System_Analyze, Summarise_All)
    System_Summariser = agent.System_Summariser(System_Thinker) # the new system summarized

    # Phase 4
    Compare_All = agent.Compare_All(System_Summariser, Summarise_All)
    Discover_Vulnerability = agent.Discover_Vulnerability(System_Summariser, Summarise_All)
    Decision_All = agent.Decision_All(Discover_Vulnerability, System_Summariser, Summarise_All, Compare_All)

    print(f'Decision: {Decision_All}\n\n')
    print(f'OLD System: {Summarise_All}\n\n')
    print(f'New System: {System_Summariser}\n\n')








    # thinking = agent.Thinking(agent.load_notes).content
    # print(f'This is from Thinking Agent: {thinking}\n\n\n')

    # summarize = agent.Summarise(thinking).content
    # print(f'This is from Summarise Agent: {summarize}\n\n\n')

    # decision = agent.Decision(summarize).content
    # print(f'This is from Decision Agent: {decision}\n\n\n')
    # print(agent.generate_plan("what is my schedule workout ?"))

    # print(Ai_Agent(agent.get_data(), ""))