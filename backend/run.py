from app import create_app

flashCardsApp = create_app()


# TODO: take care later for production
if __name__ == '__main__':
    flashCardsApp.run(host='0.0.0.0', debug=True)