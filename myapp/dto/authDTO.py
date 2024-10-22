from myapp.models.authModel import AuthModel
 
class authDTO(AuthModel):
    def toDTO(self):
        return {
            'email': self.email,
            'fullName': self.full_name,
            'role': self.role,
        }
