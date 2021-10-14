#!/usr/bin/env python3

def main():
    from app import create_app, init_database, registre_blueprints

    application = create_app()
    init_database(application)
    registre_blueprints(application)
    return application


if __name__ == '__main__':
    app = main()
    app.run(debug=True)
else:
    app = main()
