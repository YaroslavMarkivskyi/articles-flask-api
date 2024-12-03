from app.modules.articles.serializers import ArticleSerializer

# Тест для методу from_dict
def test_from_dict():
    # Тестовий словник
    data = {
        "id": 1,
        "author_id": 2,
        "title": "Test Article",
        "description": "This is a test article.",
        "body": "This is the body of the test article."
    }

    article_serializer = ArticleSerializer.from_dict(data)

    assert article_serializer.id == 1
    assert article_serializer.author_id == 2
    assert article_serializer.title == "Test Article"
    assert article_serializer.description == "This is a test article."
    assert article_serializer.body == "This is the body of the test article."

# Тест для методу to_dict
def test_to_dict():
    article_serializer = ArticleSerializer(
        id=1,
        author_id=2,
        title="Test Article",
        description="This is a test article.",
        body="This is the body of the test article."
    )

    result = article_serializer.to_dict()

    assert result == {
        "id": 1,
        "author_id": 2,
        "title": "Test Article",
        "description": "This is a test article.",
        "body": "This is the body of the test article."
    }

# Тест для відсутнього id
def test_optional_id():
    data = {
        "author_id": 2,
        "title": "Test Article",
        "description": "This is a test article.",
        "body": "This is the body of the test article."
    }

    article_serializer = ArticleSerializer.from_dict(data)

    assert article_serializer.id is None
    assert article_serializer.author_id == 2
    assert article_serializer.title == "Test Article"
    assert article_serializer.description == "This is a test article."
    assert article_serializer.body == "This is the body of the test article."
