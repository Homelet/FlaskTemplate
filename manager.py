from flask_script import Server

from application import manager
from www import register

# start web server
manager.add_command("run_server", Server(host="0.0.0.0", use_debugger=True,
                                         use_reloader=True))


def main():
    register()
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc(e)
