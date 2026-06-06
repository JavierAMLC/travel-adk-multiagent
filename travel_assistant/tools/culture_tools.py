def get_local_culture_data(destination: str) -> dict:
    """Devuelve datos de cultura local, platos típicos y costumbres de la región."""
    dest = destination.lower().strip()
    if "cusco" in dest or "machu picchu" in dest:
        return {
            "status": "success",
            "dishes": ["Chiri Uchu", "Ceviche de trucha", "Cuy chactado"],
            "customs": ["Pago a la Madre Tierra (Pachamama)", "Fiesta del Inti Raymi en junio"],
            "phrases": ["Allianllachu (¿Cómo estás?)", "Sulpayki (Gracias)"]
        }
    return {
        "status": "success",
        "dishes": ["Platos tradicionales locales"],
        "customs": ["Costumbres tradicionales de la zona"],
        "phrases": ["Saludos y expresiones de cortesía comunes"]
    }