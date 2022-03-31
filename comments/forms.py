import requests
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha = raw_data.get('g-recaptcha-response')

        request_valid = requests.post('https://www.google.com/recaptcha/api/siteverify', 
                                      data={'secret': '6LfZcS4fAAAAACZE3JO3LF6E-sx2TYBBy3QaKL0n', 
                                            'response': recaptcha})

        request_valid = request_valid.json()

        if not request_valid.get('success'):
            self.add_error('text', 'ERRO ao realizar o comentário, tente novamente.')


    class Meta:
        model = Comment
        fields = ('name', 'email', 'text',)