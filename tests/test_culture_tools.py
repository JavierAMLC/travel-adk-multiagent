from travel_assistant.tools.culture_tools import get_local_culture_data


def test_get_local_culture_data_cusco():
    result = get_local_culture_data("Cusco")
    assert result["status"] == "success"
    assert "Chiri Uchu" in result["dishes"]
    assert any("Pachamama" in custom for custom in result["customs"])
    assert len(result["phrases"]) >= 2

def test_get_local_culture_data_default():
    result = get_local_culture_data("Madrid")
    assert result["status"] == "success"
    assert len(result["dishes"]) == 1