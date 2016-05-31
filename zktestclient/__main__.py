import app
import argparse


def main(host):

    app.run(host)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    args = parser.parse_args()

    if args.host is None:
        raise ValueError("no host:port specified")

    main(args.host)
