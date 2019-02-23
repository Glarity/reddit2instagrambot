import argparse
import json
import logging
from reddit2instagram import reddit


def main(args):
    logger = logging.getLogger("main")

    handler = [h for h in logger.handlers if h.get_name() == "console_handler"][0]

    if args.verbose:
        handler.setLevel(handler.level - (args.verbose * 10))

    reddit_conn = reddit.connect_reddit()
    found_posts = reddit.scrape_subreddit(reddit_conn, "RocketLeague")
    reddit.download_posts(found_posts)


def process_args():
    parser = argparse.ArgumentParser(prog='reddit2instagram')
    parser.add_argument('-v', '--verbose', action='count',
                        help='Increase the verbosity level of the console')
    return parser.parse_args()


if __name__ == "__main__":
    args = process_args()
    main(args)
