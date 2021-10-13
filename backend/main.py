#!/usr/bin/env python3

if __name__ == '__main__':
    from app import create_app, init_database

    application = create_app()
    init_database(application)
    application.run()
