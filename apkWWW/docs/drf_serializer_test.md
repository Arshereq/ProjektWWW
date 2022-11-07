from aplikacja1.Serializer import *
from aplikacja1.models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
druzyna= Druzyna(nazwa="Polska",kraj='PL')
druzyna.save()
serializer = DruzynaSerializer(druzyna)
serializer.data
content = JSONRenderer().render(serializer.data)
content
import io
pokaz=io.BytesIO(content)
data = JSONParser().parse(pokaz)
deserializer = DruzynaSerializer(data=data)
deserializer.is_valid()  
deserializer.errors 
deserializer.fields 
deserializer.validated_data 
deserializer.save()
deserializer.data
osoba = Osoba(name='Jan',surname='kowalski')
druzyna.save()

serializer = OsobaSerializer(osoba)
serializer.data
content = JSONRenderer().render(serializer.data)
content
pokaz = io.BytesIO(content)
data = JSONParser().parse(pokaz)
deserializer = OsobaSerializer(data=data)
deserializer.is_valid()
deserializer.errors
deserializer.fields
repr(deserializer)
deserializer.validated_data
deserializer.save()
deserializer.data




