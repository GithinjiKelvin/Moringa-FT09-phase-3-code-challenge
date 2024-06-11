import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.connection import get_db_connection

class TestModels(unittest.TestCase):
    # Tests for Author Class
    def test_author_creation(self):
        author = Author(1, "KelvinGithinji")
        self.assertEqual(author.name, "KelvinGithinji")

    def test_init(self):
        author = Author(1, "KelvinGithinji")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "KelvinGithinji")

    def test_save(self):
        author = Author(None, "KelvinGithinji")
        author.save()
        self.assertIsNotNone(author.id)
        self.assertIn(author.id, Author.all)

    def test_get_author_id(self):
        author = Author(1, "KelvinGithinji")
        self.assertEqual(author.get_author_id(), 1)

    def test_name_immutable(self):
        author = Author(1, "KelvinGithinji")
        with self.assertRaises(AttributeError):
            author.name = "KelvinGithinji"

    def test_author_repr(self):
        author = Author(1, "KelvinGithinji")
        self.assertEqual(repr(author), "<Author 1 KelvinGithinji>")

    def test_author_attributes(self):
        author = Author(2, "Jane Smith")
        self.assertEqual(author.id, 2)
        self.assertEqual(author.name, "Jane Smith")

    def test_id_setter(self):
        obj = Author(123, "KelvinGithinji")
        obj.id = 123
        self.assertEqual(obj.id, 123)

    def test_name_setter(self):
        obj = Author(123, "KelvinGithinji")
        self.assertEqual(obj.name, "KelvinGithinji")

    def test_saves_author(self):
        author = Author(None, "KelvinGithinji")
        author.save()
        self.assertIsNotNone(author.id)
        self.assertIn(author.id, Author.all)

# Tests for the Article Class

# Tests for Magazine class
    def test_magazine_creation(self):
        magazine = Magazine(1, "German Machines", "Vehicles")
        self.assertEqual(magazine.name, "German Machines")

    def test_saves_magazine(self):
        magazine = Magazine(None, "German Machines", "Vehicles")
        magazine.save()
        self.assertIsNotNone(magazine.id)
        self.assertIn(magazine.id, Magazine.all)

    def test_magazine_repr(self):
        magazine = Magazine(1, "German Machines", "Vehicles")
        self.assertEqual(repr(magazine), "<Magazine 1 German Machines Vehicles>")

    def test_get_magazine_id(self):
        magazine = Magazine(1, "German Machines", "Vehicles")
        self.assertEqual(magazine.get_magazine_id(), 1)

    
    def test_id_property(self):
        magazine = Magazine(1, "German Machines", "Vehicles")
        self.assertEqual(magazine.id, 1)

    def test_name_property(self):
        magazine = Magazine(1, "German Machines", "Vehicles")
        self.assertEqual(magazine.name, "German Machines")
if __name__ == "__main__":
    unittest.main()
