import pytest

from blog_app.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title="Pytest with factory")


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == "Pytest with factory"
