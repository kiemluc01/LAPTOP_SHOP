from django.db import models
from shopapp import base_models
class HistoryChat(base_models.BaseCreateUpdateModel):
    status = models.CharField("Staus chat", max_length=50)
    content = models.CharField("Content chat", max_length=1000, blank=True)
    user = models.ForeignKey("shopapp.Userprofile", related_name="user_chat", on_delete=models.CASCADE, blank=True)
    has_image = models.BooleanField("Has image",default=False, blank=True)
    
    def __str__(self) -> str:
        return 'History Chat<{}>: {}-{}'.format(self.pk, self.status, self.has_image)
    
class StaffHistorychat(base_models.BaseCreateUpdateModel):
    history = models.ForeignKey("chatbox.HistoryChat", related_name="staff_history", on_delete=models.CASCADE)
    staff = models.ForeignKey("shopapp.Userprofile", related_name="staff_chat", on_delete=models.CASCADE)
    
class ProductHistory(base_models.BaseCreateUpdateModel):
    history = models.ForeignKey("chatbox.HistoryChat", related_name="product_history", on_delete=models.CASCADE)
    product = models.ForeignKey("shopapp.Product", related_name="product_image", on_delete=models.CASCADE)

    
