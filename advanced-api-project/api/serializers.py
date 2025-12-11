from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):

    """
    Srializers boook model.data
    has custom validation to ensure the publication year is not in the future,
    """

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializers author model data.
    Includes nested Bookserializer to display books written to display books written by the author.
    N/B : the books field uses BookSerializer(many=true) to represent the reverse foreignkey relationship vial related_name="books"
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']