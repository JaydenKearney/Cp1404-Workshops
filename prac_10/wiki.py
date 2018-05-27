import wikipedia
def main():
    """Request page name and display the title, summary, and URL of the page to the user."""
    page_name = input("Please enter a page name to search (leave blank to quit): ")
    while page_name != "":
        page = wikipedia.page(page_name)
        print(page.title)
        try:
            print(wikipedia.summary(page_name))
        except wikipedia.exceptions.DisambiguationError as e:
            for option in e.options:
                print("There are many options for {}: \n {}".format(page_name, option))
        except wikipedia.exceptions.PageError:
            print("I'm sorry that page doesn't exist.")
        print(page.url)
        page_name = input("Please enter a page name to search (leave blank to quit): ")


main()