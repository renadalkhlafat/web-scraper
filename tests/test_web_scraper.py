from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count , get_citations_needed_report

def test_version():
    assert __version__ == '0.1.0'

wikipedia_url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def test_get_citations_needed_count():

    expected = 5

    actual = get_citations_needed_count(wikipedia_url)

    assert expected == actual

def test_get_citations_needed_report():

    expected = "During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] Europeans, Africans, and indigenous intermixed, creating a mixed-race casta population in a process known as mestizaje. Mestizos, people of mixed European-indigenous ancestry, constitute the majority of Mexico's population.\n"

    actual = get_citations_needed_report(wikipedia_url)[-1]

    assert expected == actual