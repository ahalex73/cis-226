# Alexander Holmes
# 10/26/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to complete --- 2 hours ---

import program_console_db
import pytest

@pytest.fixture
def veg_conn():
    veg_conn = program_console_db.Vegetables(db=":memory:")
    veg_conn.setup()

    return veg_conn


def test_add_vegetable(capsys, veg_conn):
    """Tests the add vegetable function"""
    veg_conn.add_vegetable("Carrot", 12)

    veg_conn.show_all()
    captured = capsys.readouterr()
    assert captured.out.strip("\n") == "(12, 'Carrot')"


def test_update_vegetable(capsys, veg_conn):
    """Test the update vegetable function"""
    veg_conn.add_vegetable("Carrot", 12)
    veg_conn.update_vegetable("Carrot", 6)
    
    veg_conn.show_all()
    captured = capsys.readouterr()
    assert captured.out.strip("\n") == "(6, 'Carrot')"

def test_delete_vegetable(capsys, veg_conn):
    """Tests the delete vegetable function"""
    veg_conn.add_vegetable("Carrot", 12)
    veg_conn.delete_vegetable("Carrot")

    veg_conn.show_all()
    captured = capsys.readouterr()
    assert captured.out.strip("\n") == "Carrot has been removed"
