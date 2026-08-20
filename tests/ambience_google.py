def test_abrir_google(page): # variável da fixture do pytest, não precisa criar uma página.
    page.goto("https://www.google.com/")
    page.pause()
    assert "Google" in page.title()