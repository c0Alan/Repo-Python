from datetime import datetime

class Record:
    def __init__(self, id, content, created_time):
        self.id = id
        self.content = content
        self.created_time = created_time
        
    # def __init__(self, **kwargs):
    #     for key, value in kwargs.items():
    #         setattr(self, key, value)
    
    def __init__(self, **kwargs):
        values = list(kwargs.values())
        self.id = int(values[0])
        self.content = values[1]
        self.created_time = datetime.strptime(values[2], '%Y-%m-%d %H:%M:%S')
        
    def __str__(self):
        return f'Record({self.id}, {self.content}, {self.created_time})'