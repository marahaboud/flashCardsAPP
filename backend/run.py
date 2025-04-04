from modules.app import create_app

flashCardsApp = create_app()


# TODO: take care later for production
if __name__ == '__main__':
    # This will print all the routes Flask knows about
    for rule in flashCardsApp.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule}")
    flashCardsApp.run(host='0.0.0.0', debug=True)