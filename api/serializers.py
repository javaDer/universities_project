from rest_framework import serializers
from api.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from api.models import Universities


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    def create(self, validated_data):
        """
        根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
        """
        return Snippet.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """
        根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
class ApiSerializer(serializers.Serializer):
    create_time = serializers.DateTimeField()
    city = serializers.CharField(max_length=22, allow_blank=True, default='')
    competent_department = serializers.CharField(max_length=22, allow_blank=True, default='')
    name = serializers.CharField(max_length=22, allow_blank=True, default='')
    remake = serializers.CharField(max_length=22, allow_blank=True, default='')
    school_level = serializers.CharField(max_length=6, allow_blank=True, default='')
    universities_code = serializers.CharField(max_length=24, allow_blank=True, default='')
    def create(self, validated_data):
        """
        根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
        """
        return Universities.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """
        根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
        """
        instance.city = validated_data.get('city', instance.city)
        instance.competent_department = validated_data.get('competent_department', instance.competent_department)
        instance.name = validated_data.get('name', instance.name)
        instance.remake = validated_data.get('remake', instance.remake)
        instance.school_level = validated_data.get('school_level', instance.school_level)
        instance.universities_code = validated_data.get('universities_code', instance.universities_code)
        instance.save()
        return instance
