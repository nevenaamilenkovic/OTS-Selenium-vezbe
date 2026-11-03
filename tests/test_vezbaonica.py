import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import lokatori


def nadji(driver: WebDriver, lokator):
    if lokator is None:
        pytest.fail("Lokator nije popunjen u lokatori.py")
    return driver.find_element(*lokator)


def popuni_formu(driver: WebDriver, lozinka: str = "tajna123", potvrda: str = "tajna123"):
    nadji(driver, lokatori.IME).send_keys("Petar")
    nadji(driver, lokatori.PREZIME).send_keys("Peric")
    nadji(driver, lokatori.EMAIL).send_keys("petar@primer.rs")
    nadji(driver, lokatori.LOZINKA).send_keys(lozinka)
    nadji(driver, lokatori.POTVRDA).send_keys(potvrda)
    nadji(driver, lokatori.USLOVI).click()


def test_unos_u_polja(vezbaonica: WebDriver):
    nadji(vezbaonica, lokatori.IME).send_keys("Petar")
    nadji(vezbaonica, lokatori.PREZIME).send_keys("Peric")
    nadji(vezbaonica, lokatori.EMAIL).send_keys("petar@primer.rs")

    assert nadji(vezbaonica, lokatori.IME).get_attribute("value") == "Petar"
    assert nadji(vezbaonica, lokatori.PREZIME).get_attribute("value") == "Peric"
    assert nadji(vezbaonica, lokatori.EMAIL).get_attribute("value") == "petar@primer.rs"


def test_lozinka_i_potvrda_su_razlicita_polja(vezbaonica: WebDriver):
    lozinka = nadji(vezbaonica, lokatori.LOZINKA)
    potvrda = nadji(vezbaonica, lokatori.POTVRDA)
    assert lozinka != potvrda

    lozinka.send_keys("tajna123")
    potvrda.send_keys("drugacija")

    assert lozinka.get_attribute("value") == "tajna123"
    assert potvrda.get_attribute("value") == "drugacija"


def test_lozinke_koje_se_ne_poklapaju(vezbaonica: WebDriver, wait: WebDriverWait):
    popuni_formu(vezbaonica, potvrda="drugacija")

    nadji(vezbaonica, lokatori.POSALJI).click()

    poruka = wait.until(EC.visibility_of_element_located((By.ID, "rezultat")))
    assert poruka.text == "Lozinke se ne poklapaju."


def test_uspesna_prijava(vezbaonica: WebDriver, wait: WebDriverWait):
    popuni_formu(vezbaonica)

    nadji(vezbaonica, lokatori.POSALJI).click()

    poruka = wait.until(EC.visibility_of_element_located((By.ID, "rezultat")))
    assert poruka.text == "Prijava primljena: Petar Peric."
    assert vezbaonica.find_element(By.ID, "broj-polaznika").text == "Ukupno: 5 polaznika"


def test_brisanje_polaznika(vezbaonica: WebDriver):
    nadji(vezbaonica, lokatori.OBRISI_MARKO_ILIC).click()

    celije = [td.text for td in vezbaonica.find_elements(By.CSS_SELECTOR, "#polaznici td")]
    assert "Ilić" not in celije
    assert "Jovanović" in celije