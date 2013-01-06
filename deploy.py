import main
main.create_tables()

import models
user = models.User(username="Hugo", password="123", email="pepe@123.com")
user.save()
print "Creando usuario de prueba:", user
