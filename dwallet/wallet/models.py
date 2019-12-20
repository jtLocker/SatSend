from django.db import models
from django.contrib.auth.models import User
from cryptos import *

# gen_wallet generates a private key aka wallet 
# os.urandom should be "unpredictable enough" https://docs.python.org/3.5/library/os.html#os.urandom
def gen_wallet():
    return sha256(entropy_to_words(os.urandom(16)))

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    privkey = models.CharField(max_length=64, default=gen_wallet)

    def __str__(self):
        return self.user.username
    