class Message:
    def __init__(self, email:str, subject:str, message:str, ID:str):
        self.email = email
        self.subject = subject
        self.message = message
        self.ID=ID

    
    def to_dict(self):
        json_dict = {
            'email': self.email,
            'subject': self.subject,
            'message': self.subject,
            'id': self.ID
        }

        return json_dict
    

    def to_json(self):
        return self.to_dict()


