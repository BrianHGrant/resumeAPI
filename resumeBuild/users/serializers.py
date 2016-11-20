from rest_framework import serializers
from users.models import User, Address, Job, Certification, Affiliation, Interest, Education, Skill

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ( 'id', 'street', 'city', 'state', 'zipcode' )

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ( 'id', 'name', 'email', 'address')

class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = AddressSerializer()
    class Meta:
        model = Job
        fields = ( 'id', 'title', 'company', 'address', 'startDate', 'endDate', 'description', 'user')

class CertificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Certification
        fields = ('id', 'name', 'user')

class AffiliationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Affiliation
        fields = ('id', 'name', 'user')

class InterestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Interest
        fields = ('id', 'name', 'user')

class Education(serializers.ModelSerializer):
    user = UserSerializer()
    address = AddressSerializer()
    class Meta:
        model = Education
        fields = ('id', 'school', 'fieldOfStudy', 'description', 'user', 'address')

class Skill(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Skill
        fields = ('id', 'name', 'user', 'skillType')
