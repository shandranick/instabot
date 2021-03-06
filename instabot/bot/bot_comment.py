"""
    Bot functions to generate and post a comments.

    Instructions to file with comments:
        one line - one comment.

    Example:
        lol
        kek

"""
from tqdm import tqdm

from . import limits

def comment(self, media_id, comment_text):
    if not self.check_media(media_id):
        return True
    if limits.check_if_bot_can_comment(self):
        delay.comment_delay(self)
        if super(self.__class__, self).comment(media_id, comment_text):
            self.total_commented += 1
            return True
    else:
        self.logger.info("Out of comments for today.")
    return False

def comment_medias(self, medias):
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                delay.follow_delay(self)
                while not self.comment(media, text):
                    delay.follow_delay(self)
    self.logger.info("DONE: Total commented on %d medias. " % self.total_commented)
    return True

def comment_hashtag(self, hashtag, amount=None):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_hashtag_medias(hashtag)
    return self.comment_medias(medias[:amount])

def comment_users(self, user_ids):
    # user_id = self.convert_to_user_id(user_id)
    # TODO: Put a comment to last media of every user from list
    pass

def comment_geotag(self, geotag):
    # TODO: comment every media from geotag
    pass

def is_commented(self, media_id):
    # TODO: get_media_commenters returns _usernames_ not user_ids!
    # TODO: implement self.user_id and change the method
    return self.username in self.get_media_commenters(media_id)
