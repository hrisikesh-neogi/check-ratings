import pandas as pd

class agent_Report:
    
    def __init__(self, file_path):
        """
        params:
            file_path = the path of the agents sheet.
        
        """
        self.file_path = file_path
        self.df = pd.read_excel('AgentPerformance.xlsx', skiprows=1)   
        
    def available_Agents(self):
        return list(set(df['Agent Name'].to_list()))
        
    def data(self, agent_name):
        self.agent_name = agent_name
        
        
        return df[df['Agent Name'] == self.agent_name]
    