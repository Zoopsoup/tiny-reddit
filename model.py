import praw


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.reddit_instance = controller.reddit_instance
    # TODO: move reddit api methods here

    def get_subreddit_posts(self, sort='hot'):
        """
        return iterator with a given sorting method, currently limited to 1000 posts
        """
        post_iterator = self.reddit_instance.front
        if sort == 'hot':
            return post_iterator.hot(limit=None)
        elif sort == 'new':
            return post_iterator.new(limit=None)
        elif sort == 'rising':
            return post_iterator.rising(limit=None)
        elif sort == 'controversial':
            return post_iterator.controversial(limit=None)
        elif sort == 'top':
            return post_iterator.top(limit=None)
        return

    def get_post_content(self, post):
        """
        :param post: self.reddit_instance.submission
        :return: dict containing post attributes
        """
        post_content = {'selftext': post.selftext,
                        'url': post.url,
                        'comments': post.comments}
        return post_content
