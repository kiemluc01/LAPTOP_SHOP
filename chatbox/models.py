from django.db import models
class HistoryChat(models.Model):
    status = models.CharField("Staus chat", max_length=50)
    content = models.CharField("Content chat", max_length=1000, blank=True)
    user = models.ForeignKey("shopapp.Userprofile", related_name="user_chat", on_delete=models.CASCADE, blank=True)
    has_image = models.BooleanField("Has image",default=False, blank=True)
    
    def __str__(self) -> str:
        return 'History Chat<{}>: {}-{}'.format(self.pk, self.status, self.has_image)
    
