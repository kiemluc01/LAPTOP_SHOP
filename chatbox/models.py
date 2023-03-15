from django.db import models
from shopapp.models import Userprofile

class ChatAI(models.Model):
    topic = models.CharField("Topic", max_length=150)
    key_word = models.CharField("Key Word", max_length=250)
    answer = models.CharField("Answer", max_length=250)
    
    def __str__(self) -> str:
        return 'ChatAI<{}>: {}'.format(self.pk, self.topic)
    
class HistoryChat(models.Model):
    status = models.CharField("Status", max_length=50)
    content = models.CharField("content", max_length=250)
    user = models.ForeignKey("shopapp.Userprofile", related_name="user_chatbox", on_delete=models.CASCADE)
